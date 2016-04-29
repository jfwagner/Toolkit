#!/usr/bin/env python
import re
import sys
import subprocess
import time
start = time.time()

import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import font_manager
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from matplotlib import ticker
from scipy.stats import gaussian_kde

from util import GetData
from util import get_bucket
from util import get_ellipse_coords

# ------------------------------------------------------------------------------
# COMMAND LINE ARGUMENTS
# ------------------------------------------------------------------------------
infile = sys.argv[1]
turn_first = int(sys.argv[2])
turn_last = int(sys.argv[3])
nbins = int(sys.argv[4])

turn_range = range(turn_first, turn_last + 1)

# ------------------------------------------------------------------------------
# DATA EXTRACTION
# ------------------------------------------------------------------------------
get = GetData(infile)
data = get.data_column()

turns = data[1]
x_tot = data[3]
xp_tot = data[4]
y_tot = data[5]
yp_tot = data[6]
z_tot = data[7]
e_tot = data[8]

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

x = get_turns(x_tot, turns)
xp = get_turns(xp_tot, turns)
y = get_turns(y_tot, turns)
yp = get_turns(yp_tot, turns)
z = get_turns(z_tot, turns)
e = get_turns(e_tot, turns)

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
# Working fonts: Old Standard, Playfair Display, DejaVu Serif, Droid Serif, Lato
# Roboto, STIXGeneral
# ------------------------------------------------------------------------------
DPI = 500
textwidth = 3.25

font_spec = {"font.family": "Old Standard",  # use as default font
             "font.size": 5,
             # "font.weight":"bold",
             }

rcParams['axes.unicode_minus'] = False
# rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')

rcParams['figure.figsize'] = textwidth, textwidth
rcParams.update(font_spec)

fig = plt.figure()


def plot_2d_hist(coord_1, coord_2, nbins):
    H, xedges, yedges = np.histogram2d(coord_1, coord_2, bins=nbins)
    H = np.rot90(H)   # H needs to be rotated and flipped
    H = np.flipud(H)
    Hmasked = np.ma.masked_where(H == 0, H)  # Mask pixels with a value of zero (they will appear in white)
    plt.pcolormesh(xedges, yedges, Hmasked, norm=None, vmin=0, vmax=100)

phi, delta, h = get_bucket()  # Londitudinal contour

# Getting and drawing sigma ellipses
def get_sigma_ellipse(sigma_x, sigma_y, offset_x, offset_y, number):
    d = {}
    for n in range(0, number + 1):
        d[n] = get_ellipse_coords(a=n*sigma_x, b=n*sigma_y, x=offset_x, y=offset_y, k=1)
    return d

sigma_x_xp = get_sigma_ellipse(7.16610376198e-06, 4.76160858517e-05, -7.5e-4, 0, 10)
sigma_y_yp = get_sigma_ellipse(7.12405639107e-06, 4.75602973547e-05, 0, 0.3e-3, 10)
sigma_z_x = get_sigma_ellipse(0.0745803056032, 7.16610376198e-06, 0, -7.5e-4, 10)
sigma_z_y = get_sigma_ellipse(0.0745803056032, 7.12405639107e-06, 0, 0, 10)
sigma_x_y = get_sigma_ellipse(7.16610376198e-06, 7.12405639107e-06, -7.5e-4, 0, 10)

def plot_sigma(my_dict, number):
    for n in range(0, number + 1):
        plt.plot(my_dict[n][:,0], my_dict[n][:,1], color='gray', linewidth=0.2)
    
for turn in turn_range:
    x_plot = np.asarray(x[turn], dtype='float64') * 1e-3
    xp_plot = np.asarray(xp[turn], dtype='float64') * 1e-3
    y_plot = np.asarray(y[turn], dtype='float64') * 1e-3
    yp_plot = np.asarray(yp[turn], dtype='float64') * 1e-3
    z_plot = np.asarray(z[turn], dtype='float64') * 1e-3
    e_plot = np.asarray(e[turn], dtype='float64')

    ax1 = fig.add_subplot(321)
    plot_2d_hist(x_plot, xp_plot, nbins)
    plot_sigma(sigma_x_xp, 10)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax1.set_xlabel(r"$x$ [m]")
    ax1.set_ylabel(r"$x'$ [m]")
    ax1.set_xlim([-8.5e-4, -6.5e-4])
    ax1.set_ylim([-5e-4, 5e-4])

    ax2 = fig.add_subplot(322)
    plot_2d_hist(y_plot, yp_plot, nbins)
    plot_sigma(sigma_y_yp, 10)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax2.set_xlabel(r"$y$ [m]")
    ax2.set_ylabel(r"$y'$ [m]")
    ax2.set_xlim([-8e-5, 8e-5])
    ax2.set_ylim([-2e-4, 8e-4])

    ax3 = fig.add_subplot(323)
    plot_2d_hist(z_plot, x_plot, nbins)
    plot_sigma(sigma_z_x, 10)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax3.set_xlabel(r"$z$ [m]")
    ax3.set_ylabel(r"$x$ [m]")
    ax3.set_xlim([-0.4, 0.4])
    ax3.set_ylim([-8.5e-4, -6.5e-4])

    ax4 = fig.add_subplot(324)
    plot_2d_hist(z_plot, y_plot, nbins)
    plot_sigma(sigma_z_y, 10)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax4.set_xlabel(r"$z$ [m]")
    ax4.set_ylabel(r"$y$ [m]")
    ax4.set_xlim([-0.4, 0.4])
    ax4.set_ylim([-8e-5, 8e-5])

    ax5 = fig.add_subplot(325)
    plot_2d_hist(x_plot, y_plot, nbins)
    plot_sigma(sigma_x_y, 10)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax5.set_xlabel(r"$x$ [m]")
    ax5.set_ylabel(r"$y$ [m]")
    ax5.set_xlim([-8.5e-4, -6.5e-4])
    ax5.set_ylim([-8e-5, 8e-5])

    ax6 = fig.add_subplot(326)
    plot_2d_hist(z_plot, e_plot, nbins)
    plt.contour(phi, delta, h, 40, linewidths=0.2, cmap='terrain_r')
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax6.set_ylabel(r"$\Delta E / E$")
    ax6.set_xlabel(r"$z$ [m]")
    ax6.set_xlim([-0.4, 0.4])
    ax6.set_ylim([-5e-4, 5e-4])

    plt.suptitle('    Turn {}'.format(turn), fontsize=8, fontweight='bold')

    plt.tight_layout()
    # plt.show()
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.90, wspace=0.4, hspace=0.6)
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig('dist_turn_{:02d}.png'.format(turn), dpi=DPI)
    plt.clf()

    ax = fig.add_subplot(111, projection='3d')
    xy = np.vstack([x_plot,z_plot,y_plot])
    m = gaussian_kde(xy)(xy)
    ax.scatter(x_plot, z_plot, y_plot, linewidth=0, s=0.5, c=m)
    ax.set_xlabel(r"$x$ [m]")
    ax.set_ylabel(r"$z$ [m]")
    ax.set_zlabel(r"$y$ [m]")
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='z', scilimits=(0, 0))
    ax.set_xlim([-8e-4, -7e-4])
    ax.set_zlim([-4e-5, 4e-5])
    ax.set_ylim([-0.3, 0.3])
    ax.set_title('Turn {}'.format(turn), fontsize=8, fontweight='bold')
    # for angle in range(0, 360):
    #     ax.view_init(30, angle)
    # plt.show()

    plt.savefig('dist3d_turn_{:02d}.png'.format(turn), dpi=DPI)
    plt.clf()


bashCommand = "convert -delay 70 -loop 0 dist_turn* dist.gif; convert -delay 70 -loop 0 dist3d_turn* dist3d.gif;rm -rf img; mkdir img; mv *.png img"
output = subprocess.check_output(['bash', '-c', bashCommand])

print 'It took', time.time() - start, 'seconds for a', len(x_tot), 'line file'
