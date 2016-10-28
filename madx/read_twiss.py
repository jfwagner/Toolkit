#!/usr/bin/env python
import sys

from util import GetData

infile = sys.argv[1]

data = GetData(infile).data_column(dtype='string')
name = data['NAME']
mux  = data['MUX']
muy  = data['MUY']
betx = data['BETX']
bety = data['BETY']
alfx = data['ALFX']
alfy = data['ALFY']
s    = data['S']

outfile = 'crab_installation.txt'

with open(outfile, 'w') as f:
    for n, ss, mx, my, bx, by, ax, ay in zip(name, s, mux, muy, betx, bety, alfx, alfy):
        if n.startswith('ACF'):
            print >> f, n, ss, mx, my, bx, by, ax, ay