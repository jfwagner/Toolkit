#!/usr/bin/env python
import re

import numpy as np

infile = 'dump_ip1.txt'

def is_header(line):
    return re.search(r'#|@|\*|%|\$|&', line) is not None

def get_turn(infile, turn):
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            if line_list[1] == turn:
                yield line_list

def get_tilt(infile, turn):
    start_line = get_turn(infile, turn)
    yp = []
    for line in start_line:
        yp.append(float(line[6])*1e-3)
    return np.mean(yp)*1e6

turns = 20

for i in range(1, turns + 1):
    print  i, round( get_tilt(infile, str(i)),2)