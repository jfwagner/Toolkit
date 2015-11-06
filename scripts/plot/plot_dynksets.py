#!/usr/local/bin/python
import sys
import itertools
import numpy as np

from datetime import datetime
from math import degrees
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from operator import itemgetter

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 300
textwidth = 6
font_spec = {"font.family": "serif", # use as default font
             "font.serif": ["New Century Schoolbook"], # custom serif font
             "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":12,
             "font.weight":"bold",
            }
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.618
rcParams.update(font_spec)

# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
infile = sys.argv[1]

g = open(infile, 'r')
dynk_set_data = []
for line in g.xreadlines():
    columns = line.strip('\n').split()
    if columns[0] in ('#', '@', '*', '$', '%', '%1=s', '%Ind'):
        continue
    kick = dict(turn=int(columns[0]), element=columns[1], attribute=columns[2], value=float(columns[5]))
    dynk_set_data.append(kick)
g.close()

print ' '
print '>> The plots being generated are:'
key_attribute = []
sorted_attribute = sorted(dynk_set_data, key=itemgetter('attribute'))
for key, group in itertools.groupby(sorted_attribute, key=lambda x:x['attribute']):
    if key == key:
        key_name = "%s"%key
        list_name = key_name + '_list'
        list_name= list(group)
        sorted_element = sorted(list_name, key=itemgetter('element'))
        for key_el, group_el in itertools.groupby(sorted_element, key=lambda x:x['element']):
            key_name_el = "%s"%key_el
            list_name_el = key_name + '_' + key_name_el + '_list'
            print list_name_el
            list_name_el= list(group_el)
            x = []
            y = []
            for item in list_name_el:
                x.append(int(item["turn"]))
                if key_name == 'phase':
                    y.append(degrees(float(item["value"])))
                else:
                    y.append(float(item["value"]))
            plt.plot(x, y, label = key_name_el)
            plt.xlim([min(x), max(x)])
        plt.xlabel('Turns')
        plt.ylabel(key_name.capitalize())
        plt.grid(b=None, which='major')
        plt.subplots_adjust(left=0.13, bottom=0.14, right=0.94, top=0.93)
        plt.legend(loc='lower right', prop={'size':10})
        plt.savefig('dynksets_' + key_name + '.png', dpi=DPI)
        plt.clf()

        
