#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import rc
from matplotlib import rcParams
from scipy.optimize import curve_fit
from util import GetData

infile = 'after.txt'
obs_turns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
get = GetData(infile)

sigma = 7.09 * 1e-3  # [mm], emittance = 2.5 um

for t in obs_turns:
    my_data = get.data_column(column=1, regex='{}\\b'.format(t))
    p_id = my_data[0]
    turn = my_data[1]
    y = my_data[5]
    z = my_data[7]
    y_temp = []
    z_temp = []
    turn_temp = []
    for item, zt, tt in zip(y, z, turn):
        if zt >= 75 and zt <= 76:
            y_temp.append(item)
            z_temp.append(zt)
            turn_temp.append(tt)
    # m = np.polyfit(z_temp, y_temp, 1)
    # m = np.polyfit(z, y, 1)
    # print 'Turn', t, m[0]*1e6


# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
# Plot characteristics
DPI = 500
textwidth = 3.25
font_spec = {"font.family": "serif",  # use as default font
             # "font.serif": ["New Century Schoolbook"], # custom serif font
             # "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size": 8,
             "font.weight": "bold",
             }
rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize'] = textwidth, textwidth / 1.618
rcParams.update(font_spec)

n, bins, patches = plt.hist(
    z_temp, 50, facecolor='blue', alpha=0.5, linewidth=0.3)
plt.annotate('mean(y)= ' + str(round(np.mean(y_temp), 4)) +
             ' [mm]', xy=(-75.2, 3.5), size='7')
plt.xlabel(r'z [mm]')
# plt.xlabel(r'x [m]')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.ylabel('Beam Profile')
# ax.set_ylim([1e-4,1e0])
# ax.set_yscale('log')
# plt.legend(loc='upper left', prop={'size':6})
plt.subplots_adjust(left=0.17, bottom=0.20, right=0.94, top=0.90)
plt.savefig('hist_z_plus_after.png', dpi=DPI)
plt.clf()
