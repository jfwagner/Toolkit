from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import rc
from matplotlib import rcParams
from numpy import *
from util import *

DPI = 300
textwidth = 6
rc('font',**{'family':'serif','serif':['Computer Modern Roman'], 'size':10})
rc('text', usetex=True)
rcParams['figure.figsize']=textwidth, textwidth/1.618

def plot(dump_file, coordinate_1, coordinate_2, bins, turn):
    coord_1 = "%s"%coordinate_1
    coord_2 = "%s"%coordinate_2
    turn_i = "%i"%turn
    nbins = bins

    if coord_1 == "x":
        a = 3
        d = 0
        xlabel = "x [mm]"
        xlimit = [-4e-2, 4e-2]
    elif coord_1 == "xp":
        a = 4
        d = 0
        xlabel = "$x'$ [mrad]"
        xlimit = [-2e-1, 2e-1]
    elif coord_1 == "y":
        a = 5
        d = 0
        xlabel = "y [mm]"
        # xlimit = [-7e-2, 7e-2]
        # xlimit = [-14, 14]
    elif coord_1 == "yp":
        a = 6
        d = 0.3
        xlabel = "$y'$ [mrad]"
        xlimit = [1e-1, 5e-1]
    elif coord_1 == "z":
        a = 7
        d = 0
        xlabel = "z [mm]"
        xlimit = [-3e2, 3e2]
    elif coord_1 == "e":
        a = 8
        d = 0
        xlabel = "$\Delta E/E$"
        xlimit = [-4e-4, 4e-4]
    else:
        print "Invalid option for horizontal coordinate, choose among: x, xp, y, yp, z, e"

    if coord_2 == "x":
        b = 3
        d = 0
        ylabel = "x [mm]"
        ylimit = [-3e-2, 3e-2]
    elif coord_2 == "xp":
        b = 4
        d = 0
        ylabel = "$x'$ [mrad]"
        ylimit = [-3e-1, 3e-1]
    elif coord_2 == "y":
        b = 5
        d = 0
        ylabel = "y [mm]"
        ylimit = [-0.8e-1, 0.8e-1]
    elif coord_2 == "yp":
        b = 6
        d = 0.3
        ylabel = "$y'$ [mrad]"
        # ylimit = [-2e-1, 6e-1]
    elif coord_2 == "z":
        b = 7
        d = 0
        ylabel = "z [mm]"
        ylimit = [-3e2, 3e2]
    elif coord_2 == "e":
        b = 8
        d = 0
        ylabel = "$\Delta E/E$"
        ylimit = [-4e-4, 4e-4]
    else:
        print "Invalid option for vertical coordinate , choose among: x, xp, y, yp, z, e"

    var_x, var_y = get_dump(dump_file, a, b, turn)
    x = asarray(var_x)
    y = asarray(var_y)

    H, xedges, yedges = histogram2d(var_x, var_y, bins=nbins)
    H = rot90(H)   # H needs to be rotated and flipped
    H = flipud(H)
    Hmasked = ma.masked_where(H==0,H) # Mask pixels with a value of zero
    plt.pcolormesh(xedges, yedges, Hmasked, norm=None, vmin=0, vmax=100)
    plt.colorbar()

    # Plot the sigmas
    var_2x, var_2y = get_dump(dump_file, a, b, 2)
    x_2 = asarray(var_2x)
    y_2 = asarray(var_2y)

    pts1 = get_ellipse_coords(a=std(x_2), b=std(y_2), x=0, y=d,k=1)
    plt.plot(pts1[:,0], pts1[:,1], color="black", linewidth=0.3)

    pts2 = get_ellipse_coords(a=2*std(x_2), b=2*std(y_2), x=0, y=d,k=1)
    plt.plot(pts2[:,0], pts2[:,1], color="black", linewidth=0.3)

    pts3 = get_ellipse_coords(a=3*std(x_2), b=3*std(y_2), x=0, y=d,k=1)
    plt.plot(pts3[:,0], pts3[:,1], color="black", linewidth=0.3)

    pts4 = get_ellipse_coords(a=4*std(x_2), b=4*std(y_2), x=0, y=d,k=1)
    plt.plot(pts4[:,0], pts4[:,1], color="black", linewidth=0.3)

    pts5 = get_ellipse_coords(a=5*std(x_2), b=5*std(y_2), x=0, y=d,k=1)
    plt.plot(pts5[:,0], pts5[:,1], color="black", linewidth=0.3)

    # ---------------------
    # Info for the bucket
    # ---------------------
    conversion = 299792458/(400.8e6)
    delta = linspace(-1e-3, 1e-3,6400) #delta p / p
    phi   = linspace(-3*pi*conversion,1*pi*conversion,6400)
    DELTA,PHI = meshgrid(delta,phi)

    mp = 0.938272046e9 #proton mass, eV/c^2
    e  = 1.60217657e-19#C, electron charge
    c  = 2.99792485e8  #m/s, speed of light
    h       = 35640    #RF harmonic number
    omegaRF = 400.8e6*pi*2    #Hz, omegaRF = h*omega0
    omega0  = omegaRF/h
    slip    = 3.467e-4 #Slip factor @ collission
    V       = 16e6     #V, RF voltage @ collissions
    beta    = 1.0      # Relativistic beta
    phiS    = 0.0      # Radians, synchronous RF phase
    E0      = 7e12     # Beam energy, eV
    p0      = sqrt(E0**2-mp**2) #Beam momentum, eV/c
    p = p0*(1.0+DELTA) #eV/c
    E = sqrt(p**2 + mp**2)
    DELTA_E = E/E0-1
    H1 = 0.5* omegaRF* slip*DELTA**2
    PHIp = PHI+pi
    H2 = omega0*V/(2*pi*beta**2*E)*(cos(PHI)-cos(phiS)+(PHI-phiS)*sin(phiS))

    H = H1+H2
    # plt.plot(H, DELTA_E)

    plt.title('Turn ' + turn_i)
    plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0))
    plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.xlim(xlimit)
    # plt.ylim(ylimit)

    plt.subplots_adjust(left=0.16, bottom=0.21, right=1,top=0.88)

    if turn <= 9:
        plt.savefig('dist_turn_0'+  turn_i + '_'+ coord_1 + '_' + coord_2 +'.png', dpi=DPI)
    elif turn > 9:
        plt.savefig('dist_turn_'+  turn_i + '_'+ coord_1 + '_' + coord_2 +'.png', dpi=DPI)
    plt.clf()
