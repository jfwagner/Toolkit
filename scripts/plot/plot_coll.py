#!/usr/local/bin/python
import pylab as P
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages
from util import *

# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
user_input = raw_input('impacts real, coll id, coll name, orientation, halfgap, # of particles >> ')
list_input = user_input.split(',')
infile = list_input[0].strip()
id_col = float(list_input[1])
name = '%s' %list_input[2].strip()
orientation = str(list_input[3]).strip()
halfgap = float(list_input[4])
total_particles = list_input[5]

# ------------------------------------------------------------------------------
# ############################## IMPACTS REAL ##################################
# ------------------------------------------------------------------------------   
# ------------------------------------------------------------------------------
# Extract losses in the aperture
# ------------------------------------------------------------------------------
icoll = load_data(infile, 0)
s = load_data(infile, 2)
x = load_data(infile, 3)
y = load_data(infile, 5)

x_tct = []
y_tct = []
s_tct = []
for e1,e2,e3,e4 in zip(icoll, x, y, s):
    if e1==id_col:
        x_tct.append(e2)
        y_tct.append(e3)
        s_tct.append(e4)
        
# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 300
textwidth = 6
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

# ------------------------------------------------------------------------------
# Plot the impacts on the collimator in x-y
# ------------------------------------------------------------------------------
plt.scatter(x_tct,y_tct, marker=(5,2))
plt.grid(b=None, which='major')
plt.xlabel("x [mm]")
plt.ylabel("y [mm]")
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.grid(b=None, which='major')
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_xy.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Plot the impacts on the collimator in y-s
# ------------------------------------------------------------------------------
plt.scatter(s_tct,y_tct, marker=(5,2))
plt.grid(b=None, which='major')
plt.xlabel("s [m]")
plt.ylabel("y [mm]")
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.grid(b=None, which='major')
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_sy.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Plot the impact parameter
# ------------------------------------------------------------------------------
abs_coord = []
if orientation=='vertical':
    for e1 in y_tct: 
            abs_coord.append(abs(e1) - halfgap)

plt.hist(abs_coord, 100, color='green', alpha=0.8)
plt.xlabel("Impact parameter (mm)")
plt.grid(b=None, which='major')
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_histogram_impact_parameter.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Plot the distribution histogram
# ------------------------------------------------------------------------------
plt.hist(y_tct, 100, color='green', alpha=0.8)
plt.xlabel("y (mm)")
plt.grid(b=None, which='major')
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_histogram_coordinate.png', dpi=DPI)



