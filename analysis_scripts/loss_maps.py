import os.path
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from numpy import *
from util import *

# ------------------------------------------------------------------------------
# Specify the total number of particles simulated
# ------------------------------------------------------------------------------
total_particles = 3200000
# ------------------------------------------------------------------------------
# ################################## APERTURE ##################################
# ------------------------------------------------------------------------------   
# ------------------------------------------------------------------------------
# Extract losses in the aperture
# ------------------------------------------------------------------------------
aperture_data = loadtxt("aperture.dat")
positions_LPI = []

for line in aperture_data:
    positions_LPI.append(line[2])

# ------------------------------------------------------------------------------
# Extract the unique values of the position
# ------------------------------------------------------------------------------
set_unique_positions_LPI = set(positions_LPI)
list_unique_positions_LPI = list(set_unique_positions_LPI)

# ------------------------------------------------------------------------------
# Extract from the list how many times that position appears
# ------------------------------------------------------------------------------
occurrences_LPI = [float(positions_LPI.count(position)) for position in list_unique_positions_LPI] 

# ------------------------------------------------------------------------------
# Order the tuples by amount of particles lost at that location
# ------------------------------------------------------------------------------
sorted_LPI = sorted(zip(list_unique_positions_LPI, occurrences_LPI), key=lambda t:t[1])

# ------------------------------------------------------------------------------
# Transfer the information to a file
# ------------------------------------------------------------------------------    
filename_ap = "losses_aperture.txt"
if os.path.exists(filename_ap)==True:
    os.remove(filename_ap)
    
g = open(filename_ap, "a")
for e1, e2 in sorted_LPI:
    print >> g, e1, e2
g.close()

# ------------------------------------------------------------------------------
# Convert the data to numpy arrays and normalize it
# ------------------------------------------------------------------------------   
x_aperture = asarray(list_unique_positions_LPI)
y_aperture = asarray(occurrences_LPI)/total_particles

# ------------------------------------------------------------------------------
# ############################### COLLIMATION ##################################
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Extract ID from impacts_real.dat
# ------------------------------------------------------------------------------
collimation_data = loadtxt("imp_real.dat")

id_impreal = []

for line in collimation_data:
    id_impreal.append(line[0])

# ------------------------------------------------------------------------------
# Extract ID and name from coll_summary.dat
# ------------------------------------------------------------------------------
collsum_data = loadtxt("coll_sum.dat", str)

name_collsum = []
id_collsum = []

for line in collsum_data:
    name_collsum.append(line[1])
    id_collsum.append(float(line[0]))

# ------------------------------------------------------------------------------
# Extract name and position from CollPositions
# ------------------------------------------------------------------------------
collpos_data = loadtxt("CollPositions.b1.dat", str, "%Ind")

name_collpos = []
position_collpos = []

for line in collpos_data:
    name_collpos.append(line[1])
    position_collpos.append(float(line[2]))

# ------------------------------------------------------------------------------
# Extract from the list how many times the collimator ID appears
# ------------------------------------------------------------------------------
occurrences_impreal = [float(id_impreal.count(i)) for i in id_collsum]

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
# Transfer the information to a file
# ------------------------------------------------------------------------------    
filename_coll = "losses_collimation.txt"
if os.path.exists(filename_coll)==True:
    os.remove(filename_coll)
    
f = open(filename_coll, "a")
for e1, e2, e3, e4 in zip(id_collsum, name, position, occurrences_impreal):
    print >> f, e1, e2, e3, e4
f.close()

# ------------------------------------------------------------------------------
# Convert the data to numpy arrays and normalize it
# ------------------------------------------------------------------------------   
x_coll = asarray(position)
y_coll = asarray(occurrences_impreal)/total_particles

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

# ------------------------------------------------------------------------------
# Plot bars
# ------------------------------------------------------------------------------
plt.bar(x_aperture, y_aperture, color='g', label='Aperture', log=True, width=10, align='center', edgecolor='g')
# plt.bar(x_coll, y_coll, color='r', label='Collimators', log=True, width=10, align='center', edgecolor='r')
print y_coll.size
# ------------------------------------------------------------------------------
# Annotate the IP names
# ------------------------------------------------------------------------------
ip_name = ['IP1', 'IP2', 'IR3', 'IR4', 'IP5', 'IR6', 'IR7', 'IP8']
ip_position = [800, 3332.4, 6664.721, 9997, 13329.28, 16661.7, 20000, 23315.4]

for i in range(0,8):
    plt.annotate(ip_name[i], xy=(1, 10**-4), xytext=(ip_position[i], 10**-4), weight='bold', va='bottom', ha='center', size=8)

plt.grid(b=None, which='major')
plt.xlim([0, 26658.883])
plt.ylim([0, 1])
plt.xlabel("s [m]")
plt.ylabel("Fraction of particles lost")
plt.legend(loc = 'upper left',fontsize=10)
plt.savefig('loss_map.png', dpi=DPI)
# plt.show()
