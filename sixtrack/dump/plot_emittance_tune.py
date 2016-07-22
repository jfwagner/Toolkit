#!/usr/bin/env python
import sys

from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from operator import itemgetter

import numpy as np
import scipy
import pylab

from util import GetData
from util import get_rel_params

# ------------------------------------------------------------------------------
# Define your input DUMP file
# ------------------------------------------------------------------------------
infile = sys.argv[1]
total_turns = np.int(sys.argv[2])

# ------------------------------------------------------------------------------
# Relativistic parameters
# ------------------------------------------------------------------------------
gamma_rel, beta_rel, p0, mass = get_rel_params(26e9)

# ------------------------------------------------------------------------------
# Initialization of arrays
# ------------------------------------------------------------------------------
t = np.zeros(total_turns)

term_1_x = np.zeros(total_turns)
term_2_x = np.zeros(total_turns)
term_3_x = np.zeros(total_turns)
term_4_x = np.zeros(total_turns)

term_1_y = np.zeros(total_turns)
term_2_y = np.zeros(total_turns)
term_3_y = np.zeros(total_turns)
term_4_y = np.zeros(total_turns)

det_x = np.zeros(total_turns)
em_x = np.zeros(total_turns)

det_y = np.zeros(total_turns)
em_y = np.zeros(total_turns)

mean_x = np.zeros(total_turns)
mean_y = np.zeros(total_turns)

# ------------------------------------------------------------------------------
# Extraction and treatment of data
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

tset=list(set(turns))

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

x_p = get_turns(x_tot, turns)
xp_p = get_turns(xp_tot, turns)
y_p = get_turns(y_tot, turns)
yp_p = get_turns(yp_tot, turns)
z_p = get_turns(z_tot, turns)
e_p = get_turns(e_tot, turns)


for turn in xrange(1, total_turns + 1):
    x = np.asarray(x_p[turn], dtype='float64') * 1e-3
    xp = np.asarray(xp_p[turn], dtype='float64') * 1e-3
    y = np.asarray(y_p[turn], dtype='float64') * 1e-3
    yp = np.asarray(yp_p[turn], dtype='float64') * 1e-3
    z = np.asarray(z_p[turn], dtype='float64') * 1e-3
    e = np.asarray(e_p[turn], dtype='float64')

    # Sigma matrix for X
    term_1_x[turn - 1] = np.mean(np.multiply(x, x)) - np.multiply(np.mean(x), np.mean(x))
    term_2_x[turn - 1] = np.mean(np.multiply(x, xp)) - np.multiply(np.mean(x), np.mean(xp))
    term_3_x[turn - 1] = np.mean(np.multiply(xp, x)) - np.multiply(np.mean(xp), np.mean(x))
    term_4_x[turn - 1] = np.mean(np.multiply(xp, xp)) - np.multiply(np.mean(xp), np.mean(xp))

    det_x[turn - 1] = np.multiply(term_1_x[turn - 1], term_4_x[turn - 1]) - \
        np.multiply(term_3_x[turn - 1], term_2_x[turn - 1])
    em_x[turn - 1] = np.sqrt(abs(det_x[turn - 1])) * beta_rel * gamma_rel
    mean_x[turn - 1] = np.mean(x)
     
    # Sigma matrix for Y
    term_1_y[turn - 1] = np.mean(np.multiply(y, y)) - np.multiply(np.mean(y), np.mean(y))
    term_2_y[turn - 1] = np.mean(np.multiply(y, yp)) - np.multiply(np.mean(y), np.mean(yp))
    term_3_y[turn - 1] = np.mean(np.multiply(yp, y)) - np.multiply(np.mean(yp), np.mean(y))
    term_4_y[turn - 1] = np.mean(np.multiply(yp, yp)) - np.multiply(np.mean(yp), np.mean(yp))

    det_y[turn - 1] = np.multiply(term_1_y[turn - 1], term_4_y[turn - 1]) - \
        np.multiply(term_3_y[turn - 1], term_2_y[turn - 1])
    em_y[turn - 1] = np.sqrt(abs(det_y[turn - 1])) * beta_rel * gamma_rel
    mean_y[turn - 1] = np.mean(y)

    t[turn - 1] = turn

print em_x
print em_y

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 3000
textwidth = 4
font_spec = {"font.family": "serif", # use as default font
             "font.serif": ["Computer Modern Roman"], # custom serif font
             # "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":10,
             "font.weight":"bold",
            }
rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/2
# rcParams['figure.figsize']=3, 1.7
rcParams.update(font_spec)

fig = plt.figure()

# ------------------------------------------------------------------------------
# Plot the emittance
# ------------------------------------------------------------------------------
plt.plot(t, em_x, '-o',label='X', markersize=2, linewidth=0.3)
plt.plot(t, em_y, '-o',label='Y', markersize=2, linewidth=0.3)
plt.grid(b=None, which='major')
plt.legend(loc='lower right', prop={'size': 5})
plt.xlabel('Turns')
plt.ylabel(r'$\epsilon_n$ [m]')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.savefig('emittance_vs_turns.eps', format='eps', dpi=1500)
plt.close()

# ------------------------------------------------------------------------------
# Plot the mean
# ------------------------------------------------------------------------------
plt.plot(t, mean_x,'-o', label='X', markersize=2, linewidth=0.3)
plt.plot(t, mean_y,'-o',label='Y', markersize=2, linewidth=0.3)
plt.axvline(x=10, linewidth=0.7, color='black')
# plt.grid(b=None, which='major')
plt.legend(loc='upper left', prop={'size': 5})
plt.xlabel('Turns')
plt.ylabel('Mean [m]')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.subplots_adjust(left=0.17, bottom=0.2, right=0.96, top=0.90, wspace=0.18, hspace=0.16)
# plt.show()
plt.savefig('mean_vs_turns.eps', format='eps', dpi=1500)
plt.savefig('mean_vs_turns.png', dpi=1500)
plt.close()

# ---------------
# Plot the tunes
# ---------------
FFT_x = abs(scipy.fft(mean_x))
freqs_x = np.fft.fftfreq(mean_x.size, t[1] - t[0])

xx = []
xy = []
x_fft = sorted(zip(freqs_x, FFT_x), key=itemgetter(0))
max_x = max(FFT_x)

for i, j in x_fft:
    xx.append(i)
    xy.append(j)
    if j == max_x:
        tune_x = abs(i)

print tune_x
    

FFT_y = abs(scipy.fft(mean_y))
freqs_y = np.fft.fftfreq(mean_y.size, t[1] - t[0])

yx = []
yy = []
y_fft = sorted(zip(freqs_y, FFT_y), key=itemgetter(0))
max_y = max(FFT_y)

for i, j in y_fft:
    yx.append(i)
    yy.append(j)
    if j == max_y:
        tune_y = abs(i)

print tune_y

plt.plot(yx, yy, '-o', label='Y', markersize=3, linewidth=0.5)
plt.plot(xx, xy, '-o', label='X', markersize=3, linewidth=0.5)
# pylab.plot(freqs_y,scipy.log10(FFT_x), 'rx',label = 'X')
# pylab.plot(freqs_y,scipy.log10(FFT_y), 'bx',label = 'Y')
# plt.title('Absolute value of FFT of the means')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.annotate("Fractional tune X = " + str(tune_x), xy=(-0.2, max(FFT_x)*0.8), xytext=(-0.2, max(FFT_x)*0.8), rotation='horizontal', size='5')
plt.annotate("Fractional tune Y = " + str(tune_y), xy=(-0.2, max(FFT_x)*0.78), xytext=(-0.2, max(FFT_x)*0.75), rotation='horizontal', size='5')
# plt.grid(b=None, which='major')
plt.legend(loc='upper left',prop={'size': 5})
plt.xlabel('Tune')
plt.ylabel('Amplitude')
plt.savefig('fft.eps', format='eps', dpi=1500)
plt.savefig('fft.png', dpi=1500)
plt.close()
