#!/usr/local/bin/python
import os
import sys

rootdir = sys.argv[1]
turn = float(sys.argv[2])

phase = []
particles = []

for item in os.listdir(rootdir):
    if os.path.isdir(item) == False:
        continue
    if os.path.isdir(os.path.join(rootdir, item)):
        phase.append(int(item.strip('job_')))
    for data in os.listdir(item):
            if data=='impacts_real.dat':
                particles.append(sum(1 for line in open(os.path.join(rootdir, item, data))))

if len(particles) == len(phase):
    print '>> All jobs seem to be there!'
    print '>> Number of lines = ', len(phase)
else:
    print '>> There seems to be a problem'
tau = []
for number in range(1,len(phase) + 1):
    tau.append(turn)

outfile = '3d_data.txt'
f = open(outfile,'w')
for e1, e2, e3 in zip(tau, phase, particles):
    f.write('%.0f %.0f %.0f \n' % (e1, e2, e3-1))
f.close()
    
print '>> Maximum percentage  lost = ', max(particles)/64, '%'
print '>> Number of particles lost = ', max(particles)


            