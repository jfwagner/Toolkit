#!/usr/local/bin/python
import os
import sys
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 300
textwidth = 6
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
infile = sys.argv[1]

g = open(infile, 'r')
turn = []
element = []
attribute = []
value = []
for line in g.xreadlines():
    columns = line.strip('\n').split()
    if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind':
        continue
    turn.append(int(columns[0]))
    element.append(columns[1])
    attribute.append(columns[2])
    value.append(float(columns[5]))
g.close()

for e1,e2,e3,e4 in zip(turn, element, attribute, value):
    my_dict = dict(zip(['turn', 'element', 'attribute', 'value'],[e1, e2, e3, e4]))

print my_dict