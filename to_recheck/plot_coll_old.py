import re
import sys
import numpy as np
import pylab as P
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages
from util import *

# -----------------------------
# Text and plot characteristics
# -----------------------------
DPI = 300
textwidth = 4
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

def scatter(x, y, name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y, marker=(5,2))
    ax.set_title(name + ' (Number of hits = ' + str(len(x)) + ')')
    ax.set_xlabel('x (mm)')
    ax.set_ylabel('y (mm)')
    ax.grid(b=None, which='major')
    plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
    plt.savefig('scatter_xy_' + name + '_' + '.pdf', dpi=DPI)

def histogram(x, bins, flag, name, halfgap, halfgap_minus, title):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    tile = '%s'%title
    n, bins, patches = P.hist(x, bins=bins, normed=False, histtype='bar', cumulative=False)
    ax.set_xlim([-13, 13])
    
    if flag==True:
        ax.bar(halfgap, max(n), color='g', log=False, width=0.0005, align='center', edgecolor='g')
        ax.bar(halfgap_minus, max(n), color='g', log=False, width=0.001, align='center', edgecolor='g')
        x_halfgap = np.linspace(halfgap_minus, halfgap)
        ax.fill_between(x_halfgap, max(n), facecolor='green', alpha=0.2, label='Gap')
        ax.legend(loc='upper right', prop={'size':6})
        ax.set_title(name + ' (Number of hits = ' + str(len(x)) + ')')
        ax.set_xlabel(title + '(mm)')
    else:
        print 'No halfgaps in plot'

    plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
    plt.savefig('histogram_' + title + '_' + name + '_' + '.pdf', dpi=DPI)

def plot(file_1, coord, icoll, name):
    coord = '%s'%coord
    name = '%s'%name

    print '---------------------------------------------------'
    print 'Collimator ' + name + ' selected, icoll =', int(icoll)

    # -------------
    # Get the data 
    # -------------
    coll_id, a = get_columns(file_1, 0, 7)
    x, y = get_columns(file_1, 3, 5)

    # --------------------------------
    # Choose the selected collimators
    # --------------------------------    
    var_x = []
    var_y = []
    for e1, e2, e3 in zip(coll_id, x, y):
        if e1==icoll:
            var_x.append(e2)
            var_y.append(e3)
    
    # ----------------
    # Collimator gaps
    # ----------------
    my_data_gaps = get_lines(r'collgaps.dat')
    
    icoll_temp = []
    halfgap_temp = []
    for column in my_data_gaps:
        icoll_temp.append(float(column[0]))
        halfgap_temp.append(float(column[5]))

    for e1, e2 in zip(halfgap_temp, icoll_temp):
        if e2==icoll:
            halfgap=float(e1*10**3)
            halfgap_minus=float(e1*10**3*-1)
    print 'Halfgap =', halfgap, '(mm)'

    # -----------------
    # Impact parameter
    # -----------------
    abs_coord = []

    if coord =='x':
        for e1 in var_x:
            abs_coord.append(abs(e1) - halfgap)

    if coord =='y':
        for e1 in var_y:
            abs_coord.append(abs(e1) - halfgap)

    # -----------------------------------------
    # Ignore collimators with less than 2 hits
    # -----------------------------------------
    if coord =='x':
        if len(var_x) < 2:
            print 'Could not plot. No hits for ' + name
            print '---------------------------------------------------'
        else:
            print 'Plotting...'
            print 'Number of hits = ', len(var_x)
            print '---------------------------------------------------'
            # scatter(var_x, var_y, name)
            # histogram(var_x, 100, True, name, halfgap, halfgap_minus, 'coordinate')
            histogram(abs_coord, 100, True, name, halfgap, halfgap_minus, 'impactparameter')

    elif coord =='y':
        if len(var_y) < 2:
            print 'Could not plot. No hits for ' + name
        else:
            print 'Plotting...'
            print 'Number of hits =', len(var_y)
            print '---------------------------------------------------'
            # scatter(var_x, var_y, name)    
            # histogram(var_y, 100, True, name, halfgap, halfgap_minus,'coordinate')
            histogram(abs_coord, 100, True, name, halfgap, halfgap_minus, 'impactparameter')

# -----------------
# Use the function
# -----------------
my_coll = 'TCP'
my_data = get_lines(r'info_coll.dat')
icoll_temp = []
name_temp = []
for column in my_data:
    icoll_temp.append(float(column[0]))
    name_temp.append(column[1])

icoll = []
name = []
regex = re.compile(my_coll)
for e1, e2 in zip(icoll_temp, name_temp):
    if regex.match(e2):
        icoll.append(e1)
        name.append(e2)

length = len(icoll)
print 'Number of collimators that match your search' , length
for item in name:
    print item

for number in range(1, length):
    coord_x = '.*H.*'
    coord_y = '.*V.*'
    reg_x = re.compile(coord_x)
    reg_y = re.compile(coord_y)
    if reg_x.match(name[number]):
        coord = 'x'
    elif reg_y.match(name[number]):
        coord = 'y' 
    else:
        print '>> Cannot plot, undefined collimator orientation (horizontal or vertical?)'
    plot('impacts_real.dat', coord , icoll[number], name[number])

