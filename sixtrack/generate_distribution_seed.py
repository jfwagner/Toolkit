#!/usr/bin/env python

import subprocess

import numpy as np

from util import GetData

infile = 'seed_old.txt'
get  = GetData(infile)
data = get.data_column(dtype='string')
seed = data[3]
jobs = range(1, 500 + 1)

for i, j in zip(seed, jobs):
    subprocess.call(['generate_distribution.py','19968','7e12','HL_coll','False', '1','0.9','2.5e-6','2.5e-6','0.003485','-0.000764','0.150739','0.150235','-7.5e-4','0','0','295e-6','0.003652','0.000517','0.0755','1.13e-4',i])
    subprocess.Popen(['rename.sh %s' % j], shell=True)