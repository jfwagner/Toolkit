#!/usr/bin/env python
import os
import re
import sys

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData, get_ip1

# ------------------------------------------------------------------------------
# DATA FILES
# ------------------------------------------------------------------------------
twissb1 = '/Users/andrea/Dropbox/ThesisSims/MADX/4CCs_noBB/twiss_hllhc_b1.tfs'
# KEYWORD NAME S L X Y BETX BETY ALFX ALFY MUX MUY DX DY DPX DPY PX PY

apb1 = '/Users/andrea/Dropbox/ThesisSims/MADX/4CCs_noBB/aperture_b1.tfs'
# S  L  APER_1  APER_2  APER_3  APER_4  APERTYPE

surveyb1 = '/Users/andrea/Dropbox/ThesisSims/MADX/4CCs_noBB/survey_lhcb1.tfs'
# NAME KEYWORD S L ANGLE X Y Z THETA PHI PSI GLOBALTILT SLOT_ID ASSEMBLY_ID MECH_SEP V_POS

# ------------------------------------------------------------------------------
# EXTRACTING THE DATA
# ------------------------------------------------------------------------------
def get_twiss(infile):
    if os.stat(infile).st_size == 0:
        print '>> ' + infile  + ' file is empty'
        return 0
    else:
        get     = GetData(infile)
        data    = get.data_column(dtype='string')
        name    = data[1]
        s       = np.asarray(data[2])
        l       = np.asarray(data[3])
        x       = np.asarray(data[4])
        y       = np.asarray(data[5])
        betx    = np.asarray(data[6])
        bety    = np.asarray(data[7])
        alfx    = np.asarray(data[8])
        alfy    = np.asarray(data[9])
        dx      = np.asarray(data[12])
        dy      = np.asarray(data[13])
        px      = np.asarray(data[16])
        py      = np.asarray(data[17])

    return name, s, l, x, y, betx, bety, alfx, alfy, dx, dy, px, py

def get_ap(infile):
    if os.stat(infile).st_size == 0:
        print '>> ' + infile  + ' file is empty'
        return 0
    else:
        get         = GetData(infile)
        data        = get.data_column(dtype='string')
        name        = data[0]
        s           = np.asarray(data[1], dtype='float64')
        l           = np.asarray(data[2], dtype='float64')
        aper1       = np.asarray(data[3], dtype='float64')
        aper2       = np.asarray(data[4], dtype='float64')
        aper3       = np.asarray(data[5], dtype='float64')
        aper4       = np.asarray(data[6], dtype='float64')
        apertype    = np.asarray(data[7])
    return name, s, l, aper1, aper2, aper3, aper4, apertype


nameb1, sb1, lb1, xb1, yb1, betxb1, betyb1, alfxb1, alfyb1, dxb1, dyb1, pxb1, pyb1 = get_twiss(twissb1)

nameap, sap, lap, aper1, aper2, aper3, aper4, apertype = get_ap(apb1)

# ------------------------------------------------------------------------------
# CENTERING THE DATA AROUND IP1
# ------------------------------------------------------------------------------
sb11y, betyb11 = get_ip1(sb1, betyb1)
sb11x, betxb11 = get_ip1(sb1, betxb1)

# ------------------------------------------------------------------------------
# CENTERING THE PLOT IN A SPECIFIC IR
# ------------------------------------------------------------------------------
ir_position = [0, 3332.436584, 6664.7208, 9997.005016,
     13329.28923, 16661.72582, 19994.1624, 23315.37898]
ir_number = range(1, 8)

def get_limits(ir, m):
    d_ir = {}
    for p, n in zip(ir_position, ir_number):
        d_ir[n] = p
    return d_ir[ir] - m, d_ir[ir] + m

# ------------------------------------------------------------------------------
# TREATING THE APERTURE DATA
# ------------------------------------------------------------------------------
d_ap = {}
sap2 = []
for a1, a2, a3, a4, at, l, s, n in zip(aper1, aper2, aper3, aper4, apertype, lap, sap, nameap):
    # print type(a1), a2, a3, a4
    if (a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0) or (a1 == 9.999999 and a2 == 9.999999 and a3 == 9.999999 and a4 == 9.999999):
        continue
    elif at == 'CIRCLE':
        d_ap[s] = [a1, a1, l, n]
        sap2.append(s)
    else:
        xmin = min([a1, a3])
        ymin = min([a2, a4])
        d_ap[s] = [xmin, ymin, l, n]
        sap2.append(s)

# print d_ap

xap   = []
yap   = []
sap3  = []
for item in sap2:
    if d_ap[item][2] != 0:  # Accounting for the length
        xap.append(d_ap[item][0])
        xap.append(d_ap[item][0])
        yap.append(d_ap[item][1])
        yap.append(d_ap[item][1])
        sap3.append(item - d_ap[item][2])
        sap3.append(item)
    else:
        xap.append(d_ap[item][0])
        yap.append(d_ap[item][1])
        sap3.append(item)

sb1apy, yb1ap = get_ip1(sap3, xap)
sb1apx, xb1ap = get_ip1(sap3, yap)

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
font = {'family':'serif', 'serif': ['computer modern roman']}
plt.rc('font',**font)
rcParams['figure.figsize'] = 4, 2
params = {'text.latex.preamble': [r'\usepackage{siunitx}',r'\usepackage{mathrsfs}']}  # For mu symbol and curly font
plt.rcParams.update(params)
rcParams['legend.frameon'] = 'True'
fig = plt.figure()

plt.plot(sb11y, betyb11, label=r'$\beta_y$')
plt.plot(sb11x, betxb11, label=r'$\beta_x$')
plt.xlabel('s (m)')
plt.ylabel(r'$\beta$ (m)')
min, max = get_limits(1, 130)
# plt.ylim([0,15])
plt.xlim([min, max])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.legend(loc='upper right').get_frame().set_linewidth(0.5)
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('beta_b1.png', dpi=1000)
plt.savefig('beta_b1.eps', format='eps', dpi=1000)
plt.clf()


plt.plot(sb1apy, yb1ap, color='gray')
plt.plot(sb1apy, -np.asarray(yb1ap), color='gray')
plt.xlabel('s (m)')
plt.ylabel(r'$y$ (m)')
min, max = get_limits(1, 160)
plt.ylim([-0.1, 0.1])
plt.xlim([min, max])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
# plt.legend(loc='upper right').get_frame().set_linewidth(0.5)
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('ap_b1_y.png', dpi=1000)
plt.savefig('ap_b1_y.eps', format='eps', dpi=1000)
plt.clf()

plt.plot(sb1apy, xb1ap, color='gray')
plt.plot(sb1apy, -np.asarray(yb1ap), color='gray')
plt.xlabel('s (m)')
plt.ylabel(r'$x$ (m)')
min, max = get_limits(1, 160)
plt.ylim([-0.1, 0.1])
plt.xlim([min, max])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
# plt.legend(loc='upper right').get_frame().set_linewidth(0.5)
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('ap_b1_x.png', dpi=1000)
plt.savefig('ap_b1_x.eps', format='eps', dpi=1000)
plt.clf()
