import os
import numpy as np

# Kicks in rad
kick_h = 1.9e-5
kick_v = 4.2e-5

# Turn info
failure_start = 9
failure_end = 11
end_turn = 50

turns = []
value_h = []
value_v = []

for i in range(1, failure_start):
    turns.append(i)
    value_h.append(0.0)
    value_v.append(0.0)

delta_t = failure_end - failure_start

if delta_t > 1:
    kick_h_t = np.linspace(0.0, kick_h, delta_t)
    kick_v_t = np.linspace(0.0, kick_v, delta_t)

t = range(failure_start, failure_end + 1)
for i, j, k in zip(t, kick_h_t, kick_v_t):
    turns.append(i)
    value_h.append(j)
    value_v.append(k)

for i in range(failure_end , end_turn + 1):
    turns.append(i)
    value_h.append(kick_h)
    value_v.append(kick_v)

outfile_h ='input_h'
outfile_v = 'input_v'

with open(outfile_h, 'w') as fh:
    with open(outfile_v, 'w') as fv:
        for i, j, k in zip(turns, value_h, value_v):
            fh.write('%.0f %.8f\n'%(i, j))
            fv.write('%.0f %.8f\n'%(i, k))
