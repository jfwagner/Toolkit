#!/usr/local/bin/python
# ------------------------------------------------------------------------------
# A script to read TFS files
# ------------------------------------------------------------------------------
import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from util import get_ip1

# Choose your data file and open it
infile = 'twiss_lhcb1.tfs'
f = open(infile, 'r')

# Skip rows starting with certain symbols
column_filter = ('#', '@', '*', '$', '%', '%1=s', '%Ind') #ToDo:function

# Choose which parameters you want to extract to a list
my_list = ['S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME']
my_dict = {i:[] for i in my_list}

# Extract the associated column index
col_idx = []
col_name = []
for line in f.xreadlines():
    columns = line.strip('\n').split()
    for idx, value in enumerate(columns):
        if value in my_list:         # for item in my_list: /if value == item: 
            col_idx.append(idx-1)
            col_name.append(value)
    for index, name in zip(col_idx, col_name):
        if columns[0] in column_filter:
            continue
        if name != 'NAME':
            my_dict[name].append(float(columns[index]))
        else:
            my_dict[name].append(columns[index].strip('"'))
f.close()

# Plot characteristics
DPI = 300
textwidth = 6
font_spec = {"font.family": "serif",      # use as default font
             "font.serif": ["New Century Schoolbook"],  # custom serif font
             "font.sans-serif": ["helvetica"],            # custom sans-serif font
             "font.size":14,
             "font.weight":"bold",
            }
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.618
rcParams.update(font_spec)

# Triplet
# regex_list_triplet = ['MQXFA', 'MQXFB']
# name_triplet = []
# position_triplet = []
# length_triplet = []
# for a in regex_list_triplet:
#     regex = re.compile(a)
#     for a, b, c in zip( my_dict['NAME'],  my_dict['S'],  my_dict['L']):
#         if regex.match(a):
#             name_triplet.append(a)
#             position_triplet.append(float(b))
#             length_triplet.append(float(c))

# for s, element, l in zip(position_triplet, name_triplet, length_triplet):
#     f = s-l
#     plt.bar(f, 3e3, l, 2.3e4,  color = 'r', alpha=0.7)

# for a,b in zip(my_dict['NAME'], my_dict['S']):
#     if a == 'TAXN.4R1':
#         print a,b

element_names = []
if [ my_dict['NAME'][i]==my_dict['NAME'][i-1] for i in range(len(my_dict['NAME'])) ]:
    print 'nope'
print len(element_names)
print len(my_dict['NAME'])
print len(my_dict['S'])

# Dipoles
# regex_list_dipole = ['MBX', 'MBRC', 'MBRB', 'MBRS']
regex_list_dipole = ['TAXN']
name_dipole = []
position_dipole = []
length_dipole = []
for a in regex_list_dipole:
    regex = re.compile(a)
    for a, b, c in zip( my_dict['NAME'],  my_dict['S'],  my_dict['L']):
        if regex.match(a):
            name_dipole.append(a)
            position_dipole.append(float(b))
            length_dipole.append(float(c))

for s, element, l in zip(position_dipole, name_dipole, length_dipole):
    f = s-l
    plt.bar(f, 3e3, l, 2.3e4,  color = 'B', alpha=0.7)

# Beta functions
sx, beta_x = get_ip1(my_dict['S'], my_dict['BETX'])
sy, beta_y = get_ip1(my_dict['S'], my_dict['BETY'])
plt.plot(sx, beta_x, label='Beta x')
plt.plot(sy, beta_y, label='Beta y')
plt.xlabel("s (m)")
plt.ylabel("Beta functions (m)")
plt.xlim([-200,200])
plt.ylim([0,3e4])
plt.grid(b=None, which='major')
# plt.title('HL-LHC Optics 1.2, IP1')
plt.legend(loc='upper right', prop={'size':9})
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.subplots_adjust(left=0.12, bottom=0.15, right=0.97, top=0.91)
plt.savefig('beta_functions.png', dpi=DPI)
plt.clf()

# Orbit
# plt.plot(my_dict['X'], my_dict['BETX'], label='X')
# plt.plot(my_dict['Y'], my_dict['BETY'], label='Y')
# plt.xlabel("s (m)")
# plt.ylabel("Orbit (m)")
# plt.grid(b=None, which='major')
# plt.title('HL-LHC Optics 1.2')
# plt.legend(loc='upper right', prop={'size':6})
# plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
# plt.savefig('orbits.png', dpi=DPI)
# plt.clf()