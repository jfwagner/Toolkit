import subprocess
from plot_distributions import plot

infile = "dump_ip1.txt"
# line = subprocess.check_output(["tail", "-1", infile])
# value = line.strip("\n").split()

# last_turn = int(value[1]) + 1

# last = int(value[1])

last_turn = 50

for n in range(1, last_turn):
    plot(infile, "y", "yp", 30, n)

for n in range(1, last_turn):
    plot(infile, "x", "xp", 30, n)

for n in range(1, last_turn):
    plot(infile, "z", "y", 30, n)