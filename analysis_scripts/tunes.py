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

infile = "../../sixtrack/dump.txt"

DPI = 300
textwidth = 4
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

turns = 200
total_turns = np.zeros(turns)
mean_x = np.zeros(turns)
mean_y = np.zeros(turns)

for i in range(1, turns):
    xf, yf = get_dump(infile, 3, 5, i)
    x = np.asarray(xf)
    y = np.asarray(yf)
    mean_x[i] = np.mean(x)
    mean_y[i] = np.mean(y)
    total_turns[i] = i

# Plot
print mean_x.size
print mean_y.size
print total_turns.size

plt.plot(total_turns, mean_x, 'b', label = 'X')
plt.plot(total_turns, mean_y, 'r', label = 'Y')
plt.title('Evolution of the mean with the number of turns')
# plt.xlim([0,40])
# plt.ylim([-30,30])
plt.grid(b=None, which='major')
plt.legend(loc = 'lower left')
plt.xlabel('Turns')
plt.ylabel('Mean of the position')
plt.tight_layout()
plt.savefig('mean_vs_turns.png', dpi=DPI)
plt.close()

FFT_x = abs(scipy.fft(mean_x))
freqs_x = scipy.fftpack.fftfreq(mean_x.size, total_turns[1]-total_turns[0])

FFT_y = abs(scipy.fft(mean_y))
freqs_y = scipy.fftpack.fftfreq(mean_y.size, total_turns[1]-total_turns[0])

# pylab.plot(abs(a), 'rx',label = 'X')
pylab.plot(freqs_y, FFT_y,  'r',label = 'Y')
pylab.plot(freqs_x, FFT_x,  'b',label = 'X')

# pylab.plot(freqs_y,scipy.log10(FFT_x), 'rx',label = 'X')
# pylab.plot(freqs_y,scipy.log10(FFT_y), 'bx',label = 'Y')

plt.title('Absolute value of FFT of the means')
# plt.xlim([0.28, 0.34])
# plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.grid(b=None, which='major')
plt.legend(loc = 'upper left')
plt.xlabel('Tune')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.savefig('fft.png', dpi=DPI)
plt.close()


