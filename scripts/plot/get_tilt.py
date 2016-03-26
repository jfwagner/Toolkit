#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import rc
from matplotlib import rcParams
from scipy.optimize import curve_fit
from util import GetData

infile = 'dump.txt'
obs_turns = [1, 2, 3, 4, 5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15]
get = GetData(infile)

for t in obs_turns:
    my_data = get.data_column(column=1, regex='{}\\b'.format(t))
    p_id = my_data[0]
    turn = my_data[1]
    y = my_data[5]
    z = my_data[7]
    m = np.polyfit(z, y, 1)
    print 'Turn', t, m[0]*1e6



