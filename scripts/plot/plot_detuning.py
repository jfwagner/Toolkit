#!/usr/bin/env python
import sys
import numpy as np
from math import degrees
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams


def detune_1(k, v, t, tau):
    return ((-k * (v**2) * tau) / 2) * np.exp((-2 * t) / tau)


def detune_2(f, t):
    return -f * 2 * np.pi * t


def exp(t, tau):
    return np.exp(-t / tau)

k2 = 346
k = 86
# k=0.4
tau = 400e-6
v = 3.4
t = np.linspace(0, 400e-6, 400)
f = 1000
f2 = 4000

phase_rad = detune_2(f, t)
phase_deg = []
for angle in phase_rad:
    phase_deg.append(degrees(angle))

phase_rad_2 = detune_2(f2, t)
phase_deg_2 = []
for angle in phase_rad_2:
    phase_deg_2.append(degrees(angle))

exp = exp(t, tau)

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

plt.plot(t, phase_deg, label='1 kHz (86.5 Hz/MV$^2$)')
plt.plot(t, phase_deg_2, label='4 kHz (346 Hz/MV$^2$)')
plt.xlabel('Time (s)')
plt.ylabel('Phase (deg)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.grid(b=None, which='major')
plt.subplots_adjust(left=0.13, bottom=0.14, right=0.94, top=0.93)
plt.legend(loc='lower left', prop={'size': 10})
# plt.show()
plt.savefig('detuning.png', dpi=DPI)
plt.clf()

fig, ax1 = plt.subplots()
ax1.plot(t, exp, 'b')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('V/V$_0$')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax2 = ax1.twinx()
ax2.plot(t, phase_deg, 'r')
ax2.set_ylabel('Phase (deg)')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
# plt.grid(b=None, which='major')
plt.subplots_adjust(left=0.10, bottom=0.14, right=0.87, top=0.93)
plt.savefig('voltage.png', dpi=DPI)
plt.clf()
# plt.show()
