#!/usr/bin/env python

import numpy as np
import os
import sys

assert len(sys.argv)== 3
numCoreJobs = int(sys.argv[1])
numTailJobs = int(sys.argv[2])

f = 0.95 # relative weighting of core

def processFolder(folder,numJobs):
    impactsCount = 0
    
    impactsFile = open(os.path.join(folder, "impacts_real.dat"), 'r')
    for line in impactsFile.xreadlines():
        if line.startswith("#"):
            continue
        ls = line.split()
        if ls[7] == "4":
            continue
        
        impactsCount += 1
    impactsFile.close()

    aperLossCount = 0
    aperFile = open(os.path.join(folder, "LPI_test.s"), "r")
    for line in aperFile.xreadlines():
        aperLossCount += 1
    aperFile.close()

    fort3=open(os.path.join(folder,"fort.3"),"r")
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
    fort3.close()

    #return impactsCount, aperLossCount, fort3_pairs*fort3_packs
    return float(impactsCount+aperLossCount)/float(fort3_pairs*fort3_packs*numJobs)
    
print "Total losses = ", ( processFolder("core",numCoreJobs)*f + processFolder("tail",numTailJobs)*(1.0-f) ) * 100, "%"
