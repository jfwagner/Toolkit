#!/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------------------
# Function to generate a particle distribution as input for the collimation routine in SixTrack (round beams at symmetry point)
# ----------------------------------------------------------------------------------------------------------------------------
import datetime
import sys
import random
from math import sqrt, pi

import numpy as np

from util import get_bucket

# Pass the Command Line Arguments
# --------------------------------------------------------------------------------------------------------------
particles = int(sys.argv[1])
jobs = np.int(sys.argv[2])

def dist_generator(particles, emittance_x, beta_x, alpha_x, emittance_y, beta_y, alpha_y, bunch, spread, factor, job, seed=0, fort13=False):

    job_str = '%s'%job
    # print '>> Generating distribution for job', job
    
    # Proton mass [eV/c^2], energy [eV], number of particles, relativistic gamma, relativistic beta
    # --------------------------------------------------------------------------------------------------------------
    c = 2.99792485e8  # m/s
    mp = 0.938272046e9 # eV/c^2
    e_tot = 26e9  # eV
    gamma_rel = e_tot / mp
    beta_rel = sqrt(gamma_rel**2 - 1) / gamma_rel

    # Twiss Parameter Gamma
    # --------------------------------------------------------------------------------------------------------------
    gamma_x = (1 + alpha_x**2)/beta_x
    gamma_y = (1 + alpha_y**2)/beta_y

    # Standard Deviations, transverse plane x
    # --------------------------------------------------------------------------------------------------------------
    dx = -0.1094101846
    dpx = -0.002663251097
    tx_max = sqrt((emittance_x*beta_x + dx**2*spread**2)/(beta_rel*gamma_rel))	   # beam enveloppe
    txp_max = sqrt((emittance_x*gamma_x)/(beta_rel*gamma_rel))
    
    # Standard Deviations, transverse plane y
    # --------------------------------------------------------------------------------------------------------------
    ty_max = sqrt((emittance_y*beta_y)/(beta_rel*gamma_rel))	# beam enveloppe
    typ_max = sqrt((emittance_y*gamma_y)/(beta_rel*gamma_rel))   # beam amplitude

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
    x_t = np.asarray(np.random.normal(0, factor * tx_max, particles))
    xp_t = np.asarray(np.random.normal(0, factor * txp_max, particles))
    y_t = np.asarray(np.random.normal(0, factor * ty_max, particles))
    yp_t = np.asarray(np.random.normal(0, factor * typ_max, particles))

    # Rotating the Transverse Distribution
    # --------------------------------------------------------------------------------------------------------------
    angle_x = np.arctan(-alpha_x/beta_x)
    x  = x_t*np.cos(angle_x) - xp_t*np.sin(angle_x)
    xp = x_t*np.sin(angle_x) + xp_t*np.cos(angle_x)

    angle_y = np.arctan(-alpha_y/beta_y)
    y  = y_t*np.cos(angle_y) - yp_t*np.sin(angle_y)
    yp = y_t*np.sin(angle_y) + yp_t*np.cos(angle_y)
    
    # Generating the Longitudinal Distribution
    # --------------------------------------------------------------------------------------------------------------
    z = []
    E = []
    dp = []
    p0 = sqrt((e_tot - mp) * (e_tot + mp))
    
    while len(z) < particles:
        # Generate for as long time as is needed
        particle_z = random.gauss(0,1)
        particle_e = random.gauss(0,1)
        trial_z = particle_z * bunch
        trial_e = e_tot * (1 + particle_e*spread) #eV

        trial_p = sqrt((trial_e - mp) * (trial_e + mp))
        dPP = (trial_p - p0) / p0

        # print 'dist', trial_z

        h = get_bucket('SPS_inj', plot=False, z=trial_z, DELTA=dPP)  # Longitudinal contour
        # print h
        Hmargin = -1

        if h <= Hmargin:
            # print trial_z, bunch
            #inside bucket; accept!
            z.append(float(trial_z))
            E.append(float(trial_e))
            dp.append(dPP)
        else:
            print 'Trying again,', h
        # print len(z)
            
    zz = np.asarray(z)
    EE = np.asarray(E)
    ddp = np.asarray(dp)

    if fort13==False:
        outfile = 'init_dist_' + job_str + '.txt'
        with open(outfile, 'w') as f:
            for e1, e2, e3, e4, e5, e6 in zip(x, xp, y, yp, z, E):
                f.write('%8.6e %8.6e %8.6e %8.6e %8.6e %8.6e\n' % (e1, e2, e3, e4, e5, e6))
    elif fort13==True:
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

                f.write(str(e_tot*1e-6) + "\n") #MeV
                f.write(str(EE[i]*1e-6) + "\n") #MeV
                f.write(str(EE[i+1]*1e-6) + "\n") #MeV
                
# Call the function
# --------------------------------------------------------------------------------------------------------------
job_range = range(1, int(jobs) + 1)
with open('seed.txt', 'a') as g:
    print >> g, datetime.datetime.now()
for n in job_range:
    j = '%s'%n
    dist_generator(particles, 0.9e-6, 51.8375213, 1.50895801, 3.0e-6, 46.54197726, -1.392739114, 0.2, 14e-4, 1, j, seed=0, fort13=True)
                 # particles, emittance_x, beta_x, alpha_x, emittance_y, beta_y, alpha_y, bunch, spread 10.7e-4, factor, job, seed=0, fort13=False


