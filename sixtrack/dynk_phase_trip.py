#!/bin/bash
import os
from math import degrees
from math import radians
import numpy as np

phases_rad = []
phases_degree = []
for value in range(1,361):
    phases_rad.append(radians(value))
    phases_degree.append(value)

tau = 1

for angle_rad, angle_degree in zip(phases_rad, phases_degree):
    p='%s'%int(angle_degree)
    print angle_degree, angle_rad
    outfile = 'crab_2_' + p
    failure = 7 + tau
    end = 50
    f = open(outfile,'w')
    f.write('1 0.0\n')
    f.write('7 0.0\n')
    f.write('%.0f %.8f\n'%(failure, angle_rad))
    f.write('%.0f %.8f\n'%(end, angle_rad))
