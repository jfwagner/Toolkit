import  sys
import subprocess

# line = subprocess.check_output(['tail', '-1','data/tot_dump.dat'])
# last_turn = line.strip("\n").split()[1]

last_turn = '14'
tup = []
initial_particles = 0
remaining_particles = 0
print 'starting reading...'
for line in open('dump.txt'):
    line = line.strip("\n").split()
    if line[1] == '1':
        initial_particles += 1
    if line[1] == last_turn:
        remaining_particles += 1

f = open('particle_count.txt', 'w')
lost = initial_particles - remaining_particles
print  >> f,'%i particles from %i lost in %i turns' %(lost, initial_particles, int(last_turn))
percentage_lost = (lost * 100) / initial_particles
print  >> f, 'Percentage of particles lost = %s' % percentage_lost 
f.close()
