#!/usr/bin/env python
import operator
import os
import sys

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import rc
from matplotlib import rcParams

from operator import itemgetter

from util import GetData


# --------------------------------------------------------------------
# Extract the data
# --------------------------------------------------------------------
infile = 'imp_real_data.txt'
get = GetData(infile)


def get_turn(tau):
    my_data = get.data_column(column=0, regex=tau)
    return my_data[0], my_data[1], my_data[2], my_data[3]

tau_1, phase_1, bunch_1, detuning_1 = get_turn(r'1')
tau_2, phase_2, bunch_2, detuning_2 = get_turn(r'2')
tau_3, phase_3, bunch_3, detuning_3 = get_turn(r'3')
tau_4, phase_4, bunch_4, detuning_4 = get_turn(r'4')


def get_max(tau, phase, bunch, detuning):
    return max(zip(tau, phase, bunch, detuning), key=lambda item: item[2])


def get_phase(tau, phase, bunch, detuning):
    for i, j, k, l in zip(tau, phase, bunch, detuning):
        if l == 3:
            return i, j, k, l


def get_max_3k(tau, phase, bunch, detuning):
    t = []
    p = []
    b = []
    d = []
    for i, j, k, l in zip(tau, phase, bunch, detuning):
        if l <= 3:
            t.append(i)
            p.append(j)
            b.append(k)
            d.append(l)
    return max(zip(t, p, b, d), key=lambda item: item[2])

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
# Plot characteristics
DPI = 300
textwidth = 6
font_spec = {"font.family": "serif",  # use as default font
             "font.serif": ["New Century Schoolbook"],  # custom serif font
             "font.sans-serif": ["helvetica"],  # custom sans-serif font
             "font.size": 12,
             "font.weight": "bold",
             }
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize'] = textwidth, textwidth / 1.618
rcParams.update(font_spec)
el = Ellipse((2, -1), 0.5, 0.5)

# ------------------------------------------------------------------------------
# Phase vs Losses
# ------------------------------------------------------------------------------
plt.scatter(phase_1, bunch_1, marker="+", color="blue", label='1 turn')
plt.scatter(phase_2, bunch_2, marker="+",  color="red", label='2 turns')
plt.scatter(phase_3, bunch_3, marker="+", color="green", label='3 turns')
plt.scatter(phase_4, bunch_4, marker="+",  color="orange", label='4 turns')

plt.xlabel("Phase shift (deg)")
plt.ylabel(r"Bunch lost (\%)")
plt.xlim([0, 360])
# plt.ylim([0,100])
plt.grid(b=None, which='major')
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.legend(loc='upper left', prop={'size': 6})
plt.subplots_adjust(left=0.13, bottom=0.14, right=0.94, top=0.93)
plt.savefig('phase_losses.png', dpi=DPI)
plt.clf()


# ------------------------------------------------------------------------------
# Detuning vs Losses
# ------------------------------------------------------------------------------
plt.scatter(detuning_1, bunch_1, marker="+", color="blue", label='1 turn')
plt.scatter(detuning_2, bunch_2, marker="+",  color="red", label='2 turns')
plt.scatter(detuning_3, bunch_3, marker="+", color="green", label='3 turns')
plt.scatter(detuning_4, bunch_4, marker="+",  color="orange", label='4 turns')


def get_loss(detuning, bunch, phase):
    x = []
    y = []
    p = []
    for i, j, k in zip(detuning, bunch, phase):
        if i <= 3:
            x.append(i)
            y.append(j)
            p.append(k)
    return max(zip(x, y, p), key=lambda item: item[1])

x1, y1, p1 = get_loss(detuning_1, bunch_1, phase_1)
plt.annotate(str(y1), xy=(x1, y1), xytext=(x1 - 0.2 * x1, y1 + 0.1 * y1), size='11', color='blue',
             arrowprops=dict(arrowstyle="wedge,tail_width=0.7", fc="0.6", ec="none", patchB=el, connectionstyle="arc3,rad=-0.3"))

x2, y2, p2 = get_loss(detuning_2, bunch_2, phase_2)
plt.annotate(str(y2), xy=(x2, y2), xytext=(x2 - 0.2 * x2, y2 + 0.1 * y2), size='11', color='red',
             arrowprops=dict(arrowstyle="wedge,tail_width=0.7", fc="0.6", ec="none", patchB=el, connectionstyle="arc3,rad=-0.3"))

x3, y3, p3 = get_loss(detuning_3, bunch_3, phase_3)
plt.annotate(str(y3), xy=(x3, y3), xytext=(x3 - 0.2 * x3, y3 + 0.1 * y3), size='11', color='green',
             arrowprops=dict(arrowstyle="wedge,tail_width=0.7", fc="0.6", ec="none", patchB=el, connectionstyle="arc3,rad=-0.3"))

x4, y4, p4 = get_loss(detuning_4, bunch_4, phase_4)
plt.annotate(str(y4), xy=(x4, y4), xytext=(x4 - 0.2 * x4, y4 + 0.1 * y4), size='11', color='orange',
             arrowprops=dict(arrowstyle="wedge,tail_width=0.7", fc="0.6", ec="none", patchB=el, connectionstyle="arc3,rad=-0.3"))


plt.xlabel("Detuning (kHz)")
plt.ylabel(r"Bunch lost (\%)")
plt.xlim([0, 3])
# plt.ylim([0,100])
# plt.grid(b=None, which='major')
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.legend(loc='upper left', prop={'size': 6})
plt.subplots_adjust(left=0.13, bottom=0.14, right=0.94, top=0.93)
plt.savefig('detuning_losses.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Detuning
# ------------------------------------------------------------------------------
plt.scatter(detuning_1, phase_1, marker="+", color="blue", label='1 turn')
plt.scatter(detuning_2, phase_2, marker="+",  color="red", label='2 turns')
plt.scatter(detuning_3, phase_3, marker="+", color="green", label='3 turns')
plt.scatter(detuning_4, phase_4, marker="+",  color="orange", label='4 turns')
plt.annotate('96', xy=(3, 96), xytext=(4.3, 100), size='11', color='blue', arrowprops=dict(arrowstyle="wedge,tail_width=0.7",
                                                                                           fc="0.6", ec="none", patchB=el, connectionstyle="arc3,rad=-0.3"))
plt.annotate('192', xy=(3, 192), xytext=(4, 210), size='11', color='red', arrowprops=dict(arrowstyle="wedge,tail_width=0.7",
                                                                                          fc="0.6", ec="none", patchB=el, connectionstyle="arc3,rad=-0.3"))
plt.annotate('276', xy=(3, 276), xytext=(3.7, 300), size='11', color='green', arrowprops=dict(arrowstyle="wedge,tail_width=0.7",
                                                                                              fc="0.6", ec="none", patchB=el, connectionstyle="arc3,rad=-0.3"))
plt.axvspan(3, 12, alpha=0.2, color='blue')
plt.ylabel("Phase shift (deg)")
plt.xlabel(r"Detuning (kHz)")
plt.ylim([0, 360])
plt.xlim([0, 12])
# plt.grid(b=None, which='major')
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.legend(loc='lower right', prop={'size': 8})
plt.subplots_adjust(left=0.13, bottom=0.14, right=0.94, top=0.93)
plt.savefig('phase_detuning.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Writing output file
# ------------------------------------------------------------------------------
outfile = 'summary.txt'
try:
    os.remove(outfile)
except OSError:
    pass

with open(outfile, 'w') as log:
    print >> log, 'Tau | Phase(deg) | Max Bunch Lost (%) | Detuning (kHz)'
    print >> log, '------------------------------------------------------------------------'
    print >>log, get_max(tau_1, phase_1, bunch_1, detuning_1)
    print >>log, get_max(tau_2, phase_2, bunch_2, detuning_2)
    print >>log, get_max(tau_3, phase_3, bunch_3, detuning_3)
    print >>log, get_max(tau_4, phase_4, bunch_4, detuning_4)
    print >> log, ' '
    print >> log, 'Tau | Phase(deg) | Detuning <= 3 (kHz)| Max Bunch Lost (%)'
    print >> log, '------------------------------------------------------------------------'
    print >>log, '1', p1, x1, y1
    print >>log, '2', p2, x2, y2
    print >>log, '3', p3, x3, y3
    print >>log, '4', p4, x4, y4
    print >> log, ' '
    print >> log, 'Tau | Max Phase(deg) | Bunch Lost (%) | Detuning (kHz)'
    print >> log, '------------------------------------------------------------------------'
    print >>log, get_phase(tau_1, phase_1, bunch_1, detuning_1)
    print >>log, get_phase(tau_2, phase_2, bunch_2, detuning_2)
    print >>log, get_phase(tau_3, phase_3, bunch_3, detuning_3)
    print >>log, get_phase(tau_4, phase_4, bunch_4, detuning_4)
