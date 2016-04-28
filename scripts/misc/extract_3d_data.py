#!/usr/bin/env python
import math
import os
import subprocess
import sys

rootdir = sys.argv[1]
turn = float(sys.argv[2])
tot_particles = float(sys.argv[3])*1e-2

phase = []
particles = []

for item in os.listdir(rootdir):
    if os.path.isdir(item) == False:
        continue
    if os.path.isdir(os.path.join(rootdir, item)):
        phase.append(float(item.strip('job_')))
    for data in os.listdir(item):
        if data=='impacts_real.dat':
            particles.append(float(sum(1 for line in open(os.path.join(rootdir, item, data)))-1)/tot_particles)

if len(particles) == len(phase):
    print '>> All jobs seem to be there!'
    print '>> Number of lines = ', len(phase)
else:
    print '>> There seems to be a problem'
tau = []
for number in range(1,len(phase) + 1):
    tau.append(turn)

time = 8.8928*1e-5
detune = []
for i, j in zip(tau, phase):
    detune.append(((math.radians(j)/(2*math.pi*i*time)))*1e-3)

outfile = '3d_data.txt'
f = open(outfile,'w')
for e1, e2, e3, e4 in zip(tau, phase, particles, detune):
    f.write('%.2f %.2f %.5f %.2f \n' % (e1, e2, e3, e4))
f.close()
    
print '>> Maximum percentage  lost  = ', max(particles)


            