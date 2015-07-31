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
textwidth = 4
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

def file_len(fname):
    with open(fname) as d:
        for d, l in enumerate(d):
            pass
    return d + 1

def plot_losses(collimators, aperture):

    fig = plt.figure()
    # ax1 = fig.add_subplot(211)
    # ax2 = fig.add_subplot(212)
    ax2 = fig.add_subplot(111)

    fig.subplots_adjust(hspace=.5)


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

    # ax1.bar(turn_keys, turn_values, log = True, width = 0.08, align = 'center')
    # ax1.set_xlim([0,51])
    # ax1.set_xlabel( r'\textbf{Turn number}')
    # ax1.grid(b=None, which='major')

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

    normalized_coll = []
    for e1, e2 in zip(s_keys_coll, s_values_coll):
        normalized_coll.append(float(e2)/3840000)
    print max(normalized_coll)

    ax2.bar(s_keys_coll, normalized_coll, color = 'r', label = 'Collimators', log = True, width = 10, align = 'center', edgecolor = 'r')
    ax2.set_xlabel( r'\textbf{s[m]}')
    ax2.set_xlim([0, 27000])
    fig.text(0.05, 0.5, r'\textbf{Fraction of the beam lost}', ha='center', va='center', rotation='vertical', size=8)
    ax2.annotate('IP1', xy=(1, 10**-4), xytext=(800, 10**-4), weight='bold', va='bottom', ha='center', size=8)
    ax2.annotate('IP2', xy=(1, 10**-4), xytext=(3332.4, 10**-4), weight='bold', va='bottom', ha='center', size=8)
    ax2.annotate('IR3', xy=(1, 10**-4), xytext=(6664.721, 10**-4), weight='bold', va='bottom', ha='center', size=8)
    ax2.annotate('IR4', xy=(1, 10**-4), xytext=(9997, 10**-4), weight='bold', va='bottom', ha='center', size=8)
    ax2.annotate('IP5', xy=(1, 10**-4), xytext=(13329.28, 10**-4), weight='bold', va='bottom', ha='center', size=8)
    ax2.annotate('IR6', xy=(1, 10**-4), xytext=(16661.7, 10**-4), weight='bold', va='bottom', ha='center', size=8)
    ax2.annotate('IR7', xy=(1, 10**-4), xytext=(20000, 10**-4), weight='bold', va='bottom', ha='center', size=8)
    ax2.annotate('IP8', xy=(1, 10**-4), xytext=(23315.4, 10**-4), weight='bold', va='bottom', ha='center', size=8)
    ax2.grid(b=None, which='major')

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

        normalized_ap = []
        for e1, e2 in zip(s_keys_ap, s_values_ap):
            normalized_ap.append(float(e2)/3840000)
        print max(normalized_ap)

        print  >> f, 'Particles lost in the aperture = %i' % len(s_a)

        f.close()

        ax2.bar(s_keys_ap, normalized_ap, color = 'g', label = 'Aperture', log = True, width = 10, align = 'center', edgecolor = 'g')
    ax2.legend(loc = 'upper left',fontsize=10 )


    # plt.show()
    plt.subplots_adjust(left=0.18, bottom=0.18, right=0.95, top=0.93)
    pp = PdfPages('losses.pdf')
    pp.savefig()
    pp.close()
    plt.savefig('losses.png')
