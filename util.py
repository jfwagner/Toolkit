# --------------------------------------------
# Series of useful functions to help plotting
# --------------------------------------------
import re
from numpy import *

def get_lines(infile):
    """Extracts the lines of a data file. Used in the get_columns function."""
    for character in open(infile):
        columns = character.strip('\n').split()
        if columns[0] == '#' or columns[0] == '@' or columns[0] == '*' or columns[0] == '$' or columns[0] == '%' or columns[0] == '%1=s':
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
        var_x = asarray(a)
        var_y = asarray(b)
    elif type == "string":
        var_x = a
        var_y = b
    return var_x, var_y

def get_column(infile, column_number, data_type):
    """Extracts a column of a data file using the get_lines function. 

    The function arguments' are (in order): 
    - File
    - Number of the desired column
    - Indicate if the data structure to return should be an array or a list

    Example:
    var_x = get_columns('LHCAperture_old.dat', 2, "array")
    """
    my_column = []
    my_data = get_lines(infile)
    for columns in my_data:
        my_column.append(columns[column_number])
    if data_type == "array":
        my_final_column = asarray(my_column)
    elif data_type == "list":
        my_final_column = my_column
    return my_final_column

def get_dump(infile, turn_number, column_number):
    my_column = []
    my_data = get_lines(infile)
    for columns in my_data:
        if columns[1] == turn_number:
            my_column.append(float(columns[column_number])*(10**(-3)))
    my_final_column = asarray(my_column)
    return my_final_column

# def get_dump(infile, col_number_a, col_number_b, turn):
#     turn_i = '%i'%turn
#     a = []
#     b = []
#     my_data = get_lines(infile)
#     for column in my_data:
#         if column[1] == turn_i:
#             a.append(float(column[col_number_a]))
#             b.append(float(column[col_number_b]))
#     var_x = asarray(a)
#     var_y = asarray(b)
#     return var_x, var_y

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

def get_element(infile, column_name, column_position, regex, text_height):
    """This function extracts the information relevant to the plotting of the accelerator's elements.

    The function arguments' are (in order):
    - File 
    - Number of the column corresponding to the name
    - Number of the column corresponding to the position
    - List of regular expressions defining the elements you want to plot (e.g. all that start with the 
    letter 'V')
    - The height at which the name of the element will appear in the plot

    Example:
    name, pos, height = get_element('twiss_ip1_b1.tfs', 0, 3, ['VC+'], 0.6)
    """
    name = []
    position = []
    my_data = get_lines(infile)
    for column in my_data:
        name.append(column[column_name].strip('"'))
        position.append(float(column[column_position]))

    new_name = []
    new_position = []
    for expression in regex:
        regex = re.compile(expression)
        for e1, e2 in zip(name,position):
            if regex.match(e1):
                new_name.append(e1)
                new_position.append(e2)
    return new_name, new_position, text_height

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
    pts = zeros((360*k+1, 2))

    beta = -angle * pi/180.0
    sin_beta = sin(beta)
    cos_beta = cos(beta)
    alpha = radians(r_[0.:360.:1j*(360*k+1)])
 
    sin_alpha = sin(alpha)
    cos_alpha = cos(alpha)
    
    pts[:, 0] = x + (a * cos_alpha * cos_beta - b * sin_alpha * sin_beta)
    pts[:, 1] = y + (a * cos_alpha * sin_beta + b * sin_alpha * cos_beta)

    return pts
