#!/usr/bin/env python
import sys
import numpy as np
from collections import Counter
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

infile_impacts = 'impacts_real.dat'

f = open(infile_impacts, 'r')
turn = []
for line in f.xreadlines():
    columns = line.strip('\n').split()
    if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind':
        continue
    turn.append(int(columns[9]))
f.close()

turn_array = np.asarray(turn)
turns_dict = Counter(turn)

x = []
y = []
for key in sorted(turns_dict):
    x.append(float(key))
    y.append(float(turns_dict[key]))

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
# Plot characteristics
DPI = 300
textwidth = 6
font_spec = {"font.family": "serif", # use as default font
             "font.serif": ["New Century Schoolbook"], # custom serif font
             "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":10,
             "font.weight":"bold",
            }
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.618
rcParams.update(font_spec)

weight = np.ones_like(turn_array)
print weight
plt.hist(turn, 150, color='black', alpha=0.8, linewidth=0.1, weights=weight)
plt.xlim([0,20])
plt.xlabel("Turn")
plt.ylabel("Bunch lost (\%)")
plt.savefig('loss_turns.png', dpi=DPI)
plt.clf()
