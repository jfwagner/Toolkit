#!/usr/local/bin/python
# ------------------------------------------------------------------------------
# A script to read TFS files
# ------------------------------------------------------------------------------
import re
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from util import get_ip1
from util import get_madx_columns
from util import plot_elem

# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
infile_b1_twiss = sys.argv[1]
infile_b2_twiss = sys.argv[2]
infile_b1_survey = sys.argv[3]
infile_b2_survey = sys.argv[4]
headers = sys.argv[5:]

# Constants
gamma_rel = 7460.52280875
beta_rel = 0.999999991017
emittance = 2.5e-6

# TWISS, BEAM 1
#-------------------------------------------------------------------------------
# Get the twiss data as a dictionary
for item in headers:
    data_dict = get_madx_columns(infile_b1_twiss, item)
    print data_dict[item]
    
    # data_dict[item]
    # print  '%s' %(item + '_twiss_b1')
#     var = data_dict[item]

# print S_twiss_b1
    

# Extract the data from the dictionary to lists for each column
# s_twiss_b1 = twiss_b1['S']
# l_twiss_b1 = twiss_b1['L']
# name_twiss_b1 = twiss_b1['NAME']
# x_twiss_b1 = twiss_b1['X']
# y_twiss_b1 = twiss_b1['Y']
# beta_x_twiss_b1 = twiss_b1['BETX']
# beta_y_twiss_b1 = twiss_b1['BETY']

# # TWISS, BEAM 2
# #-------------------------------------------------------------------------------
# # Get the twiss data as a dictionary
# twiss_b2 = get_madx_columns(infile_b2_twiss, 'S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME')

# # Extract the data from the dictionary to lists for each column
# s_twiss_b2 = twiss_b2['S']
# l_twiss_b2 = twiss_b2['L']
# name_twiss_b2 = twiss_b2['NAME']
# x_twiss_b2 = twiss_b2['X']
# y_twiss_b2 = twiss_b2['Y']
# beta_x_twiss_b2 = twiss_b2['BETX']
# beta_y_twiss_b2 = twiss_b2['BETY']

# # SURVEY, BEAM 1
# #-------------------------------------------------------------------------------
# # Get the survey data as a dictionary
# survey_b1 = get_madx_columns(infile_b1_survey, 'S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME')

# # Extract the data from the dictionary to lists for each column
# s_survey_b1 = survey_b1['S']
# l_survey_b1 = survey_b1['L']
# name_survey_b1 = survey_b1['NAME']
# x_survey_b1 = survey_b1['X']
# y_survey_b1 = survey_b1['Y']
# beta_x_survey_b1 = survey_b1['BETX']
# beta_y_survey_b1 = survey_b1['BETY']

# # SURVEY, BEAM 2
# #-------------------------------------------------------------------------------
# # Get the survey data as a dictionary
# survey_b2 = get_madx_columns(infile_b2_survey, 'S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME')

# # Extract the data from the dictionary to lists for each column
# s_survey_b2 = survey_b2['S']
# l_survey_b2 = survey_b2['L']
# name_survey_b2 = survey_b2['NAME']
# x_survey_b2 = survey_b2['X']
# y_survey_b2 = survey_b2['Y']
# beta_x_survey_b2 = survey_b2['BETX']
# beta_y_survey_b2 = survey_b2['BETY']


# # ------------------------------------------------------------------------------
# # PLOTTING
# # ------------------------------------------------------------------------------
# # Plot characteristics
# DPI = 300
# textwidth = 6
# font_spec = {"font.family": "serif", # use as default font
#              "font.serif": ["New Century Schoolbook"], # custom serif font
#              "font.sans-serif": ["helvetica"], # custom sans-serif font
#              "font.size":14,
#              "font.weight":"bold",
#             }
# rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
# rcParams['figure.figsize']=textwidth, textwidth/1.618
# rcParams.update(font_spec)

# # Plot the vertical orbit
# plt.plot(s_twiss_b1, y_twiss_b1,color='blue', label='Beam 1')
# plt.plot(s_twiss_b2, y_twiss_b2,color='red', label='Beam 2')
# plt.xlabel("s (m)")
# plt.ylabel("Vertical orbit (m)")
# plt.xlim([-200,200])
# plt.grid(b=None, which='major')
# plt.legend(loc='lower right', prop={'size':9})
# plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
# plt.subplots_adjust(left=0.12, bottom=0.15, right=0.97, top=0.91)
# plt.savefig('orbit_y.png', dpi=DPI)
# plt.clf()


# # Plot the beta functions
# plt.plot(sx_b1_twiss, betax_b1_twiss, label='Beta x')
# plt.plot(sy_b1_twiss, betay_b1_twiss, label='Beta y')
# plt.xlabel("s (m)")
# plt.ylabel("Beta functions (m)")
# plt.xlim([-200,200])
# plt.ylim([0,3e4])
# plt.grid(b=None, which='major')
# plt.legend(loc='lower right', prop={'size':9})
# plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))

# # Plot the elements
# height = 3e3
# bottom = 2.4e4
# plot_elem('red', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
# plot_elem('blue', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
# plot_elem('orange', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
# plot_elem('black', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'TCT') # Tertiary collimators
# plot_elem('green', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'ACF') # CRab cavities

# # Save the plot
# plt.subplots_adjust(left=0.12, bottom=0.15, right=0.97, top=0.91)
# plt.savefig('beta_functions.png', dpi=DPI)
# plt.clf()

# # Plot the beams
# # BEAM 1
# # Y
# s_b1_twiss_array = np.asarray(s_b1_twiss)
# y_b1_twiss_array = np.asarray(y_b1_twiss)
# y_b1_survey_array = np.asarray(y_b1_survey)
# betay_b1_twiss_array = np.asarray(betay_b1_twiss)
# emy_b1_twiss_array = np.asarray(emy_b1_twiss)
# sigy_b1_twiss_array = np.asarray(sigy_b1_twiss)
# sigma_y_b1 = np.sqrt(np.dot(emy_b1_twiss_array,betay_b1_twiss_array))
# # X
# x_b1_twiss_array = np.asarray(x_b1_twiss)
# x_b1_survey_array = np.asarray(x_b1_survey)
# betax_b1_twiss_array = np.asarray(betax_b1_twiss)
# emx_b1_twiss_array = np.asarray(emx_b1_twiss)
# sigx_b1_twiss_array = np.asarray(sigx_b1_twiss)
# sigma_x_b1 = np.sqrt(np.dot(emx_b1_twiss_array,betax_b1_twiss_array))
# # BEAM 2
# # Y
# s_b2_twiss_array = np.asarray(s_b2_twiss)
# y_b2_twiss_array = np.asarray(y_b2_twiss)
# y_b2_survey_array = np.asarray(y_b2_survey)
# betay_b2_twiss_array = np.asarray(betay_b2_twiss)
# emy_b2_twiss_array = np.asarray(emy_b2_twiss)
# sigy_b2_twiss_array = np.asarray(sigy_b2_twiss)
# sigma_y_b2 = np.sqrt(np.dot(emy_b2_twiss_array,betay_b2_twiss_array))
# # X
# x_b2_twiss_array = np.asarray(x_b2_twiss)
# x_b2_survey_array = np.asarray(x_b2_survey)
# betax_b2_twiss_array = np.asarray(betax_b2_twiss)
# emx_b2_twiss_array = np.asarray(emx_b2_twiss)
# sigx_b2_twiss_array = np.asarray(sigx_b2_twiss)
# sigma_x_b2 = np.sqrt(np.dot(emx_b2_twiss_array,betax_b2_twiss_array))

# # VERTICAL ORBIT
# plt.plot(s_b1_twiss_array, y_b1_twiss_array, color='blue', label='Beam 1')
# plt.plot(s_b2_twiss_array, y_b2_twiss_array, color='red', label='Beam 2')
# plt.xlabel("s (m)")
# plt.ylabel("Vertical orbit (m)")
# plt.xlim([-200,200])
# plt.grid(b=None, which='major')
# plt.legend(loc='lower right', prop={'size':9})
# plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
# height = 0.01
# bottom = 0.03
# plot_elem('red', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
# plot_elem('blue', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
# plot_elem('orange', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
# plot_elem('black', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'TCT') # Tertiary collimators
# plot_elem('green', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'ACF') # CRab cavities
# plt.subplots_adjust(left=0.12, bottom=0.15, right=0.97, top=0.91)
# plt.savefig('orbit_y.png', dpi=DPI)
# plt.clf()

# HORIZONTAL ORBIT
# plt.plot(s_b1_twiss_array, x_b1_twiss_array, color='blue', label='Beam 1')
# plt.plot(s_b2_twiss_array, x_b2_twiss_array, color='red', label='Beam 2')
# plt.xlabel("s (m)")
# plt.ylabel("Horizontal orbit (m)")
# plt.xlim([-200,200])
# plt.grid(b=None, which='major')
# plt.legend(loc='lower right', prop={'size':9})
# plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
# height = 0.01
# bottom = 0.03
# plot_elem('red', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
# plot_elem('blue', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
# plot_elem('orange', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
# plot_elem('black', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'TCT') # Tertiary collimators
# plot_elem('green', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'ACF') # CRab cavities
# plt.subplots_adjust(left=0.12, bottom=0.15, right=0.97, top=0.91)
# plt.savefig('orbit_x.png', dpi=DPI)
# plt.clf()
