#!/usr/bin/env python

import sys

import numpy as np

import matplotlib.mlab as mlab
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from scipy.stats import norm

from util import GetData

infile = sys.argv[1]
infile_2 = sys.argv[2]

def get_data(infile):
    get = GetData(infile)
    data = get.data_column()

    x  = np.asarray(data[0])
    xp = data[1]
    y  = data[2]
    yp = data[3]

    sigma_x = np.std(x)
    sigma_y = np.std(y)
    mu, std = norm.fit(x)
    return sigma_x, sigma_y, mu, std, x, y

sigma_x, sigma_y, mu, std, x, y = get_data(infile)
sigma_x2, sigma_y2, mu2, std2, x2, y2 = get_data(infile_2)

print sigma_x
# ------------------------------------------------------------------------------
# Plotting
# ------------------------------------------------------------------------------
font_spec = {"font.size": 10, }
rcParams.update(font_spec)
rcParams['figure.figsize'] = 4, 2
fig = plt.figure()
ax = fig.add_subplot(111)

sigma = 7.09e-6
# sigma_tail = 1.8*sigma_core
mean = 0.0

weights_core = np.ones_like(x)/len(x)
weights_tail = np.ones_like(x2)/len(x2)
# n, bins, patches = plt.hist(x/sigma_x, 50, weights=weights, facecolor='blue', alpha=0.50, linewidth=0.2)
plt.hist(x/sigma, 100, facecolor='blue', alpha=0.50, linewidth=0.2)
plt.hist(x2/sigma, 100, facecolor='red', alpha=0.50, linewidth=0.2)
xt = np.linspace(min(x/sigma), max(x/sigma_x), 100)
# p = norm.pdf(xt, mu, sigma_x/sigma)
# plt.plot(xt, p, 'k', linewidth=0.5)
# y = mlab.normpdf(bins, mean, 1)
# l = plt.plot(bins, y, 'r-', linewidth=0.5)
# yt = mlab.normpdf(bins, mean, 1.8)
# lt = plt.plot(bins, yt, 'g-', linewidth=0.5)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
ax.set_yscale('log')
plt.xlabel(r'x [$\sigma_{core}$]')
plt.ylabel('Beam Profile')
plt.xlim([-8,8])
# plt.ylim([1e-4,1])
plt.subplots_adjust(left=0.16, bottom=0.25, right=0.94, top=0.88)
plt.savefig('x_profile.png', dpi=1000)
plt.savefig('x_profile.eps', format='eps', dpi=1000)
plt.clf()