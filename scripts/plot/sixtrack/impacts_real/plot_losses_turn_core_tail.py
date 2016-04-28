import numpy as np
import matplotlib.mlab as mlab
import pylab as P
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

# ------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------


def get_losses(infile, particles, factor):
    get = GetData(infile)
    data = get.data_column(column=7, regex=r'1\b')
    losses = dict(Counter(data[9]))  # Gives {turns : number of particles}
    # x = losses.keys()  # Gives [turns]
    x = losses.keys()
    y = losses.values()
    xt = []
    yt = []
    sel_turns = []
    for turn in range(1, 21):
        xt.append(turn)
        if turn not in x:
            yt.append(0.0)
        elif turn in x:
            for e1, e2 in zip(x, y):
                if e1 == turn:
                    yt.append(e2 * factor)

    y_norm = []
    for i in yt:
        y_norm.append(float(i) / (particles * 1e-2))
    xf = []
    yf = []
    count = 0
    for i, j in sorted(zip(xt, y_norm)):
        count = count + j
        yf.append(float(count))
        xf.append(i)
    return xf, yf


def get_full_turns(x, y, factor):
    xt = []
    yt = []
    sel_turns = []
    for turn in range(1, 21):
        xt.append(turn)
        if turn not in x:
            yt.append(0.0)
        elif turn in x:
            for e1, e2 in zip(x, y):
                if e1 == turn:
                    yt.append(e2 * factor)
    return xt, yt


def get_total_bunch(xc, yc, xt, yt):
    x = []
    y = []
    for e1, e2, e3, e4 in zip(xc, yc, xt, yt):
        if e1 == e3:
            x.append(e1)
            y.append(e2 + e4)
    return x, y


def remove_cleaning(x, y, failure):
    xt = []
    yt = []
    cleaning = y[failure - 1]
    for e1, e2 in zip(x, y):
        xt.append(e1)
        yt.append(e2 - cleaning)
    return xt, yt


def get_all(infile_core, particles_core, infile_tail, particles_tail):
    x_1cc, y_1cc = get_losses(infile_core, particles_core, 0.95)
    x_1ct, y_1ct = get_losses(infile_tail, particles_tail, 0.05)
    # xf_1cc, yf_1cc = get_full_turns(x_1cc, y_1cc, 0.95)
    # xf_1ct, yf_1ct = get_full_turns(x_1ct, y_1ct, 0.05)
    x1c, y1c = get_total_bunch(x_1cc, y_1cc, x_1ct, y_1ct)
    x, y = remove_cleaning(x1c, y1c, 5)
    return np.asarray(x), np.asarray(y)


def get_delta(x, y, bunches):
    xt = []
    yt = []
    for e1, e2 in zip(x, y):
        if e1 >= 5:
            xt.append(e1 - 5)
            yt.append(e2)

    previous = None
    nextt = None
    for index, obj in enumerate(yt):
        # TODO Bounds-checking
        previous = yt[index]
        nextt = yt[index + 1]
        # print previous,'    ' ,nextt,'    ' ,abs(nextt - previous)
        print index + 1, '    ', '%.8E' % ((abs(nextt - previous)) * 1e-2 * 2.2 * 1e11 * bunches)
        # try:
        #     raise Exception('mm')
        # except IndexError:
        #     print 'Index error'
        #     continue

# ------------------------------------------------------------------------------
# DATA EXTRACTION & TREATMENT
# ------------------------------------------------------------------------------
x1c, y1c = get_all('1C_core.dat', 9984000, '1C_tail.dat', 9984000)
x2c, y2c = get_all('2C_core.dat', 9984000, '2C_tail.dat', 9964032)
x4c, y4c = get_all('4C_core.dat', 9984000, '4C_tail.dat', 9984000)
# x1d, y1d = get_all('1D_core.dat', 9964032,'1D_tail.dat', 9964032)
x2d, y2d = get_all('2D_core.dat', 9964032, '2D_tail.dat', 9964032)
x3c, y3c = get_all('3C_core.dat', 9984000, '3C_tail.dat', 9984000)
x3d, y3d = get_all('3D_core.dat', 9984000, '3D_tail.dat', 9984000)
x4d, y4d = get_all('4D_core.dat', 9984000, '4D_tail.dat', 9984000)
x1d = np.linspace(1, 20, 20)
y1d = np.zeros(20)

a = x2d
b = y2d
# x,y=get_losses('2C_core.dat',  9984000, 0.95)
# xt,yt=get_full_turns(x,y, 0.95)


# get_delta(a, b, 2748)
# for e1, e2 in zip(a, b):
#     print e1-5, e2

# get_delta(a, b, 1374)

# ------------------------------------------------------------------------------
# PLOTTING
# ------------------------------------------------------------------------------
DPI = 500
textwidth = 3.25
font_spec = {"font.family": "serif",  # use as default font
             # "font.serif": ["New Century Schoolbook"], # custom serif font
             # "font.sans-serif": ["helvetica"], # custom sans-serif font
             "font.size": 8,
             "font.weight": "bold",
             }
rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
rcParams['figure.figsize'] = textwidth, textwidth / 1.2
rcParams.update(font_spec)

fig = plt.figure()
# ------------------------------------------------------------------------------
ax1 = fig.add_subplot(221)
plt.plot(x1c - 5, y1c, '-o', linewidth=0.5,
         markersize=3, label='Case 1C', color='#002db3')
plt.plot(x1d - 5, y1d, '-o', linewidth=0.5,
         markersize=3, label='Case 1D', color='#32bbcd')
ax1.set_xlim([0, 10])
ax1.set_ylim([-0.001, 0.030])
ax1.legend(loc='upper left', prop={'size': 5})
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
# ------------------------------------------------------------------------------
ax2 = fig.add_subplot(222)
plt.plot(x2c - 5, y2c, '-o', linewidth=0.5,
         markersize=3, label='Case 2C', color='#456300')
plt.plot(x2d - 5, y2d, '-o', linewidth=0.5,
         markersize=3, label='Case 2D', color='#9ccd32')
ax2.legend(loc='upper left', prop={'size': 5})
ax2.set_ylim([-0.01, 0.25])
plt.setp(ax2.get_xticklabels(), visible=False)
ax2.set_xlim([0, 10])
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
# ------------------------------------------------------------------------------
ax3 = fig.add_subplot(223)
# plt.scatter(5, 0.1521, marker=(5,1), color='yellow', linewidth=0.5, edgecolor='black')
plt.axvline(x=5, linewidth=0.7, color='black')
ax3.annotate('Beam dump', xy=(4.4, 0.7), xytext=(4.4, 0.7),
             rotation='vertical', size='4', verticalalignment='center')
plt.plot(x3c - 5, y3c, '-o', linewidth=0.5,
         markersize=3, label='Case 3C', color='#694100')
plt.plot(x3d - 5, y3d, '-o', linewidth=0.5,
         markersize=3, label='Case 3D', color='#e19100')
plt.plot(5, 0.1521, 'y*', label='Damage limit')
ax3.set_ylim([-0.1, 2.5])
ax3.legend(loc='upper left', prop={'size': 5})
ax3.set_xlim([0, 10])
# ------------------------------------------------------------------------------
ax4 = fig.add_subplot(224)
# plt.scatter(5, 0.1521, marker=(5,1), color='yellow', linewidth=0.5, edgecolor='black')
plt.axvline(x=5, linewidth=0.7, color='black')
ax4.annotate('Beam dump', xy=(4.4, 7), xytext=(4.4, 7),
             rotation='vertical', size='4', verticalalignment='center')
plt.plot(x4c - 5, y4c, '-o', linewidth=0.5,
         markersize=3, label='Case 4C', color='#500914')
plt.plot(x4d - 5, y4d, '-o', linewidth=0.5,
         markersize=3, label='Case 4D', color='#ea1640')
plt.plot(5, 0.1521, 'y*')
ax4.legend(loc='upper left', prop={'size': 5})
ax4.set_ylim([-1, 25])
ax4.set_xlim([0, 10])
# ------------------------------------------------------------------------------
fig.text(0.5, 0.04, 'Turns after the failure', ha='center', va='center')
fig.text(0.06, 0.5,
         'Fraction of bunch lost\nin the collimators [\%]', ha='center', va='center', rotation='vertical')
# ------------------------------------------------------------------------------
plt.tight_layout()
plt.subplots_adjust(left=0.18, bottom=0.14, right=0.95, top=0.91, hspace=0.16)
plt.savefig('losses.png', dpi=DPI)
plt.clf()
# plt.show()
