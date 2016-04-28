#!/usr/bin/env python
import sys

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData

infile_before = 'before.txt'
get_before = GetData(infile_before)
my_data_before = get_before.data_column(column=1, regex=r'2\b')
yp_before = my_data_before[6]
z_before = my_data_before[7]
delta_before = my_data_before[8]

infile_after = 'after.txt'
get_after = GetData(infile_after)
my_data_after = get_after.data_column(column=1, regex=r'2\b')
yp_after = my_data_after[6]
z_after = my_data_after[7]
delta_after = my_data_after[8]

y = []
x = []
for a, b, c, d, e, f in zip(yp_before, delta_before, z_before, yp_after, delta_after, z_after):
    term_1 = d / (1 + e)
    term_2 = a / (1 + b)
    y.append((term_1 - term_2)*7*1e12)
    x.append(c)