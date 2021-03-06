from numpy import *

# ----------
# CONSTANTS
# ----------
beta = 0.15 # [m]
c = 299792458 # [m/s]
n = 4 # integer
E = 7e12 # [eV]
omega = (400.79e6)*2*pi # [rad/s]
theta = 590e-6/2 # [rad]

# --------------------------------
# CRAB UPSTREAM: OPENING THE BUMP
# --------------------------------
print "------------------------------"
print "UPSTREAM: CRAB1"
print "------------------------------"

# Position
# ---------
s1 = zeros(4)
s1[0] = 26494.25920
s1[1] = 26495.30920
s1[2] = 26500.85920
s1[3] = 26501.90920

print "Positions (m)"
print s1
print " "

# Beta functions (vertical)
# --------------------------
b1 = zeros(4)
b1[0] = 2791.594664
b1[1] = 2888.919979
b1[2] = 3431.069503
b1[3] = 3538.881847

# Alpha functions (vertical)
# ---------------------------
a1 = zeros(4)
a1[0] = -45.9481519
a1[1] = -46.7426238
a1[2] = -50.9419753
a1[3] = -51.7364472

# Phase advance
# -------------
p1 = zeros(4)
p1[0] = abs(60.0678167 - 60.3200491)*2*pi
p1[1] = abs(60.0678755 - 60.3200491)*2*pi
p1[2] = abs(60.0681560 - 60.3200491)*2*pi
p1[3] = abs(60.0682039 - 60.3200491)*2*pi

print "Phase advances (deg)"
print p1*(360/(2*pi))
print " "

# Initialize voltage array
# -------------------------
V1 = zeros(4)

# Calculate the voltage
# ---------------------
V1 = (c*E*tan(theta)*10**(-6))/(omega*sqrt(beta*b1)*sin(p1)*n)
print "Voltages (MV)"
print V1
print " "

# ---------------------------------
# CRAB DOWNSTREAM: CLOSING THE BUMP
# ---------------------------------
print "------------------------------"
print "DOWNSTREAM: CRAB2"
print "------------------------------"
# Position
#---------
s2 = zeros(4)
s2[0] = 153.57400
s2[1] = 154.62400
s2[2] = 160.17400
s2[3] = 161.22400

print "Positions (m)"
print s2
print " "

# Beta functions (vertical)
#--------------------------
b2 = zeros(4)
b2[0] = 3794.802841
b2[1] = 3754.402506
b2[2] = 3544.459277
b2[3] = 3505.421633

# Alpha functions (vertical)
#---------------------------
a2 = zeros(4)
a2[0] = 19.2898718
a2[1] = 19.1866376
a2[2] = 18.6409712
a2[3] = 18.5377370

# Phase advance
# -------------
p2 = zeros(4)
p2[0] = (0.2521059)*2*pi
p2[1] = (0.2521502)*2*pi
p2[2] = (0.2523922)*2*pi
p2[3] = (0.2524396)*2*pi

print "Phase advances (deg)"
print p2*(360/(2*pi))
print " "

# Phase advance between cavities
# ------------------------------
p = zeros(4)
p = deg2rad(p1 + p2)
print sin(p)

# Initialize voltage array
#-------------------------
V2 = zeros(4)

# Calculate the voltage
# ---------------------
V2 = sqrt(b1/b2)*(cos(p))*V1
print "Voltages (MV)"
print V2
