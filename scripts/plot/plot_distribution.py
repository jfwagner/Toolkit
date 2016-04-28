#!/usr/bin/env python

import sys
from collections import defaultdict
from datetime import datetime

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import get_ellipse_coords

start_time = datetime.now()

# Feed the input to the script by command line
infile = sys.argv[1]
coord_hor = sys.argv[2]
coord_ver = sys.argv[3]
turn_first = int(sys.argv[4])
turn_last = int(sys.argv[5])
turns = range(turn_first, turn_last + 1)
nbins = int(sys.argv[6])

print '>> Plotting distribution', coord_hor, ',', coord_ver

# Create a series of dictionaries to associate information to each input coord.
coords = ['x', 'xp', 'y', 'yp', 'z', 'e']

col_number = [3, 4, 5, 6, 7, 8]
d_1 = {k: v for k, v in zip(coords, col_number)}  # dict comprehension

# limits = [[-9e-4, -6e-4], [-7e-4, 7e-4], [-8e-5, 8e-5], [-0.5e-3, 0], [-0.02, 0.02], [-2e-4, 2e-4]] # Pencil
# limits = [[-1e-4, 1e-4], [1e-4, 5e-4], [7e-4, 8e-4], [-2e-4, 2e-4],
# [-0.4, 0.4], [-5e-4, 5e-4]] # Optics 1.2, IP5
limits = [[-7.9e-4, -7.1e-4], [-3e-4, 3e-4], [-8e-5, 8e-5],
          [1e-4, 5e-4], [-0.4, 0.4], [-5e-4, 5e-4]]  # Optics 1.2, IP1
# limits = [[-4e-5, 4e-5], [-2e-4, 2e-4], [-8e-5, 8e-5], [-5e-4, 5e-4],
# [-0.4, 0.4], [-5e-4, 5e-4]]  # Optics 1.0, IP1
d_2 = {k: v for k, v in zip(coords, limits)}

# offset = [0, 3e-4, 7.5e-4, 0, 0, 0]  # Optics 1.2, IP5
offset = [-7.5e-4, 0, 0, 0.3e-3, 0, 0]  # Optics 1.2, IP1
# offset = [0, 0, 0, 0, 0, 0]
d_3 = {k: v for k, v in zip(coords, offset)}

# Loop >ONCE< through the DUMP file to extract >only< the relevant information
# ID turn s[m] x[mm] xp[mrad] y[mm] yp[mrad] z[mm] dE/E ktrack
turn_data = defaultdict(lambda: defaultdict(list))
with open(infile, 'r') as f:
    for line in f.xreadlines():
        if '#' in line:
            continue
        columns = line.strip('\n').split()
        turn = int(columns[1])
        if turn not in turns:
            continue
        if coord_ver == 'e':
            coord_tot_1 = float(columns[d_1[coord_hor]]) * 10**-3
            coord_tot_2 = float(columns[d_1[coord_ver]])
        elif coord_hor == 'e':
            coord_tot_1 = float(columns[d_1[coord_ver]])
            coord_tot_2 = float(columns[d_1[coord_ver]]) * 10**-3
        else:
            coord_tot_1 = float(columns[d_1[coord_hor]]) * 10**-3
            coord_tot_2 = float(columns[d_1[coord_ver]]) * 10**-3
        turn_data[turn]['coord_tot_1'].append(coord_tot_1)
        turn_data[turn]['coord_tot_2'].append(coord_tot_2)


for turn in turns:
    print '>> Turn', turn
    coord_1 = turn_data[turn]['coord_tot_1']
    coord_2 = turn_data[turn]['coord_tot_2']

    # Plot characteristics
    DPI = 300
    textwidth = 6
    font_spec = {"font.family": "serif",  # use as default font
                 "font.serif": ["New Century Schoolbook"],  # custom serif font
                 "font.sans-serif": ["helvetica"],  # custom sans-serif font
                 "font.size": 12,
                 "font.weight": "bold"}
    rc('text', usetex=True)
    rc('text.latex', preamble=r'\usepackage{cmbright}')
    rcParams['figure.figsize'] = textwidth, textwidth / 1.618
    rcParams.update(font_spec)

    # 2D histogram
    H, xedges, yedges = np.histogram2d(coord_1, coord_2, bins=nbins)
    H = np.rot90(H)   # H needs to be rotated and flipped
    H = np.flipud(H)
    Hmasked = np.ma.masked_where(H == 0, H)  # Mask pixels with a value of zero
    plt.pcolormesh(xedges, yedges, Hmasked, norm=None, vmin=0, vmax=100)
    plt.colorbar()

    z_points = np.linspace(-0.4, 0.4, 100)
    y_points = -295 * 1e-6 * z_points
    plt.plot(z_points, y_points, color='green', label='-295 (should be)')

    # z_points_a = np.linspace(-0.4,0.4,100)
    # y_points_a = -210*1e-6*z_points
    # plt.plot(z_points_a, y_points_a, color='red', label='-210 (1 sigma)')

    z_points_b = np.linspace(-0.4, 0.4, 100)
    y_points_b = -256 * 1e-6 * z_points
    plt.plot(z_points_b, y_points_b, color='orange',
             label='-256 (whole bunch)')

    plt.legend(loc='lower left', prop={'size': 10})

    plt.title('Turn {}'.format(turn))
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    # Add the correct units to the labels depending on the coordinate
    for letter in coord_hor:
        if letter == 'p':
            plt.xlabel(coord_hor.strip('p') + "' [rad]")
        elif letter == 'e':
            plt.xlabel("$\Delta E/E$")
        else:
            plt.xlabel(coord_hor + ' [m]')

    for letter in coord_ver:
        if letter == 'p':
            plt.ylabel(coord_ver.strip('p') + "' [rad]")
        elif letter == 'e':
            plt.ylabel("$\Delta E/E$")
        else:
            plt.ylabel(coord_ver + ' [m]')

    # plt.xlim(d_2[coord_hor])
    # plt.ylim(d_2[coord_ver])

    # Plot the bucket or the sigmas
    if coord_hor == 'z' and coord_ver == 'e':
        mp = 0.938272046e9                 # proton mass, eV/c^2
        e = 1.60217657e-19                # C, electron charge
        c = 2.99792485e8                  # m/s, speed of light
        h = 35640                         # RF harmonic number
        omegaRF = 400.8e6 * np.pi * 2           # Hz, omegaRF = h*omega0
        omega0 = omegaRF / h
        slip = 3.467e-4                      # Slip factor @ collission
        V = 16e6                          # V, RF voltage @ collissions
        beta = 1.0                           # Relativistic beta
        phiS = 0.0                           # Radians, synchronous RF phase
        E0 = 7e12                          # Beam energy, eV
        p0 = np.sqrt(E0 ** 2 - mp ** 2)    # Beam momentum, eV/c

        conversion = 299792458 / 400.8e6
        delta = np.linspace(-1e-3 * conversion, 1e-3 *
                            conversion, 200)  # delta p / p
        phi = np.linspace(-3 * np.pi, 1 * np.pi, 200)
        DELTA, PHI = np.meshgrid(delta, phi)

        p = p0 * (1.0 + DELTA)  # eV/c
        E = np.sqrt(p ** 2 + mp ** 2)

        DELTA_E = E / E0 - 1

        H1 = 0.5 * omegaRF * slip * DELTA ** 2
        H2 = omega0 * V / (2 * np.pi * beta ** 2 * E) * \
            (np.cos(PHI) - np.cos(phiS) + (PHI - phiS) * np.sin(phiS))

        H = H1 + H2

        PHIp = PHI + np.pi  # above transition energy
        plt.contour(PHIp * 0.1, DELTA_E, H, 40,
                    linewidths=0.3, cmap='terrain_r')

    elif coord_hor == 'e' or coord_ver == 'e':
        print '>> No sigmas nor bucket for this coordinate combination. Try (z,e).'
    else:
        sigmas = [7.16610376198e-06, 4.76160858517e-05, 7.12405639107e-06,
                  4.75602973547e-05, 0.0745803056032, 767.801389427e-06]
        d_sigma = {k: v for k, v in zip(coords, sigmas)}  # dict comprehension

        std_coord_1 = d_sigma[coord_hor]
        std_coord_2 = d_sigma[coord_ver]

        pts1 = get_ellipse_coords(a=std_coord_1, b=std_coord_2, x=d_3[
                                  coord_hor], y=d_3[coord_ver], k=1)
        plt.plot(pts1[:, 0], pts1[:, 1], color="black", linewidth=0.3)

        pts2 = get_ellipse_coords(
            a=2 * std_coord_1, b=2 * std_coord_2, x=d_3[coord_hor], y=d_3[coord_ver], k=1)
        plt.plot(pts2[:, 0], pts2[:, 1], color="black", linewidth=0.3)

        pts3 = get_ellipse_coords(
            a=3 * std_coord_1, b=3 * std_coord_2, x=d_3[coord_hor], y=d_3[coord_ver], k=1)
        plt.plot(pts3[:, 0], pts3[:, 1], color="black", linewidth=0.3)

        pts4 = get_ellipse_coords(
            a=4 * std_coord_1, b=4 * std_coord_2, x=d_3[coord_hor], y=d_3[coord_ver], k=1)
        plt.plot(pts4[:, 0], pts4[:, 1], color="black", linewidth=0.3)

        pts5 = get_ellipse_coords(
            a=5 * std_coord_1, b=5 * std_coord_2, x=d_3[coord_hor], y=d_3[coord_ver], k=1)
        plt.plot(pts5[:, 0], pts5[:, 1], color="black", linewidth=0.3)

    plt.subplots_adjust(left=0.14, bottom=0.17, right=1, top=0.82)
    plt.savefig('dist_turn_{:02d}_{}_{}.png'.format(
        turn, coord_hor, coord_ver), dpi=DPI)
    plt.clf()

end_time = datetime.now()
print('>> Duration: {}'.format(end_time - start_time))
