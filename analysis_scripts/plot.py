import subprocess
from plot_distributions import plot
from plot_absorptions import plot_losses

plot_losses('data/tot_absorptions.dat', 'data/tot_aperture.dat')

infile = "../../sixtrack/dump.txt"
line = subprocess.check_output(["tail", "-1", infile])
value = line.strip("\n").split()

last_turn = int(value[1]) + 1

last = int(value[1])

for n in range(1, last_turn):
    plot(infile, "y", "yp", 30, n)

