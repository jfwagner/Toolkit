#!/usr/bin/env python
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from numpy import *
from util import *

# ------------------------------------------------------------------------------
# Define your input DUMP file
# ------------------------------------------------------------------------------
infile = "sixtrack/dump_ip1.txt"

# ------------------------------------------------------------------------------
# Specify how many turns you want to read
# ------------------------------------------------------------------------------
total_turns = 100

# ------------------------------------------------------------------------------
# Relativistic parameters
# ------------------------------------------------------------------------------
gamma_rel = 7460.52280875
beta_rel = 0.999999991017

# ------------------------------------------------------------------------------
# Initialization of arrays
# ------------------------------------------------------------------------------
t = zeros(total_turns)
    
term_1_x = zeros(total_turns)
term_2_x = zeros(total_turns)
term_3_x = zeros(total_turns)
term_4_x = zeros(total_turns)

term_1_y = zeros(total_turns)
term_2_y = zeros(total_turns)
term_3_y = zeros(total_turns)
term_4_y = zeros(total_turns)

det_x = zeros(total_turns)
em_x = zeros(total_turns)

det_y = zeros(total_turns)
em_y = zeros(total_turns)

# ------------------------------------------------------------------------------
# Extraction and treatment of data
# ------------------------------------------------------------------------------
for turn in range(1, total_turns + 1):
    turn_i = '%s' %turn
    x = get_dump(infile, turn_i, 3)
    xp = get_dump(infile, turn_i, 4)
    y = get_dump(infile, turn_i, 5)
    yp = get_dump(infile, turn_i, 6)
    # Sigma matrix for X
    term_1_x[turn-1] = mean(multiply(x,x)) - multiply(mean(x), mean(x))
    term_2_x[turn-1] = mean(multiply(x,xp)) - multiply(mean(x),mean(xp))
    term_3_x[turn-1] = mean(multiply(xp,x)) - multiply(mean(xp), mean(x))
    term_4_x[turn-1] = mean(multiply(xp,xp)) - multiply(mean(xp),mean(xp))

    det_x[turn-1] = multiply(term_1_x[turn-1], term_4_x[turn-1]) - multiply(term_3_x[turn-1], term_2_x[turn-1])
    em_x[turn-1] = sqrt(abs(det_x[turn-1]))*beta_rel*gamma_rel

    # Sigma matrix for Y
    term_1_y[turn-1] = mean(multiply(y,y)) - multiply(mean(y), mean(y))
    term_2_y[turn-1] = mean(multiply(y,yp)) - multiply(mean(y),mean(yp))
    term_3_y[turn-1] = mean(multiply(yp,y)) - multiply(mean(yp), mean(y))
    term_4_y[turn-1] = mean(multiply(yp,yp)) - multiply(mean(yp),mean(yp))

    det_y[turn-1] = multiply(term_1_y[turn-1], term_4_y[turn-1]) - multiply(term_3_y[turn-1], term_2_y[turn-1])
    em_y[turn-1] = sqrt(abs(det_y[turn-1]))*beta_rel*gamma_rel

    t[turn-1] = turn

print em_x
print em_y

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 300
textwidth = 4
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

# ------------------------------------------------------------------------------
# Plot the emittance
# ------------------------------------------------------------------------------
plt.plot(t, em_x, 'b', label='X')
plt.plot(t, em_y, 'r', label='Y')
plt.grid(b=None, which='major')
plt.legend(loc='lower right')
plt.xlabel('Turns')
plt.ylabel(r'$\epsilon_n$ [m]')
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.tight_layout()
plt.savefig('emittance_vs_turns.png', dpi=DPI)
plt.close()

# ------------------------------------------------------------------------------
# Plot the mean
# ------------------------------------------------------------------------------
plt.plot(t, mean_x, 'b', label='X')
plt.plot(t, mean_y, 'r', label='Y')
plt.grid(b=None, which='major')
plt.legend(loc='upper left')
plt.xlabel('Turns')
plt.ylabel('Mean [m]')
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.savefig('mean_vs_turns.png', dpi=DPI)
plt.close()

# ---------------
# Plot the tunes
# ---------------
FFT_x = abs(scipy.fft(mean_x))
freqs_x = scipy.fftpack.fftfreq(mean_x.size, total_turns[1]-total_turns[0])

FFT_y = abs(scipy.fft(mean_y))
freqs_y = scipy.fftpack.fftfreq(mean_y.size, total_turns[1]-total_turns[0])

pylab.plot(freqs_y, FFT_y,  'r',label = 'Y')
pylab.plot(freqs_x, FFT_x,  'b',label = 'X')
# pylab.plot(freqs_y,scipy.log10(FFT_x), 'rx',label = 'X')
# pylab.plot(freqs_y,scipy.log10(FFT_y), 'bx',label = 'Y')
plt.title('Absolute value of FFT of the means')
plt.grid(b=None, which='major')
plt.legend(loc = 'upper left')
plt.xlabel('Tune')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.savefig('fft.png', dpi=DPI)
plt.close()
