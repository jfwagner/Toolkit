import pylab as P
from numpy import *
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from matplotlib.backends.backend_pdf import PdfPages
from util import *

# ------------------------------------------------------------------------------
# Specify the total number of particles simulated
# ------------------------------------------------------------------------------
total_particles = 6406400
# ------------------------------------------------------------------------------
# ############################## IMPACTS REAL ##################################
# ------------------------------------------------------------------------------   
# ------------------------------------------------------------------------------
# Extract losses in the aperture
# ------------------------------------------------------------------------------
impacts_data = loadtxt("impacts_real.dat")

s = []
x = []
y= []
icoll = []
for line in impacts_data:
    s.append(line[2])
    x.append(line[3])
    y.append(line[5])
    icoll.append(line[0])

x_tct = []
y_tct = []
for e1,e2,e3 in zip(icoll, x, y):
    if e1==55:
        x_tct.append(e2)
        y_tct.append(e3)

# ------------------------------------------------------------------------------
# Plot characteristics
# ------------------------------------------------------------------------------
DPI = 300
textwidth = 6
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

# ------------------------------------------------------------------------------
# Plot the impacts on the collimator
# ------------------------------------------------------------------------------
plt.scatter(x_tct,y_tct, marker=(5,2))
plt.grid(b=None, which='major')
# plt.xlim([0, 26658.883])
# plt.ylim([0, 1])
plt.xlabel("x [mm]]")
plt.ylabel("y [mm]")
plt.title("TCTVA.5L1.B1, hits = 107093")
plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('TCTVA.5L1.B1.png', dpi=DPI)

# ------------------------------------------------------------------------------
# Halfgap (to be read from collgaps)
# ------------------------------------------------------------------------------
halfgap = 3.173017361
halfgap_minus = halfgap -1

# ------------------------------------------------------------------------------
# Impact parameter
# ------------------------------------------------------------------------------
abs_coord = []
for e1 in y_tct: #or x, depending on your collimator
        abs_coord.append(abs(e1) - halfgap)

# ------------------------------------------------------------------------------
# Plot the impact parameter
# ------------------------------------------------------------------------------        
histogram_coll(abs_coord, 700, False, 'TCTVA.5L1.B1' , halfgap, halfgap_minus, 'Impact parameter')

# ------------------------------------------------------------------------------
# Plot the histogram
# ------------------------------------------------------------------------------   
histogram_coll(y_tct, 100, True, 'TCTVA.5L1.B1', halfgap, halfgap_minus,'coordinate')

