#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import rc
from matplotlib import rcParams
from util import GetData

infile = 'dump.txt'
get = GetData(infile)

# --------------------------------------------------------------------
# Parameters
# --------------------------------------------------------------------
emittance_norm = 2.5e-6  # um
# --------------------------------------------------------------------
beta_x = 0.150739  # [m]
beta_y = 0.150235
# --------------------------------------------------------------------
alpha_x = 0.003485
alpha_y = -0.000764
# --------------------------------------------------------------------
gamma_x = (1 + alpha_x**2) / beta_x
gamma_y = (1 + alpha_y**2) / beta_y
# --------------------------------------------------------------------
energy = 7e12  # Beam energy at collision [eV]

# --------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------
m_p = 938.272046e6  # Proton mass [eV/c^2]
c = 299792458  # Speed of light [m/s]
gamma_rel = energy / m_p  # Relativistic gamma
beta_rel = np.sqrt(1 - (1 / gamma_rel**2))  # Relativistic beta
emittance_geom = emittance_norm / (beta_rel * gamma_rel)
sigma_x = np.sqrt(emittance_geom * beta_x)
sigma_y = np.sqrt(emittance_geom * beta_y)

# --------------------------------------------------------------------
# Uncomment for single particle
# --------------------------------------------------------------------
# my_data = get.data_column(column=0, regex=r'1\b')
# turn = my_data[1]
# x = my_data[3]
# xp = my_data[4]
# y = my_data[5]
# yp = my_data[6]

# --------------------------------------------------------------------
# Uncomment for whole bunch
# --------------------------------------------------------------------
my_data = get.data_column()
turn_temp = my_data[1]

y = []
yp = []
turn = []
for t in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    filter_turn = get.data_column(column=1, regex='{}\\b'.format(t))
    turn_temp = filter_turn[1]
    y_temp = filter_turn[5]
    yp_temp = filter_turn[6]
    # Sigma matrix for Y
    term_1_y = np.mean(np.multiply(y_temp, y_temp)) - \
        np.multiply(np.mean(y_temp), np.mean(y_temp))
    term_2_y = np.mean(np.multiply(y_temp, yp_temp)) - \
        np.multiply(np.mean(y_temp), np.mean(yp_temp))
    term_3_y = np.mean(np.multiply(yp_temp, y_temp)) - \
        np.multiply(np.mean(yp_temp), np.mean(y_temp))
    term_4_y = np.mean(np.multiply(yp_temp, yp_temp)) - \
        np.multiply(np.mean(yp_temp), np.mean(yp_temp))
    det_y = np.multiply(term_1_y, term_4_y) - np.multiply(term_3_y, term_2_y)
    y.append(np.sqrt(abs(det_y)) * 1e-6)
    # yp.append(np.mean(yp_temp))
    turn.append(t)

# for i, j in zip(turn, y):
#     print i, j


# failure_turn = 5

# def get_cs_invariant(turn, y, yp, alpha, beta, gamma):
#     em = []
#     em_geom = []
#     sigma = []
#     sigma_geom = []
#     t = []
#     for i, j, k in zip(y, yp, turn):
#         term_1 = gamma*pow(i*1e-3,2)
#         term_2 = 2*alpha*i*j*1e-6
#         term_3 = beta*pow(j*1e-3,2)
#         t.append(k)
#         em.append((term_1 + term_2 + term_3)/(beta_rel*gamma_rel))
#         # em_geom.append((term_1 + term_2 + term_3)/(beta_rel*gamma_rel))
#         # sigma.append(np.sqrt((term_1 + term_2 + term_3)*beta_y))
#         # sigma_geom.append(np.sqrt(((term_1 + term_2 + term_3)/(beta_rel*gamma_rel))*beta_y)/sigma_y)
#     return t, em

def get_delta(turn, coord):
    new_turn = []
    new_coord = []
    for i, j in sorted(zip(turn, coord)):
        if i == 1:
            continue
        elif i == 2:
            coord_0 = j
        new_turn.append(i)
        new_coord.append(abs(coord_0 - j))
    return new_turn, new_coord


def get_sigma(turn, em_geom, beta, sigma):
    t = []
    sig = []
    sig_norm = []
    for i, j in zip(turn, em_geom):
        t.append(i)
        sig.append(np.sqrt(beta * j))
        sig_norm.append(np.sqrt(beta * j) / sigma)
    return t, sig, sig_norm


# t_y, em_y = get_cs_invariant(turn, y, yp, alpha_y, beta_y, gamma_y)
t_dy, em_dy = get_delta(turn, y)
t_sy, sig_y, sig_norm_y = get_sigma(t_dy, em_dy, beta_y, sigma_y)


for i, j, k in zip(t_sy, sig_y, sig_norm_y):
    print i, j, k

# t1, y1 = get_delta(turn, y)


# for i, j in zip(t_y, em_y):
#     print i, j

# # ----------------------------------------------------------------------
# # PLOTTING
# # ----------------------------------------------------------------------
# # Plot characteristics
# DPI = 300
# textwidth = 6
# font_spec = {"font.family": "serif", # use as default font
#              "font.serif": ["New Century Schoolbook"], # custom serif font
#              "font.sans-serif": ["helvetica"], # custom sans-serif font
#              "font.size":12,
#              "font.weight":"bold",
#             }
# rc('text', usetex=True)
# rc('text.latex', preamble=r'\usepackage{cmbright}')
# rcParams['figure.figsize']=textwidth, textwidth/1.618
# rcParams.update(font_spec)


# plt.plot(t_sy, sig_norm_y, marker="+", color="blue")
# plt.xlabel("Turns")
# plt.ylabel(r"$\Delta y \ \ [\sigma]$")
# plt.subplots_adjust(left=0.13, bottom=0.14, right=0.94, top=0.93)
# plt.savefig('y_displacement.png', dpi=DPI)
# plt.clf()
