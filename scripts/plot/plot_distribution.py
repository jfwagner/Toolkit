#!/usr/local/bin/python
import sys
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from util import *

start_time = datetime.now()

# Feed the input to the script by command line
infile = sys.argv[1]
coord_hor = sys.argv[2]
coord_ver = sys.argv[3]
turn = float(sys.argv[4])
nbins =  int(sys.argv[5])

print '>> Plotting distribution', coord_hor, ',', coord_ver

# Create a series of dictionaries to associate information to each input coord.
coords = ['x', 'xp', 'y', 'yp', 'z', 'e']

col_number = [3, 4, 5, 6, 7, 8]
my_tup_1 = zip(coords, col_number)
d_1 = {}
for k, v in my_tup_1:
    d_1[k] = v
    
limits = [[-4e-5, 4e-5], [-2e-4, 2e-4], [-8e-5, 8e-5], [1e-4, 5e-4], [-0.4, 0.4], [-5e-4, 5e-4]]
my_tup_2 = zip(coords, limits)
d_2 = {}
for k, v in my_tup_2:
    d_2[k] = v

offset = [0, 0, 0, 0.3e-3, 0, 0]
my_tup_3 = zip(coords, offset)
d_3 = {}
for k, v in my_tup_3:
    d_3[k] = v
    
# Loop >ONCE< through the DUMP file to extract >only< the relevant information
# ID turn s[m] x[mm] xp[mrad] y[mm] yp[mrad] z[mm] dE/E ktrack
f = open(infile, 'r')
coord_1 = []
coord_2 = []

for t in range(1, int(turn) + 1):
    turn_i = "%i"%t
    print '>> Turn', t

    for line in f.xreadlines():
        columns = line.strip('\n').split()
        if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind' or columns[1] != turn_i:
            continue
        if coord_ver == 'e':
            coord_2.append(float(columns[d_1[coord_ver]]))
            coord_1.append(float(columns[d_1[coord_hor]])*10**-3)
        elif coord_hor == 'e':
            coord_1.append(float(columns[d_1[coord_ver]]))
            coord_2.append(float(columns[d_1[coord_ver]])*10**-3)
        else:
            coord_1.append(float(columns[d_1[coord_hor]])*10**-3)
            coord_2.append(float(columns[d_1[coord_ver]])*10**-3)

    # Plot characteristics
    DPI = 300
    textwidth = 6
    rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
    rc('text', usetex=True)
    rcParams['figure.figsize']=textwidth, textwidth/1.618

    # 2D histogram
    H, xedges, yedges = np.histogram2d(coord_1, coord_2, bins=nbins)
    H = np.rot90(H)   # H needs to be rotated and flipped
    H = np.flipud(H)
    Hmasked = np.ma.masked_where(H==0,H) # Mask pixels with a value of zero
    plt.pcolormesh(xedges, yedges, Hmasked, norm=None, vmin=0, vmax=100)
    plt.colorbar()

    plt.title('Turn ' + turn_i)
    plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0))
    plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))

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

    plt.xlim(d_2[coord_hor])
    plt.ylim(d_2[coord_ver])

    # Plot the bucket or the sigmas
    if coord_hor == 'z' and coord_ver == 'e':
        mp = 0.938272046e9 #proton mass, eV/c^2
        e  = 1.60217657e-19 #C, electron charge
        c  = 2.99792485e8   #m/s, speed of light
        h       = 35640    #RF harmonic number
        omegaRF = 400.8e6*np.pi*2    #Hz, omegaRF = h*omega0
        omega0  = omegaRF/h
        slip    = 3.467e-4 #Slip factor @ collission
        V       = 16e6     #V, RF voltage @ collissions
        beta    = 1.0      # Relativistic beta
        phiS    = 0.0      # Radians, synchronous RF phase
        E0      = 7e12     # Beam energy, eV
        p0      = np.sqrt(E0**2-mp**2) #Beam momentum, eV/c
        
        conversion = 299792458/(400.8e6)
        delta = np.linspace(-1e-3*conversion, 1e-3*conversion,200) #delta p / p
        phi   = np.linspace(-3*np.pi,1*np.pi,200)
        DELTA,PHI = np.meshgrid(delta,phi)

        p = p0*(1.0+DELTA) #eV/c
        E = np.sqrt(p**2 + mp**2)
        
        DELTA_E = E/E0-1
        
        H1 = 0.5* omegaRF* slip*DELTA**2
        H2 = omega0*V/(2*np.pi*beta**2*E)*(np.cos(PHI)-np.cos(phiS)+(PHI-phiS)*np.sin(phiS))
        
        H = H1+H2

        PHIp = PHI+np.pi #above transition energy
        plt.contour(PHIp*0.1,DELTA_E,H,40, linewidths=0.3, cmap='terrain_r')
        
    elif coord_hor == 'e' or coord_ver == 'e':
        print '>> No sigmas nor bucket for this coordinate combination. Try (z,e).'
    else:
        pts1 = get_ellipse_coords(a=np.std(coord_1), b=np.std(coord_2), x=0, y=d_3[coord_ver],k=1)
        plt.plot(pts1[:,0], pts1[:,1], color="black", linewidth=0.3)

        pts2 = get_ellipse_coords(a=2*np.std(coord_1), b=2*np.std(coord_2), x=0, y=d_3[coord_ver],k=1)
        plt.plot(pts2[:,0], pts2[:,1], color="black", linewidth=0.3)

        pts3 = get_ellipse_coords(a=3*np.std(coord_1), b=3*np.std(coord_2), x=0, y=d_3[coord_ver],k=1)
        plt.plot(pts3[:,0], pts3[:,1], color="black", linewidth=0.3)

        pts4 = get_ellipse_coords(a=4*np.std(coord_1), b=4*np.std(coord_2), x=0, y=d_3[coord_ver],k=1)
        plt.plot(pts4[:,0], pts4[:,1], color="black", linewidth=0.3)

        pts5 = get_ellipse_coords(a=5*np.std(coord_1), b=5*np.std(coord_2), x=0, y=d_3[coord_ver],k=1)
        plt.plot(pts5[:,0], pts5[:,1], color="black", linewidth=0.3)


    plt.subplots_adjust(left=0.14, bottom=0.17, right=1, top=0.82)
    
    if t <= 9:
        plt.savefig('dist_turn_0'+  turn_i + '_'+ coord_hor + '_' + coord_ver +'.png', dpi=DPI)
    elif t > 9:
        plt.savefig('dist_turn_'+  turn_i + '_'+ coord_hor + '_' + coord_ver +'.png', dpi=DPI)
    
    plt.clf()

f.close()

end_time = datetime.now()
print('>> Duration: {}'.format(end_time - start_time))