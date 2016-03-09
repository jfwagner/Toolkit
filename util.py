#!/usr/local/bin/python
# --------------------------------------------
# Series of useful functions to help plotting
# --------------------------------------------
from __future__ import division
import re
from matplotlib import pyplot as plt
import numpy as np


class GetData:

    def __init__(self, infile):
        self.infile = infile

    def is_header(self, line):
        """
        Returns True if the line contains any of the symbols: @, #, $, %, &, *
        --> Useful to skip lines that contain any of these symbols at any position.
        --> Used in the data_line function.
        """
        return re.search(r'#|@|\*|%|\$|&', line) is not None

    def data_line(self, column=None, regex=None):
        """
        Generator function that returns the lines of a file, skipping the lines
        containing the symbols: @, #, $, %, &, *.
        >> a = get_columns('dump.txt')
        >> a.next()
        --> Useful to read big data files (avoid loading a whole list in memory).
        --> Used in the data_array function.
        """
        with open(self.infile, 'r') as data:  # using with the file is closed automatically
            for line in data:
                if self.is_header(line):
                    continue
                # split on contiguous blank spaces and remove return of line
                line_list = line.strip('\n').split()
                if (column and regex) is not None:
                    if re.match(regex, line_list[column]):
                        yield line_list
                elif (column and regex) is None:
                    yield line_list
                else:
                    print 'Column or regex missing from arguments'

    def data_column(self, dtype=float, column=None, regex=None):
        """
        Returns a dictionary of lists, containing the columns of the data file.
        The dictionary keys are the number of the columns.
        """
        start_line = self.data_line(column, regex).next()
        data_dict = {key: [] for key, item in enumerate(
            start_line)}  # Create keys and empty lists
        for line in self.data_line(column, regex):
            for count, item in enumerate(line):
                if type(item) == str:
                    # Strip needed for MAD-X output
                    data_dict[count].append(item.strip('"'))
                else:
                    data_dict[count].append(float(item))  # Fill in the lists
        return data_dict


class PlotData(GetData):

    def basic(self, x_coord, y_coord, filename, title=None, x_label=None, y_label=None, x_lim=None, y_lim=None, scatter=False, column=None, regex=None):
        data_dict = PlotData(self.infile).data_column(column, regex)
        x = data_dict[x_coord]
        y = data_dict[y_coord]

        DPI = 300
        textwidth = 6
        font_spec = {"font.family": "serif",  # use as default font
                     # custom serif font
                     "font.serif": ["New Century Schoolbook"],
                     # custom sans-serif font
                     "font.sans-serif": ["helvetica"],
                     "font.size": 12,
                     "font.weight": "bold"}
        rc('text', usetex=True)
        rc('text.latex', preamble=r'\usepackage{cmbright}')
        rcParams['figure.figsize'] = textwidth, textwidth / 1.618
        rcParams.update(font_spec)

        if scatter:
            plt.scatter(x, y)
        else:
            plt.plot(x, y)

        plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.grid(b=None, which='major')

        if title is not None:
            plt.title(title)

        if x_label is not None:
            plt.xlabel(x_label)

        if y_label is not None:
            plt.ylabel(y_label)

        if x_lim is not None:
            plt.xlim(x_lim)

        if y_lim is not None:
            plt.ylim(y_lim)

        plt.subplots_adjust(left=0.13, bottom=0.14, right=0.94, top=0.93)
        plt.savefig(filename + '.png', dpi=DPI)
        plt.clf()


def get_ip1(x, y):
    """Treats the x and y coordinates already extracted from the data in order to easily plot
    around IP1 (i.e. convert s coordinate of 26900 m to -100 m).
    The function arguments' are the variables x and y that you want to treat, respectively . 
    Example:
    var_x, var_y = get_ip1(var_x, var_y)
    """
    zipped = zip(x, y)
    x_temp = []
    y_temp = []
    for e1, e2 in zipped:
        if e1 < (26658.8832 / 2):
            x_temp.append(e1)
            y_temp.append(e2)
        if e1 >= (26658.8832 / 2):
            x_temp.append(e1 - 26658.8832)
            y_temp.append(e2)
    x = []
    y = []
    for e1, e2 in sorted(zip(x_temp, y_temp), key=lambda t: t[0]):
        x.append(e1)
        y.append(e2)
    return x, y


def get_bucket():
    """ Returns the data needed to plot the RF bucket of LHC.
    Adapted from Kyrre Sjobak.
    Usage: plt.contour(PHIp * 0.1, DELTA_E, H, 40, linewidths=0.3, cmap='terrain_r')
    """
    mp = 0.938272046e9                 # proton mass, eV/c^2
    e = 1.60217657e-19                 # C, electron charge
    c = 2.99792485e8                   # m/s, speed of light
    h = 35640                          # RF harmonic number
    omegaRF = 400.8e6 * np.pi * 2      # Hz, omegaRF = h*omega0
    omega0 = omegaRF / h
    slip = 3.467e-4                    # Slip factor @ collission
    V = 16e6                           # V, RF voltage @ collissions
    beta = 1.0                         # Relativistic beta
    phiS = 0.0                         # Radians, synchronous RF phase
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

    return PHIp * 0.1, DELTA_E, H


def get_ir(ir, s, coord):
    """This function stores the information relevant to the plotting of a specific Interaction Region (IR), 
    i.e. the position of the IR in the accelerator and the limit of the vertical coordinate.

    The function arguments' are (in order):
    - Number of the IR (from 1 to 8, both included)
    - Limit in the vertical coordinate

    Example:
    position, ylim = get_ir(2, 0.6)
    """
    t = (0, 3332.436584, 6664.7208, 9997.005016,
         13329.28923, 16661.72582, 19994.1624, 23315.37898)
    zipped = zip(s, coord)
    s_temp = []
    coord_temp = []
    for i, j in zipped:
        s_temp.append(i - t[int(ir) - 1])
        coord_temp.append(j)
    s_new, coord_new = get_ip1(s_temp, coord_temp)
    return s_new, coord_new


def plot_elem(color, height, bottom, name_in=[], s_in=[], l_in=[], *args):
    """
    >> Input: color, height and bottom of the element, list of all the names, positions and lengths, list of element names
    >> Output: bar plot

    Example:
    plot_elem('red', height, bottom, name_b1_twiss, s_b1_twiss, l_b1_twiss,  'MQXFA', 'MQXFB') # Triplet: Q1, Q3, Q2
    """
    regex_list = list(args)
    name_out = []
    s_out = []
    l_out = []
    for a in regex_list:
        regex = re.compile(a)
        for list_1, list_2, list_3 in zip(name_in, s_in, l_in):
            if regex.match(list_1):
                name_out.append(list_1)
                s_out.append(float(list_2))
                l_out.append(float(list_3))
    for s, element, l in zip(s_out, name_out, l_out):
        f = s - l
        # left, height, width, bottom
        plt.bar(f, height, l, bottom, color=color, alpha=0.7)


def load_data_coll(infile, coll_id):
    f = open(infile, 'r')
    s = []
    x = []
    y = []
    for line in f.xreadlines():
        columns = line.strip('\n').split()
        if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind' or columns[0] != coll_id:
            continue
        s.append(float(columns[2]))
        x.append(float(columns[3]))
        y.append(float(columns[5]))
    f.close()
    s_array = np.asarray(s)
    x_array = np.asarray(x)
    y_array = np.asarray(y)
    return s_array, x_array, y_array


def get_ellipse_coords(a=0.0, b=0.0, x=0.0, y=0.0, angle=0.0, k=2):
    """ Draws an ellipse using (360*k + 1) discrete points; based on pseudo code
    given at http://en.wikipedia.org/wiki/Ellipse
    k = 1 means 361 points (degree by degree)
    a = major axis distance,
    b = minor axis distance,
    x = offset along the x-axis
    y = offset along the y-axis
    angle = clockwise rotation [in degrees] of the ellipse;
        * angle=0  : the ellipse is aligned with the positive x-axis
        * angle=30 : rotated 30 degrees clockwise from positive x-axis
    """
    pts = np.zeros((360 * k + 1, 2))

    beta = -angle * np.pi / 180.0
    sin_beta = np.sin(beta)
    cos_beta = np.cos(beta)
    alpha = np.radians(np.r_[0.:360.:1j * (360 * k + 1)])

    sin_alpha = np.sin(alpha)
    cos_alpha = np.cos(alpha)

    pts[:, 0] = x + (a * cos_alpha * cos_beta - b * sin_alpha * sin_beta)
    pts[:, 1] = y + (a * cos_alpha * sin_beta + b * sin_alpha * cos_beta)

    return pts


def get_madx_columns(infile, *args):
    """
    >> Input: data file to read, list of column headers that you want to extract
    >> Output: a dictionary of lists, key accesible with the name of the header

    Example:
    dict_b1_twiss = get_madx_columns(infile_b1_twiss, 'S', 'L', 'BETX', 'BETY', 'X', 'Y', 'NAME')
    dict_b1_twiss['S']
    """

    f = open(infile, 'r')
    # Skip rows starting with certain symbols
    column_filter = ('#', '@', '*', '$', '%', '%1=s',
                     '%Ind')  # ToDo:function in util.py
    extract_header = ('#', '@', '$', '%', '%1=s', '%Ind')

    # Choose which parameters you want to extract to a list
    my_list = list(args)
    my_dict = {i: [] for i in my_list}

    # Extract the associated column index
    col_idx = []
    col_name = []  # ToDo: convert this to tuple to skip the zip
    for line in f.xreadlines():
        columns = line.strip('\n').split()
        for idx, value in enumerate(columns):
            if columns[0] in extract_header:
                continue
            if value in my_list:  # for item in my_list: /if value == item:
                col_idx.append(idx - 1)
                col_name.append(value)
        for index, name in zip(col_idx, col_name):
            if columns[0] in column_filter:
                continue
            if name != 'NAME':
                my_dict[name].append(float(columns[index]))
            elif name == 'NAME':
                my_dict[name].append(columns[index].strip('"'))
    f.close()
    return my_dict


def plot_twiss_beams(s, coord, energy, norm_em, beta, ip, lim):
    m = 938272046  # eV/c
    gamma_rel = energy / m
    beta_rel = np.sqrt(1 - (1 / gamma_rel**2))
    geom_em = norm_em / (gamma_rel * beta_rel)
    if ip == '1':
        s_final, coord_final = get_ip1(s, coord)
        s_temp, beta_final = get_ip1(s, beta)
    else:
        s_ip, coord_ip = get_ir(ip, s, coord)
        s_temp, beta_ip = get_ir(ip, s, beta)
        s_final, coord_final = get_ip1(s_ip, coord_ip)
        s_temp, beta_final = get_ip1(s_ip, beta_ip)
    # sigma
    sigma = []
    for i in beta_final:
        sigma.append(np.sqrt(geom_em * i))
    one_sigma = []
    for i, j in zip(sigma, coord_final):
        one_sigma.append(j + i)
    m_one_sigma = []
    for i, j in zip(sigma, coord_final):
        m_one_sigma.append(j - i)
    five_sigma = []
    for i, j in zip(sigma, coord_final):
        five_sigma.append(j + 5 * i)
    m_five_sigma = []
    for i, j in zip(sigma, coord_final):
        m_five_sigma.append(j - 5 * i)

    s_final_2 = []
    coord_final_2 = []
    one_sigma_2 = []
    m_one_sigma_2 = []
    five_sigma_2 = []
    m_five_sigma_2 = []
    for e1, e2, e3, e4, e5, e6 in zip(s_final, coord_final, one_sigma, m_one_sigma, five_sigma, m_five_sigma):
        if abs(e1) < float(lim):
            s_final_2.append(e1)
            coord_final_2.append(e2)
            one_sigma_2.append(e3)
            m_one_sigma_2.append(e4)
            five_sigma_2.append(e5)
            m_five_sigma_2.append(e6)

    return s_final_2, coord_final_2, one_sigma_2, m_one_sigma_2, five_sigma_2, m_five_sigma_2


def plot_twiss(s, coord, ip, lim):
    if ip == '1':
        s_final, coord_final = get_ip1(s, coord)
    else:
        s_ip, coord_ip = get_ir(ip, s, coord)
        s_final, coord_final = get_ip1(s_ip, coord_ip)

    s_final_2 = []
    coord_final_2 = []

    for e1, e2 in zip(s_final, coord_final):
        if abs(e1) < float(lim):
            s_final_2.append(e1)
            coord_final_2.append(e2)

    return s_final_2, coord_final_2
