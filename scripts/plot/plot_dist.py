from plot_distributions import plot

infile = "dump_ip1.txt"
last_turn = 50

for n in range(1, last_turn):
    plot(infile, "y", "yp", 30, n)

for n in range(1, last_turn):
    plot(infile, "x", "xp", 30, n)

for n in range(1, last_turn):
    plot(infile, "z", "y", 30, n)