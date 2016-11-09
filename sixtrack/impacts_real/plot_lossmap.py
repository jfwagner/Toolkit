#!/usr/bin/python
# ------------------------------------------------------------------------------
# USAGE: plot_lossmap.py B2 core tail
# or: plot_lossmap.py B2 to analyze in place without weights
# ------------------------------------------------------------------------------
import glob
import operator
import os
import re
import sys

import numpy as np
import matplotlib

from collections import defaultdict
from decimal import Decimal
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

beam = sys.argv[1]
title = sys.argv[2]

print len(sys.argv)

if len(sys.argv) == 5:
    print ' '
    print '>> Working with core and tail'
    dir_core = sys.argv[3]
    dir_tail = sys.argv[4]
elif len(sys.argv) == 2:
    print ' '
    sys.exit('>> Tail directory missing. Aborting.')
elif len(sys.argv) == 3:
    print ' '
    print '>> Working in current directory'

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
# font = {'family':'serif', 'serif': ['computer modern roman']}
# plt.rc('font',**font)
rcParams['figure.figsize'] = 4, 2
params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{mathrsfs}']}
plt.rcParams.update(params)
rcParams['legend.frameon'] = 'True'
fig = plt.figure()

# ------------------------------------------------------------------------------
# Function to deal with core and tail data files
# ------------------------------------------------------------------------------


def get_dist(data_file, dir_core, dir_tail, core_weight, tail_weight):

    if data_file == 'loss_maps.txt':
        col_1 = 1
        col_2 = 3
    elif data_file == 'aperture.txt':
        col_1 = 0
        col_2 = 2

    x = []
    y = []
    if os.path.isfile(dir_core + '/' + data_file) and os.path.isfile(dir_tail + '/' + data_file):
        print ' '
        print '>> File ' + data_file + ' present for core and tail'

        get_core = GetData(dir_core + '/' + data_file)
        data_core = get_core.data_column(dtype='string')
        xc_coll = data_core[col_1]
        yc_coll = data_core[col_2]

        get_tail = GetData(dir_tail + '/' + data_file)
        data_tail = get_tail.data_column(dtype='string')
        xt_coll = data_tail[col_1]
        yt_coll = data_tail[col_2]

        for i, k in zip(xc_coll, yc_coll):
            for j, l in zip(xt_coll, yt_coll):
                if i == j:

                    x.append(float(i))
                    y.append(core_weight * float(k) + tail_weight * float(l))
                    xc_coll.remove(i)
                    yc_coll.remove(k)
                    xt_coll.remove(j)
                    yt_coll.remove(l)

        for i, k in zip(xc_coll, yc_coll):
            x.append(float(i))
            y.append(core_weight * float(k))
        for j, l in zip(xt_coll, yt_coll):
            x.append(float(j))
            y.append(tail_weight * float(l))

    elif os.path.isfile(dir_core + '/' + data_file) == False:
        print ' '
        print '>> File ' + data_file + ' present only for tail'

        get_tail = GetData(dir_tail + '/' + data_file)
        data_tail = get_tail.data_column(dtype='string')
        xt_coll = data_tail[col_1]
        yt_coll = data_tail[col_2]
        for j, l in zip(xt_coll, yt_coll):
            x.append(float(j))
            y.append(tail_weight * float(l))

    elif os.path.isfile(dir_tail + '/' + data_file) == False:
        print ' '
        print '>> File ' + data_file + ' present only for core'

        get_core = GetData(dir_core + '/' + data_file)
        data_core = get_core.data_column(dtype='string')
        xc_coll = data_core[col_1]
        yc_coll = data_core[col_2]
        for j, l in zip(xc_coll, yc_coll):
            x.append(float(j))
            y.append(core_weight * float(l))
    return x, y

# ------------------------------------------------------------------------------
# Different options if core and tail directories are present or not
# ------------------------------------------------------------------------------
ax1 = fig.add_subplot(111)
b1 = {}
b2 = {}
ips = np.linspace(1, 8, 8)

b1_pos = [800, 3332.436584, 6664.7208, 9997.005016,
          13329.28923, 16661.72582, 19994.1624,  23315.37898]
for i, j in zip(ips, b1_pos):
    b1[i] = j

b2_pos = [800, 23326.59898,  19994.1624, 16661.72582,
          13329.28923,  9997.005016,  6664.7208,  3343.656584]
for i, j in zip(ips, b2_pos):
    b2[i] = j


def plot_ip_labels(thedict, height, size):
    for i, j in zip(thedict.keys(), thedict.values()):
        if i == 1 or i == 2 or i == 5 or i == 8:
            my_ip = 'IP'
        if i == 3 or i == 4 or i == 6 or i == 7:
            my_ip = 'IR'
        ax1.annotate(my_ip + str(int(i)), xy=(1, height), xytext=(j, height),
                     weight='bold', va='bottom', ha='center', size=size, color='red')


if len(sys.argv) == 5:
    x_coll, y_coll = get_dist('loss_maps.txt', dir_core, dir_tail, 0.95, 0.05)
    x_ap, y_ap = get_dist('aperture.txt', dir_core, dir_tail, 0.95, 0.05)
    plt.bar(x_coll, y_coll, align="center",
            linewidth=0, width=60, color="black", label="Collimation: " + "{:.2E}".format(Decimal(np.sum(y_coll))) + " \%")
    plt.bar(x_ap, y_ap, color="green",
                align="center", linewidth=0, width=60, label="Aperture: " + "{:.2E}".format(Decimal(np.sum(y_ap))) + " \%")
    plt.xlabel("Position (m)")
    plt.ylabel(r'Percentage of bunch lost')
    plt.xlim([0, 26658.883])
    plt.title(title)
    plt.legend(loc='best', prop={'size': 5}).get_frame().set_linewidth(0.5)
    ax1.set_yscale('log')
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color='gray', linestyle='-', which="minor", linewidth=0.1)

    height = max(y_coll) / 200
    text_size = 5
    if beam == 'B1':
        plot_ip_labels(b1, height, text_size)
    elif beam == 'B2':
        plot_ip_labels(b2, height, text_size)
    else:
        print '>> Please input B1 or B2 as first argument'

    plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
    plt.savefig('loss_map.png', dpi=1000)
    plt.savefig('loss_map.eps', format='eps', dpi=1000)
    plt.clf()


elif len(sys.argv) == 3:
    files = glob.glob('*.txt')
    for txt in files:
        if txt == 'loss_maps.txt':
            print ' '
            print '>> File ' + txt + ' present'
            get = GetData(txt)
            data = get.data_column(dtype='string')
            x_coll = np.asarray(data[1], dtype='float64')
            y_coll = np.asarray(data[3], dtype='float64')
        elif txt == 'aperture.txt':
            print ' '
            print '>> File ' + txt + ' present'
            get = GetData(txt)
            data = get.data_column(dtype='string')
            x_ap = np.asarray(data[0], dtype='float64')
            y_ap = np.asarray(data[2], dtype='float64')
    # ------------------------------------------------------------------------------
    # Plotting lossmaps
    # ------------------------------------------------------------------------------
    if os.path.exists('loss_maps.txt') == False and os.path.exists('aperture.txt') == False:
        sys.exit('>> No losses')
    else:
        if os.path.exists('loss_maps.txt') and os.path.exists('aperture.txt') == False:
            plt.bar(x_coll, y_coll, align="center",
                    linewidth=0, width=60, color="black", label="Collimation: " + "{:.2E}".format(Decimal(np.sum(y_coll)))  + " \%")
            plt.xlabel("Position (m)")
            plt.ylabel(r'Percentage of bunch lost')
            plt.xlim([0, 26658.883])
            plt.legend(loc='best', prop={'size': 5}).get_frame().set_linewidth(0.5)
            ax1.set_yscale('log')
            plt.title(title)
            ax1.set_axisbelow(True)
            ax1.yaxis.grid(color='gray', linestyle='-', which="minor", linewidth=0.1)
        elif os.path.exists('aperture.txt') and os.path.exists('loss_maps.txt') == False:
            plt.bar(x_ap, y_ap, color="green",
                        align="center", linewidth=0, width=60, label="Aperture: " + "{:.2E}".format(Decimal(np.sum(y_ap))) + " \%")
            plt.xlabel("Position (m)")
            plt.ylabel(r'Percentage of bunch lost')
            plt.xlim([0, 26658.883])
            plt.title(title)
            plt.legend(loc='best', prop={'size': 5}).get_frame().set_linewidth(0.5)
            ax1.set_yscale('log')
            ax1.set_axisbelow(True)
            ax1.yaxis.grid(color='gray', linestyle='-', which="minor", linewidth=0.1)
        elif os.path.exists('aperture.txt') and os.path.exists('loss_maps.txt'):
            plt.bar(x_coll, y_coll, align="center",
                    linewidth=0, width=60, color="black", label="Collimation: " + "{:.2E}".format(Decimal(np.sum(y_coll)))  + " \%")
            plt.bar(x_ap, y_ap, color="green",
                        align="center", linewidth=0, width=60, label="Aperture: " + "{:.2E}".format(Decimal(np.sum(y_ap))) + " \%")
            plt.xlabel("Position (m)")
            plt.ylabel(r'Percentage of bunch lost')
            plt.xlim([0, 26658.883])
            plt.title(title)
            plt.legend(loc='best', prop={'size': 5}).get_frame().set_linewidth(0.5)
            ax1.set_yscale('log')
            ax1.set_axisbelow(True)
            ax1.yaxis.grid(color='gray', linestyle='-', which="minor", linewidth=0.1)
            
            height = max(y_coll) / 200
            text_size = 5
            if beam == 'B1':
                plot_ip_labels(b1, height, text_size)
            elif beam == 'B2':
                plot_ip_labels(b2, height, text_size)
            else:
                print '>> Please input B1 or B2 as first argument'

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

if len(sys.argv) == 5:
    files_ccoll = glob.glob(dir_core + '/t*.txt')
    print ' '
    print '>>', len(files_ccoll), 'collimator files have been found in ' + dir_core
    if len(files_ccoll) != 0:
        d_core = {}
        for txt in files_ccoll:
            xc, yc, namec = get_turns(txt)
            d_core[namec.replace(dir_core.upper() + '/', '')] = yc

    files_tcoll = glob.glob(dir_tail + '/t*.txt')
    print ' '
    print '>>', len(files_tcoll), 'collimator files have been found in ' + dir_tail
    if len(files_tcoll) != 0:
        d_tail = {}
        for txt in files_tcoll:
            xt, yt, namet = get_turns(txt)
            d_tail[namet.replace(dir_tail.upper() + '/', '')] = yt

    d = {}

    if len(files_ccoll) != 0 and len(files_tcoll) != 0:
        for i, j in zip(d_core.keys(), d_core.values()):
            for k, l in zip(d_tail.keys(), d_tail.values()):
                if i == k:
                    d[i] = np.asarray(j) * 0.95 + np.asarray(l) * 0.05

        for i, j in zip(d.keys(), d.values()):
            for k, l in zip(d_core.keys(), d_core.values()):
                if i != k:
                    d[k] = np.asarray(l) * 0.95

        for i, j in zip(d.keys(), d.values()):
            for k, l in zip(d_tail.keys(), d_tail.values()):
                if i != k:
                    d[k] = np.asarray(l) * 0.05

    elif len(files_ccoll) != 0 and len(files_tcoll) == 0:
        for k, l in zip(d_core.keys(), d_core.values()):
            d[k] = np.asarray(l) * 0.95

    elif len(files_ccoll) == 0 and len(files_tcoll) != 0:
        for k, l in zip(d_tail.keys(), d_tail.values()):
            d[k] = np.asarray(l) * 0.05


elif len(sys.argv) == 3:
    files_coll = glob.glob('t*.txt')
    d = {}
    for txt in files_coll:
        x, y, name = get_turns(txt)
        d[name] = y

# After this part, a dictionary named "d" must contain the information of losses
#  per turn for each collimator.

# ------------------------------------------------------------------------------
# Sort the created dictionary by number of losses
# ------------------------------------------------------------------------------
sorted_d = sorted(d.items(), key=lambda x: sum(x[1]), reverse=True)
x_t = np.linspace(1, len(d[d.keys()[0]]), len(d[d.keys()[0]]))  # turns


def plot_coll(coll_name, d, sorted_d, x_t):
    number = 0
    for name in d.keys():
        if name.startswith(coll_name):
            number += 1
    if coll_name == 'TCP':
        my_map = matplotlib.cm.terrain
    elif coll_name == 'TCS':
        my_map = matplotlib.cm.terrain
    elif coll_name == 'TCT':
        my_map = matplotlib.cm.terrain
    counter = 0
    for i in range(0, int(len(sorted_d))):
        if sorted_d[i][0].startswith(coll_name):
            counter += 1
            cmap = my_map
            plt.bar(x_t, sorted_d[i][1], label=str(sorted_d[i][0]),
                    color=cmap((float(counter)) / (1.7 * float(number))), linewidth=0)
            plt.legend(bbox_to_anchor=(1, 0.5), loc='center left',
                       prop={'size': 4}).get_frame().set_linewidth(0.5)
            plt.xlabel('Turns')
            plt.ylabel(r'Percentage of bunch lost')
            plt.xlim([0, max(x_t)])
            plt.title(title)
            plt.yscale('log')
            # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
            plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
            # plt.savefig(coll_name + '.png', dpi=1000)
            fig.savefig(coll_name + '.png', dpi=1000, bbox_inches='tight')
            plt.savefig(coll_name + '.eps', format='eps', dpi=1000)
    plt.clf()


plot_coll('TCP', d, sorted_d, x_t)
plot_coll('TCS', d, sorted_d, x_t)
plot_coll('TCT', d, sorted_d, x_t)


# ------------------------------------------------------------------------------
# Losses per collimator group
# ------------------------------------------------------------------------------
def get_cumulative_loss(sorted_d, name):
    cumulated = []
    d = defaultdict(list)
    for i in range(0, int(len(sorted_d))):
        if sorted_d[i][0].startswith(name):
            for t in range(0, len(sorted_d[i][1])):
                d[t].append(sorted_d[i][1][t])
    for t in range(0, len(sorted_d[i][1])):
        cumulated.append(sum(d[t]))
    return cumulated

names = ['tcp', 'tcs', 'tct', 'tcl']
ax = fig.add_subplot(111)
themap = matplotlib.cm.terrain

number = 0
for n in names:
    number += 1
    tc = get_cumulative_loss(sorted_d, n.upper())
    if sum(tc) != 0:
        ax.bar(x_t, tc, label=n.upper(),
               color=themap(float(number) / (1.5 * float(len(names)))), linewidth=0)

lgd = ax.legend(bbox_to_anchor=(1, 0.5), loc='center left',
                prop={'size': 4}).get_frame().set_linewidth(0.5)
plt.xlabel('Turns')
plt.ylabel(r'Percentage of bunch lost')
plt.xlim([0, max(x_t)])
plt.yscale('log')
plt.title(title)
fig.savefig('all_colls.png', dpi=1000, bbox_inches='tight')
plt.savefig('all_colls.eps', format='eps', dpi=1000)
plt.clf()
