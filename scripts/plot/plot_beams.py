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
column_filter = ('#', '@', '*', '$', '%', '%1=s', '%Ind') #ToDo:function in util.py
extract_header = ('#', '@', '$', '%', '%1=s', '%Ind')

# Choose which parameters you want to extract to a list
my_list = ['S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME']
my_dict = {i:[] for i in my_list}

# Extract the associated column index
col_idx = []
col_name = [] #ToDo: convert this to tuple to skip the zip
for line in f.xreadlines():
    columns = line.strip('\n').split()
    for idx, value in enumerate(columns):
        if columns[0] in extract_header:
                continue
        if value in my_list: # for item in my_list: /if value == item: 
            col_idx.append(idx-1)
            col_name.append(value)
    for index, name in zip(col_idx, col_name):
        if columns[0] in column_filter:
            continue
        if name != 'NAME':
            my_dict[name].append(float(columns[index]))
        elif name == 'NAME':
            my_dict[name].append(columns[index].strip('"'))
f.close()

if len(my_dict['NAME'])!=len(my_dict['S']):
    print '>> Something is wrong: length of names is not equal to length of s positions'

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
# Plot characteristics
DPI = 300
textwidth = 6
font_spec = {"font.family": "serif", # use as default font
             "font.serif": ["New Century Schoolbook"], # custom serif font
             "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":14,
             "font.weight":"bold",
            }
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.618
rcParams.update(font_spec)

# Plot the beta functions
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
plt.legend(loc='lower right', prop={'size':9})
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))

# Function to plot different elements
def plot_elem(color, height, bottom, *args):
    regex_list = list(args)
    name = []
    position = []
    length = []
    for a in regex_list:
        regex = re.compile(a)
        dict_s, dict_name = get_ip1(my_dict['S'], my_dict['NAME'])
        dict_s_2, dict_l = get_ip1(my_dict['S'], my_dict['L'])
        for a, b, c in zip( dict_name, dict_s, dict_l):
            if regex.match(a):
                name.append(a)
                position.append(float(b))
                length.append(float(c))
    for s, element, l in zip(position, name, length):
        f = s-l
        plt.bar(f, height, l, bottom, color=color, alpha=0.7) # left, height, width, bottom

# Use the function to plot groups of elements
height=3e3
bottom=2.4e4
plot_elem('red', height, bottom, 'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
plot_elem('blue', height, bottom, 'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
plot_elem('orange', height, bottom, 'TAXS', 'TAXN') # Passive protectors: TAS, TAN
plot_elem('black', height, bottom, 'TCT') # Tertiary collimators
plot_elem('green', height, bottom, 'ACF') # CRab cavities

# Save the plot
plt.subplots_adjust(left=0.12, bottom=0.15, right=0.97, top=0.91)
plt.savefig('beta_functions.png', dpi=DPI)
plt.clf()