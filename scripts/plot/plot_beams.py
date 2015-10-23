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
from util import get_madx_columns
from util import plot_elem

# Data files
infile_b1_twiss = 'twiss_lhcb1.tfs'
infile_b1_survey = 'survey_ip1_b1.tfs'
infile_b2_twiss = 'twiss_lhcb2.tfs'
infile_b2_survey = 'survey_ip1_b2.tfs'

# Get the columns for each file
dict_b1_twiss = get_madx_columns(infile_b1_twiss, 'S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME')
dict_b1_survey = get_madx_columns(infile_b1_survey, 'S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME')
dict_b2_twiss = get_madx_columns(infile_b2_twiss, 'S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME')
dict_b2_survey = get_madx_columns(infile_b2_survey, 'S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME')

# Constants
gamma_rel = 7460.52280875
beta_rel = 0.999999991017
emittance = 2.5e-6

# Treat data for IP1
s_b1_twiss, name_b1_twiss = get_ip1(dict_b1_twiss['S'], dict_b1_twiss['NAME']) #ToDo: fix the get_ip1 function
temp, l_b1_twiss = get_ip1(dict_b1_twiss['S'], dict_b1_twiss['L'])
temp, y_b1_twiss = get_ip1(dict_b1_twiss['S'], dict_b1_twiss['Y'])
sx_b1_twiss, betax_b1_twiss = get_ip1(dict_b1_twiss['S'], dict_b1_twiss['BETX'])
sy_b1_twiss, betay_b1_twiss = get_ip1(dict_b1_twiss['S'], dict_b1_twiss['BETY'])

s_b1_survey, name_b1_survey = get_ip1(dict_b1_survey['S'], dict_b1_survey['NAME']) #ToDo: fix the get_ip1 function
temp, l_b1_survey = get_ip1(dict_b1_survey['S'], dict_b1_survey['L'])
temp, y_b1_survey = get_ip1(dict_b1_survey['S'], dict_b1_survey['Y'])
sx_b1_survey, betax_b1_survey = get_ip1(dict_b1_survey['S'], dict_b1_survey['BETX'])
sy_b1_survey, betay_b1_survey = get_ip1(dict_b1_survey['S'], dict_b1_survey['BETY'])

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
plt.plot(sx_b1_twiss, betax_b1_twiss, label='Beta x')
plt.plot(sy_b1_twiss, betay_b1_twiss, label='Beta y')
plt.xlabel("s (m)")
plt.ylabel("Beta functions (m)")
plt.xlim([-200,200])
plt.ylim([0,3e4])
plt.grid(b=None, which='major')
plt.legend(loc='lower right', prop={'size':9})
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))

# Plot the elements
height = 3e3
bottom = 2.4e4
plot_elem('red', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
plot_elem('blue', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
plot_elem('orange', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
plot_elem('black', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'TCT') # Tertiary collimators
plot_elem('green', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'ACF') # CRab cavities

# Save the plot
plt.subplots_adjust(left=0.12, bottom=0.15, right=0.97, top=0.91)
plt.savefig('beta_functions.png', dpi=DPI)
plt.clf()

# Plot the beams
s_b1_twiss_array = np.asarray(s_b1_twiss)
y_b1_twiss_array = np.asarray(y_b1_twiss)
y_b1_survey_array = np.asarray(y_b1_survey)
betay_b1_twiss_array = np.asarray(betay_b1_twiss)
sigma_y = np.sqrt(betay_b1_twiss_array*emittance)

plt.plot(s_b1_twiss_array, y_b1_twiss_array + y_b1_survey_array, color='blue', label='Beam 1')
plt.plot(s_b1_twiss_array, y_b1_twiss_array + y_b1_survey_array  + sigma_y, color='blue')
plt.plot(s_b1_twiss_array, y_b1_twiss_array + y_b1_survey_array - sigma_y, color='blue')
plt.xlabel("s (m)")
plt.ylabel("Orbit (m)")
plt.xlim([-200,200])
# plt.ylim([0,3e4])
plt.grid(b=None, which='major')
plt.legend(loc='lower right', prop={'size':9})
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
plt.show()
