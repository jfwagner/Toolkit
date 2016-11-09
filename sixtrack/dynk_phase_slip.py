#!/usr/bin/python
from math import radians

failure_start = 150
failure_end = 200
angle = 60

outfile = 'phase_slip'
f = open(outfile,'w')

f.write('1 0.0\n')
f.write('%.0f 0.0\n'%(failure_start))


for t in range(failure_start + 1, failure_end + 1):
    f.write('%.0f %.8f\n'%(t, (t - failure_start)*(radians(angle))))
