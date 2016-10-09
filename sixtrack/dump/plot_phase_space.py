#!/usr/bin/env python
import os
import sys
import subprocess

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

# ------------------------------------------------------------------------------
# COMMAND LINE ARGUMENTS
# ------------------------------------------------------------------------------
infile = sys.argv[1]  # dump file

# ------------------------------------------------------------------------------
# CONSTANTS
# ------------------------------------------------------------------------------
# # Beam energy at collision [eV]
# energy = 26e9

# # Proton mass [eV/c^2]
# m_p = 938.272046e6

# # Speed of light [m/s]
# c = 299792458

# # Relativistic gamma
# gamma_rel = energy/m_p

# # Relativistic beta
# beta_rel = np.sqrt(1-(1/gamma_rel**2))

# # Lattice characteristics
# orbit_x = -0.000750
# orbit_xp = 0.000000
# beta_x = 0.150739
# alpha_x = 0.003485

# orbit_y = -0.000000
# orbit_yp = 0.000295
# beta_y = 0.150235
# alpha_y = -0.000764

# # Emittances
# em_n = 2.5 * 1e-6
# em_g = em_n/(gamma_rel*beta_rel)

# ------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------

# def do_floquet(beta, alpha, em, c, cp, norm=True):
#     term_1 = c/np.sqrt(beta)
#     term_2 = (c*alpha)/np.sqrt(beta) + np.sqrt(beta)*cp
#     if norm==True:
#         return np.linalg.norm(np.array([term_1, term_2]))/np.sqrt(em)
#     else:
#         return term_1, term_2

# def get_sigma(x, xp, beta):
#     term_1_x = np.mean(np.multiply(x,x)) - np.multiply(np.mean(x), np.mean(x))
#     term_2_x = np.mean(np.multiply(x,xp)) - np.multiply(np.mean(x),np.mean(xp))
#     term_3_x = np.mean(np.multiply(xp,x)) - np.multiply(np.mean(xp), np.mean(x))
#     term_4_x = np.mean(np.multiply(xp,xp)) - np.multiply(np.mean(xp),np.mean(xp))
#     det_x = np.multiply(term_1_x, term_4_x) - np.multiply(term_3_x, term_2_x)
#     return np.sqrt(np.sqrt(abs(det_x))*beta)

# def get_tilt(y, yp, z, sigma_z, sigma_y, coord='y'):
#     term_1 = []
#     term_1p = []
#     term_2 = []
#     term_2p = []
#     for particle_y, particle_yp, particle_z in zip(y, yp, z):
#         if particle_z > 0.9*sigma_z and particle_z < 1.1*sigma_z:
#             term_1.append(particle_y)
#             term_1p.append(particle_yp)
#         if particle_z > -1.1*sigma_z and particle_z < -0.9*sigma_z:
#             term_2.append(particle_y)
#             term_2p.append(particle_yp)
#     if coord == 'y':
#         dy_plus, cs = do_floquet(-0.000764, 0.150235, 3.35*1e-10, term_1, term_1p, 0.0, 0.000295)
#         dy_minus, cs = do_floquet(-0.000764, 0.150235, 3.35*1e-10, term_2, term_2p, 0.0, 0.000295)
#     elif coord == 'x':
#         dy_plus, cs = do_floquet(0.003485, 0.150739, 3.35*1e-10, term_1, term_1p,  -0.000750, 0.0)
#         dy_minus, cs = do_floquet(0.003485, 0.150739, 3.35*1e-10, term_2, term_2p, -0.000750, 0.0)
#     return abs(dy_plus - dy_minus)/2
#     return (np.mean(term_1) - np.mean(term_2))/2*sigma_z

# def phase_space(alpha, beta, c, cp):
#     return beta*cp + alpha*c

# outfile = 'parameters.txt'
# try:
#     os.remove(outfile)
# except OSError:
#     pass
    
# ------------------------------------------------------------------------------
# DATA EXTRACTION
# ------------------------------------------------------------------------------
get  = GetData(infile)
data = get.data_column()

p_id   = np.asarray(data[0], dtype='float64')
turns  = np.asarray(data[1], dtype='float64')
x_tot  = np.asarray(data[3], dtype='float64') * 1e-3 
xp_tot = np.asarray(data[4], dtype='float64') * 1e-3 
y_tot  = np.asarray(data[5], dtype='float64') * 1e-3 
yp_tot = np.asarray(data[6], dtype='float64') * 1e-3
z_tot  = np.asarray(data[7], dtype='float64') * 1e-3
e_tot  = np.asarray(data[8], dtype='float64')


# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
DPI=600
font_spec = {"font.family": "serif", # use as default font
             "font.serif": ["Computer Modern Roman"], # custom serif font
             # "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":10,
             "font.weight":"bold",
            }
rc('text', usetex=True)
rcParams['figure.figsize']= 5, 3
rcParams.update(font_spec)

fig = plt.figure()

x_mean = []
y_mean = []
t1     = []
for turn in set(turns):
    x_plot1  = []
    y_plot1  = []
    for tt, x, y in zip(turns, x_tot, y_tot):
        if tt == turn:
            x_plot1.append(x)
            y_plot1.append(y)
    x_mean.append(np.mean(x_plot1))
    y_mean.append(np.mean(y_plot1))
    t1.append(turn)
    print turn

plt.plot(t1, x_mean, '--o', markersize=3, linewidth=0.2, color='red')
plt.plot(t1, y_mean, '--o', markersize=3, linewidth=0.2, color='blue')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.xlabel(r"Turns")
plt.ylabel(r"Amplitude")
plt.subplots_adjust(left=0.15, bottom=0.20, right=0.85, top=0.91)
plt.savefig('amplitude.png', dpi=DPI)
plt.clf()   

for particle in set(p_id):
    t       = []
    number  = []
    x_plot  = []
    xp_plot = []
    y_plot  = []
    yp_plot = []
    for turn, pid, x, xp, y, yp in zip(turns, p_id, x_tot, xp_tot, y_tot, yp_tot):
        if pid == particle:
            t.append(turn)
            number.append(pid)
            x_plot.append(x)
            xp_plot.append(xp)
            y_plot.append(y)
            yp_plot.append(yp)
    print particle, len(x_plot)
    
    
    plt.plot(x_plot, xp_plot, '--o', markersize=3, linewidth=0.3)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlabel(r"$x$ [m]")
    plt.ylabel(r"$x'$ [rad]")
    plt.subplots_adjust(left=0.17, bottom=0.15, right=0.96, top=0.90, wspace=0.18, hspace=0.16)
    plt.savefig('x_xp' + str(particle)  + '.png', dpi=DPI)
    plt.clf()

    plt.plot(y_plot, yp_plot, '--o', markersize=3, linewidth=0.2, color='red')
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.xlabel(r"$y$ [m]")
    plt.ylabel(r"$y'$ [rad]")
    plt.subplots_adjust(left=0.15, bottom=0.20, right=0.85, top=0.91)
    plt.savefig('y_yp' + str(particle)  + '.png', dpi=DPI)
    plt.clf()






