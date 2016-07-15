#!/usr/bin/env python
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from util import *

# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
infile = sys.argv[1]
id_col = float(sys.argv[2])
name = '%s' % sys.argv[3]
orientation = str(sys.argv[4])
halfgap = float(sys.argv[5]) * 10**3
total_particles = sys.argv[6]

# ------------------------------------------------------------------------------
# ############################## IMPACTS REAL ############################
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Extract losses in the aperture
# ------------------------------------------------------------------------------
from datetime import datetime
start_time = datetime.now()
s_tct, x_tct, y_tct = load_data_coll(infile, sys.argv[2])

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 300
textwidth = 6
rc('font', **{'family': 'serif',
              'serif': ['Computer Modern Roman'], 'size': 10})
rc('text', usetex=True)
rcParams['figure.figsize'] = textwidth, textwidth / 1.618

# ------------------------------------------------------------------------------
# Plot the impacts on the collimator in x-y
# ------------------------------------------------------------------------------
plt.scatter(x_tct, y_tct, marker=(5, 2))
plt.grid(b=None, which='major')
plt.xlabel("x [mm]")
plt.ylabel("y [mm]")
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.grid(b=None, which='major')
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_xy.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Coordinate dependent plots
# ------------------------------------------------------------------------------
if orientation == 'vertical':
    coord_tct = y_tct
    my_label = "y [mm]"
elif orientation == 'horizontal':
    coord_tct = x_tct
    my_label = "x [mm]"

# ------------------------------------------------------------------------------
# Impacts on the collimator in coord-s
# ------------------------------------------------------------------------------
plt.scatter(s_tct, coord_tct, marker=(5, 2))
plt.grid(b=None, which='major')
plt.xlabel("s [m]")
plt.ylabel(my_label)
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.grid(b=None, which='major')
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_scoord.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Histogram of coord
# ------------------------------------------------------------------------------
n, bins, patches = plt.hist(
    coord_tct, 100, color='green', alpha=0.8, linewidth=0.1)
plt.bar(halfgap, max(n), color='blue', log=False, width=0.0005,
        align='center', edgecolor='blue', linewidth=0.1)
plt.bar(-1 * halfgap, max(n), color='blue', log=False, width=0.0005,
        align='center', edgecolor='blue', linewidth=0.1)
x_halfgap = np.linspace(-1 * halfgap, halfgap)
plt.fill_between(x_halfgap, max(n), facecolor='blue',
                 alpha=0.2, label='Gap', linewidth=0.1)
plt.xlabel(my_label)
plt.grid(b=None, which='major')
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.legend(loc='upper right', prop={'size': 6})
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_histogram_coord.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Histogram of the impact parameter
# ------------------------------------------------------------------------------
abs_coord = []
for e1 in coord_tct:
    abs_coord.append(abs(e1) - halfgap)

plt.hist(abs_coord, 100, color='green', alpha=0.8, linewidth=0.1)
plt.xlabel("Impact parameter (mm)")
plt.grid(b=None, which='major')
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_histogram_impact_parameter.png', dpi=DPI)
plt.clf()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
