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
# Beam energy at collision [eV]
energy = 7e12

# Proton mass [eV/c^2]
m_p = 938.272046e6

# Speed of light [m/s]
c = 299792458

# Relativistic gamma
gamma_rel = energy/m_p

# Relativistic beta
beta_rel = np.sqrt(1-(1/gamma_rel**2))

# Lattice characteristics
orbit_x = -0.000750
orbit_xp = 0.000000
beta_x = 0.150739
alpha_x = 0.003485

orbit_y = -0.000000
orbit_yp = 0.000295
beta_y = 0.150235
alpha_y = -0.000764

# Emittances
em_n = 2.5 * 1e-6
em_g = em_n/(gamma_rel*beta_rel)

# ------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------

def do_floquet(beta, alpha, em, c, cp, norm=True):
    term_1 = c/np.sqrt(beta)
    term_2 = (c*alpha)/np.sqrt(beta) + np.sqrt(beta)*cp
    if norm==True:
        return np.linalg.norm(np.array([term_1, term_2]))/np.sqrt(em)
    else:
        return term_1, term_2

def get_sigma(x, xp, beta):
    term_1_x = np.mean(np.multiply(x,x)) - np.multiply(np.mean(x), np.mean(x))
    term_2_x = np.mean(np.multiply(x,xp)) - np.multiply(np.mean(x),np.mean(xp))
    term_3_x = np.mean(np.multiply(xp,x)) - np.multiply(np.mean(xp), np.mean(x))
    term_4_x = np.mean(np.multiply(xp,xp)) - np.multiply(np.mean(xp),np.mean(xp))
    det_x = np.multiply(term_1_x, term_4_x) - np.multiply(term_3_x, term_2_x)
    return np.sqrt(np.sqrt(abs(det_x))*beta)

def get_tilt(y, yp, z, sigma_z, sigma_y, coord='y'):
    term_1 = []
    term_1p = []
    term_2 = []
    term_2p = []
    for particle_y, particle_yp, particle_z in zip(y, yp, z):
        if particle_z > 0.9*sigma_z and particle_z < 1.1*sigma_z:
            term_1.append(particle_y)
            term_1p.append(particle_yp)
        if particle_z > -1.1*sigma_z and particle_z < -0.9*sigma_z:
            term_2.append(particle_y)
            term_2p.append(particle_yp)
    if coord == 'y':
        dy_plus, cs = do_floquet(-0.000764, 0.150235, 3.35*1e-10, term_1, term_1p, 0.0, 0.000295)
        dy_minus, cs = do_floquet(-0.000764, 0.150235, 3.35*1e-10, term_2, term_2p, 0.0, 0.000295)
    elif coord == 'x':
        dy_plus, cs = do_floquet(0.003485, 0.150739, 3.35*1e-10, term_1, term_1p,  -0.000750, 0.0)
        dy_minus, cs = do_floquet(0.003485, 0.150739, 3.35*1e-10, term_2, term_2p, -0.000750, 0.0)
    return abs(dy_plus - dy_minus)/2
    return (np.mean(term_1) - np.mean(term_2))/2*sigma_z

def phase_space(alpha, beta, c, cp):
    return beta*cp + alpha*c

outfile = 'parameters.txt'
try:
    os.remove(outfile)
except OSError:
    pass
    
# ------------------------------------------------------------------------------
# DATA EXTRACTION
# ------------------------------------------------------------------------------
get = GetData(infile)
data = get.data_column()

x_tot= np.asarray(data[3], dtype='float64')* 1e-3 - orbit_x
xp_tot= np.asarray(data[4], dtype='float64')* 1e-3 - orbit_xp
y_tot= np.asarray(data[5], dtype='float64')* 1e-3 - orbit_y
yp_tot= np.asarray(data[6], dtype='float64')* 1e-3 - orbit_yp
z_tot= np.asarray( data[7] , dtype='float64')* 1e-3
e_tot= np.asarray( data[8] , dtype='float64')


particle_id=[]
for num, turn, x, xp, y, yp, z, e in zip(data[0], data[1], x_tot, xp_tot, y_tot, yp_tot, z_tot, e_tot):
    if turn==1:
        if abs(x) < 1e-6 and  abs(xp) < 1e-5 and abs(y) < 1e-6 and abs(yp) < 1e-5 and abs(z) <1e-2:
            particle_id.append(num)
print particle_id
x_f  = []
xp_f = []
y_f  = []
yp_f = []
t = []
for num, turn, x, xp, y, yp, z, e in zip(data[0], data[1], x_tot, xp_tot, y_tot, yp_tot, z_tot, e_tot):
    if num == particle_id[0]:
        x_f.append(x)
        xp_f.append(xp)
        y_f.append(y)
        yp_f.append(yp)
        t.append(turn)

# x_n  = []
# y_n  = []
# x_ps = []  # phase space
# y_ps = []
# for turn, x, xp, y, yp in zip(t, x_f, xp_f, y_f, yp_f):
#     x_n.append(do_floquet(beta_x, alpha_x, em_g, x, xp, True))
#     y_n.append(do_floquet(beta_y, alpha_y, em_g, y, yp, True))
#     x_ps.append(phase_space(alpha_x, beta_x, x, xp))
#     y_ps.append(phase_space(alpha_y, beta_y, y, yp))

# print len(t), len(x_n), len(y_n)

# for t, x, y in zip(t, x_n, y_n):
#     xp_n.append(phase_space(alpha_x, beta_x, ))


# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
# textwidth = 3.25
# textwidth = 8
font_spec = {"font.family": "serif", # use as default font
             "font.serif": ["Computer Modern Roman"], # custom serif font
             # "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":10,
             "font.weight":"bold",
            }
rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
# rcParams['figure.figsize']=textwidth, textwidth/1.2
rcParams['figure.figsize']=5, 3
rcParams.update(font_spec)



fig = plt.figure()
# plt.plot(x_f, xp_f, '--o', markersize=3, linewidth=0.3)
# plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
# plt.xlabel(r"$x$ [m]")
# plt.ylabel(r"$x'$ [rad]")
# for t,x,xp in zip(t, x_f, xp_f):
#     plt.annotate(str(t), xy=(x, xp), xytext=(x, xp + 0.5e-6), rotation='horizontal', size='4', horizontalalignment='center', verticalalignment='right')
# plt.subplots_adjust(left=0.17, bottom=0.15, right=0.96, top=0.90, wspace=0.18, hspace=0.16)
# plt.savefig('x_xp.png', dpi=DPI)
# plt.clf()

plt.plot(y_f, yp_f, '--o', markersize=3, linewidth=0.2)
tu=np.linspace(1,20,20)
for t,x,xp in zip(tu, y_f, yp_f):
    plt.annotate(str(t), xy=(x, xp), xytext=(x, xp + 0.1*1e-4), rotation='horizontal', size='4', horizontalalignment='center', verticalalignment='bottom')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.xlabel(r"$y$ [m]")
plt.ylabel(r"$y'$ [rad]")
plt.ylim([-2*1e-4, 3*1e-4])
# plt.subplots_adjust(left=0.14, bottom=0.15, right=0.96, top=0.90, wspace=0.18, hspace=0.16)
# plt.savefig('y_yp_z.png', dpi=DPI)
plt.subplots_adjust(left=0.15, bottom=0.20, right=0.85, top=0.91)
plt.savefig('phase_space_4cc_c.eps', format='eps', dpi=1500)
plt.clf()
    
# for i,j
# def get_turns(coord, turns):
#     d = {}
#     for t in set(turns):
#         d[t] = []
#     for t, c in zip(turns, coord):
#         d[t].append(c)
#     counter = 0
#     for item in d.keys():
#         counter = counter + len(d[item])
#     if counter != len(coord):
#         print '>> Dictionary was not correctly created'
#     return d

# x = get_turns(x_tot, turns)
# xp = get_turns(xp_tot, turns)
# y = get_turns(y_tot, turns)
# yp = get_turns(yp_tot, turns)
# z = get_turns(z_tot, turns)
# e = get_turns(e_tot, turns)



# for turn in set(turns):
#     c =0
#     x_n = []
#     xp_n = []
#     y_n = []
#     yp_n = []
#     x_f = []
#     xp_f = []
#     y_f = []
#     yp_f = []
#     for x_turn, xp_turn, y_turn, yp_turn in zip(x[turn], xp[turn], y[turn], yp[turn]):
#         if abs(x_turn) < 1*e-6:
#             print 'yes'
    #     i, j= do_floquet(beta_x, alpha_x, em_g, x_turn, xp_turn, False)
    #     x_n.append(i)
    #     xp_n.append(j)
    #     k, l= do_floquet(beta_y, alpha_y, em_g, y_turn, yp_turn, False)
    #     y_n.append(k)
    #     yp_n.append(l)
    # # print np.std(x_n)
    # for i, j in zip(x_n, xp_n):
    #     if (i**2 + j**2)/np.sqrt(em_g) <= np.std(x[2]):
    #         x_f.append(i)
    #         xp_f.append(j)
    # for i, j in zip(y_n, yp_n):
    #     if (i**2 + j**2)/np.sqrt(em_g) <= np.std(y[2]):
    #         y_f.append(i)
    #         yp_f.append(j)
    # xx = np.linalg.norm(np.array([np.mean(x_f), np.mean(xp_f)]))/np.sqrt(em_g)
    # yy = np.linalg.norm(np.array([np.mean(y_f), np.mean(yp_f)]))/np.sqrt(em_g)
    # print turn, xx, yy
        
            
            
    #         c=c+1
    # print turn,c
    # print turn, len(x_n)
        # dy = do_floquet(beta_y, alpha_y, em_g, y_turn, yp_turn)
        # print dx, dy

# x_2 = np.asarray(x[2], dtype='float64')* 1e-3
# xp_2 = np.asarray(xp[2], dtype='float64')* 1e-3
# y_2 = np.asarray(y[2], dtype='float64')* 1e-3
# yp_2 = np.asarray(yp[2], dtype='float64')* 1e-3

# sigma_x = np.std(x_2 - orbit_x)
# sigma_xp = np.std(xp_2 - orbit_xp)
# sigma_y = np.std(y_2 - orbit_y)
# sigma_yp = np.std(yp_2 - orbit_yp)


# c=0
# xt=[]
# xpt=[]
# for i, j in zip(x_2 - orbit_x, xp_2):
#     if abs(i) < sigma_x and abs(j) < sigma_xp:
#         c=c+1
#         xt.append(i)
#         xpt.append(j)

# for turn in set(data[1]):
#     for xx, xxp, yy, yyp in zip(x[turn], xp[turn], y[turn], yp[turn]):
#         print xx



# with open(outfile, 'a') as g:
#     print >> g, '# TURN DX DY'
#     for turn in set(data[1]):
#         x_turn = []
#         xp_turn = []
#         y_turn = []
#         yp_turn = []
#         for xx, xxp, yy, yyp in zip(x[turn], xp[turn], y[turn], yp[turn]):
#             print xx, sigma_x
            # if abs(xx) < sigma_x:
                # print 'yes'
        #         x_turn.append(np.mean(xx*1e-3 - orbit_x))
        #         xp_turn.append(np.mean(xxp*1e-3 - orbit_xp))
        #     elif abs(yy) < sigma_y:
        #         y_turn.append(np.mean(yy*1e-3 - orbit_y))
        #         yp_turn.append(np.mean(yyp*1e-3 - orbit_yp))
        # print x_turn
            # dx = do_floquet(beta_x, alpha_x, em_g, x_turn, xp_turn)
        # xp_turn = np.mean(np.asarray(xp[turn], dtype='float64') * 1e-3 - orbit_xp)
        # y_turn = np.mean(np.asarray(y[turn], dtype='float64') * 1e-3 - orbit_y)
        # yp_turn = np.mean(np.asarray(yp[turn], dtype='float64') * 1e-3 - orbit_yp)
        # z_turn = np.asarray(z[turn], dtype='float64') * 1e-3
        # e_turn = np.asarray(e[turn], dtype='float64')
        # dx = do_floquet(beta_x, alpha_x, em_g, x_turn, xp_turn)
        # dy = do_floquet(beta_y, alpha_y, em_g, y_turn, yp_turn)
        # print turn, dx, dy
        # print >> g, turn, "{:.2E}".format(dx), "{:.2E}".format(dy), "{:.2E}".format(dx)

# plt.scatter(x[1], xp[1])
# plt.scatter(xt, xpt)

# plt.show()