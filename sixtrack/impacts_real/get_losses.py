#!/usr/bin/env python
# ------------------------------------------------------------------------------
# Script to extract data from impacts_real.
# The files "impacts_real.dat", "coll_summary.dat" and "CollPositionsHL.b1.dat"
# must be in the folder where you execute the script.
# Header of "impacts_real.dat":
# 1=icoll 2=c_rotation 3=s 4=x 5=xp 6=y 7=yp 8=nabs 9=np 10=ntu
# ------------------------------------------------------------------------------
# USAGE: get_losses.py 100 200 B2
# -----------------------------------------------------------------------------
import os
import re
import sys
from collections import Counter

import numpy as np

from util import GetData

if len(sys.argv) != 4 and len(sys.argv) != 5:
    print "Usage: get_losses.py jobs turns(0=auto) {B1|B2} (failTurn)"
    print "jobs is the number of job folders, used for normalization with total number of particles simulated."
    print "turns is the number of turns the tracking has been ran for"
    print "failTurn is the last good turn before the failure, which by definition has 0 losses."
    print "Got: ", sys.argv
    exit(1)
    
# ------------------------------------------------------------------------------
# Specify how many runs of 19968 particles (current limit in SixTrack) are
# contained in your "impacts_real.dat" (>1 if concatenated file)
# ------------------------------------------------------------------------------
fort3 = open("fort.3",'r')
fort3_currBlock = None
fort3_blockLine = None
for line in fort3.xreadlines():
    if line.startswith("TRACKING"):
        assert fort3_currBlock==None
        fort3_currBlock="TRACK"
        continue
    elif line.startswith("COLLIMATION"):
        assert fort3_currBlock==None
        fort3_currBlock="COLL"
        fort3_blockLine=0
        continue

    if fort3_currBlock=="TRACK":
        ls = line.split()
        fort3_turns = int(ls[0])
        fort3_pairs = int(ls[2])*2
        fort3_currBlock = None #Done parsing TRACK block
    elif fort3_currBlock=="COLL":
        fort3_blockLine += 1
        if fort3_blockLine == 2:
            ls = line.split()
            fort3_packs=int(ls[0])
            fort3_currBlock = None #Done parsing COLL block
            
jobs_str = sys.argv[1]
turns = int(sys.argv[2])
if turns==0:
    turns = fort3_turns
    sixtrack_particle_limit = fort3_packs*fort3_pairs
    print "AutoSetup from fort.3..."
    print "fort3_packs=",fort3_packs
    print "fort3_pairs=",fort3_pairs
else:
    sixtrack_particle_limit = 19968
print "turns=", turns
print "sixtrack_particle_limit=",sixtrack_particle_limit

simulated_particles = int(jobs_str) * sixtrack_particle_limit
beam = sys.argv[3]
if len(sys.argv) == 5:
    failTurn = int(sys.argv[4])
    if failTurn < 0 or failTurn > turns:
        print ">> failTurn must be >=0 and < turns"
        exit(1)
else:
    failTurn = 0

print ' '
print 'Number of simulated particles: ', simulated_particles, '(100 %)'

# ------------------------------------------------------------------------------
# Associating name with collimator ID
# ------------------------------------------------------------------------------
infile_collsum = 'coll_summary.dat'
get_collsum = GetData(infile_collsum)
#get_collsum = GetData(infile_collsum)
data_collsum = get_collsum.data_column(dtype='string')

names_collsum = data_collsum[1]
numbers_collsum = data_collsum[0]
length_collsum = map(float,data_collsum[6])

numbers_dict = {} # Collimator name from ID
names_dict = {}   # Collimator ID from name
length_dict = {}  # Collimator length from ID
for i in range(len(names_collsum)):
    numbers_dict[int(numbers_collsum[i])] = names_collsum[i]
    names_dict[names_collsum[i]] = int(numbers_collsum[i])
    length_dict[int(numbers_collsum[i])] = length_collsum[i]
    
    

# ------------------------------------------------------------------------------
# Associating name with position
# ------------------------------------------------------------------------------
if beam == 'B1':
    infile_3 = 'CollPositionsHL.b1.dat'
elif beam == 'B2':
    infile_3 = 'CollPositions.b2.dat'
else:
    print "beam must be B1 or B2, got", beam
    exit(1)

get_3 = GetData(infile_3)
data_3 = get_3.data_column(dtype='string')

names = data_3[1]
position = data_3[2]

translator_dict = {} # Position from collimator name
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


num_lines = sum(1 for line in open('impacts_real.dat'))

print 'Number of recorded impacts: ', float(num_lines) - float(jobs_str),  '(' + str(round((float(num_lines - int(jobs_str)) / simulated_particles) * 100, rounding)) + ' %)'

print
print ">> Finding the baseLosses, failTurn =",failTurn
#Finding the baseLoss
if failTurn !=0:
    baseLossAperture = 0
    totalLossAperture = 0
    
    apFile = open("LPI_test.s",'r')
    for line in apFile.xreadlines():
        if is_header(line):
            continue
        ls = line.strip('\n').split()
        totalLossAperture +=1
        if int(ls[1]) <= failTurn:
            baseLossAperture += 1
    apFile.close()

    baseLossAllColl = 0
    totalLossAllColl = 0
    baseLossPerColl = {}
    collFile = open("impacts_real.dat",'r')
    for line in collFile.xreadlines():
        if is_header(line):
            continue
        ls = line.strip('\n').split()
        if int(ls[7]) == 4: # Skip scatterings
            continue
        totalLossAllColl +=1
        name = numbers_dict[int(ls[0])]
        if not name in baseLossPerColl.keys():
            baseLossPerColl[name] = 0
        if int(ls[9]) <= failTurn:
            baseLossAllColl += 1
            baseLossPerColl[name] +=1
    collFile.close()
else:
    baseLossAperture = 0
    totalLossAperture = 0

    baseLossAllColl = 0
    totalLossAllColl = 0

    baseLossPerColl = {}

print "baseLossAllColl =",baseLossAllColl,"/",totalLossAllColl, "/", simulated_particles
print "baseLossAperture =",baseLossAperture,"/",totalLossAperture, "/", simulated_particles
simulated_particles_afterFail = simulated_particles - baseLossAllColl - baseLossAperture
print "simulated_particles_afterFail =",simulated_particles_afterFail

normFile = open("normalization.txt",'w')
normFile.write("beam="+beam+"\n")
normFile.write("sixtrack_particle_limit="+str(sixtrack_particle_limit)+"\n")
normFile.write("jobs="+jobs_str+"\n")
normFile.write("simulated_particles="+str(simulated_particles)+"\n")
normFile.write("failTurn="+str(failTurn)+"\n")
normFile.write("baseLossAllColl="+str(baseLossAllColl)+"\n")
normFile.write("baseLossAperture="+str(baseLossAperture)+"\n")
normFile.write("simulated_particles_afterFail="+str(simulated_particles_afterFail)+"\n")
normFile.close()

def get_impacts(infile, column, skipPreFail=False):
    elas = 0
    inelas = 0
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            if skipPreFail==True and int(line_list[9])<=failTurn:
                continue
            if line_list[7] != '4':
                inelas += 1
                yield line_list[column]
            else:
                elas += 1
    print ' '
    print "skipPreFail:",skipPreFail
    print 'Total number of scattered protons: ', elas, '(' + str(round((float(elas) / simulated_particles) * 100, rounding)) + ' %)'
    print 'Total number of absorbed protons: ', inelas, '(' + str(round((float(inelas) / simulated_particles) * 100, rounding)) + ' %)'

    
if num_lines - int(jobs_str) != 0.0:
    
    # ------------------------------------------------------------------------------
    # Impacts per collimator
    # ------------------------------------------------------------------------------
    coll_data = []
    start_line = get_impacts(infile, 0,True)
    for line in start_line:
        coll_data.append(numbers_dict[int(line)])

    coll_data_all = []
    start_line = get_impacts(infile, 0, False)
    for line in start_line:
        coll_data_all.append(numbers_dict[int(line)])
        
    coll_dict = Counter(coll_data)
    print ' '

    if len(coll_dict) != 0:
        coll_out = 'loss_maps.txt'
        with open(coll_out, 'w') as g:
            print >> g, '# Name Position Absorptions Percentage Fraction/meter Length[meter]'
            for i, j in zip(coll_dict.keys(), coll_dict.values()):
                print 'Absorptions in collimator ' + str(i) + ': ', j,  '(' + str(round((float(j) / simulated_particles_afterFail) * 100, rounding)) + ' %)'
                print >> g, i, translator_dict[str(i)], j, (float(j) / simulated_particles_afterFail) * 100, float(j) / simulated_particles_afterFail / length_dict[names_dict[i]], length_dict[names_dict[i]]


    # ------------------------------------------------------------------------------
    # Losses per turn
    # ------------------------------------------------------------------------------
    turn_data = []
    start_line_t = get_impacts(infile, 9,False)
    for line in start_line_t:
        turn_data.append(line)
    turns_dict = Counter(turn_data)
    turns_out = 'data_turn.txt'
    tt = []
    vv = []
    with open(turns_out, 'w') as h:
        print >> h, '# Position Absorptions Percentage'
        for t in range(1, turns + 2):
            try:
                turns_dict[str(t)]
                tt.append(t)
                vv.append(turns_dict[str(t)])
            except KeyError:
                tt.append(t)
                vv.append(0)
        assert len(tt)==len(vv)
        cumLoss =  np.cumsum(vv[:0] + vv[:-1])
        if failTurn != 0:
            #baseLossAllColl = cumLoss[failTurn-1]
            cumLoss -= baseLossAllColl
        else:
            baseLossAllColl = 0
        
        for i, j in zip(tt, cumLoss):
            print >> h, i, j, (float(j) / simulated_particles_afterFail) * 100
        print 'File', turns_out, 'created; baseLossAllColl=',baseLossAllColl, "endLoss=",cumLoss[-1]
    # -----------------------------------------------------------------------------
    # Creating a dict of dicts in order to access the losses per turn for each
    # collimator. Dict contains name of coll, turn number and losses in that turn.
    # -----------------------------------------------------------------------------
    d = {}
    assert len(coll_data_all) == len(turn_data)
    for name in translator_dict.keys():        
       coll_name = []
       for i, j in zip(coll_data_all, turn_data):
           if i == name:
               coll_name.append(j)
       if len(coll_name) > 0:
           c = Counter(coll_name)
           d[name] = dict(c)

    print ' '
    print '>> Getting losses per turn for each collimator:'


    def get_coll(name):
        turn = []
        value = []
        try:
            d[name]
            outfile = name.translate(None, '.').lower() + '.txt'
            with open(outfile, 'w') as g:
                print >> g, '# Position Absorptions Percentage Fraction/meter'
                for t in range(1, turns + 2):
                    try:
                        d[name][str(t)]
                        turn.append(t)
                        value.append(d[name][str(t)])
                    except KeyError:
                        turn.append(t)
                        value.append(0)
                assert len(turn) == len(value)
                cumLoss =  np.cumsum(value[:0] + value[:-1])
                if failTurn != 0:
                    baseLossColl = cumLoss[failTurn-1]
                    cumLoss -= baseLossColl
                    if not baseLossColl == baseLossPerColl[name]:
                        print "WARNING!!!", baseLossColl, baseLossPerColl[name], name
                        print "probably a bug..."
                else:
                    baseLossColl = 0
                
                for i, j in zip(turn, cumLoss):
                    print >> g, i, j, (float(j) / simulated_particles_afterFail) * 100, float(j) / simulated_particles_afterFail / length_dict[names_dict[name]]
                print 'File', outfile, 'created; baseLossColl=',baseLossColl, "endLoss=",cumLoss[-1]
        except KeyError:
            print '(Collimator', name,  'not found or without losses)'

    for col in translator_dict.keys():
        get_coll(col)

else:
    print ' '
    print '>> No losses in the collimation system'


# ------------------------------------------------------------------------------
# Extracting losses in the aperture
# ------------------------------------------------------------------------------


def get_lpi(infile,skipPreFail=False):
    with open(infile, 'r') as data:
        for line in data:
            if is_header(line):
                continue
            line_list = line.strip('\n').split()
            if skipPreFail and int(line_list[1]) <= failTurn:
                continue
            yield line_list[2]

print ' '
infile_4 = 'LPI_test.s'
outfile_ap = 'aperture.txt'
if os.stat(infile_4).st_size == 0:
    print '>> No losses in the aperture'
else:
    ap_data = []
    start_line = get_lpi(infile_4,True)
    for line in start_line:
        ap_data.append(float(line))
    lpi_dict = Counter(ap_data)
    with open(outfile_ap, 'w') as g:
        print >> g, '# Position Absorptions Percentage Fraction/meter'
        for i, j in zip(lpi_dict.keys(), lpi_dict.values()):
            print >> g, i, j, (float(j) / simulated_particles_afterFail) * 100, float(j)/simulated_particles_afterFail/10e-2

    num_lines_ap = sum(1 for line in open('LPI_test.s'))
    print '>> Number of losses in the aperture: ', num_lines_ap,  '(' + str(round((float(num_lines_ap - 1) / simulated_particles_afterFail) * 100, rounding)) + ' %) baseloss=',baseLossAperture

### Aperture losses as function of turn
turns_ap_out = 'data_turn_aperture.txt'
turns_ap_losses = np.zeros(turns+1)
turns_ap_inf = open(infile_4,'r')
for line in turns_ap_inf.xreadlines():
    if is_header(line):
        continue
    ls = line.strip('\n').split()
    turns_ap_losses[int(ls[1])]+=1
turns_ap_inf.close()

turns_ap_outf = open(turns_ap_out,'w')
turns_ap_outf.write('# Position Absorptions Percentage\n')
lossSum = 0
for t in xrange(1,turns+1):
    lossSum += turns_ap_losses[t]
    turns_ap_outf.write("%i %i %f\n" %(t,lossSum, (float(lossSum)/simulated_particles_afterFail) * 100 ) )
turns_ap_outf.close()
