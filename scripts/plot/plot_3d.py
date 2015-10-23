#!/usr/local/bin/python
import sys
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.tri as mtri

infile = 'data.txt'

g = open(infile, 'r')
tau = []
phase = []
particles = []
for line in g.xreadlines():
    columns = line.strip('\n').split()
    if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind':
        continue
    tau.append(float(columns[0]))
    phase.append(float(columns[1]))
    particles.append((float(columns[2])/6400)*100)
g.close()


t1_p = []
t1_f = []
t2_p = []
t2_f = []
t3_p = []
t3_f = []
t4_p = []
t4_f = []
for e1, e2, e3 in zip(tau, phase, particles):
    if e1 == 1:
        t1_p.append(e3)
        t1_f.append(e2)
    if e1 == 2:
        t2_p.append(e3)
        t2_f.append(e2)
    if e1 == 3:
        t3_p.append(e3)
        t3_f.append(e2)
    if e1 == 4:
        t4_p.append(e3)
        t4_f.append(e2)
max_1 = max(t1_p)
max_2 = max(t2_p)
max_3 = max(t3_p)
max_4 = max(t4_p)

print 'Maximums'
print '----------------------'

for e1, e2 in zip(t1_p, t1_f):
    if e1==max_1:
        print 'tau 1',e2,e1
for e1, e2 in zip(t2_p, t2_f):
    if e1==max_2:
        print 'tau 2',e2,e1
for e1, e2 in zip(t3_p, t3_f):
    if e1==max_3:
        print 'tau 3',e2,e1
for e1, e2 in zip(t4_p, t4_f):
    if e1==max_4:
        print 'tau 4',e2,e1

X = np.asarray(tau)
Y = np.asarray(phase)
Z = np.asarray(particles)

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
# Plot characteristics
DPI = 300
textwidth = 6
font_spec = {"font.family": "serif", # use as default font
             "font.serif": ["New Century Schoolbook"], # custom serif font
             "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size":8,
             "font.weight":"bold",
            }
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize']=textwidth, textwidth/1.618
rcParams.update(font_spec)


triang = mtri.Triangulation(X, Y)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
# ax.plot_trisurf(triang, Z, cmap=plt.cm.CMRmap)
ax.plot_trisurf(Y, X, Z, cmap=cm.jet, linewidth=0.2)
ax.set_ylabel("Time constant of failure (turns)")
ax.set_xlabel("Phase trip (degrees)")
ax.set_zlabel("Bunch lost (\%)")
ax.set_xlim([0,360])
# plt.grid(b=None, which='major')
# plt.title('Loss Maps')
# plt.legend(loc='upper right', prop={'size':6})
# plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('phases.png', dpi=DPI)
plt.clf()
# plt.show()