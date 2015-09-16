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
from datetime import datetime
start_time = datetime.now()
s_tct = load_data_coll(infile, 2, list_input[1])
x_tct = load_data_coll(infile, 3, list_input[1])
y_tct = load_data_coll(infile, 5, list_input[1])
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
        
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
# Plot the distribution histogram
# ------------------------------------------------------------------------------
n, bins, patches = plt.hist(y_tct, 100, color='green', alpha=0.8, linewidth=0.1)
plt.bar(halfgap, max(n), color='blue', log=False, width=0.0005, align='center', edgecolor='blue', linewidth=0.1)
plt.bar(-1*halfgap, max(n), color='blue', log=False, width=0.0005, align='center', edgecolor='blue', linewidth=0.1)
x_halfgap = linspace(-1*halfgap, halfgap)
plt.fill_between(x_halfgap, max(n), facecolor='blue', alpha=0.2, label='Gap', linewidth=0.1)
plt.xlabel("y (mm)")
plt.grid(b=None, which='major')
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.legend(loc='upper right', prop={'size':6})
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_histogram_coordinate.png', dpi=DPI)
plt.clf()

# ------------------------------------------------------------------------------
# Plot the impact parameter
# ------------------------------------------------------------------------------
abs_coord = []
if orientation=='vertical':
    for e1 in y_tct: 
            abs_coord.append(abs(e1) - halfgap)

plt.hist(abs_coord, 100, color='green', alpha=0.8, linewidth=0.1)
plt.xlabel("Impact parameter (mm)")
plt.grid(b=None, which='major')
plt.title(name + ". Hits = " + str(len(x_tct)) + '/' + str(total_particles))
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig(name + '_histogram_impact_parameter.png', dpi=DPI)
plt.clf()





