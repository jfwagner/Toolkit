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
        xlabel = "x [mm]"
        xlimit = [-4e-2, 4e-2]
    elif coord_1 == "xp":
        a = 4
        xlabel = "$x'$ [mrad]"
        xlimit = [-2e-1, 2e-1]
    elif coord_1 == "y":
        a = 5
        xlabel = "y [mm]"
        xlimit = [-7e-2, 7e-2]
    elif coord_1 == "yp":
        a = 6
        xlabel = "$y'$ [mrad]"
        xlimit = [1e-1, 5e-1]
    elif coord_1 == "z":
        a = 7
        xlabel = "z [mm]"
        xlimit = [-3e2, 3e2]
    elif coord_1 == "e":
        a = 8
        xlabel = "$\Delta E/E$"
        xlimit = [-4e-4, 4e-4]
    else:
        print "Invalid option for horizontal coordinate, choose among: x, xp, y, yp, z, e"

    if coord_2 == "x":
        b = 3
        ylabel = "x [mm]"
        ylimit = [-3e-2, 3e-2]
    elif coord_2 == "xp":
        b = 4
        ylabel = "$x'$ [mrad]"
        ylimit = [-3e-1, 3e-1]
    elif coord_2 == "y":
        b = 5
        ylabel = "y [mm]"
        ylimit = [-0.8e-1, 0.8e-1]
    elif coord_2 == "yp":
        b = 6
        ylabel = "$y'$ [mrad]"
        ylimit = [0, 6e-1]
    elif coord_2 == "z":
        b = 7
        ylabel = "z [mm]"
        ylimit = [-3e2, 3e2]
    elif coord_2 == "e":
        b = 8
        ylabel = "$\Delta E/E$"
        ylimit = [-4e-4, 4e-4]
    else:
        print "Invalid option for vertical coordinate , choose among: x, xp, y, yp, z, e"

    var_x, var_y = get_dump(dump_file, a, b, turn)
    x = asarray(var_x)
    y = asarray(var_y)

    H, xedges, yedges = histogram2d(var_x, var_y, bins=nbins)
    # H needs to be rotated and flipped
    H = rot90(H)
    H = flipud(H)
    # Mask zeros
    Hmasked = ma.masked_where(H==0,H) # Mask pixels with a value of zero
    plt.pcolormesh(xedges, yedges, Hmasked, norm=None, vmin=0, vmax=100)
    plt.colorbar()

    plt.title('Turn ' + turn_i)
    plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0))
    plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(xlimit)
    plt.ylim(ylimit)

    plt.subplots_adjust(left=0.16, bottom=0.21, right=1,top=0.88)

    if turn <= 9:
        plt.savefig('dist_turn_0'+  turn_i + '_'+ coord_1 + '_' + coord_2 +'.png', dpi=DPI)
    elif turn > 9:
        plt.savefig('dist_turn_'+  turn_i + '_'+ coord_1 + '_' + coord_2 +'.png', dpi=DPI)
    plt.clf()
