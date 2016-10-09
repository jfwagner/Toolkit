#!/usr/bin/env python

import itertools
from operator import itemgetter

from math import degrees
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams


# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------

infile = 'dynksets.dat'

dynk_set_data = []
with open(infile, 'r') as f:
    for line in f.xreadlines():
        columns = line.strip('\n').split()
        if columns[0] in ('#', '@', '*', '$', '%', '%1=s', '%Ind'):
            continue
        kick = dict(turn=int(columns[0]), element=columns[
                    1], attribute=columns[2], value=float(columns[5]))
        dynk_set_data.append(kick)

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
font_spec = {"font.size": 10, }
rcParams.update(font_spec)
rcParams['figure.figsize'] = 4, 2

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

    plt.ylim([0, max(y)*1.3])
    plt.xlabel('Turns')
    plt.ylabel(key.capitalize())
    plt.subplots_adjust(left=0.13, bottom=0.2, right=0.94, top=0.93)
    plt.legend(loc='lower right', fontsize=4)
    plt.savefig('dynksets_' + key + '.png',  dpi=1000)
    plt.savefig('dynksets_' + key + '.eps', format='eps', dpi=1000)
    plt.clf()