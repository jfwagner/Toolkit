from collections import Counter

from numpy import loadtxt

def build_centroid(data, turn, element):
    accumulated_x = data[turn][element]['accumulated']['x']
    accumulated_y = data[turn][element]['accumulated']['y']
    accumulated_z = data[turn][element]['accumulated']['z']
    total = data[turn][element]['accumulated']['total']
    centroid_x = mean() # TODO  
    centroid_y = 0 # TODO
    data[turn][element]['centroid']['x'] = centroid_x
    data[turn][element]['centroid']['y'] = centroid_y
    del data[turn][element]['accumulated']

infile = 'whatever'
data = {}
old_element = None
with open(infile) as f:
    line = f.readline()
    columns = loadtxt(line)
    turn = columns[0]
    element = columns[1]
    # check if finished processing element
    if old_element is not None and old_element != element:
        build_centroid(data, old_turn, old_element)
    x = column[2]
    y = column[3]
    z = column[4]
    if turn not in data:
        data[turn] = {}
    if element not in data[turn]:
        data[turn][element] = {'accumulated': Counter()}
    data[turn][element]['x'] += x
    data[turn][element]['y'] += y
    data[turn][element]['z'] += z
    data[turn][element]['total'] += 1
    old_turn = turn
    old_element = element

# TODO: do shit with data
# print data[1][26000]['centroid']['x']
# print data[1][26000]['centroid']['y']

# iterate data
for turn, elements in data:
    print turn
    for element, values in elements:
        print element, values['centroid']['x'], values['centroid']['y'] 

# Data structure before building centroid
# {1:
#     {
#         26000: 
#             {
#                 'x': 3423243,
#                 'y': 3423243,
#                 'z': 3423243,
#                 'total'
#             },
#         35000:
#             {

#             }
#     }
# }