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
title = sys.argv[2]
file_name = sys.argv[3]
infile_2 = sys.argv[4]
title_2 = sys.argv[5]


get = GetData(infile)
data = get.data_column()

turns = np.asarray(data[0], dtype='float64')
dx = np.asarray(data[1], dtype='float64')
dy = np.asarray(data[2], dtype='float64')
angle_x = np.asarray(data[3], dtype='float64')
angle_y = np.asarray(data[4], dtype='float64')
em_x = np.asarray(data[5], dtype='float64')
em_y = np.asarray(data[6], dtype='float64')
# sigma_x = np.asarray(data[7], dtype='float64')
# sigma_y = np.asarray(data[8], dtype='float64')

# ------------------------------------------------------------------------------
# Decaying voltage np.asarray(data loading
# ------------------------------------------------------------------------------
get_2 = GetData(infile_2)
data_2 = get_2.data_column()

turns_2 = np.asarray(data_2[0], dtype='float64')
dx_2 = np.asarray(data_2[1], dtype='float64')
dy_2 = np.asarray(data_2[2], dtype='float64')
angle_x_2 = np.asarray(data_2[3], dtype='float64')
angle_y_2 = np.asarray(data_2[4], dtype='float64')
em_x_2 = np.asarray(data_2[5], dtype='float64')
em_y_2 = np.asarray(data_2[6], dtype='float64')
# sigma_x_2 = np.asarray(data_2[7], dtype='float64')
# sigma_y_2 = np.asarray(data_2[8], dtype='float64')

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

# ------------------------------------------------------------------------------
# Constant voltage
# ------------------------------------------------------------------------------
maxi = max (dy)
for i, j in zip(turns, dy):
    if j == maxi:
        my = j
        t = i
print t, my

txt = max(dy_2)*(0.5)

# ax1 = fig.add_subplot(221)
# plt.axvline(x=0, linewidth=0.7, color='black')
# plt.axvline(x=5, linewidth=0.7, color='black')
# plt.scatter(turns-5, dy, color='blue', label='YZ Angle', s=3)
# plt.scatter(turns-5, dx, color='red', label='XZ Angle', s=3)
# plt.plot(turns-5, dy, color='blue', linewidth=0.5)
# plt.plot(turns-5, dx, color='red', linewidth=0.5)
# ax1.annotate("Max = " + str(my) + r"$\sigma$", xy=(8, max(dy)*1.1), xytext=(8, max(dy)*1.1), rotation='horizontal', size='4')
# plt.legend(loc='upper left', prop={'size': 4})
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
# plt.xlim([-5,15])
# plt.ylim([-max(dy)*0.1,max(dy)*1.3])
# fig.text(0.04, 0.5, r'Normalized [$\sigma$]', ha='center', va='center', rotation='vertical')
# plt.setp(ax1.get_xticklabels(), visible=False)

ax1 = fig.add_subplot(221)
ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
plt.axvline(x=0, linewidth=0.7, color='black')
plt.axvline(x=5, linewidth=0.7, color='black')
plt.scatter(turns-5, em_y, color='blue', label='Y displacement', s=3)
plt.scatter(turns-5, em_x, color='red', label='X displacement', s=3)
plt.plot(turns-5, dy, color='blue', linewidth=0.5)
plt.plot(turns-5, dx, color='red', linewidth=0.5)
ax1.annotate('Failure starts', xy=(-1, txt), xytext=(-1, txt), rotation='vertical', size='4', verticalalignment='center')
ax1.annotate('Failure ends', xy=(4, txt), xytext=(4, txt), rotation='vertical', size='4', verticalalignment='center')
ax1.annotate("Max = " + str(my) + r"$\sigma$", xy=(8, max(dy)*1.1), xytext=(8, max(dy)*1.1), rotation='horizontal', size='4')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.title(title)
plt.xlim([-5,15])
plt.ylim([-max(dy)*0.1,max(dy)*1.3])
plt.legend(loc='upper left', prop={'size': 4})
plt.setp(ax1.get_xticklabels(), visible=False)


maxi = max (angle_y)
for i, j in zip(turns, angle_y):
    if j == maxi:
        my = j
        t = i
print t, my

ax2 = fig.add_subplot(223)
plt.axvline(x=0, linewidth=0.7, color='black')
plt.axvline(x=5, linewidth=0.7, color='black')
plt.scatter(turns-5, angle_y, color='blue', label='YZ Angle', s=3)
plt.scatter(turns-5, angle_x, color='red', label='XZ Angle', s=3)
plt.plot(turns-5, angle_y, color='blue', linewidth=0.5)
plt.plot(turns-5, angle_x, color='red', linewidth=0.5)
ax2.annotate("Max = " + str(my) + r"$\sigma$", xy=(8, max(angle_y)*1.1), xytext=(8, max(angle_y)*1.1), rotation='horizontal', size='4')
plt.legend(loc='upper left', prop={'size': 4})
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.xlim([-5,15])
plt.ylim([-max(angle_y)*0.1,max(angle_y)*1.3])
plt.xlabel('Turns')
fig.text(0.04, 0.5, r'Normalized [$\sigma$]', ha='center', va='center', rotation='vertical')


# ------------------------------------------------------------------------------
# Decaying voltage
# ------------------------------------------------------------------------------
maxi = max (dy_2)
for i, j in zip(turns_2, dy_2):
    if j == maxi:
        my = j
        t = i
print t, my
    

ax3 = fig.add_subplot(222)
plt.axvline(x=0, linewidth=0.7, color='black')
plt.axvline(x=5, linewidth=0.7, color='black')
plt.scatter(turns_2-5, em_y_2, color='blue', label='Y displacement', s=3)
plt.scatter(turns_2-5, em_x_2, color='red', label='X displacement', s=3)
plt.plot(turns_2-5, dy_2, color='blue', linewidth=0.5)
plt.plot(turns_2-5, dx_2, color='red', linewidth=0.5)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
ax3.annotate('Failure starts', xy=(-1, txt), xytext=(-1, txt), rotation='vertical', size='4', verticalalignment='center')
ax3.annotate('Failure ends', xy=(4, txt), xytext=(4, txt), rotation='vertical', size='4', verticalalignment='center')
ax3.annotate("Max = " + str(my) + r"$\sigma$", xy=(8, max(dy)*1.1), xytext=(8, max(dy)*1.1), rotation='horizontal', size='4')
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_yticklabels(), visible=False)
plt.title(title_2)
plt.xlim([-5,15])
plt.ylim([-max(dy)*0.1,max(dy)*1.3])
plt.legend(loc='upper left', prop={'size': 4})


maxi = max (angle_y_2)
for i, j in zip(turns_2, angle_y_2):
    if j == maxi:
        my = j
        t = i
print t, my

ax4 = fig.add_subplot(224)
plt.axvline(x=0, linewidth=0.7, color='black')
plt.axvline(x=5, linewidth=0.7, color='black')
plt.scatter(turns_2-5, angle_y_2, color='blue', label='YZ Angle', s=3)
plt.scatter(turns_2-5, angle_x_2, color='red', label='XZ Angle', s=3)
plt.plot(turns_2-5, angle_y_2, color='blue', linewidth=0.5)
plt.plot(turns_2-5, angle_x_2, color='red', linewidth=0.5)
ax4.annotate("Max = " + str(my) + r"$\sigma$", xy=(8, max(angle_y)*1.1), xytext=(8, max(angle_y)*1.1), rotation='horizontal', size='4')
plt.legend(loc='upper left', prop={'size': 4})
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.xlim([-5,15])
plt.ylim([-max(angle_y)*0.1,max(angle_y)*1.3])
plt.xlabel('Turns')
fig.text(0.04, 0.5, r'Normalized [$\sigma$]', ha='center', va='center', rotation='vertical')
plt.setp(ax4.get_yticklabels(), visible=False)
plt.tight_layout()
plt.subplots_adjust(left=0.14, bottom=0.12, right=0.96, top=0.90, wspace=0.18, hspace=0.16)
# plt.show()
plt.savefig(file_name + '.png', dpi=DPI)
plt.clf()
