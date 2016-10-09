#!/usr/bin/env python
import os
import re
import sys

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

turns = int(sys.argv[1])
failure_turn = int(sys.argv[2])
thetitle = sys.argv[3]
particles_bunch = 2.2e11*2748

def get_file(infile):
    if os.stat(infile).st_size == 0:
        print '>> ' + infile  + ' file is empty'
        return 0
    else:
        d = {}
        get = GetData(infile)
        data = get.data_column()
        position = data[0]
        percentage = data[1]
        for i, j in zip(position, percentage):
            d[i] = j
        return d

def get_bunch(file_core, file_tail):
    counter = 0
    if os.stat(file_core).st_size == 0 and os.stat(file_tail).st_size == 0:
        print '>> Tail and core missing'
        return 0, 0, 0
    elif os.stat(file_core).st_size == 0 and os.stat(file_tail).st_size != 0:
        print '>> Core missing'
        dict_tail = get_file(file_tail)
        for k, l in zip(dict_tail.keys(), dict_tail.values()):
            dict_tail[k] = l*0.05*particles_bunch
            counter += l*0.05
        return dict_tail.keys(), dict_tail.values(), counter
    elif os.stat(file_core).st_size != 0 and os.stat(file_tail).st_size == 0:
        print '>> Tail missing'
        dict_core = get_file(file_core)
        for k, l in zip(dict_core.keys(), dict_core.values()):
             dict_core[k] = l*0.95*particles_bunch
             counter += l*0.95
        return dict_core.keys(), dict_core.values(), counter
    else:
        dict_core = get_file(file_core)
        dict_tail = get_file(file_tail)
        for i, j in zip(dict_core.keys(), dict_core.values()):
            for k, l in zip(dict_tail.keys(), dict_tail.values()):
                if i == k:
                    dict_core[i] = (j*0.95 + l*0.05)*particles_bunch
                    counter +=  j*0.95 + l*0.05
                    print i, j, l, j*0.95 + l*0.05
                    print counter
        return dict_core.keys(), dict_core.values(), counter


x_ap, y_ap, tot_ap = get_bunch('ap_core.txt', 'ap_tail.txt')
x_coll, y_coll, tot_coll = get_bunch('coll_core.txt', 'coll_tail.txt')

# print max(y_coll)
# print tot_coll

def extract(infile, col_1, col_2):
    if os.stat(infile).st_size == 0:
        print '>> ' + infile  + ' file is empty'
        return 0, 0
    else:
        get = GetData(infile)
        data = get.data_column()
        turn = data[col_1]
        value = data[col_2]
        return turn, value


turn_core, tcp_core = extract('tcp_core.txt', 0, 1)
turn_tail, tcp_tail = extract('tcp_tail.txt', 0, 1)

turn_core_coll, coll_core = extract('collsys_core.txt', 0, 1)
turn_tail_coll, coll_tail = extract('collsys_tail.txt', 0, 1)


def get_loss_turn(turn, tcp):
    if tcp == 0:
        losses = []
        turn_ll = []
        for t in range(1, turns + 1):
             turn_ll.append(float(t))
             losses.append(0)
    else:
        losses_raw = sorted(zip(turn, tcp), key= lambda x:x[0])
        losses = []
        turn_ll = []
        loss = 0
        for t in range(1, turns + 1):
            count = 0
            for i, j in losses_raw:
                if i == t:
                    loss += j
                    turn_ll.append(i)
                    losses.append(loss)
                else:
                    count += 1
                if count == len(losses_raw):
                   turn_ll.append(float(t))
                   losses.append(loss)
    return turn_ll, losses

t_core, l_core = get_loss_turn(turn_core, tcp_core)
t_tail, l_tail = get_loss_turn(turn_tail, tcp_tail)


l = []
for i, j in zip(l_core, l_tail):
    l.append(i*0.95 + j*0.05)

t_core_coll, l_core_coll = get_loss_turn(turn_core_coll, coll_core)
t_tail_coll, l_tail_coll = get_loss_turn(turn_tail_coll, coll_tail)

ll = []
for i, j in zip(l_core_coll, l_tail_coll):
    ll.append(i*0.95 + j*0.05)

# ------------------------------------------------------------------------------
# Plotting
# ------------------------------------------------------------------------------
def give_tot(percentage):
    if percentage == 0:
        return str(0)
    elif percentage < 0.0999:
        return '{:.2e}'.format(percentage)
    elif percentage > 0.0999:
        return str(round(percentage, 2))

if tot_coll != ll[turns-1]:
    print '>> Problem: Total percentages do not match'
    
tot_collsys = give_tot(ll[turns-1])
tot_aperture = give_tot(tot_ap)
tot_tcp = give_tot(l[turns-1])



font_spec = {"font.size": 10, }
rcParams.update(font_spec)
rcParams['legend.frameon'] = 'True'
rcParams['figure.figsize'] = 4, 2
fig = plt.figure()
ax2 = fig.add_subplot(111)
plt.bar(x_coll, y_coll, align="center",
        linewidth=0, width=60, color="black", label="Collimation: " + tot_collsys +'%')
plt.bar(x_ap, y_ap, color="green",
            align="center", linewidth=0, width=60, label="Aperture: " + tot_aperture +'%')
# plt.title("Losses from a single bunch, HL-LHC 1.2")
plt.title(thetitle)
plt.xlabel("Position (m)")
plt.ylabel("Number of Protons Lost")
plt.xlim([0, 26658.883])
plt.legend(loc='upper left', prop={'size': 6})
ax2.set_yscale('log')
ax2.set_axisbelow(True)
ax2.yaxis.grid(color='gray', linestyle='-', which="minor", linewidth=0.3)

height = max(y_coll) / 1000
text_size = 10
ax2.annotate('IP2', xy=(1, height), xytext=(3332.4, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax2.annotate('IR3', xy=(1, height), xytext=(6664.721, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax2.annotate('IR4', xy=(1, height), xytext=(9997, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax2.annotate('IP5', xy=(1, height), xytext=(13329.28, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax2.annotate('IR6', xy=(1, height), xytext=(16661.7, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax2.annotate('IR7', xy=(1, height), xytext=(20000, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')
ax2.annotate('IP8', xy=(1, height), xytext=(23315.4, height),
             weight='bold', va='bottom', ha='center', size=text_size, color='red')

plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('loss_map.png', dpi=1000)
plt.savefig('loss_map.eps', format='eps', dpi=1000)
plt.clf()


plt.bar(t_core_coll, ll, align='center', color='blue', label='Collimation System: ' + tot_collsys + '%', linewidth=0.5)
plt.bar(t_core, l, align='center', color='red', label='Primary Collimator: ' + tot_tcp + '%', linewidth=0.5)
plt.xlabel('Turns')
plt.ylabel(r'Percentage of Beam Lost (%)')
plt.title(thetitle)
plt.xlim([0, turns])
plt.axvline(x=failure_turn, linewidth=0.7, color='black')
plt.annotate('Failure', xy=(failure_turn - 1.5,  (max(ll) + max(ll)* 0.7) / 2), rotation='vertical', size='6', verticalalignment='center')
if ll[turns-1] < 0.0999:
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.legend(loc='upper left', prop={'size': 6})
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('tcp.png', dpi=1000)
plt.savefig('tcp.eps', format='eps', dpi=1000)
plt.clf()

plt.plot(t_core_coll, ll, '-o',color='blue', label='Collimation System: ' + tot_collsys + '%', linewidth=0.5)
plt.plot(t_core, l, '-o',color='red', label='Primary Collimator: ' + tot_tcp + '%', linewidth=0.5)
plt.xlabel('Turns')
plt.ylabel(r'Percentage of Beam Lost (%)')
plt.title(thetitle)
plt.xlim([0, turns])
plt.axvline(x=failure_turn, linewidth=0.7, color='black')
plt.annotate('Failure', xy=(failure_turn - 1.5,  (max(ll) + max(ll)* 0.7) / 2), rotation='vertical', size='6', verticalalignment='center')
if ll[turns-1] < 0.0999:
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.legend(loc='upper left', prop={'size': 6})
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('tcp_scatter.png', dpi=1000)
plt.savefig('tcp_scatter.eps', format='eps', dpi=1000)
plt.clf()

