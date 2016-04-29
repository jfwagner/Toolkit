#!/usr/bin/env python
import re
import sys
import subprocess
import time
start = time.time()

import numpy as np
import matplotlib
from matplotlib import font_manager
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from matplotlib import ticker

from util import GetData
from util import get_bucket
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

rcParams['figure.figsize'] = textwidth, textwidth / 1.2
rcParams.update(font_spec)

fig = plt.figure()


def plot_2d_hist(coord_1, coord_2, nbins):
    H, xedges, yedges = np.histogram2d(coord_1, coord_2, bins=nbins)
    H = np.rot90(H)   # H needs to be rotated and flipped
    H = np.flipud(H)
    Hmasked = np.ma.masked_where(H == 0, H)  # Mask pixels with a value of zero
    plt.pcolormesh(xedges, yedges, Hmasked, norm=None, vmin=0, vmax=100)

phi, delta, h = get_bucket()

# ty = np.asarray(x[1], dtype='float64')
for turn in turn_range:
    x_plot = np.asarray(x[turn], dtype='float64') * 1e-3
    xp_plot = np.asarray(xp[turn], dtype='float64') * 1e-3
    y_plot = np.asarray(y[turn], dtype='float64') * 1e-3
    yp_plot = np.asarray(yp[turn], dtype='float64') * 1e-3
    z_plot = np.asarray(z[turn], dtype='float64') * 1e-3
    e_plot = np.asarray(e[turn], dtype='float64')

    ax1 = fig.add_subplot(221)
    plot_2d_hist(x_plot, xp_plot, nbins)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax1.set_xlabel("x [m]")
    ax1.set_ylabel(r"$x'$ [m]")
    ax1.set_xlim([-8.5e-4, -6.5e-4])
    ax1.set_ylim([-5e-4, 5e-4])

    ax2 = fig.add_subplot(222)
    plot_2d_hist(y_plot, yp_plot, nbins)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax2.set_xlabel("y [m]")
    ax2.set_ylabel(r"$y'$ [m]")
    ax2.set_xlim([-8e-5, 8e-5])
    ax2.set_ylim([-2e-4, 8e-4])

    ax3 = fig.add_subplot(223)
    plot_2d_hist(z_plot, y_plot, nbins)
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax3.set_xlabel("z [m]")
    ax3.set_ylabel("y [m]")
    ax3.set_xlim([-0.4, 0.4])
    ax3.set_ylim([-8e-5, 8e-5])

    ax4 = fig.add_subplot(224)
    plot_2d_hist(z_plot, e_plot, nbins)
    plt.contour(phi, delta, h, 40, linewidths=0.3, cmap='terrain_r')
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax4.set_ylabel(r"$\Delta E / E$")
    ax4.set_xlabel("z [m]")
    ax4.set_xlim([-0.4, 0.4])
    ax4.set_ylim([-5e-4, 5e-4])

    plt.suptitle('    Turn {}'.format(turn), fontsize=8, fontweight='bold')

    plt.tight_layout()
    # plt.show()
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.90, wspace=0.4)
    plt.savefig('dist_turn_{:02d}.png'.format(turn), dpi=DPI)
    plt.clf()

bashCommand = "convert -delay 70 -loop 0 *.png dist.gif; rm -rf img; mkdir img; mv *.png img"
output = subprocess.check_output(['bash', '-c', bashCommand])

print 'It took', time.time() - start, 'seconds for a', len(x_tot), 'line file'
