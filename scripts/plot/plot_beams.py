#!/usr/local/bin/python
# ------------------------------------------------------------------------------
# This script is designed to plot MAD-X output. It will issue one type of plot
# at a time. If you want to plot several types, launch this script several times
# with another script instead of modifying this one.
# ------------------------------------------------------------------------------
# Example of use (options can be written in any order):
# plot_beams.py -t_b1 twiss_ip1_b1.tfs -t_b2 twiss_ip1_b2.tfs -p ORBIT -ip 8 -lim 250
# ------------------------------------------------------------------------------
from __future__ import division
import argparse
import re
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from util import get_ip1
from util import get_ir
from util import get_madx_columns
from util import plot_elem
from util import plot_twiss


## feed the input to the script by command line ##
__author__ = 'Andrea Santamaria Garcia'
 
parser = argparse.ArgumentParser(description='This is a script to plot data from tfs files.')
parser.add_argument('-t_b1','--twiss_b1', help='Twiss Beam 1 file',required=True)
parser.add_argument('-t_b2','--twiss_b2', help='Twiss Beam 2 file', required=True)
parser.add_argument('-s_b1','--survey_b1', help='Survey Beam 1 file',required=False)
parser.add_argument('-s_b2','--survey_b2', help='Survey Beam 2 file', required=False)
parser.add_argument('-p','--plot', help='Plot type', required=True)
parser.add_argument('-ip','--plot_ip', help='Plotting around a certain IP', required=True)
parser.add_argument('-lim','--limit', help='Horizontal limit of the plot', required=True)
args = parser.parse_args()
 
## show the values specified by the user##
print " "
print "********************************************"
print "PLOTTING PARAMETERS"
print "********************************************"
print ("Twiss file for Beam 1: %s" % args.twiss_b1 )
print ("Twiss file for Beam 2: %s" % args.twiss_b2 )
print ("Survey file for Beam 1: %s" % args.survey_b1 )
print ("Survey file for Beam 2: %s" % args.survey_b2 )
print ("Plot type: %s" % args.plot )
print ("Plotting around IP: %s" % args.plot_ip )
print ("from: %s" % args.limit )

## put the data from the twiss tfs file in a dictionary ##
twiss_b1 = get_madx_columns(args.twiss_b1, 'S', 'X', 'Y', 'BETX', 'BETY', 'NAME', 'L')
twiss_b2 = get_madx_columns(args.twiss_b2, 'S', 'X', 'Y', 'BETX', 'BETY', 'NAME', 'L')

## plot characteristics ##
DPI = 300
textwidth = 6
font_spec = {"font.family": "serif", # use as default font
             "font.serif": ["New Century Schoolbook"], # custom serif font
             #"font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":14,
             "font.weight":"bold",
            }
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.618
rcParams.update(font_spec)
fig = plt.figure()


## start the correct plot loop ##
if args.plot == "ORBIT": ## orbit plots ##
   
    if args.survey_b1 is None and args.survey_b2 is None: # no survey files

        print " "
        print ">> TWISS"
        
        ## beam 1 data ##
        s_b1_y, y_b1, one_sigma_y_b1, m_one_sigma_y_b1, five_sigma_y_b1, m_five_sigma_y_b1 = plot_twiss(twiss_b1['S'], twiss_b1['Y'], 7e12, 2.5e-6, twiss_b1['BETY'], args.plot_ip, args.limit)
        s_b1_x, x_b1, one_sigma_x_b1, m_one_sigma_x_b1, five_sigma_x_b1, m_five_sigma_x_b1 = plot_twiss(twiss_b1['S'], twiss_b1['X'], 7e12, 2.5e-6, twiss_b1['BETX'], args.plot_ip, args.limit)

        ## beam 2 data ##
        s_b2_y, y_b2, one_sigma_y_b2, m_one_sigma_y_b2, five_sigma_y_b2, m_five_sigma_y_b2 = plot_twiss(twiss_b2['S'], twiss_b2['Y'], 7e12, 2.5e-6, twiss_b2['BETY'], args.plot_ip, args.limit)
        s_b2_x, x_b2, one_sigma_x_b2, m_one_sigma_x_b2, five_sigma_x_b2, m_five_sigma_x_b2 = plot_twiss(twiss_b2['S'], twiss_b2['X'], 7e12, 2.5e-6, twiss_b2['BETX'], args.plot_ip, args.limit)
            
    if (args.survey_b1 is not None) != (args.survey_b2 is not None): # only one survey file
        print " "
        print ">> You are missing one survey file. Exiting program..."
        sys.exit()
        
    if args.survey_b1 is not None and args.survey_b2 is not None: # both survey files

        print " "
        print ">> SURVEY"
        print ">> Sorry, the survey option is not available yet"
        sys.exit()
        
    ## starting the orbit plots ##
    print ">> Plotting vertical orbit..."

    ## VERTICAL ORBIT ##
    plt.clf()
    ax1 = fig.add_subplot(111)
    
    ## plot beam 1 ##
    ax1.plot(s_b1_y, y_b1, color='blue', label='Beam 1')
    ax1.plot(s_b1_y, one_sigma_y_b1, color='blue')
    ax1.plot(s_b1_y, m_one_sigma_y_b1, color='blue')
    ax1.fill_between(s_b1_y, one_sigma_y_b1, m_one_sigma_y_b1, facecolor='blue')
    ax1.plot(s_b1_y, m_five_sigma_y_b1, color='blue', alpha=0.3)
    ax1.fill_between(s_b1_y, one_sigma_y_b1, five_sigma_y_b1, facecolor='blue', alpha=0.3)
    ax1.fill_between(s_b1_y, m_five_sigma_y_b1, m_one_sigma_y_b1, facecolor='blue', alpha=0.3)

    ## plot beam 2 ##
    ax1.plot(s_b2_y, y_b2, color='red', label='Beam 2')
    ax1.plot(s_b2_y, one_sigma_y_b2, color='red')
    ax1.plot(s_b2_y, m_one_sigma_y_b2, color='red')
    ax1.fill_between(s_b2_y, one_sigma_y_b2, m_one_sigma_y_b2, facecolor='red')
    ax1.plot(s_b2_y, m_five_sigma_y_b2, color='red', alpha=0.3)
    ax1.fill_between(s_b2_y, one_sigma_y_b2, five_sigma_y_b2, facecolor='red', alpha=0.3)
    ax1.fill_between(s_b2_y, m_five_sigma_y_b2, m_one_sigma_y_b2, facecolor='red', alpha=0.3)

    ## plot the elements ##
    height = max(five_sigma_y_b1)/5
    bottom = max(five_sigma_y_b1) + max(five_sigma_y_b1)/4
    s_temp, name  = get_ir(args.plot_ip, twiss_b1['S'], twiss_b1['NAME'])
    s, l = get_ir(args.plot_ip, twiss_b1['S'], twiss_b1['L'])
    plot_elem('red', height, bottom, name, s, l, 'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
    plot_elem('blue', height, bottom, name, s, l, 'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
    plot_elem('orange', height, bottom, name, s, l, 'TAXS', 'TAXN') # Passive protectors: TAS, TAN
    plot_elem('black', height, bottom, name, s, l, 'TCT') # Tertiary collimators
    plot_elem('green', height, bottom, name, s, l, 'ACF') # Crab cavities

    ## set the plot details ##
    ax1.set_xlabel("s (m)")
    ax1.set_ylabel(r"$y, \sigma_y, 5 \sigma_y$ [m]")
    ax1.set_xlim([-float(args.limit), float(args.limit)])
    ax1.set_title('IP' + args.plot_ip )
    ax1.grid(b=None, which='major')
    ax1.legend(loc='lower right', prop={'size':9})
    ax1.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.94, top=0.90)
    plt.savefig('orbit_y_IP' + args.plot_ip + '.png', dpi=DPI)
    plt.clf()

    print ">> Plotting horizontal orbit..."
    
    ## HORIZONTAL ORBIT ##
    plt.clf()
    ax2 = fig.add_subplot(111)
    
    ## plot beam 1 ##
    ax2.plot(s_b1_x, x_b1, color='blue', label='Beam 1')
    ax2.plot(s_b1_x, one_sigma_x_b1, color='blue')
    ax2.plot(s_b1_x, m_one_sigma_x_b1, color='blue')
    ax2.plot(s_b1_x, m_five_sigma_x_b1, color='blue', alpha=0.3)
    ax2.fill_between(s_b1_x, one_sigma_x_b1, m_one_sigma_x_b1, facecolor='blue')
    ax2.fill_between(s_b1_x, one_sigma_x_b1, five_sigma_x_b1, facecolor='blue', alpha=0.3)
    ax2.fill_between(s_b1_x, m_five_sigma_x_b1, m_one_sigma_x_b1, facecolor='blue', alpha=0.3)

    ## plot beam 2 ##
    ax2.plot(s_b2_x, x_b2, color='red', label='Beam 2')
    ax2.plot(s_b2_x, one_sigma_x_b2, color='red')
    ax2.plot(s_b2_x, m_one_sigma_x_b2, color='red')
    ax2.plot(s_b2_x, m_five_sigma_x_b2, color='red', alpha=0.3)
    ax2.fill_between(s_b2_x, one_sigma_x_b2, m_one_sigma_x_b2, facecolor='red')
    ax2.fill_between(s_b2_x, one_sigma_x_b2, five_sigma_x_b2, facecolor='red', alpha=0.3)
    ax2.fill_between(s_b2_x, m_five_sigma_x_b2, m_one_sigma_x_b2, facecolor='red', alpha=0.3)

    ## plot the elements ##
    height = max(five_sigma_x_b1)/5
    bottom = max(five_sigma_x_b1) + max(five_sigma_x_b1)/4
    s_temp, name  = get_ir(args.plot_ip, twiss_b1['S'], twiss_b1['NAME'])
    s, l = get_ir(args.plot_ip, twiss_b1['S'], twiss_b1['L'])
    plot_elem('red', height, bottom, name, s, l,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
    plot_elem('blue', height, bottom, name, s, l,  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
    plot_elem('orange', height, bottom, name, s, l,  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
    plot_elem('black', height, bottom, name, s, l,  'TCT') # Tertiary collimators
    plot_elem('green', height, bottom, name, s, l,  'ACF') # Crab cavities

    ## set the plot details ##
    ax2.set_xlabel("s (m)")
    ax2.set_ylabel(r"$x, \sigma_x, 5 \sigma_x$ [m]")
    ax2.set_xlim([-float(args.limit), float(args.limit)])
    ax1.set_title('IP' + args.plot_ip )
    ax2.grid(b=None, which='major')
    ax2.legend(loc='lower right', prop={'size':9})
    ax2.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.94, top=0.90)
    plt.savefig('orbit_x_IP' + args.plot_ip + '.png', dpi=DPI)
    plt.clf()

    print ">> DONE!"
   
else:
    print " "
    print ">> Sorry, the " + args.plot +  " plotting option does not exist"
    sys.exit()
