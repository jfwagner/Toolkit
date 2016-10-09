#!/usr/bin/env python
import sys

from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import rcParams

from util import GetData
from util import plot_2d_hist

turns = int(sys.argv[1])

def extract(infile, col_1, col_2, col_3=0):
    get = GetData(infile)
    data = get.data_column()
    turn = data[col_1]
    value = data[col_2]
    if col_3 == 0:
        return turn, value
    else:
        value_2 = data[col_3]
        return turn, value, value_2

# turn, sigma = extract('sigmas.txt', 0, 1)

turn_t, tilt = extract('tilt.txt', 0, 1)

# turn_l, tcp = extract('tcp.txt', 0, 1)

# turn_z, sigma_z, z = extract('sigma_z.txt', 0, 1, 2)

# losses_raw = sorted(zip(turn_l,tcp), key= lambda x:x[0])

# losses = []
# turn_ll = []
# loss = 0
# for t in range(1, turns + 1):
#     count = 0
#     for i, j in losses_raw:
#         if i == t:
#             loss += j
#             turn_ll.append(i)
#             losses.append(loss)
#         else:
#             count += 1
#         if count == len(losses_raw):
#            turn_ll.append(float(t))
#            losses.append(loss)

# ------------------------------------------------------------------------------
# Plotting
# ------------------------------------------------------------------------------
font_spec = {"font.size": 10, }
rcParams.update(font_spec)
rcParams['figure.figsize'] = 4, 2
fig = plt.figure()

# plt.plot(turn, sigma)
# plt.xlabel('Turns')
# plt.ylabel(r'Displacement ($\sigma$)')


# plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
# plt.savefig('sigma.png', dpi=1000)
# plt.savefig('sigma.eps', format='eps', dpi=1000)
# plt.clf()


plt.plot(turn_t, tilt)
plt.xlabel('Turns')
plt.ylabel(r'Crossing angle ($\mu$rad)')


plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
plt.savefig('tilt.png', dpi=1000)
plt.savefig('tilt.eps', format='eps', dpi=1000)
plt.clf()

# plt.bar(turn_ll, losses, align='center')
# plt.xlabel('Turns')
# plt.ylabel(r'Particles Lost in the TCP (%)')
# plt.xlim([0, turns])


# plt.subplots_adjust(left=0.16, bottom=0.19, right=0.94, top=0.88)
# plt.savefig('tcp.png', dpi=1000)
# plt.savefig('tcp.eps', format='eps', dpi=1000)
# plt.clf()
# counter = 0
# for t in range(1, turns + 1):
#     x = []
#     y = []
#     for i, j, k in zip(turn_z, sigma_z, z):
#         if t == i:
#             x.append(k)
#             y.append(j)
#     for p in y:
#         if p >= 5.7:
#             counter += 1
#     print t, round(counter*100/19968.0,2)
#     plot_2d_hist(x, y, 50)
#     plt.ylim([0,18])
#     plt.xlim([-0.3,0.3])
#     plt.xlabel('z (m)')
#     plt.ylabel(r'$\Delta \sigma_y$')
#     plt.axhline(y=5.7, linewidth=0.7, color='black')
#     plt.suptitle('    Turn {}'.format(t), fontsize=8, fontweight='bold')
#     plt.savefig('sigmay_z_{:02d}.png'.format(t), dpi=1000)
#     plt.clf()