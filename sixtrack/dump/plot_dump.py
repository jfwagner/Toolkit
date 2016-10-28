#!/usr/bin/env python
import re
import sys
import subprocess
import time
start = time.time()

import numpy as np
import matplotlib
from matplotlib import cm
from matplotlib import font_manager
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from matplotlib import ticker
from scipy.stats import gaussian_kde
from matplotlib.ticker import FuncFormatter

from util import GetData
from util import get_bucket
from util import get_rel_params
from util import get_sigmas
from util import get_sigma_ellipse
from util import get_ellipse_coords
from util import plot_2d_hist
from util import plot_sigma

# ------------------------------------------------------------------------------
# COMMAND LINE ARGUMENTS
# ------------------------------------------------------------------------------
infile     = sys.argv[1]
machine    = sys.argv[2]
turn_first = int(sys.argv[3])
turn_last  = int(sys.argv[4])
nbins      = int(sys.argv[5])

turn_range = range(turn_first, turn_last + 1)

# ------------------------------------------------------------------------------
# DATA EXTRACTION
# ------------------------------------------------------------------------------
get  = GetData(infile)
data = get.data_column()

turns  = data[1]
x_tot  = data[3]
xp_tot = data[4]
y_tot  = data[5]
yp_tot = data[6]
z_tot  = data[7]
e_tot  = data[8]

# ------------------------------------------------------------------------------
# DATA ORGANIZATION IN TERMS OF TURNS
# ------------------------------------------------------------------------------


def get_turns(coord, turns):
    d = {}
    for t in set(turns):
        d[t] = []
    for t, c in zip(turns, coord):
        d[t].append(c)
    counter = 0
    for item in d.keys():
        counter = counter + len(d[item])
    if counter != len(coord):
        print '>> Dictionary was not correctly created'
    return d

x  = get_turns(x_tot, turns)
xp = get_turns(xp_tot, turns)
y  = get_turns(y_tot, turns)
yp = get_turns(yp_tot, turns)
z  = get_turns(z_tot, turns)
e  = get_turns(e_tot, turns)


# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
if machine=='HL_coll':
    gamma_rel, beta_rel, p0, mass = get_rel_params(7e12)
    alpha_x = 0.003485
    alpha_y = -0.000764
    beta_x = 0.150739
    beta_y = 0.150235
    
    sigma_x, sigma_xp = get_sigmas(alpha_x, beta_x, 2.5e-6, 0.003652, 1.13e-4, beta_rel, gamma_rel)
    sigma_y, sigma_yp = get_sigmas(alpha_y, beta_y, 2.5e-6, 0.000517, 1.13e-4, beta_rel, gamma_rel)
    sigma_z = 0.0755
    lines = 40
    
    offset_x  = -7.5e-4
    offset_xp = 0.0
    offset_y  = 0.0 
    offset_yp = 0.3e-3

    x_lim  = [-7.9e-4, -7.1e-4]
    xp_lim = [-3e-4, 3e-4]
    y_lim  = [-8e-5, 8e-5]
    yp_lim = [-1e-4, 6e-4]
    z_lim  = [-0.4, 0.4]
    e_lim  = [-4.5e-4, 4.5e-4]

    freq = '400'

elif machine=='HL_coll_tcp':
    gamma_rel, beta_rel, p0, mass = get_rel_params(7e12)
    alpha_x = 2.1177081
    alpha_y = -1.0986181
    beta_x = 158.417774
    beta_y = 78.495404
    
    sigma_x, sigma_xp = get_sigmas(alpha_x, beta_x, 3.5e-6, 0.0, 1.13e-4, beta_rel, gamma_rel)
    sigma_y, sigma_yp = get_sigmas(alpha_y, beta_y, 3.5e-6, 0.0, 1.13e-4, beta_rel, gamma_rel)
    sigma_z = 0.0755
    lines = 40
    
    offset_x  = 0.0
    offset_xp = 0.0
    offset_y  = 0.0 
    offset_yp = 0.0

    x_lim  = [-2e-3, 2e-3]
    xp_lim = [-2e-5, 2e-5]
    y_lim  = [-2e-3, 2e-3]
    yp_lim = [-3e-5, 3e-5]
    z_lim  = [-0.4, 0.4]
    e_lim  = [-4.5e-4, 4.5e-4]

    freq = '400'


elif machine=='HL_coll_tcp_200':
    gamma_rel, beta_rel, p0, mass = get_rel_params(7e12)
    alpha_x = 2.1177081
    alpha_y = -1.0986181
    beta_x = 158.417774
    beta_y = 78.495404
    
    sigma_x, sigma_xp = get_sigmas(alpha_x, beta_x, 3.5e-6, 0.0, 1.13e-4, beta_rel, gamma_rel)
    sigma_y, sigma_yp = get_sigmas(alpha_y, beta_y, 3.5e-6, 0.0, 1.13e-4, beta_rel, gamma_rel)
    sigma_z = 2*0.0755
    lines = 80
    
    offset_x  = 0.0
    offset_xp = 0.0
    offset_y  = 0.0 
    offset_yp = 0.0

    x_lim  = [-2e-3, 2e-3]
    xp_lim = [-2e-5, 2e-5]
    y_lim  = [-2e-3, 2e-3]
    yp_lim = [-3e-5, 3e-5]
    z_lim  = [-0.8, 0.8]
    e_lim  = [-4.5e-4, 4.5e-4]

    freq = '200'

elif machine=='HL_coll_200':
    gamma_rel, beta_rel, p0, mass = get_rel_params(7e12)

    alpha_x = 0.003485
    alpha_y = -0.000764
    beta_x = 0.150739
    beta_y = 0.150235
    
    sigma_x, sigma_xp = get_sigmas(alpha_x, beta_x, 2.5e-6, 0.003652, 1.13e-4, beta_rel, gamma_rel)
    sigma_y, sigma_yp = get_sigmas(alpha_y, beta_y, 2.5e-6, 0.000517, 1.13e-4, beta_rel, gamma_rel)
    sigma_z = 2*0.0755
    lines = 80
    
    offset_x  = -7.5e-4
    offset_xp = 0.0
    offset_y  = 0.0 
    offset_yp = 0.3e-3

    x_lim  = [-7.9e-4, -7.1e-4]
    xp_lim = [-3e-4, 3e-4]
    y_lim  = [-8e-5, 8e-5]
    yp_lim = [-1e-4, 6e-4]
    z_lim  = [-0.8, 0.8]
    e_lim  = [-4.5e-4, 4.5e-4]

    freq = '200'

elif machine=='SPS_inj':
    gamma_rel, beta_rel, p0, mass = get_rel_params(26e9)

    alpha_x = 1.50895801
    alpha_y = -1.392739114
    beta_x = 51.8375213
    beta_y = 46.54197726
    
    sigma_x, sigma_xp = get_sigmas(alpha_x, beta_x, 0.9e-6, 0.0, 10.7e-4, beta_rel, gamma_rel)
    sigma_y, sigma_yp = get_sigmas(alpha_y, beta_y, 3.0e-6, 0.0, 10.7e-4, beta_rel, gamma_rel)
    sigma_z = 0.3
    lines = 40
    
    offset_x  = 0.0
    offset_xp = 0.0
    offset_y  = 0.0 
    offset_yp = 0.0

    x_lim  = [-1e-2, 1e-2]
    xp_lim = [-0.5e-3, 0.5e-3]
    y_lim  = [-14e-3, 14e-3]
    yp_lim = [-4e-4, 4e-4]
    z_lim  = [-0.8, 0.8]
    e_lim  = [-8e-3, 8e-3]

    freq = '200'

else:
    print '>> Please choose "HL_coll" or "SPS_inj" (2nd argument)'

n_ellipses = 20
sigma_x_xp = get_sigma_ellipse(sigma_x, sigma_xp, offset_x, offset_xp, n_ellipses, alpha_x, beta_x)
sigma_y_yp = get_sigma_ellipse(sigma_y, sigma_yp, offset_y, offset_yp, n_ellipses, alpha_x, beta_x)
sigma_z_x  = get_sigma_ellipse(sigma_z, sigma_x, 0, offset_x, n_ellipses, 0, 0)
sigma_z_y  = get_sigma_ellipse(sigma_z, sigma_y, 0, offset_y, n_ellipses, 0, 0)
sigma_x_y  = get_sigma_ellipse(sigma_x, sigma_y, offset_x, offset_y, n_ellipses, 0, 0)

for turn in turn_range:
    x_plot  = np.asarray(x[turn],  dtype='float64') * 1e-3
    xp_plot = np.asarray(xp[turn], dtype='float64') * 1e-3
    y_plot  = np.asarray(y[turn],  dtype='float64') * 1e-3
    yp_plot = np.asarray(yp[turn], dtype='float64') * 1e-3
    z_plot  = np.asarray(z[turn],  dtype='float64') * 1e-3
    e_plot  = np.asarray(e[turn],  dtype='float64')
    
    # ------------------------------------------------------------------------------
    # rcParams['figure.figsize'] = 3.25, 3.25
    # fig = plt.figure()
    # ax1 = fig.add_subplot(321)
    # plot_2d_hist(x_plot, xp_plot, nbins)
    # plot_sigma(sigma_x_xp, 10)
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    # ax1.set_xlabel(r"$x$ [m]")
    # ax1.set_ylabel(r"$x'$ [m]")
    # ax1.set_xlim(x_lim)
    # ax1.set_ylim(xp_lim)

    # ax2 = fig.add_subplot(322)
    # plt.bar(0.924451437*1e-3, 6e-5, bottom=-3e-5, linewidth=0, color='gray', width=0.6, alpha=0.5)
    # plt.bar(-0.924451437*1e-3, 6e-5, bottom=-3e-5, linewidth=0, color='gray', width=-0.6, alpha=0.5)
    # plot_2d_hist(y_plot, yp_plot, nbins)
    # plot_sigma(sigma_y_yp, 10)
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    # ax2.set_xlabel(r"$y$ [m]")
    # ax2.set_ylabel(r"$y'$ [m]")
    # ax2.set_ylim(yp_lim)
    # ax2.set_xlim(y_lim)

    # ax3 = fig.add_subplot(323)
    # plot_2d_hist(z_plot, x_plot, nbins)
    # plot_sigma(sigma_z_x, 10)
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    # ax3.set_xlabel(r"$z$ [m]")
    # ax3.set_ylabel(r"$x$ [m]")
    # ax3.set_xlim(z_lim)
    # ax3.set_ylim(x_lim)

    # ax4 = fig.add_subplot(324)
    # plt.barh(0.924451437*1e-3, 0.6,  left=-0.3, linewidth=0, color='gray', height=1e-3, alpha=0.5)
    # plt.barh(-0.924451437*1e-3, 0.6, left=-0.3, linewidth=0, color='gray',  height=-1e-3, alpha=0.5)
    # plot_2d_hist(z_plot, y_plot, nbins)
    # plot_sigma(sigma_z_y, 10)
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    # ax4.set_xlabel(r"$z$ [m]")
    # ax4.set_ylabel(r"$y$ [m]")
    # ax4.set_xlim(z_lim)
    # ax4.set_ylim(y_lim)

    # ax5 = fig.add_subplot(325)
    # plt.barh(0.924451437*1e-3, 0.6, left=-0.4, linewidth=0, color='gray', height=1e-3, alpha=0.5)
    # plt.barh(-0.924451437*1e-3, 0.6, left=-0.4, linewidth=0, color='gray',  height=-1e-3, alpha=0.5)
    # plot_2d_hist(x_plot, y_plot, nbins)
    # plot_sigma(sigma_x_y, 10)
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    # ax5.set_xlabel(r"$x$ [m]")
    # ax5.set_ylabel(r"$y$ [m]")
    # ax5.set_xlim(x_lim)
    # ax5.set_ylim(y_lim)

    # zz, delta, h = get_bucket(machine) 
    # ax6 = fig.add_subplot(326)
    # plot_2d_hist(z_plot, e_plot, nbins)
    # plt.contour(zz, delta, h, lines, linewidths=0.2, cmap='terrain_r')
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    # ax6.set_ylabel(r"$\Delta E / E$")
    # ax6.set_xlabel(r"$z$ [m]")
    # ax6.set_xlim(z_lim)
    # ax6.set_ylim(e_lim)


    # plt.suptitle('    Turn {}'.format(turn) + ', ' + freq + 'MHz', fontsize=8, fontweight='bold')

    # plt.tight_layout()
    # plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.90, wspace=0.4, hspace=0.6)
    # plt.savefig('dist_turn_{:02d}.png'.format(turn), dpi=1000)
    # plt.clf()

    # ------------------------------------------------------------------------------
    font_spec = {"font.size": 5, }
    rcParams['figure.figsize'] = 4,2
    # params = {'text.latex.preamble': [r'\mathchardef\mhyphen="2D']}
    # rcParams['text.latex.unicode']=True
    plt.rcParams.update(font_spec)
    fig = plt.figure()
    ax7 = fig.add_subplot(121)
    halfgap = 0.1093825692E-02
    plt.bar(halfgap, 6e-5, bottom=-3e-5, linewidth=0, color='gray', width=0.6, alpha=0.5)
    plt.bar(-halfgap, 6e-5, bottom=-3e-5, linewidth=0, color='gray', width=-0.6, alpha=0.5)
    plot_2d_hist(y_plot, yp_plot, nbins)
    plot_sigma(sigma_y_yp, 20)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax7.set_xlabel(r"$y$ [m]")
    ax7.set_ylabel(r"$y'$ [rad]")
    ax7.set_ylim(yp_lim)
    ax7.set_xlim(y_lim)

    ax8 = fig.add_subplot(122)
    plot_2d_hist(z_plot, y_plot, nbins)
    plt.barh(halfgap, 0.6,  left=-0.3, linewidth=0, color='gray', height=1e-3, alpha=0.5)
    plt.barh(-halfgap, 0.6, left=-0.3, linewidth=0, color='gray',  height=-1e-3, alpha=0.5)
    plot_sigma(sigma_z_y, 20)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax8.set_xlabel(r"$z$ [m]")
    ax8.set_ylabel(r"$y$ [m]")
    ax8.set_xlim(z_lim)
    ax8.set_ylim(y_lim)

    # plt.suptitle('    Turn {}'.format(turn) + ', ' + freq + 'MHz', fontsize=8, fontweight='bold')
    plt.suptitle('    Turn {}'.format(turn), fontsize=8, fontweight='bold')
    # plt.suptitle('Crabbing at IP1', fontsize=8, fontweight='bold')
    plt.subplots_adjust(left=0.1, bottom=0.3, right=0.96, top=0.75, wspace=0.4, hspace=0.6)
    plt.savefig('vertical_plane_{:02d}.png'.format(turn), dpi=1000)
    plt.savefig('vertical_plane_{:02d}.eps'.format(turn),format='eps', dpi=1000)
    plt.clf()

    # ------------------------------------------------------------------------------
    # rcParams['figure.figsize'] = 3, 1.5
    # fig = plt.figure()
    # zz, delta, h = get_bucket(machine)
    # ax9 = fig.add_subplot(111)
    # plot_2d_hist(z_plot, e_plot, nbins)
    # plt.contour(zz, delta, h, lines, linewidths=0.2, cmap='terrain_r')
    # plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    # plt.title('    Turn {}'.format(turn) + ', ' + freq + 'MHz', fontsize=8, fontweight='bold')
    # ax9.set_ylabel(r"$\Delta E / E$")
    # ax9.set_xlabel(r"$z$ [m]")
    # ax9.set_xlim(z_lim)
    # ax9.set_ylim(e_lim)

    # plt.subplots_adjust(left=0.15, bottom=0.2, right=0.96, top=0.90, wspace=0.4, hspace=0.6)
    # plt.savefig('longitudinal_{:02d}.png'.format(turn), dpi=1000)
    # plt.savefig('longitudinal_{:02d}.eps'.format(turn),format='eps', dpi=1000)
    # plt.clf()

# bashCommand = "convert -delay 70 -loop 0 dist_turn* dist.gif;rm -rf img; mkdir img; mv *.png img"
# output = subprocess.check_output(['bash', '-c', bashCommand])