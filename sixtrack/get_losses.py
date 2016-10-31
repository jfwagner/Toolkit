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

import collections
import numpy as np

from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

# ------------------------------------------------------------------------------
# Specify how many runs of 19968 particles (current limit in SixTrack) are
# contained in your "impacts_real.dat" (>1 if concatenated file)
# ------------------------------------------------------------------------------
simulated_particles = float(sys.argv[1])*19968

print ' '
print 'Number of simulated particles: ', int(simulated_particles), '(100 %)'

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
    elas   = 0
    inelas = 0
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            if line_list[7] != '4':
                inelas +=1
                yield line_list[column]
            else:
                elas +=1
    print 'Number of scattered protons: ', elas, '(' + str(round((float(elas)/simulated_particles)*100, rounding)) + ' %)'
    print 'Number of absorbed protons: ', inelas, '(' + str(round((float(inelas)/simulated_particles)*100, rounding)) + ' %)'


num_lines = sum(1 for line in open('impacts_real.dat'))
print 'Number of recorded impacts: ', num_lines - 1,  '(' + str(round((float(num_lines - 1)/simulated_particles)*100, rounding)) + ' %)'


# ------------------------------------------------------------------------------
# Impacts per collimator
# ------------------------------------------------------------------------------
coll_data = []
start_line = get_impacts(infile, 0)
for line in start_line:
    coll_data.append(numbers_dict[float(line)])

coll_dict = Counter(coll_data)
print ' '
coll_out = 'data_coll.txt'
with open(coll_out, 'w') as g:
    print >> g, '# Name Position Absorptions Percentage'
    for i, j in zip(coll_dict.keys(), coll_dict.values()):
         print 'Absorptions in collimator ' + str(i) + ': ', j,  '(' + str(round((float(j)/simulated_particles)*100, rounding)) + ' %)'
         print >> g, i, translator_dict[str(i)], j, (float(j)/simulated_particles)*100


# ------------------------------------------------------------------------------
# Losses per turn
# ------------------------------------------------------------------------------
turn_data = []
start_line_t = get_impacts(infile, 9)
for line in start_line_t:
    turn_data.append(line)

turns_dict = Counter(turn_data)
turns_out = 'data_turn.txt'
with open(turns_out, 'w') as h:
    for i, j in zip(turns_dict.keys(), turns_dict.values()):
         print >> h, i, j, (float(j)/simulated_particles)*100

for name in translator_dict.keys():
    coll_name = []
    for i, j in zip(coll_data, turn_data):
        if i == name:
            coll_name.append(j)
    if len(coll_name) > 0:
        print name, Counter(coll_name)



# a = sorted(a, key=lambda x: x.modified, reverse=True)

# def get_tcp(infile, column):
#     with open(infile, 'r') as data:
#         for line in data:
#             if is_header(line):
#                 continue
#             line_list = line.strip('\n').split()
#             if line_list[7] != 4:
#                 yield line_list[0], line_list[9]


# tcp_data = []
# start_line = get_tcp(infile, 0)
# for line in start_line:
#     tcp_data.append(line)

# collsys_data = []
# start_line = get_impacts(infile, 9)
# for line in start_line:
#     collsys_data.append(line)
    
# collsystem_dict = collections.OrderedDict(sorted(Counter(collsys_data).items()))

# outfile = 'collsys.txt'
# print ' '
# print '>> Losses in the collimation system per turn, non cumulative:'
# with open(outfile, 'w') as f:
#     for i, j in zip(collsystem_dict.keys(), collsystem_dict.values()):
#         print i, round(float(j)*100 / simulated_particles,6), \
#         '{:.2e}'.format((float(j)/ simulated_particles)*particles_per_bunch*bunches)
#         print >> f, i,  round(float(j)*100 / simulated_particles,8)

# tcp_losses = []
# for i, j in tcp_data:
#     if i == '29':
#         tcp_losses.append(j)

# tcp_dict = collections.OrderedDict(sorted(Counter(tcp_losses).items()))

# outfile = 'tcp.txt'
# print ' '
# print '>> Losses in the TCP per turn, non cumulative:'
# with open(outfile, 'w') as f:
#     for i, j in zip(tcp_dict.keys(), tcp_dict.values()):
#         print i, round(float(j)*100 / simulated_particles,2), \
#         '{:.2e}'.format((float(j)/ simulated_particles)*particles_per_bunch*bunches)
#         print >> f, i,  round(float(j)*100 / simulated_particles,8)

# print ' '
# print '>> Losses in the TCP per turn, cumulative:'
# percentage_tcp = 0
# protons_tcp = 0
# for i, j in zip(tcp_dict.keys(), tcp_dict.values()):
#     percentage_tcp += float(j)*100 / simulated_particles
#     protons_tcp += float(j)/ simulated_particles*particles_per_bunch*bunches
#     print i, round(percentage_tcp, 2),'{:.2e}'.format(protons_tcp), \
#         round(percentage_tcp*1e-2 * beam_energy, 2)

# tct_losses = []
# for i, j in tcp_data:
#     if i == '54':
#         tct_losses.append(j)

# tct_dict = collections.OrderedDict(sorted(Counter(tct_losses).items()))

# print ' '
# print '>> Losses in the TCT per turn, non cumulative:'
# for i, j in zip(tct_dict.keys(), tct_dict.values()):
#     print i, round(float(j)*100 / simulated_particles,5), \
#     '{:.2e}'.format((float(j)/ simulated_particles)*particles_per_bunch*bunches)

# print ' '
# print '>> Losses in the TCT per turn, cumulative:'
# percentage_tct = 0
# protons_tct = 0
# for i, j in zip(tct_dict.keys(), tct_dict.values()):
#     percentage_tct += float(j)*100 / simulated_particles
#     protons_tct += float(j)/ simulated_particles*particles_per_bunch*bunches
#     print i, round(percentage_tct, 5),'{:.2e}'.format(protons_tct)

# # ------------------------------------------------------------------------------
# # Extracting losses in the aperture
# # ------------------------------------------------------------------------------


# def get_lpi(infile):
#     with open(infile, 'r') as data:
#         for line in data:
#             if is_header(line):
#                 continue
#             line_list = line.strip('\n').split()
#             yield line_list[2]


# infile_4 = 'LPI_test.s'
# outfile_ap = 'aperture.txt'
# if os.stat(infile_4).st_size == 0:
#     open(outfile_ap, 'a').close()
#     print '>> No losses in the aperture'
# else:
#     ap_data = []
#     start_line = get_lpi(infile_4)
#     for line in start_line:
#         ap_data.append(float(line))
#     lpi_dict = Counter(ap_data)
#     lpi_values = np.asarray(lpi_dict.values())
#     aperture_losses = sum(lpi_dict.values()) / simulated_particles
#     with open(outfile_ap, 'w') as g:
#         for k, l in zip(lpi_dict.keys(), lpi_dict.values()):
#             print >> g, k, round(float(l)*100 / simulated_particles, 8)


# outfile_coll = 'collimation.txt'
# with open(outfile_coll, 'w') as f:
#     for i, j in zip(impacts_dict.keys(), impacts_dict.values()):
#         print i, i, round(float(j)*100 / simulated_particles, 8)
#         print >> f, i, round(float(j)*100 / simulated_particles, 8)

