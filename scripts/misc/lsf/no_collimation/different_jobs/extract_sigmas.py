from util import GetData

get = GetData('data.txt')
# Turn 6, 8, 15

def get_tau(tau):
    data = get.data_column(column=0, regex=tau)
    return data[0], data[1], data[2], data[8]

tau_1, phase_1, turn_1, sigy_1 = get_tau(r'1')
tau_2, phase_2, turn_2, sigy_2 = get_tau(r'2')
tau_3, phase_3, turn_3, sigy_3 = get_tau(r'3')
tau_4, phase_4, turn_4, sigy_4 = get_tau(r'4')

max_1 = '217'
max_2 = '359'
max_3 = '359'
max_4 = '359'

for tau, phase, turn, sigy in zip(tau_1, phase_1, turn_1, sigy_1):
    if int(turn) == 1:
        offset = sigy
    if phase == max_1 and turn == '6':
        print float(sigy) - float(offset), tau, phase
    if phase == max_1 and turn == '8':
        print float(sigy) - float(offset), tau, phase
    if phase == max_1 and turn == '10':
        print float(sigy) - float(offset), tau, phase


for tau, phase, turn, sigy in zip(tau_2, phase_2, turn_2, sigy_2):
    if int(turn) == 1:
        offset = sigy
    if phase == max_2 and turn == '6':
        print float(sigy) - float(offset), tau, phase
    if phase == max_2 and turn == '8':
        print float(sigy) - float(offset), tau, phase
    if phase == max_2 and turn == '10':
        print float(sigy) - float(offset), tau, phase


for tau, phase, turn, sigy in zip(tau_3, phase_3, turn_3, sigy_3):
    if int(turn) == 1:
        offset = sigy
    if phase == max_3 and turn == '6':
        print float(sigy) - float(offset), tau, phase
    if phase == max_3 and turn == '8':
        print float(sigy) - float(offset), tau, phase
    if phase == max_3 and turn == '10':
        print float(sigy) - float(offset), tau, phase

for tau, phase, turn, sigy in zip(tau_4, phase_4, turn_4, sigy_4):
    if int(turn) == 1:
        offset = sigy
    if phase == max_4 and turn == '6':
        print float(sigy) - float(offset), tau, phase
    if phase == max_4 and turn == '8':
        print float(sigy) - float(offset), tau, phase
    if phase == max_4 and turn == '10':
        print float(sigy) - float(offset), tau, phase


# print phase_1
# print type(max_1)