#!/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------------------
# Function to generate a particle distribution as input for the collimation routine in SixTrack (round beams at symmetry point)
# Example for SPS:
# generate_distribution.py 64 26e9 'SPS_inj' True 1 1 0.9e-6 3.0e-6 1.50895801 -1.392739114 51.8375213 46.54197726 0 0 0.2 14e-4
# ----------------------------------------------------------------------------------------------------------------------------
import datetime
import sys
import random

import numpy as np

from util import get_bucket
from util import get_rel_params
from util import get_sigmas

# Pass the Command Line Arguments
# --------------------------------------------------------------------------------------------------------------
particles    = int(sys.argv[1])
energy       = float(sys.argv[2])
machine      = sys.argv[3]
fort13       = sys.argv[4]
jobs         = int(sys.argv[5])
factor       = float(sys.argv[6])
emittance_x  = float(sys.argv[7])
emittance_y  = float(sys.argv[8])
alpha_x      = float(sys.argv[9])
alpha_y      = float(sys.argv[10])
beta_x       = float(sys.argv[11])
beta_y       = float(sys.argv[12])
dispersion_x = float(sys.argv[13])
dispersion_y = float(sys.argv[14])
bunch        = float(sys.argv[15])
spread       = float(sys.argv[16])


def dist_generator(particles, energy, machine, fort13, jobs, factor, emittance_x, emittance_y, alpha_x, alpha_y, beta_x, beta_y, dispersion_x, dispersion_y, bunch, spread, seed=0):

    job_str = '%s'%jobs
    
    # Getting the Transverse sigmas (amplitudes of phase space ellipse)
    # --------------------------------------------------------------------------------------------------------------
    gamma_rel, beta_rel, p0, mass = get_rel_params(energy)
    tx_max, txp_max               = get_sigmas(alpha_x, beta_x, emittance_x, dispersion_x, spread, beta_rel, gamma_rel)
    ty_max, typ_max               = get_sigmas(alpha_y, beta_y, emittance_y, dispersion_y, spread, beta_rel, gamma_rel)

    # Seeding
    # --------------------------------------------------------------------------------------------------------------
    if seed == 0:
        myseed = random.randint(0, 429496729)
    else:
        myseed = seed
    with open('seed.txt', 'a') as g:
        print >> g,  'job ', job_str ,'seed ', myseed
    np.random.seed(myseed)
    random.seed(myseed)
    
    # Generating the Transverse Distribution
    # --------------------------------------------------------------------------------------------------------------
    x_t  = np.asarray(np.random.normal(0, factor * tx_max, particles))
    xp_t = np.asarray(np.random.normal(0, factor * txp_max, particles))
    y_t  = np.asarray(np.random.normal(0, factor * ty_max, particles))
    yp_t = np.asarray(np.random.normal(0, factor * typ_max, particles))

    # Rotating the Transverse Distribution
    # --------------------------------------------------------------------------------------------------------------
    angle_x = np.arctan(-alpha_x/beta_x)
    x       = x_t*np.cos(angle_x) - xp_t*np.sin(angle_x)
    xp      = x_t*np.sin(angle_x) + xp_t*np.cos(angle_x)

    angle_y = np.arctan(-alpha_y/beta_y)
    y       = y_t*np.cos(angle_y) - yp_t*np.sin(angle_y)
    yp      = y_t*np.sin(angle_y) + yp_t*np.cos(angle_y)
    
    # Generating the Longitudinal Distribution
    # --------------------------------------------------------------------------------------------------------------
    z  = []
    E  = []
    dp = []
    
    while len(z) < particles:
        # Generate for as long time as is needed
        particle_z = random.gauss(0,1)
        particle_e = random.gauss(0,1)
        trial_z    = particle_z * bunch
        trial_e    = energy * (1 + particle_e*spread) #eV

        trial_p = np.sqrt((trial_e - mass) * (trial_e + mass))
        dPP     = (trial_p - p0) / p0
        h       = get_bucket(machine, plot=False, z=trial_z, DELTA=dPP)  # Longitudinal contour

        Hmargin = -1
        if h <= Hmargin:
            z.append(float(trial_z))
            E.append(float(trial_e))
            dp.append(dPP)
        else:
            print 'Outside margin, trying again,', h
  
    zz  = np.asarray(z)
    EE  = np.asarray(E)
    ddp = np.asarray(dp)

    if fort13=='False':
        outfile = 'init_dist_' + job_str + '.txt'
        with open(outfile, 'w') as f:
            for e1, e2, e3, e4, e5, e6 in zip(x, xp, y, yp, z, E):
                f.write('%8.6e %8.6e %8.6e %8.6e %8.6e %8.6e\n' % (e1, e2, e3, e4, e5, e6))
    elif fort13=='True':
        outfile = 'fort.13'
        with open(outfile, 'w') as f:
            for i in xrange(0, particles, 2):
                f.write(str(x[i]*1e3) + "\n") #mm
                f.write(str(xp[i]*1e3) + "\n") #mrad
                f.write(str(y[i]*1e3) + "\n") #mm
                f.write(str(yp[i]*1e3) + "\n") #mrad
                f.write(str(zz[i]*1e3) + "\n") #mm
                f.write(str(ddp[i]) + "\n") #-

                f.write(str(x[i+1]*1e3) + "\n") #mm
                f.write(str(xp[i+1]*1e3) + "\n") #mrad
                f.write(str(y[i+1]*1e3) + "\n") #mm
                f.write(str(yp[i+1]*1e3) + "\n") #mrad
                f.write(str(zz[i+1]*1e3) + "\n") #mm
                f.write(str(ddp[i+1]) + "\n") #-

                f.write(str(energy*1e-6) + "\n") #MeV
                f.write(str(EE[i]*1e-6) + "\n") #MeV
                f.write(str(EE[i+1]*1e-6) + "\n") #MeV
    else:
        print 'Please input True or False in the fourth argument'
                
# Call the function
# --------------------------------------------------------------------------------------------------------------
job_range = range(1, int(jobs) + 1)
with open('seed.txt', 'a') as g:
    print >> g, datetime.datetime.now()
for n in job_range:
    j = '%s'%n
    dist_generator(particles, energy, machine, fort13, jobs, factor, emittance_x, emittance_y, alpha_x, alpha_y, beta_x, beta_y, dispersion_x, dispersion_y, bunch, spread)
    


