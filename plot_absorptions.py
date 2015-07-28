# ---------------------------------------------------
# Function to plot loss maps from the SixTrack output
# ---------------------------------------------------
import os

import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import rc
from matplotlib import rcParams

DPI = 300
textwidth = 7
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':15, 'weight':'bold'})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.4

def file_len(fname):
    with open(fname) as d:
        for d, l in enumerate(d):
            pass
    return d + 1

def plot_losses(collimators, aperture):

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    # fig.subplots_adjust(hspace=.7)


    (name_c, turn_c, s_c) = np.loadtxt(collimators, unpack = True)
    zip_coll_turn = zip(turn_c, s_c)

    f = open('particle_count.txt', 'a')

    if os.path.getsize(aperture) > 0:
        a = float(file_len(aperture))
        if a > 1:
            flag = True
            (name_a, turn_a, s_a, x, xp, y, yp, e, h, t) = np.loadtxt(aperture, unpack = True)
            zip_ap_turn = zip(turn_a, s_a)
        elif a == 1:
             flag = False
             print 'One particle was lost in the aperture'
             print  >> f, 'Particles lost in the aperture = 1' 
    else:
         flag = False
         print 'No particles were lost in the aperture'
         print  >> f, 'Particles lost in the aperture = 0' 


    # First Plot
    # -----------

    pairs = []
    for item in zip_coll_turn:
        pairs.append(item)

    if flag == True:
        for item in zip_ap_turn:
            pairs.append(item)

    sorted_turn = sorted(pairs, key = lambda t: t[0])
    turn = []
    for e1, e2 in sorted_turn:
        turn.append(e1)

    turn_count = Counter(turn)
    turn_values = turn_count.values()
    turn_keys = turn_count.keys()

    ax1.bar(turn_keys/960000, turn_values, log = True, width = 0.08, align = 'center')
    ax1.set_xlim([0, max(turn_keys)])
    ax1.set_xlabel( r'\textbf{Turn number}')
    ax1.grid(b=None, which='major')

    # Second Plot
    # -----------

    pairs_coll = []
    for item in zip_coll_turn:
        pairs_coll.append(item)

    sorted_s_coll = sorted(pairs_coll, key = lambda t: t[1])
    s_coll = []
    for e1, e2 in sorted_s_coll:
        s_coll.append(e2)

    s_count_coll = Counter(s_coll)
    s_values_coll = s_count_coll.values()
    s_keys_coll = s_count_coll.keys()

    ax2.bar(s_keys_coll, s_values_coll, color = 'r', label = 'Collimators', log = True, width = 20, align = 'center', edgecolor = 'r')

    if flag == True:
        pairs_ap = []
        for item in zip_ap_turn:
            pairs_ap.append(item)

        sorted_s_ap = sorted(pairs_ap, key = lambda t: t[1])
        s_ap = []
        for e1, e2 in sorted_s_ap:
            s_ap.append(e2)

        s_count_ap = Counter(s_ap)
        s_values_ap = s_count_ap.values()
        s_keys_ap = s_count_ap.keys()

        print  >> f, 'Particles lost in the aperture = %i' % len(s_a)

        f.close()

        ax2.bar(s_keys_ap, s_values_ap, color = 'g', label = 'Aperture', log = True, width = 20, align = 'center', edgecolor = 'g')

    ax2.set_xlabel( r'\textbf{s[m]}')
    ax2.set_xlim([0, 27000])
    ax2.legend(loc = 'lower left',fontsize=8 )
    fig.text(0.04, 0.5, r'\textbf{Lost particles in the simulation}', ha='center', va='center', rotation='vertical')
    ax2.annotate('IP1', xy=(1, 150), xytext=(800, 150), weight='bold', va='bottom', ha='center', size=15)
    ax2.annotate('IP2', xy=(1, 150), xytext=(3332.4, 150), weight='bold', va='bottom', ha='center', size=15)
    ax2.annotate('IR3', xy=(1, 150), xytext=(6664.721, 150), weight='bold', va='bottom', ha='center', size=15)
    ax2.annotate('IR4', xy=(1, 150), xytext=(9997, 150), weight='bold', va='bottom', ha='center', size=15)
    ax2.annotate('IP5', xy=(1, 150), xytext=(13329.28, 150), weight='bold', va='bottom', ha='center', size=15)
    ax2.annotate('IR6', xy=(1, 150), xytext=(16661.7, 150), weight='bold', va='bottom', ha='center', size=15)
    ax2.annotate('IR7', xy=(1, 150), xytext=(20000, 150), weight='bold', va='bottom', ha='center', size=15)
    ax2.annotate('IP8', xy=(1, 150), xytext=(23315.4, 150), weight='bold', va='bottom', ha='center', size=15)
    ax2.grid(b=None, which='major')

    plt.subplots_adjust(left=0.14, bottom=0.12, right=0.95, top=0.93, hspace=0.57)
    # plt.show()
    plt.savefig('losses.png', dpi=DPI)
