#!/usr/local/bin/python
import math
import os
import subprocess
import sys

rootdir = os.getcwd()

for item in os.listdir(rootdir):
   if os.path.isdir(item) == False:
        continue
   p = os.path.join(rootdir, item, 'results')
   for folder in os.listdir(p):
      if os.stat(os.path.join(rootdir, item, 'results', folder, 'impacts_real.dat')).st_size <= 64:
         print 'Missing', os.path.join(rootdir, item, 'results', folder)
      else:
         print 'NOT Missing', os.path.join(rootdir, item, 'results', folder)
         subprocess.call(['plot_loss_turn.py', '19968', '5'], cwd=os.path.join(rootdir, item, 'results', folder))