#!/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------------------
# Function to generate a particle distribution as input for the collimation routine in SixTrack (round beams at symmetry point)
# ----------------------------------------------------------------------------------------------------------------------------
import datetime
import sys
import random
from math import sqrt, pi

import numpy as np

from longitudinalDyn import longitudinalHamiltonian

# Pass the Command Line Arguments
# --------------------------------------------------------------------------------------------------------------
particles = int(sys.argv[1])
jobs = np.int(sys.argv[2])

Hcalculator = longitudinalHamiltonian("HL_coll")
Hmargin = -0.005  #Hamiltonian to accept below

def dist_generator(particles, emittance, beta, bunch, spread, factor, job, seed=0):

    job_str = '%s'%job
    # print '>> Generating distribution for job', job
    
    # Proton mass [eV/c^2], energy [eV], number of particles, relativistic gamma, relativistic beta
    # --------------------------------------------------------------------------------------------------------------
    mp = 0.938272046e9
    e_tot = 7e12
    gamma_rel = e_tot/mp
    beta_rel = sqrt(gamma_rel**2 - 1)/gamma_rel

    # Twiss Parameters
    # --------------------------------------------------------------------------------------------------------------
    gamma = 1/beta

    # Standard Deviations, transverse plane x, y => t
    # --------------------------------------------------------------------------------------------------------------
    t_max = sqrt((emittance*beta)/(beta_rel*gamma_rel))	   # beam enveloppe
    tp_max = sqrt(emittance/(beta*beta_rel*gamma_rel))     # beam amplitude

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
    x = np.random.normal(0, factor*t_max, particles)
    xp = np.random.normal(0, factor*tp_max, particles)
    y = np.random.normal(0, factor*t_max, particles)
    yp = np.random.normal(0, factor*tp_max, particles)
    
    # Generating the Longitudinal Distribution
    # --------------------------------------------------------------------------------------------------------------
    z = []
    E = []
    p0 = sqrt((e_tot-mp)*(e_tot+mp))
    
    while len(z) < particles:
        # Generate for as long time as is needed
        particle_z = random.gauss(0,1)
        particle_e = random.gauss(0,1)
        trial_z = particle_z*bunch
        trial_e = e_tot*(1 + particle_e*spread) #eV

        phi = Hcalculator.omegaRF*trial_z*1e-3/(2.99792485e8*beta_rel)-pi
        trial_p = sqrt((trial_e-mp)*(trial_e+mp))
        dPP = (trial_p-p0)/p0
        particle_longitudinal_H = Hcalculator.calcH(dPP,phi)[0]

        if particle_longitudinal_H <= Hmargin:
            #inside bucket; accept!
            z.append(float(trial_z))
            E.append(float(trial_e)*10**(-6))
            
    outfile = 'init_dist_' + job_str + '.txt'
    with open(outfile, 'w') as f:
        for e1, e2, e3, e4, e5, e6 in zip(x, xp, y, yp, z, E):
            f.write('%8.6e %8.6e %8.6e %8.6e %8.6e %8.6e\n' % (e1, e2, e3, e4, e5, e6))

            
# Call the function
# --------------------------------------------------------------------------------------------------------------
job_range = range(1, int(jobs) + 1)
with open('seed.txt', 'a') as g:
    print >> g, datetime.datetime.now()
for n in job_range:
    j = '%s'%n
    dist_generator(particles, 2.5e-6, 0.15, 75.5, 1.13e-4, 1, j, seed=0) # (particles, emittance, beta, bunch, spread, factor, job)



