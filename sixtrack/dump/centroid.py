#!/usr/bin/env python
import heapq
import random
import re
import sys

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams


from util import get_rel_params

turns = int(sys.argv[1])
failure_turn = int(sys.argv[2])
thetitle = sys.argv[3]
infile = 'dump.txt'

sigma = np.sqrt(3.35e-10)

# TCP MARKER
alpha_x = 2.1177081
alpha_y = -1.0986181
beta_x  = 158.417774
beta_y  = 78.495404
# # IP3
# alpha_x = 2.315986
# alpha_y = -2.635533
# beta_x  = 122.173726
# beta_y  = 217.616330

def is_header(line):
    return re.search(r'#|@|\*|%|\$|&', line) is not None

def get_turn(infile, turn):
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            if line_list[1] == str(turn):
                yield line_list

def do_floquet(infile, turn):
    start_line = get_turn(infile, turn)
    x  = []
    xp = []
    y  = []
    yp = []
    z  = []
    pid = []
    for line in start_line:
        idf = int(line[0])
        xf  = float(line[3])*1e-3
        xpf = float(line[4])*1e-3
        yf  = float(line[5])*1e-3
        ypf = float(line[6])*1e-3
        zf = float(line[7])*1e-3
        x.append(xf/np.sqrt(beta_x))
        y.append(yf/np.sqrt(beta_y))
        xp.append((xf*alpha_x)/np.sqrt(beta_x) + xpf*np.sqrt(beta_x))
        yp.append((yf*alpha_y)/np.sqrt(beta_y) + ypf*np.sqrt(beta_y))
        z.append(zf)
        pid.append(idf)
    return pid, x, xp, y, yp, z

def get_radius(x, xp, y, yp):
    gamma_rel, beta_rel, p0, mass = get_rel_params(7e12)

    term_1_x = np.mean(np.multiply(x,x)) - np.multiply(np.mean(x), np.mean(x))
    term_2_x = np.mean(np.multiply(x,xp)) - np.multiply(np.mean(x),np.mean(xp))
    term_3_x = np.mean(np.multiply(xp,x)) - np.multiply(np.mean(xp), np.mean(x))
    term_4_x = np.mean(np.multiply(xp,xp)) - np.multiply(np.mean(xp),np.mean(xp))

    term_1_y = np.mean(np.multiply(y,y)) - np.multiply(np.mean(y), np.mean(y))
    term_2_y = np.mean(np.multiply(y,yp)) - np.multiply(np.mean(y),np.mean(yp))
    term_3_y = np.mean(np.multiply(yp,y)) - np.multiply(np.mean(yp), np.mean(y))
    term_4_y = np.mean(np.multiply(yp,yp)) - np.multiply(np.mean(yp),np.mean(yp))

    det_x = np.multiply(term_1_x, term_4_x) - np.multiply(term_3_x, term_2_x)
    em_x = np.sqrt(abs(det_x))

    det_y = np.multiply(term_1_y, term_4_y) - np.multiply(term_3_y, term_2_y)
    em_y = np.sqrt(abs(det_y))

    return np.sqrt(em_x), np.sqrt(em_y)


n = 0
o = 0


x2 = []
y2 = []
outfile = 'sigma.txt'
with open(outfile, 'w') as f:
    for turn in range(0, turns + 1):
        pid, x, xp, y, yp, z = do_floquet(infile, turn)
        for i, j, k, l in zip(pid, y, yp, z):
            # if i == the_particle:
            if i == 1:
                x2.append(turn)
                y2.append(np.sqrt((n-j)**2 + (o-k)**2)/sigma)
                print >> f, turn, round(np.sqrt((n-j)**2 + (o-k)**2)/sigma,6), l

font_spec = {"font.size": 10, }
rcParams.update(font_spec)
rcParams['legend.frameon'] = 'True'
rcParams['figure.figsize'] = 4, 2
fig = plt.figure()
plt.plot(x2, y2,color='blue')
plt.xlabel('Turns')
plt.ylabel(r'Displacement ($\sigma_y$)')
plt.title(thetitle)
plt.xlim([0, turns])
plt.axvline(x=failure_turn, linewidth=0.7, color='black')
plt.annotate('Failure', xy=(failure_turn - 1.5,  (max(y2) + max(y2)* 0.7) / 2), rotation='vertical', size='6', verticalalignment='center')
if y2[turns-1] < 0.0999:
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('sigma.png', dpi=1000)
plt.savefig('sigma.eps', format='eps', dpi=1000)
plt.clf()



yf = np.fft.fft(y2)
freqs = np.fft.fftfreq(len(y2))
plt.plot(abs(freqs),abs(yf))
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.xlim([0.30, 0.37])
# plt.ylim([0, 3])
plt.ylim([0, 1500])
plt.savefig('fft.png', dpi=1000)
plt.savefig('fft.eps', format='eps', dpi=1000)
plt.clf()

sel_freqs = []
sel_amp = []
d = {}
for i, j in zip(abs(freqs), abs(yf)):
    if i > 0 and i < 1:
        d[j] = i
        sel_freqs.append(i)
        sel_amp.append(j)


maximums = heapq.nlargest(20, sel_amp)
for i in maximums:
    print d[i], i