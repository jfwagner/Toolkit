import os

rootdir = '/home/andrea/afs_lhc_mib/cc_sims/tau_1/results'

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
    print '>> Correct!'

tau = []
for number in range(1,len(phase) + 1):
    tau.append(1)

outfile = 'tau_1.txt'
f = open(outfile,'w')
for e1, e2, e3 in zip(tau, phase, particles):
    print max(particles)
    f.write('%.0f %.0f %.0f \n' % (e1, e2, e3-1))
f.close()
    



            