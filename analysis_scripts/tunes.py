import warnings
import numpy as np
from matplotlib import pyplot as plt
from numpy import dot
from random import gauss
# from sympy import *
from util import *
import pylab
import scipy
import scipy.fftpack
from matplotlib import rc
from matplotlib import rcParams

infile = "sixtrack/dump_ip1.txt"

DPI = 300
textwidth = 4
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

beta = 150 #mm
turns = 500
total_turns = np.zeros(turns)
mean_x = np.zeros(turns)
mean_y = np.zeros(turns)
sigma_x = np.zeros(turns)
sigma_y = np.zeros(turns)


for i in range(1, turns):
    xf, yf = get_dump(infile, 3, 5, i)
    x = np.asarray(xf)
    y = np.asarray(yf)
    mean_x[i] = np.mean(x)
    mean_y[i] = np.mean(y)
    sigma_x[i] = np.sigma(x)
    sigma_y[i] = np.sigma(y)
    total_turns[i] = i

print mean_x.size
print mean_y.size
print total_turns.size

# --------------
# Plot the mean
# --------------
plt.plot(total_turns, mean_x, 'b', label = 'X')
plt.plot(total_turns, mean_y, 'r', label = 'Y')
plt.title('Evolution of the mean with the number of turns')
plt.grid(b=None, which='major')
plt.legend(loc = 'lower left')
plt.xlabel('Turns')
plt.ylabel('<x> [mm]')
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.tight_layout()
plt.savefig('mean_vs_turns.png', dpi=DPI)
plt.close()

# -------------------
# Plot the emittance
# -------------------
em_x = sigma_x**2/beta
em_y = sigma_y**2/beta

plt.plot(total_turns, em_x, 'b', label = 'X')
plt.plot(total_turns, em_y, 'r', label = 'Y')
plt.title('Evolution of the emittance with the number of turns')
plt.grid(b=None, which='major')
plt.legend(loc = 'lower left')
plt.xlabel('Turns')
plt.ylabel(r'$\epsilon_n$ [mm]')
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.tight_layout()
plt.savefig('emittance_vs_turns.png', dpi=DPI)
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


