#!/usr/local/bin/python
# ------------------------------------------------------------------------------
# A script to read TFS files
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
from util import get_madx_columns
from util import plot_elem
from util import plot_beams

# ------------------------------------------------------------------------------
# Feed the input to the script by command line
# ------------------------------------------------------------------------------
__author__ = 'Andrea Santamaria Garcia'
 
parser = argparse.ArgumentParser(description='This is a script to plot data from tfs files.')
parser.add_argument('-t_b1','--twiss_b1', help='Twiss Beam 1 file',required=True)
parser.add_argument('-t_b2','--twiss_b2',help='Twiss Beam 2 file', required=True)
parser.add_argument('-s_b1','--survey_b1', help='Survey Beam 1 file',required=False)
parser.add_argument('-s_b2','--survey_b2',help='Survey Beam 2 file', required=False)
parser.add_argument('-p','--plot',help='Plot type', required=True)
parser.add_argument('-ip1','--plot_ip1',help='Plotting around IP1', required=True)
args = parser.parse_args()
 
## show values ##
print " "
print "********************************************"
print "PLOTTING PARAMETERS"
print "********************************************"
print ("Twiss file for Beam 1: %s" % args.twiss_b1 )
print ("Twiss file for Beam 2: %s" % args.twiss_b2 )
print ("Survey file for Beam 1: %s" % args.survey_b1 )
print ("Survey file for Beam 2: %s" % args.survey_b2 )
print ("Plot type: %s" % args.plot )
print ("Plotting around IP1: %s" % args.plot_ip1 )
print " "

## put the data in a dictionary ##
twiss_b1 = get_madx_columns(args.twiss_b1, 'S', 'X', 'Y', 'BETX', 'BETY', 'NAME', 'L')
twiss_b2 = get_madx_columns(args.twiss_b2, 'S', 'X', 'Y', 'BETX', 'BETY', 'NAME', 'L')

## plot characteristics ##
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
fig = plt.figure()

## start the correct plot loop ##

if args.plot == "ORBIT":
    
    ## beam 1 data ##
    s_b1_y, y_b1, one_sigma_y_b1, m_one_sigma_y_b1, five_sigma_y_b1, m_five_sigma_y_b1 = plot_beams(twiss_b1['S'], twiss_b1['Y'], 7e12, 2.5e-6, twiss_b1['BETY'], args.plot_ip1)
    s_b1_x, x_b1, one_sigma_x_b1, m_one_sigma_x_b1, five_sigma_x_b1, m_five_sigma_x_b1 = plot_beams(twiss_b1['S'], twiss_b1['X'], 7e12, 2.5e-6, twiss_b1['BETX'], args.plot_ip1)

    ## beam 2 data ##
    s_b2_y, y_b2, one_sigma_y_b2, m_one_sigma_y_b2, five_sigma_y_b2, m_five_sigma_y_b2 = plot_beams(twiss_b2['S'], twiss_b2['Y'], 7e12, 2.5e-6, twiss_b2['BETY'], args.plot_ip1)
    s_b2_x, x_b2, one_sigma_x_b2, m_one_sigma_x_b2, five_sigma_x_b2, m_five_sigma_x_b2 = plot_beams(twiss_b2['S'], twiss_b2['X'], 7e12, 2.5e-6, twiss_b2['BETX'], args.plot_ip1)

    ## VERTICAL ORBIT ##
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
    s_temp, name  = get_ip1(twiss_b1['S'], twiss_b1['NAME'])
    s, l = get_ip1(twiss_b1['S'], twiss_b1['L'])
    plot_elem('red', height, bottom, name, s, l,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
    plot_elem('blue', height, bottom, name, s, l,  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
    plot_elem('orange', height, bottom, name, s, l,  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
    plot_elem('black', height, bottom, name, s, l,  'TCT') # Tertiary collimators
    plot_elem('green', height, bottom, name, s, l,  'ACF') # Crab cavities
    ax1.set_xlabel("s (m)")
    ax1.set_ylabel(r"$y, \sigma_y, 5 \sigma_y$ [m]")
    ax1.set_xlim([-200,200])
    ax1.grid(b=None, which='major')
    ax1.legend(loc='lower right', prop={'size':9})
    ax1.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.94, top=0.90)
    plt.savefig('orbit_y.png', dpi=DPI)
    plt.clf()


    ## HORIZONTAL ORBIT ##
    ax2 = fig.add_subplot(111)
    ## plot beam 1 ##
    ax2.plot(s_b1_x, x_b1, color='blue', label='Beam 1')
    ax2.plot(s_b1_x, one_sigma_x_b1, color='blue')
    ax2.plot(s_b1_x, m_one_sigma_x_b1, color='blue')
    ax2.fill_between(s_b1_x, one_sigma_x_b1, m_one_sigma_x_b1, facecolor='blue')
    ax2.plot(s_b1_x, m_five_sigma_x_b1, color='blue', alpha=0.3)
    ax2.fill_between(s_b1_x, one_sigma_x_b1, five_sigma_x_b1, facecolor='blue', alpha=0.3)
    ax2.fill_between(s_b1_x, m_five_sigma_x_b1, m_one_sigma_x_b1, facecolor='blue', alpha=0.3)

    ## plot beam 2 ##
    ax2.plot(s_b2_x, x_b2, color='red', label='Beam 2')
    ax2.plot(s_b2_x, one_sigma_x_b2, color='red')
    ax2.plot(s_b2_x, m_one_sigma_x_b2, color='red')
    ax2.fill_between(s_b2_x, one_sigma_x_b2, m_one_sigma_x_b2, facecolor='red')
    ax2.plot(s_b2_x, m_five_sigma_x_b2, color='red', alpha=0.3)
    ax2.fill_between(s_b2_x, one_sigma_x_b2, five_sigma_x_b2, facecolor='red', alpha=0.3)
    ax2.fill_between(s_b2_x, m_five_sigma_x_b2, m_one_sigma_x_b2, facecolor='red', alpha=0.3)

    ## plot the elements ##
    height = max(five_sigma_x_b1)/5
    bottom = max(five_sigma_x_b1) + max(five_sigma_x_b1)/4
    s_temp, name  = get_ip1(twiss_b1['S'], twiss_b1['NAME'])
    s, l = get_ip1(twiss_b1['S'], twiss_b1['L'])
    plot_elem('red', height, bottom, name, s, l,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
    plot_elem('blue', height, bottom, name, s, l,  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
    plot_elem('orange', height, bottom, name, s, l,  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
    plot_elem('black', height, bottom, name, s, l,  'TCT') # Tertiary collimators
    plot_elem('green', height, bottom, name, s, l,  'ACF') # Crab cavities
    ax2.set_xlabel("s (m)")
    ax2.set_ylabel(r"$x, \sigma_x, 5 \sigma_x$ [m]")
    ax2.set_xlim([-200,200])
    ax2.grid(b=None, which='major')
    ax2.legend(loc='lower right', prop={'size':9})
    ax2.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.94, top=0.90)
    plt.savefig('orbit_x.png', dpi=DPI)
    plt.clf()
   
elif args.plot == "BETA":
    if args.plot_ip1 == "no":
        plt.plot(twiss_b1['S'], twiss_b1['BETY'] ,color='blue', label='Beta Y')
        plt.plot(twiss_b1['S'], twiss_b1['BETX'] , color='green', label='Beta X')
        ## plot the elements ##
        height = max(twiss_b1['BETY'])/5
        bottom = max(twiss_b1['BETY']) + max(twiss_b1['BETY'])/6
        plot_elem('red', height, bottom, twiss_b1['NAME'], twiss_b1['S'], twiss_b1['L'],  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
        plot_elem('blue', height, bottom, twiss_b1['NAME'], twiss_b1['S'], twiss_b1['L'],  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
        plot_elem('orange', height, bottom, twiss_b1['NAME'], twiss_b1['S'], twiss_b1['L'],  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
        plot_elem('black', height, bottom, twiss_b1['NAME'], twiss_b1['S'], twiss_b1['L'],  'TCT') # Tertiary collimators
        plot_elem('green', height, bottom, twiss_b1['NAME'], twiss_b1['S'], twiss_b1['L'],  'ACF') # Crab cavities
        plt.xlabel("s (m)")
        plt.ylabel("Beta functions (m)")
        plt.xlim([-200,200])
        plt.grid(b=None, which='major')
        plt.legend(loc='lower right', prop={'size':9})
        plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
        plt.subplots_adjust(left=0.15, bottom=0.15, right=0.94, top=0.90)
        plt.savefig('beta_functions.png', dpi=DPI)
        plt.clf()
    elif args.plot_ip1 == "yes":
        s_b1_temp, betay_b1 = get_ip1(twiss_b1['S'], twiss_b1['BETY'])
        s_b1, betax_b1 = get_ip1(twiss_b1['S'], twiss_b1['BETX'])
        plt.plot(s_b1, betay_b1, color='blue', label='Beta Y')
        plt.plot(s_b1, betax_b1, color='green', label='Beta X')
        ## plot the elements ##
        height = max(twiss_b1['BETY'])/5
        bottom = max(twiss_b1['BETY']) + max(twiss_b1['BETY'])/6
        s_temp, name  = get_ip1(twiss_b1['S'], twiss_b1['NAME'])
        s, l = get_ip1(twiss_b1['S'], twiss_b1['L'])
        plot_elem('red', height, bottom, name, s, l,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
        plot_elem('blue', height, bottom, name, s, l,  'MBX', 'MBRC', 'MBRS', 'MBRB', 'MB') # Dipoles: D1, D2, D3, D4
        plot_elem('orange', height, bottom, name, s, l,  'TAXS', 'TAXN') # Passive protectors: TAS, TAN
        plot_elem('black', height, bottom, name, s, l,  'TCT') # Tertiary collimators
        plot_elem('green', height, bottom, name, s, l,  'ACF') # Crab cavities
        plt.xlabel("s (m)")
        plt.ylabel("Beta functions (m)")
        plt.xlim([-200,200])
        plt.grid(b=None, which='major')
        plt.legend(loc='lower right', prop={'size':9})
        plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
        plt.subplots_adjust(left=0.15, bottom=0.15, right=0.94, top=0.90)
        plt.savefig('beta_functions.png', dpi=DPI)
        plt.clf()
    else:
        print "Input for plottinga round IP1 option should be yes or no"
else:
    print "Sorry, that plotting option does not exist"

