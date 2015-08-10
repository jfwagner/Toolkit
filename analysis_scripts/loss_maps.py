from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from numpy import *
from util import *

DPI = 300
textwidth = 6
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

total_particles = 31724800

# --------------
# LOAD THE DATA
# --------------
# Extract collimator name and position from CollPositions
id_pos, s = get_columns("CollPositions.b1.dat", 0, 2, "float")
temp_1, name_pos = get_columns("CollPositions.b1.dat", 1, 1, "string")

# Extract collimator name and index correlation from coll_summary
temp_2, absorptions = get_columns("coll.dat", 0, 3, "float")
id_sum, name_sum = get_columns("coll.dat", 0, 1, "string")

# Extract losses from impacts_real
id_impacts, temp_3 = get_columns("impacts_real.dat", 0, 1, "string")

# Extract losses in the aperture
temp_4, aperture = get_columns("aperture_losses.txt", 0, 2, "string")

# ---------------
# TREAT THE DATA
# ---------------
list_ids = set(id_impacts)
l1 = list(list_ids)

name = []
iden = []
oc = []
for i in range(0, len(l1)):
    for j in range(0, len(id_sum)):
        if l1[i]==id_sum[j]:
            name.append(name_sum[j])
            iden.append(l1[i])
            break

occurrences = []            
for i in iden:
    occurrences.append(float(id_impacts.count(i)))

position = []
for i in range(0, len(name)):
    for j in range(0, len(name_pos)):
        if name[i]==name_pos[j]:
            position.append(s[j])
            break
my_zip = zip(iden, position, name, occurrences)
sorted_zip = sorted(my_zip, key=lambda t:t[1])
# for e1, e2, e3, e4 in sorted_zip:
#     print e1, e2, e3, e4

list_aperture = set(aperture)
l3 = list(list_aperture)

occurrences_ap = []  
for i in l3:
    occurrences_ap.append(float(aperture.count(i)))

x_a = zeros(len(l3))
for i in range(0, len(l3)):
    x_a[i] = l3[i]

y_a = asarray(occurrences_ap)/total_particles

l3_1 = []
for i in l3:
    l3_1.append(float(i))

my_zip_1 = zip(l3, occurrences_ap)
sorted_zip_1 = sorted(my_zip_1, key=lambda t:t[1])
for e1, e2 in sorted_zip_1:
    print e1, e2

x_c = asarray(position)
y_c = asarray(occurrences)/total_particles

plt.bar(x_a, y_a, color = 'g', label = 'Aperture', log = True, width = 10, align = 'center', edgecolor = 'g')
plt.bar(x_c, y_c, color = 'r', label = 'Collimators', log = True, width = 10, align = 'center', edgecolor = 'r')
plt.annotate('IP1', xy=(1, 10**-4), xytext=(800, 10**-4), weight='bold', va='bottom', ha='center', size=8)
plt.annotate('IP2', xy=(1, 10**-4), xytext=(3332.4, 10**-4), weight='bold', va='bottom', ha='center', size=8)
plt.annotate('IR3', xy=(1, 10**-4), xytext=(6664.721, 10**-4), weight='bold', va='bottom', ha='center', size=8)
plt.annotate('IR4', xy=(1, 10**-4), xytext=(9997, 10**-4), weight='bold', va='bottom', ha='center', size=8)
plt.annotate('IP5', xy=(1, 10**-4), xytext=(13329.28, 10**-4), weight='bold', va='bottom', ha='center', size=8)
plt.annotate('IR6', xy=(1, 10**-4), xytext=(16661.7, 10**-4), weight='bold', va='bottom', ha='center', size=8)
plt.annotate('IR7', xy=(1, 10**-4), xytext=(20000, 10**-4), weight='bold', va='bottom', ha='center', size=8)
plt.annotate('IP8', xy=(1, 10**-4), xytext=(23315.4, 10**-4), weight='bold', va='bottom', ha='center', size=8)
plt.xlim([0, 27000])
plt.legend(loc = 'upper left',fontsize=10)
plt.savefig('loss_map.png', dpi=DPI)
# plt.show()
