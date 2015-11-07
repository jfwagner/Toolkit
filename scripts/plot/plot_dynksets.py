#!/usr/local/bin/python

import sys
import itertools
from operator import itemgetter

from math import degrees
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams


# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------

DPI = 300
textwidth = 6
font_spec = {"font.family": "serif",  # use as default font
             "font.serif": ["New Century Schoolbook"],  # custom serif font
             "font.sans-serif": ["helvetica"],  # custom sans-serif font
             "font.size": 12,
             "font.weight": "bold"}
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize'] = textwidth, textwidth/1.618
rcParams.update(font_spec)


# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------

infile = sys.argv[1]

dynk_set_data = []
with open(infile, 'r') as f:
    for line in f.xreadlines():
        columns = line.strip('\n').split()
        if columns[0] in ('#', '@', '*', '$', '%', '%1=s', '%Ind'):
            continue
        kick = dict(turn=int(columns[0]), element=columns[1], attribute=columns[2], value=float(columns[5]))
        dynk_set_data.append(kick)

print ' '
print '>> The plots being generated are:'
sorted_attribute = sorted(dynk_set_data, key=itemgetter('attribute'))
for key, group in itertools.groupby(sorted_attribute, key=itemgetter('attribute')):
    sorted_element = sorted(group, key=itemgetter('element'))
    for key_el, group_el in itertools.groupby(sorted_element, key=itemgetter('element')):
        print key + '_' + key_el + '_list'
        x = []
        y = []
        for item in group_el:
            x.append(int(item["turn"]))
            if key == 'phase':
                y.append(degrees(float(item["value"])))
            else:
                y.append(float(item["value"]))
        plt.plot(x, y, label=key_el)
        plt.xlim([min(x), max(x)])
    plt.xlabel('Turns')
    plt.ylabel(key.capitalize())
    plt.grid(b=None, which='major')
    plt.subplots_adjust(left=0.13, bottom=0.14, right=0.94, top=0.93)
    plt.legend(loc='lower right', prop={'size': 10})
    plt.savefig('dynksets_' + key + '.png', dpi=DPI)
    plt.clf()
