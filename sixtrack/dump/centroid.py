#!/usr/bin/env python
import re
import sys

import numpy as np

from util import get_rel_params

turns = int(sys.argv[1])
infile = 'dump.txt'

alpha_x = 0.003485
alpha_y = -0.000764
beta_x  = 0.150739
beta_y  = 0.150235

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
    x =  []
    xp = []
    y  = []
    yp = []
    for line in start_line:
        xf  = float(line[3])*1e-3
        xpf = float(line[4])*1e-3
        yf  = float(line[5])*1e-3
        ypf = float(line[6])*1e-3
        x.append(xf/np.sqrt(beta_x))
        y.append(yf/np.sqrt(beta_y))
        xp.append((xf*alpha_x)/np.sqrt(beta_x) + xpf*np.sqrt(beta_x))
        yp.append((yf*alpha_y)/np.sqrt(beta_y) + ypf*np.sqrt(beta_y))
    return x, xp, y, yp

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


x1, xp1, y1, yp1 = do_floquet(infile,1)
rx1, ry1 = get_radius(x1, xp1, y1, yp1)

x2, xp2, y2, yp2 = do_floquet(infile,2)
rx2, ry2 = get_radius(x2, xp2, y2, yp2)

print '>> Phase space radius for first turn: ' + str(rx1) + ' ' + str(ry1)
print '>> Phase space radius for second turn, crabs on: ' + str(rx2) + ' ' + str(ry2)

print '>> Phase space radius normalized with the second turn values:'

for turn in range(2, turns + 1):
    x, xp, y, yp = do_floquet(infile, turn)
    rx, ry = get_radius(x, xp, y, yp)
    print turn, round(abs(1 - (rx/rx2)),3), round(abs(1 - (ry/ry2)),3)
