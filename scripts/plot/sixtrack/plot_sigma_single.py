#!/usr/bin/env python

import sys

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

# ------------------------------------------------------------------------------
# Constant voltage data loading
# ------------------------------------------------------------------------------
infile = sys.argv[1]
# title = sys.argv[2]

get = GetData(infile)
data = get.data_column()

turns = np.asarray(data[0], dtype='float64')
dx = np.asarray(data[1], dtype='float64')
dy = np.asarray(data[2], dtype='float64')
cx = np.asarray(data[3], dtype='float64')
cy = np.asarray(data[4], dtype='float64')

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
DPI = 500
textwidth = 3.25
font_spec = {"font.family": "serif", # use as default font
             # "font.serif": ["New Century Schoolbook"], # custom serif font
             # "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":8,
             "font.weight":"bold",
            }
rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.2
rcParams.update(font_spec)



fig = plt.figure()


ax1 = fig.add_subplot(111)
# plt.axvline(x=0, linewidth=0.7, color='black')
# plt.axvline(x=5, linewidth=0.7, color='black')
for item in set(turns):
    sx_t = []
    sy_t = []
    for t, sx, sy, csx, csy in zip(turns, dx, dy, cx, cy):
        if t == item:
            sx_t.append(sx)
            sy_t.append(sy)
    print item, len(sx_t)
            # n, bins, patches = plt.hist(sy_t, 50, normed=1, facecolor='blue', alpha=0.75, label='Y')
            # plt.scatter(item, sy, color='blue', label='Y', s=3)
            # plt.scatter(item, sx, color='red', label='X', s=3)
# plt.scatter(turns_2-5, angle_x_2, color='red', label='XZ Angle', s=3)
# plt.plot(turns_2-5, angle_y_2, color='blue', linewidth=0.5)
# plt.plot(turns_2-5, angle_x_2, color='red', linewidth=0.5)
# ax1.annotate("Max = " + str(my) + r"$\sigma$", xy=(8, max(angle_y)*1.1), xytext=(8, max(angle_y)*1.1), rotation='horizontal', size='4')
# plt.legend(loc='upper left', prop={'size': 4})
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
# plt.xlim([-5,15])
# plt.ylim([-max(angle_y)*0.1,max(angle_y)*1.3])
# plt.xlabel('Turns')
# fig.text(0.04, 0.5, r'Normalized [$\sigma$]', ha='center', va='center', rotation='vertical')
# plt.setp(ax1.get_yticklabels(), visible=False)
# plt.tight_layout()
# plt.subplots_adjust(left=0.14, bottom=0.12, right=0.96, top=0.90, wspace=0.18, hspace=0.16)
# plt.show()
            # plt.savefig('dist_turn_{}.png'.format(t), dpi=DPI)
            # plt.clf()
