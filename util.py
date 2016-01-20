# --------------------------------------------
# Series of useful functions to help plotting
# --------------------------------------------
from __future__ import division
import re
from matplotlib import pyplot as plt
import numpy as np

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

def get_lines(infile):
    """Extracts the lines of a data file. Used in the get_columns function."""
    for character in open(infile):
        columns = character.strip('\n').split()
        if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s' or columns[0] == '%Ind':
            continue
        yield columns
        
def get_columns(infile, x, y, type):
    """Extracts the columns of a data file using the get_lines function. 

    The function arguments' are (in order): 
    - File
    - Number of the column corresponding to coordinate x
    - Number of the column corresponding to coordinate y
    - Indicate if the data to return are strings or floats

    Example:
    var_x, var_y = get_columns('LHCAperture_old.dat', 0, 2, "float")
    """
    a = []
    b = []
    my_data = get_lines(infile)
    for column in my_data:
        if type == "string":
            a.append(column[x])
            b.append(column[y])
        elif type == "float":
            a.append(float(column[x]))
            b.append(float(column[y]))
    if type == "float":
        var_x = np.asarray(a)
        var_y = np.asarray(b)
    elif type == "string":
        var_x = a
        var_y = b
    return var_x, var_y

def get_column(infile, column_number, data_structure, data_type):
    """Extracts a column of a data file using the get_lines function. 

    The function arguments' are (in order): 
    - File
    - Number of the desired column
    - Indicate if the data structure to return should be an array or a list

    Example:
    var_x = get_columns('LHCAperture_old.dat', 2, "array")
    """
    my_column = []
    my_data = list(get_lines(infile))
    if data_type == "string":
        for columns in my_data:
            my_column.append(columns[column_number])
    elif data_type == "float":
        for columns in my_data:
            my_column.append(float(columns[column_number]))
    if data_structure == "array":
        my_final_column = asarray(my_column)
    elif data_structure == "list":
        my_final_column = my_column
    return my_final_column

def get_ip1(x,y):
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
    return x,y

def get_ir(ir, ylim):
    """This function stores the information relevant to the plotting of a specific Interaction Region (IR), 
    i.e. the position of the IR in the accelerator and the limit of the vertical coordinate.

    The function arguments' are (in order):
    - Number of the IR (from 1 to 8, both included)
    - Limit in the vertical coordinate

    Example:
    position, ylim = get_ir(2, 0.6)
    """
    t = (0, 3332.436584, 6664.7208, 9997.005016, 13329.28923, 16661.72582, 19994.1624, 23315.37898)
    position = t[ir-1]
    return position, ylim

def plot_elem(color, height, bottom, name_in = [], s_in = [], l_in = [], *args):
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
        f = s-l
        plt.bar(f, height, l, bottom, color=color, alpha=0.7) # left, height, width, bottom

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
    pts = np.zeros((360*k+1, 2))

    beta = -angle * np.pi/180.0
    sin_beta = np.sin(beta)
    cos_beta = np.cos(beta)
    alpha = np.radians(np.r_[0.:360.:1j*(360*k+1)])
 
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
    column_filter = ('#', '@', '*', '$', '%', '%1=s', '%Ind') #ToDo:function in util.py
    extract_header = ('#', '@', '$', '%', '%1=s', '%Ind')

    # Choose which parameters you want to extract to a list
    my_list = list(args)
    my_dict = {i:[] for i in my_list}

    # Extract the associated column index
    col_idx = []
    col_name = [] #ToDo: convert this to tuple to skip the zip
    for line in f.xreadlines():
        columns = line.strip('\n').split()
        for idx, value in enumerate(columns):
            if columns[0] in extract_header:
                    continue
            if value in my_list: # for item in my_list: /if value == item: 
                col_idx.append(idx-1)
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

def plot_beams(x, y, energy, norm_em, beta_x, beta_y, ip1):
    m = 938272046 #eV/c
    gamma_rel = energy/m
    beta_rel = np.sqrt(1-(1/gamma_rel**2))
    geom_em = norm_em/(gamma_rel*beta_rel)
    if ip1 == 'yes':
        x_final, y_final = get_ip1(x,y)
        beta_x_final, beta_y_final = get_ip1(beta_x, beta_y)
    elif ip1 == 'no':
        x_final = x
        y_final = y
        beta_x_final = beta_x
        beta_y_final = beta_y
    # sigma x
    sigma_x = []
    for i in beta_x_final:
        print i
        sigma_x.append(np.sqrt(geom_em*i))
    one_sigma_x = []
    for i, j in zip(sigma_x, x_final):
        one_sigma_x.append(j + i)
    m_one_sigma_x = []
    for i, j in zip(sigma_x, x_final):
        m_one_sigma_x.append(j - i)
    five_sigma_x = []
    for i, j in zip(sigma_x, x_final):
        five_sigma_x.append(j + 5*i)
    m_five_sigma_x = []
    for i, j in zip(sigma_x, x_final):
        m_five_sigma_x.append(j - 5*i)
    # sigma y
    sigma_y = []
    for i in beta_y_final:
        sigma_y.append(np.sqrt(geom_em*i))
    one_sigma_y = []
    for i, j in zip(sigma_y, y_final):
        one_sigma_y.append(j + i)
    m_one_sigma_y = []
    for i, j in zip(sigma_y, y_final):
        m_one_sigma_y.append(j - i)
    five_sigma_y = []
    for i, j in zip(sigma_y, y_final):
        five_sigma_y.append(j + 5*i)
    m_five_sigma_y = []
    for i, j in zip(sigma_y, y_final):
        m_five_sigma_y.append(j - 5*i)
    return x_final, y_final, one_sigma_x, m_one_sigma_x, five_sigma_x, m_five_sigma_x, one_sigma_y, m_one_sigma_y, five_sigma_y, m_five_sigma_y