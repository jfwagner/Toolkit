#!/usr/bin/python
import glob
import operator
import os
import re
import sys

import numpy as np
import matplotlib

from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
rcParams['legend.frameon'] = 'True'
rcParams['figure.figsize'] = 4, 2
fig = plt.figure()

# ------------------------------------------------------------------------------
# Seeing which data files exist (created with get_losses.py)
# ------------------------------------------------------------------------------
files = glob.glob('*.txt')
for txt in files:
    if txt == 'loss_maps.txt':
        get = GetData(txt)
        data = get.data_column(dtype='string')
        x_coll = np.asarray(data[1], dtype='float64')
        y_coll = np.asarray(data[3], dtype='float64')
    elif txt == 'aperture.txt':
        get = GetData(txt)
        data = get.data_column(dtype='string')
        x_ap = np.asarray(data[0], dtype='float64')
        y_ap = np.asarray(data[2], dtype='float64')

# ------------------------------------------------------------------------------
# Plotting lossmaps
# ------------------------------------------------------------------------------
ax1 = fig.add_subplot(111)
plt.bar(x_coll, y_coll, align="center",
        linewidth=0, width=60, color="black", label="Collimation: " + str(round(np.sum(y_coll), 2)) + " \%")
if os.path.exists('aperture.txt'):
        plt.bar(x_ap, y_ap, color="green",
                align="center", linewidth=0, width=60, label="Aperture: " + str(round(np.sum(y_ap), 2)) + " \%")
plt.xlabel("Position (m)")
plt.ylabel("Number of Protons Lost")
plt.xlim([0, 26658.883])
plt.legend(loc='upper left', prop={'size': 6})
ax1.set_yscale('log')
ax1.set_axisbelow(True)
ax1.yaxis.grid(color='gray', linestyle='-', which="minor", linewidth=0.3)

height = max(y_coll) / 500
text_size = 5
ax1.annotate('IP2', xy=(1, height), xytext=(3332.4, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax1.annotate('IR3', xy=(1, height), xytext=(6664.721, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax1.annotate('IR4', xy=(1, height), xytext=(9997, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax1.annotate('IP5', xy=(1, height), xytext=(13329.28, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax1.annotate('IR6', xy=(1, height), xytext=(16661.7, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax1.annotate('IR7', xy=(1, height), xytext=(20000, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax1.annotate('IP8', xy=(1, height), xytext=(23315.4, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')

plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('loss_map.png', dpi=1000)
plt.savefig('loss_map.eps', format='eps', dpi=1000)
plt.clf()

# ------------------------------------------------------------------------------
# Losses per turn
# ------------------------------------------------------------------------------
ax2 = fig.add_subplot(111)

def get_turns(infile):
    get = GetData(infile)
    data = get.data_column()
    x = np.asarray(data[0], dtype='float64')
    y = np.asarray(data[2], dtype='float64')
    if 'b1' in infile:
        name = txt.replace('b1.txt', '').upper()
    elif 'b2' in infile:
        name = txt.replace('b2.txt', '').upper()
    elif infile == 'data_turn.txt':
        name = 'Collimation system'
    return x, y, name

files_coll = glob.glob('t*.txt')
d = {}
for txt in files_coll:
    x, y, name = get_turns(txt)
    d[name] = y

# ------------------------------------------------------------------------------
# Sort the created dictionary by number of losses
# ------------------------------------------------------------------------------
sorted_d = sorted(d.items(), key=lambda x: sum(x[1]), reverse=True)

x_t, y_t, name_t = get_turns('data_turn.txt')

def plot_coll(coll_name, x_t, y_t):
    if coll_name == 'TCP':
        my_map = matplotlib.cm.autumn
        number = 4.0
    elif coll_name == 'TCS':
        my_map = matplotlib.cm.winter
        number = 17.0
    elif coll_name == 'TCT':
        my_map = matplotlib.cm.spring
        number = 17.0
    counter = 0
    for i in range(0, int(len(sorted_d))):
        if sorted_d[i][0].startswith(coll_name):
            counter += 1
            print counter
            cmap = my_map
            plt.plot(x_t, sorted_d[i][1], label=str(sorted_d[i][0]),
                     color=cmap(counter / number))
            plt.fill_between(x,0,y,color=cmap(counter / number))
            plt.legend(loc='upper left', prop={'size': 5})
            plt.xlabel('Turns')
            plt.ylabel(r'Percentage of Beam Lost (\%)')
            plt.xlim([0, max(x_t)])
            plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
            plt.savefig(coll_name + '.png', dpi=1000)
            plt.savefig(coll_name + '.eps', format='eps', dpi=1000)
    plt.clf()


plot_coll('TCP', x_t, y_t)
plot_coll('TCS', x_t, y_t)
plot_coll('TCT', x_t, y_t)


