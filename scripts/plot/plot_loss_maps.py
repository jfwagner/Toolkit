#!/usr/local/bin/python
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
user_input = raw_input('LPI/impacts_real/coll_summary/coll_positions/total particles >> ')
list_input = user_input.split('/')
infile_lpi = list_input[0].strip()
infile_impacts = list_input[1].strip()
infile_collsum = list_input[2].strip()
infile_collpos = list_input[3].strip()
total_particles = float(list_input[4].strip())

start_time = datetime.now()
# ------------------------------------------------------------------------------
# ################################## APERTURE ##################################
# ------------------------------------------------------------------------------
g = open(infile_lpi, 'r')
pos_lpi = []
for line in g.xreadlines():
    columns = line.strip('\n').split()
    if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind':
        continue
    pos_lpi.append(float(columns[2]))
g.close()

# ------------------------------------------------------------------------------
# ############################### COLLIMATION ##################################
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Extract ID and name from coll_summary.dat
# ------------------------------------------------------------------------------
collsum_data = np.loadtxt("coll_sum.dat", str)

name_collsum = []
id_collsum = []

for line in collsum_data:
    name_collsum.append(line[1])
    id_collsum.append(float(line[0]))

# ------------------------------------------------------------------------------
# Extract name and position from CollPositions
# ------------------------------------------------------------------------------
collpos_data = np.loadtxt("CollPositions.b1.dat", str, "%Ind")

name_collpos = []
position_collpos = []

for line in collpos_data:
    name_collpos.append(line[1])
    position_collpos.append(float(line[2]))

# ------------------------------------------------------------------------------
# Associate name with ID via coll_summary, then extract correct position
# ------------------------------------------------------------------------------
name = []
for e1, e2 in zip(id_collsum, name_collsum):
    for e3 in id_collsum:
        if e3 == e1:
            name.append(e2)

position = []
for e1, e2 in zip(name_collpos, position_collpos):
    for e3 in name:
        if e3 == e1:
            position.append(e2)

# ------------------------------------------------------------------------------
# Create a frigging dictionary with the correct sh*t
# ------------------------------------------------------------------------------
my_tuple = zip(id_collsum, position)
d = {}
for k, v in my_tuple:
    d[k] = v

# ------------------------------------------------------------------------------
# Loop >ONCE< through impacts real to extract the coll ID's (no way around it)
# ------------------------------------------------------------------------------
f = open(infile_impacts, 'r')
pos = []
for line in f.xreadlines():
    columns = line.strip('\n').split()
    if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind':
        continue
    pos.append(d[int(columns[0])])
f.close()

# ------------------------------------------------------------------------------
# ################################### PLOT #####################################
# ------------------------------------------------------------------------------ 
# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 300
textwidth = 6
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

pos_coll = np.asarray(pos)
pos_ap = np.asarray(pos_lpi)

weights_coll = np.ones_like(pos_coll)/total_particles
weights_ap = np.ones_like(pos_ap)/total_particles

plt.hist(pos, 500, color='black', alpha=0.8, linewidth=0.1, weights=weights_coll, log=True, label='Collimation')
plt.hist(pos_lpi, 500, color='green', alpha=0.8, linewidth=0.1, weights=weights_ap, log=True, label='Aperture')
plt.xlabel("s (m)")
plt.ylabel("Particles lost per 10 cm")
plt.grid(b=None, which='major')
plt.title('Loss map')
plt.legend(loc='upper right', prop={'size':6})
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('loss_maps.png', dpi=DPI)
plt.clf()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))