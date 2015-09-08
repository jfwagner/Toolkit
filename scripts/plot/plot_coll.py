#!/usr/local/bin/python
import pylab as P
from numpy import *
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages
from util import *

# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
infile_1 = raw_input("What's the name of your impacts real file? >> ")
name = raw_input("What's the name of the collimator? >> ")
name = '%s'%name
id_col = raw_input("What's the collimator's ID number? >> ")
id_col= float(id_col)
halfgap = raw_input("What's the halfgap? >> ")
total_particles = raw_input("What's the total number of particles? >> ")

# ------------------------------------------------------------------------------
# ############################## IMPACTS REAL ##################################
# ------------------------------------------------------------------------------   
# ------------------------------------------------------------------------------
# Extract losses in the aperture
# ------------------------------------------------------------------------------
impacts_data = loadtxt(infile_1)

s = []
x = []
y= []
icoll = []
for line in impacts_data:
    s.append(line[2])
    x.append(line[3])
    y.append(line[5])
    icoll.append(line[0])

x_tct = []
y_tct = []
for e1,e2,e3 in zip(icoll, x, y):
    if e1==id_col:
        x_tct.append(e2)
        y_tct.append(e3)
print type(id_col)

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 300
textwidth = 6
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

# ------------------------------------------------------------------------------
# Plot the impacts on the collimator
# ------------------------------------------------------------------------------
plt.scatter(x_tct,y_tct, marker=(5,2))
plt.grid(b=None, which='major')
# plt.xlim([0, 26658.883])
# plt.ylim([0, 1])
plt.xlabel("x [mm]]")
plt.ylabel("y [mm]")
plt.title(name + "hits =" + str(len(x_tct)))
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '.png', dpi=DPI)

# ------------------------------------------------------------------------------
# Halfgap (to be read from collgaps)
# ------------------------------------------------------------------------------
halfgap = float(halfgap)
halfgap_minus = halfgap -1

# ------------------------------------------------------------------------------
# Impact parameter
# ------------------------------------------------------------------------------
abs_coord = []
for e1 in y_tct: #or x, depending on your collimator
        abs_coord.append(abs(e1) - halfgap)

# ------------------------------------------------------------------------------
# Plot the impact parameter
# ------------------------------------------------------------------------------        
histogram_coll(abs_coord, 700, False, name, halfgap, halfgap_minus, 'Impact parameter')

# ------------------------------------------------------------------------------
# Plot the histogram
# ------------------------------------------------------------------------------   
histogram_coll(y_tct, 100, True, name, halfgap, halfgap_minus,'coordinate')

