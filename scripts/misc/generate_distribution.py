#!/usr/local/bin/python
# ----------------------------------------------------------------------------------------------------------------------------
# Function to generate a particle distribution as input for the collimation routine in SixTrack (round beams at symmetry point)
# ----------------------------------------------------------------------------------------------------------------------------
from random import gauss
from math import sqrt, pi
import sys
from longitudinalDyn import longitudinalHamiltonian 
Hcalculator = longitudinalHamiltonian("HL_coll")
Hmargin = -0.005  #Hamiltonian to accept below

def dist_generator(particles, emittance, beta, bunch, spread, factor, job):

    seed = '%s'%job

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

        # f = open('beam_parameters.txt', 'w')

        # for args in (('Number of particles', particles, ''), ('Energy', e_tot, '[eV]'),('Relativistic gamma', gamma_rel, ''), 
        #              ('Relativistic beta', beta_rel, ''), ('Transverse normalized emittance', emittance, '[m]'),
        #              ('RMS bunchlength', bunch, '[m]'), ('RMS energy spread', spread, '[%]'), ('Transverse beam envelope', t_max, '[m]'), 
        #              ('Transverse beam amplitude', tp_max, '[m^-1]'), ('Beta star', beta, '[m]'), ('Sigmas', factor, '[m]')):
        #     print >> f, '{:<40} {:<40} {:<40}'.format(*args)
        # f.close()

    # --------------------------------------------------------------------------------------------------------------
    # Writing the distribution file
    # --------------------------------------------------------------------------------------------------------------
    outfile = 'init_dist_' + seed + '.txt'
    f = open(outfile,'w')

    ran_x = []
    ran_xp = []
    for i in range(0, particles):
        ran_x.append(gauss(0,1))
        ran_xp.append(gauss(0,1))

    ran_y = []
    ran_yp = []
    for i in range(0, particles):
        ran_y.append(gauss(0,1))
        ran_yp.append(gauss(0,1))

    #ran_z = []
    #ran_e = []
    #for i in range(0, particles):
    #        ran_z.append(gauss(0,1))
    #        ran_e.append(gauss(0,1))
        #print ran_z

    x = []
    for particle_x in ran_x:
        x.append(float(factor*particle_x*t_max))
    xp = []
    for particle_xp in ran_xp:
        xp.append(float(factor*particle_xp*tp_max))
    y = []
    for particle_y in ran_y:
        y.append(float(factor*particle_y*t_max))
    yp = []
    for particle_yp in ran_yp:
        yp.append(float(factor*particle_yp*tp_max))


    z = []
    E = []
    p0 = sqrt((e_tot-mp)*(e_tot+mp))

    while len(z) < particles:
        # Generate for as long time as is needed
        particle_z = gauss(0,1)
        particle_e = gauss(0,1)
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


    for e1, e2, e3, e4, e5, e6 in zip(x, xp, y, yp, z, E):
        f.write('%8.6e %8.6e %8.6e %8.6e %8.6e %8.6e\n' % (e1, e2, e3, e4, e5, e6))

    f.close()

particles = int(sys.argv[1])
# (particles, emittance, beta, bunch, spread, factor)
for number in range(1, 2):
    n = '%s'%number
    dist_generator(particles, 2.5e-6, 0.15, 75.5, 1.13e-4, 1, n)



