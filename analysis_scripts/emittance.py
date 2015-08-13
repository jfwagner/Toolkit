from numpy import *
from util import *

infile = "sixtrack/dump_ip1.txt"

total_turns = 10
    
term_1_x = zeros(total_turns)
term_2_x = zeros(total_turns)
term_3_x = zeros(total_turns)
term_4_x = zeros(total_turns)

term_1_y = zeros(total_turns)
term_2_y = zeros(total_turns)
term_3_y = zeros(total_turns)
term_4_y = zeros(total_turns)

det_x = zeros(total_turns)
em_x = zeros(total_turns)

det_y = zeros(total_turns)
em_y = zeros(total_turns)

for turn in range(1, total_turns + 1):
    turn_i = '%s' %turn
    x = get_dump(infile, turn_i, 3)
    xp = get_dump(infile, turn_i, 4)
    y = get_dump(infile, turn_i, 5)
    yp = get_dump(infile, turn_i, 6)

    # Sigma matrix for X
    term_1_x[turn-1] = mean(dot(x,x)) - dot(mean(x), mean(x))
    term_2_x[turn-1] = mean(dot(x,xp)) - dot(mean(x),mean(xp))
    term_3_x[turn-1] = mean(dot(xp,x)) - dot(mean(xp), mean(x))
    term_4_x[turn-1] = mean(dot(xp,xp)) - dot(mean(xp),mean(xp))

    det_x = dot(term_1_x, term_4_x) - dot(term_3_x, term_2_x)
    em_x[turn-1] = sqrt(abs(det_x))

    # Sigma matrix for Y
    term_1_y[turn-1] = mean(dot(y,y)) - dot(mean(y), mean(y))
    term_2_y[turn-1] = mean(dot(y,yp)) - dot(mean(y),mean(yp))
    term_3_y[turn-1] = mean(dot(yp,y)) - dot(mean(yp), mean(y))
    term_4_y[turn-1] = mean(dot(yp,yp)) - dot(mean(yp),mean(yp))

    det_y = dot(term_1_y, term_4_y) - dot(term_3_y, term_2_y)
    em_y[turn-1] = sqrt(abs(det_y))

print em_x
print em_y
