#!/usr/bin/env python
import os
import re
import sys

import collections
import numpy as np

from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

simulated_particles = float(sys.argv[1])*19968
bunches = 2748
beam_energy = 700
bunch_energy = beam_energy / bunches
particles_per_bunch = 2.2e+11

# ------------------------------------------------------------------------------
# Associating name with collimator ID
# ------------------------------------------------------------------------------
infile_2 = '/afs/cern.ch/work/a/ansantam/private/2016/commons/coll_summary.dat'
# infile_2 = 'coll_summary.dat'
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
infile_3 = '/afs/cern.ch/work/a/ansantam/private/2016/commons/CollPositionsHL.b1.dat'
# infile_3 = 'CollPositionsHL.b1.dat'
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


def is_header(line):
    return re.search(r'#|@|\*|%|\$|&', line) is not None


def get_impacts(infile, column):
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            if line_list[7] != 4:
                yield line_list[column]


coll_data = []
start_line = get_impacts(infile, 0)
for line in start_line:
    coll_data.append(translator_dict[numbers_dict[float(line)]])

impacts_dict = Counter(coll_data)


# ------------------------------------------------------------------------------
# Losses per turn in the tcp
# ------------------------------------------------------------------------------

turn_data = []
start_line_t = get_impacts(infile, 9)
for line in start_line_t:
    turn_data.append(line)

turns_dict = Counter(turn_data)

def get_tcp(infile, column):
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            if line_list[7] != 4:
                yield line_list[0], line_list[9]


tcp_data = []
start_line = get_tcp(infile, 0)
for line in start_line:
    tcp_data.append(line)

collsys_data = []
start_line = get_impacts(infile, 9)
for line in start_line:
    collsys_data.append(line)
    
collsystem_dict = collections.OrderedDict(sorted(Counter(collsys_data).items()))

outfile = 'collsys.txt'
print ' '
print '>> Losses in the collimation system per turn, non cumulative:'
with open(outfile, 'w') as f:
    for i, j in zip(collsystem_dict.keys(), collsystem_dict.values()):
        print i, round(float(j)*100 / simulated_particles,6), \
        '{:.2e}'.format((float(j)/ simulated_particles)*particles_per_bunch*bunches)
        print >> f, i,  round(float(j)*100 / simulated_particles,8)

tcp_losses = []
for i, j in tcp_data:
    if i == '29':
        tcp_losses.append(j)

tcp_dict = collections.OrderedDict(sorted(Counter(tcp_losses).items()))

outfile = 'tcp.txt'
print ' '
print '>> Losses in the TCP per turn, non cumulative:'
with open(outfile, 'w') as f:
    for i, j in zip(tcp_dict.keys(), tcp_dict.values()):
        print i, round(float(j)*100 / simulated_particles,2), \
        '{:.2e}'.format((float(j)/ simulated_particles)*particles_per_bunch*bunches)
        print >> f, i,  round(float(j)*100 / simulated_particles,8)

print ' '
print '>> Losses in the TCP per turn, cumulative:'
percentage_tcp = 0
protons_tcp = 0
for i, j in zip(tcp_dict.keys(), tcp_dict.values()):
    percentage_tcp += float(j)*100 / simulated_particles
    protons_tcp += float(j)/ simulated_particles*particles_per_bunch*bunches
    print i, round(percentage_tcp, 2),'{:.2e}'.format(protons_tcp), \
        round(percentage_tcp*1e-2 * beam_energy, 2)

tct_losses = []
for i, j in tcp_data:
    if i == '54':
        tct_losses.append(j)

tct_dict = collections.OrderedDict(sorted(Counter(tct_losses).items()))

print ' '
print '>> Losses in the TCT per turn, non cumulative:'
for i, j in zip(tct_dict.keys(), tct_dict.values()):
    print i, round(float(j)*100 / simulated_particles,5), \
    '{:.2e}'.format((float(j)/ simulated_particles)*particles_per_bunch*bunches)

print ' '
print '>> Losses in the TCT per turn, cumulative:'
percentage_tct = 0
protons_tct = 0
for i, j in zip(tct_dict.keys(), tct_dict.values()):
    percentage_tct += float(j)*100 / simulated_particles
    protons_tct += float(j)/ simulated_particles*particles_per_bunch*bunches
    print i, round(percentage_tct, 5),'{:.2e}'.format(protons_tct)

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
    lpi_values = np.asarray(lpi_dict.values())
    aperture_losses = sum(lpi_dict.values()) / simulated_particles
    with open(outfile_ap, 'w') as g:
        for k, l in zip(lpi_dict.keys(), lpi_dict.values()):
            print >> g, k, round(float(l)*100 / simulated_particles, 8)


outfile_coll = 'collimation.txt'
with open(outfile_coll, 'w') as f:
    for i, j in zip(impacts_dict.keys(), impacts_dict.values()):
        print i, i, round(float(j)*100 / simulated_particles, 8)
        print >> f, i, round(float(j)*100 / simulated_particles, 8)

