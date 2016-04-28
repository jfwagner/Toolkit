#!/usr/bin/env python
import sys

import numpy as np

from collections import Counter
from itertools import islice
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData


particles = float(sys.argv[1])
failure_turn = float(sys.argv[2])

# --------------------------------------------------------------------
# Extract the data
# --------------------------------------------------------------------
infile = 'impacts_real.dat'
get = GetData(infile)

my_data = get.data_column(column=7, regex=r'1\b')
losses = dict(Counter(my_data[9]))
x_norm = losses.keys()
y_norm = []
for i in losses.values():
    y_norm.append(float(i)/(particles*1e-2))

x = []
y = []
count = 0
for i, j in sorted(zip(x_norm, y_norm)):
    count = count + j
    y.append(float(count))
    x.append(i)

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
# Plot characteristics
# DPI = 300
# textwidth = 6
# font_spec = {"font.family": "serif", # use as default font
#              "font.serif": ["New Century Schoolbook"], # custom serif font
#              "font.sans-serif": ["helvetica"], # custom sans-serif font
#              "font.size":12,
#              "font.weight":"bold",
#             }
# rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
# rcParams['figure.figsize']=textwidth, textwidth/1.618
# rcParams.update(font_spec)

DPI = 600
textwidth = 3.25
font_spec = {"font.family": "serif", # use as default font
             # "font.serif": ["New Century Schoolbook"], # custom serif font
             # "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":8,
             "font.weight":"bold",
            }
rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.618
rcParams.update(font_spec)

plt.bar(x, y, width=1, align='center', color='green', alpha=0.6, linewidth=0.3)
plt.axvline(x=failure_turn, linewidth=0.7, color='black')
plt.annotate('Failure turn', xy=(failure_turn - 0.7,  (max(y) + max(y)*0.7)/2), rotation='vertical', size='6', verticalalignment='center')
# plt.axvline(x=failure_turn + 3, linewidth=1.5, color='black')

for i, j in zip(x,y):
    plt.annotate('{} \%'.format(round(j,4)), xy=(i, j+ 0.03*j), rotation='vertical', size='6', verticalalignment='bottom', horizontalalignment='center')
    if i == 8:
        t_9 = j
        plt.annotate('After 3 turns: {} \%'.format(round(t_9, 2)), xy=(13, max(y)+0.4*max(y)), size='6')
    else:
        continue
    if i == 15:
        t_15 = j
        plt.annotate('After 10 turns: {} \%'.format(round(t_15,2)), xy=(13, max(y)+0.3*max(y)), size='6')
    else:
        continue

    
plt.annotate('Total loss: {} \%'.format(round(sum(y_norm), 2)), xy=(13, max(y)+0.5*max(y)), size='6')
plt.axvline(x=1, linewidth=0.7, color='black')
plt.xlabel("Turns")
plt.ylabel(r"Bunch lost (\%)")
plt.xlim([0, max(x) + 0.5])
plt.ylim([0, max(y) + max(y)*0.7])
# plt.grid(b=None, which='major')
# plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
# plt.legend(loc='upper left', prop={'size':6})
plt.subplots_adjust(left=0.13, bottom=0.18, right=0.94, top=0.93)
plt.savefig('losses_turn.png', dpi=DPI)
plt.clf()
