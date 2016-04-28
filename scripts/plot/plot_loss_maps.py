#!/usr/bin/env python
# plot_loss_maps.py LPI_test.s impacts_real.dat coll_summary.dat CollPositionsHL.b1.dat 19968
import os
import sys
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
# DPI = 300
# textwidth = 6
# rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
# rc('text', usetex=True)
# rcParams['figure.figsize']=textwidth, textwidth/1.618
DPI = 600
textwidth = 3.25
font_spec = {"font.family": "serif", # use as default font
             # "font.serif": ["New Century Schoolbook"], # custom serif font
             # "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":8,
             "font.weight":"bold",
            }
rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.9
rcParams.update(font_spec)
fig = plt.figure(dpi=DPI)
ax2 = fig.add_subplot(111)
# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
infile_lpi = sys.argv[1]
infile_impacts = sys.argv[2]
infile_collsum = sys.argv[3]
infile_collpos = sys.argv[4]
total_particles = float(sys.argv[5])

start_time = datetime.now()
# ------------------------------------------------------------------------------
# ################################## APERTURE ##################################
# ------------------------------------------------------------------------------
if os.stat(infile_lpi).st_size == 0:
    print '>> No losses in the aperture'
else:
    g = open(infile_lpi, 'r')
    pos_lpi = []
    for line in g.xreadlines():
        columns = line.strip('\n').split()
        if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind' or float(columns[9]) > 8:
            continue
        pos_lpi.append(float(columns[2]))
    g.close()
    pos_ap = np.asarray(pos_lpi)
    ap_per = str(round((len(pos_ap)*100)/total_particles, 5))
    weights_ap = np.ones_like(pos_ap)/total_particles
    plt.hist(pos_lpi, 500, color='#F03C02', alpha=0.8, linewidth=0.1, weights=weights_ap, log=True, label='Aperture ')
    # plt.hist(pos_lpi, 500, color='green', alpha=0.8, linewidth=0.1, weights=weights_ap, log=True, label='Aperture ' + ap_per + '%')


# ------------------------------------------------------------------------------
# ############################### COLLIMATION ##################################
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Extract ID and name from coll_summary.dat
# ------------------------------------------------------------------------------
collsum_data = np.loadtxt(infile_collsum, str)

name_collsum = []
id_collsum = []

for line in collsum_data:
    name_collsum.append(line[1])
    id_collsum.append(float(line[0]))

# ------------------------------------------------------------------------------
# Extract name and position from CollPositions
# ------------------------------------------------------------------------------
collpos_data = np.loadtxt(infile_collpos, str, "%Ind")

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
    if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind' or float(columns[9]) > 8:
        # print columns[9]
        continue
    if columns[7] == '1':
        pos.append(d[int(columns[0])])
f.close()

# ------------------------------------------------------------------------------
# ################################### PLOT #####################################
# ------------------------------------------------------------------------------ 
pos_coll = np.asarray(pos)

# Percentages
coll_per = str(round((len(pos_coll)*100)/total_particles, 2))
print '>>', coll_per, '% lost'

# Weights
weights_coll = np.ones_like(pos_coll)/total_particles

plt.hist(pos, 500, color='#3732bb', alpha=0.8, linewidth=0.1, weights=weights_coll, log=True, label='Collimators')
# plt.hist(pos, 500, color='black', alpha=0.8, linewidth=0.1, weights=weights_coll, log=True, label='Collimation ' + coll_per + '%')
plt.xlabel("s (m)")
plt.ylabel("Number of protons lost")
plt.ylim([0,1e12])
plt.xlim([0,26658.883])
# plt.grid(b=None, which='major')
# plt.title('Loss Maps')
height = 1e8
ax2.annotate('IP2', xy=(1, height), xytext=(3332.4, height), weight='bold', va='bottom', ha='center', size=7, color='black')
ax2.annotate('IR3', xy=(1, height), xytext=(6664.721, height), weight='bold', va='bottom', ha='center', size=7, color='black')
ax2.annotate('IR4', xy=(1, height), xytext=(9997, height), weight='bold', va='bottom', ha='center', size=7, color='black')
ax2.annotate('IP5', xy=(1, height), xytext=(13329.28, height), weight='bold', va='bottom', ha='center', size=7, color='black')
ax2.annotate('IR6', xy=(1, height), xytext=(16661.7, height), weight='bold', va='bottom', ha='center', size=7, color='black')
ax2.annotate('IR7', xy=(1, height), xytext=(20000, height), weight='bold', va='bottom', ha='center', size=7, color='black')
ax2.annotate('IP8', xy=(1, height), xytext=(23315.4, height), weight='bold', va='bottom', ha='center', size=7, color='black')
plt.legend(loc='upper left', prop={'size':6})
plt.subplots_adjust(left=0.16, bottom=0.21, right=0.94, top=0.88)
plt.savefig('loss_maps.png', dpi=DPI)
plt.clf()

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))