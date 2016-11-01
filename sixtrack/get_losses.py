#!/usr/bin/env python
# ------------------------------------------------------------------------------
# Script to extract data from impacts_real.
# The files "impacts_real.dat", "coll_summary.dat" and "CollPositionsHL.b1.dat"
# must be in the folder where you execute the script.
# Header of "impacts_real.dat":
# 1=icoll 2=c_rotation 3=s 4=x 5=xp 6=y 7=yp 8=nabs 9=np 10=ntu
# ------------------------------------------------------------------------------
import os
import re
import sys
from collections import Counter

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

# ------------------------------------------------------------------------------
# Specify how many runs of 19968 particles (current limit in SixTrack) are
# contained in your "impacts_real.dat" (>1 if concatenated file)
# ------------------------------------------------------------------------------
sixtrack_particle_limit = 19968
simulated_particles = int(sys.argv[1]) * sixtrack_particle_limit

print ' '
print 'Number of simulated particles: ', simulated_particles, '(100 %)'

# ------------------------------------------------------------------------------
# Associating name with collimator ID
# ------------------------------------------------------------------------------
infile_2 = 'coll_summary.dat'
get_2 = GetData(infile_2)
get_2 = GetData(infile_2)
data_2 = get_2.data_column(dtype='string')

names_2 = data_2[1]
numbers = data_2[0]

numbers_dict = {}
for i in range(len(names_2)):
    numbers_dict[float(numbers[i])] = names_2[i]

# ------------------------------------------------------------------------------
# Associating name with position
# ------------------------------------------------------------------------------
infile_3 = 'CollPositionsHL.b1.dat'
get_3 = GetData(infile_3)
data_3 = get_3.data_column(dtype='string')

names = data_3[1]
position = data_3[2]

translator_dict = {}
for i in range(len(names)):
    translator_dict[names[i]] = float(position[i])

# Usage: translator_dict[numbers_dict[29]]

# ------------------------------------------------------------------------------
# Curating impacts real
# ------------------------------------------------------------------------------
infile = 'impacts_real.dat'
rounding = 4


def is_header(line):
    return re.search(r'#|@|\*|%|\$|&', line) is not None


def get_impacts(infile, column):
    elas = 0
    inelas = 0
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            if line_list[7] != '4':
                inelas += 1
                yield line_list[column]
            else:
                elas += 1
    print ' '
    print 'Number of scattered protons: ', elas, '(' + str(round((float(elas) / simulated_particles) * 100, rounding)) + ' %)'
    print 'Number of absorbed protons: ', inelas, '(' + str(round((float(inelas) / simulated_particles) * 100, rounding)) + ' %)'


num_lines = sum(1 for line in open('impacts_real.dat'))
print 'Number of recorded impacts: ', num_lines - int(sys.argv[1]),  '(' + str(round((float(num_lines - 1) / simulated_particles) * 100, rounding)) + ' %)'


# ------------------------------------------------------------------------------
# Impacts per collimator
# ------------------------------------------------------------------------------
coll_data = []
start_line = get_impacts(infile, 0)
for line in start_line:
    coll_data.append(numbers_dict[float(line)])

coll_dict = Counter(coll_data)
print ' '
coll_out = 'loss_maps.txt'
with open(coll_out, 'w') as g:
    print >> g, '# Name Position Absorptions Percentage'
    for i, j in zip(coll_dict.keys(), coll_dict.values()):
        print 'Absorptions in collimator ' + str(i) + ': ', j,  '(' + str(round((float(j) / simulated_particles) * 100, rounding)) + ' %)'
        print >> g, i, translator_dict[
            str(i)], j, (float(j) / simulated_particles) * 100


# ------------------------------------------------------------------------------
# Losses per turn
# ------------------------------------------------------------------------------
turn_data = []
start_line_t = get_impacts(infile, 9)
for line in start_line_t:
    turn_data.append(line)

turns_dict = Counter(turn_data)
turns_out = 'data_turn.txt'
tt = []
vv = []
with open(turns_out, 'w') as h:
    print >> h, '# Position Absorptions Percentage'
    for t in range(1, max(np.asarray(turn_data, dtype='int')) + 2):
        try:
            turns_dict[str(t)]
            tt.append(t)
            vv.append(turns_dict[str(t)])
        except KeyError:
            tt.append(t)
            vv.append(0)
    for i, j in zip(tt, np.cumsum(vv[:0] + vv[:-1]).tolist()):
        print >> h, i, j, (float(j) / simulated_particles) * 100

# -----------------------------------------------------------------------------
# Creating a dict of dicts in order to access the losses per turn for each
# collimator.
# -----------------------------------------------------------------------------
d = {}
for name in translator_dict.keys():
    coll_name = []
    for i, j in zip(coll_data, turn_data):
        if i == name:
            coll_name.append(j)
    if len(coll_name) > 0:
        c = Counter(coll_name)
        d[name] = dict(c)


print ' '
print '>> Getting losses per turn for each collimator:'


def get_coll(name, turn_data):
    turn = []
    value = []
    try:
        d[name]
        outfile = name.translate(None, '.').lower() + '.txt'
        with open(outfile, 'w') as g:
            print >> g, '# Position Absorptions Percentage'
            for t in range(1, max(np.asarray(turn_data, dtype='int')) + 2):
                try:
                    d[name][str(t)]
                    turn.append(t)
                    value.append(d[name][str(t)])
                except KeyError:
                    turn.append(t)
                    value.append(0)
            for i, j in zip(turn, np.cumsum(value[:0] + value[:-1]).tolist()):
                print >> g, i, j, (float(j) / simulated_particles) * 100
            print 'File', outfile, 'created'
    except KeyError:
        print 'Collimator', name,  'not found or without losses'

# ------------------------------------------------------------------------------
# Primaries
# ------------------------------------------------------------------------------
get_coll('TCP.D6L7.B1', turn_data)
get_coll('TCP.B6L7.B1', turn_data)

# ------------------------------------------------------------------------------
# TCTs IP1
# ------------------------------------------------------------------------------
get_coll('TCTPH.4L1.B1', turn_data)
get_coll('TCTPV.4L1.B1', turn_data)
get_coll('TCTH.6L1.B1', turn_data)
get_coll('TCTV.6L1.B1', turn_data)

# ------------------------------------------------------------------------------
# TCTs IP5
# ------------------------------------------------------------------------------
get_coll('TCTPH.4L5.B1', turn_data)
get_coll('TCTPV.4L5.B1', turn_data)
get_coll('TCTH.6L5.B1', turn_data)
get_coll('TCTV.6L5.B1', turn_data)

# ------------------------------------------------------------------------------
# Extracting losses in the aperture
# ------------------------------------------------------------------------------


def get_lpi(infile):
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            yield line_list[2]

print ' '
infile_4 = 'LPI_test.s'
outfile_ap = 'aperture.txt'
if os.stat(infile_4).st_size == 0:
    open(outfile_ap, 'a').close()
    print '>> No losses in the aperture'
else:
    ap_data = []
    start_line = get_lpi(infile_4)
    for line in start_line:
        ap_data.append(float(line))
    lpi_dict = Counter(ap_data)
    with open(outfile_ap, 'w') as g:
        print >> g, '# Position Absorptions Percentage'
        for i, j in zip(lpi_dict.keys(), lpi_dict.values()):
            print >> g, i, j, (float(j) / simulated_particles) * 100

num_lines_ap = sum(1 for line in open('LPI_test.s'))
print '>> Number of losses in the aperture: ', num_lines_ap,  '(' + str(round((float(num_lines_ap - 1) / simulated_particles) * 100, rounding)) + ' %)'
