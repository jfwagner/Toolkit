from numpy import *
from util import *

xf, yf = get_columns("init_dist_1.txt", 0, 2, "float")

x = asarray(xf)
y = asarray(yf)

beta = 0.15
gamma_rel = 7460.52
beta_rel = 0.999999991

print " "
print "Checking that the initial distribution has been correctly generated"
print " "

print "----------------------------------------- "
print "X COORDINATE"
print "----------------------------------------- "
if x.size == 6400:
    print "Array size for x coordinate is correct", x.size
else:
    print "Array size is", x.size
print "Geometrical emittance [m]: ",  std(x)**2/beta
print "Normalized emittance [m]: ", (std(x)**2/beta)*beta_rel*gamma_rel
print "Sigma x:", std(x)
print " "

print "----------------------------------------- "
print "Y COORDINATE"
print "----------------------------------------- "
if y.size == 6400:
    print "Array size for y coordinate is correct", y.size
else:
    print "Array size is", y.size
print "Geometrical emittance [m]: ",  std(y)**2/beta
print "Normalized emittance [m]: ", (std(y)**2/beta)*beta_rel*gamma_rel
print "Sigma y:", std(y)
print " "
