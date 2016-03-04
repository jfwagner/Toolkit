#!/usr/bin/python
from __future__ import division

import os

import numpy as np

max_tau = 4
taus = []
for value in range(1, max_tau + 1):
    taus.append(value)

min_turn = 7
max_turn = 50

turns = []
for value in range(min_turn + 1, max_turn + 1):
    turns.append(value)
    
turns_const = []
for value in range(2, min_turn + 1):
    turns_const.append(value)

def decay(voltage, turn, min_turn, tau):
    return float(voltage*np.exp(-(turn - min_turn)/tau))

voltages = dict(zip(['CRAB2A', 'CRAB2B', 'CRAB2C', 'CRAB2D'], [2.421832080, 2.421832080, 2.421832080, 2.421832080]))

for tau in taus:
    for key, val in voltages.items():
        outfile = 'voltage_{}_{}'.format(tau, key)
        try:
            os.remove(outfile)
        except OSError:
            pass
        f = open(outfile, 'w')
        f.write('1 0.0\n')
        for turn_const in turns_const:
            f.write('%.0f %.15f\n'%(turn_const, val))
        for turn in turns:
            f.write('%.0f %.15f\n'%(turn, decay(val, turn, min_turn, tau)))
        f.close()

