import numpy as np
import matplotlib.pyplot as plt

#Make intersecting data:
xmax = 10.0
N1 = 11
h1 = xmax/float(N1-1)
N2 = 21
h2 = xmax/float(N2-1)
print "xmax =", xmax
print "N1   =", N1
print "N2   =", N2
print "h1   =", h1
print "h2   =", h2
X1 = np.linspace(0,xmax,N1)
X2 = np.linspace(0,xmax,N2)
#... scramble the X'es:
X1 = X1+np.random.normal(loc=0.0,scale=0.1*h1,size=N1)
X2 = X2+np.random.normal(loc=0.0,scale=0.1*h2,size=N2)
#... Y-values
Y1 = np.sin(X1)
Y2 = np.cos(X2)

#Add torture points
# X1 = list(X1)
# X2 = list(X2)
# Y1 = list(Y1)
# Y2 = list(Y2)
# X1.append(12.0)
# Y1.append(0.0)
# X2.append(12.0)
# Y2.append(0.0)

# #May comment out for identical lines
# # X1.append(12.5)
# # Y1.append(+0.5)
# # X2.append(12.5)
# # Y2.append(-0.5)

# X1.append(13.0)
# Y1.append(0.0)
# X2.append(13.0)
# Y2.append(0.0)

# #May comment out for identical endpoints
# #X1.append(14.0)
# #Y1.append(1.0)
# #X2.append(14.0)
# #Y2.append(-1.0)
# X1.append(15.0)
# Y1.append(0.0)
# X2.append(15.0)
# Y2.append(0.0)

# X1 = np.array(X1)
# X2 = np.array(X2)
# Y1 = np.array(Y1)
# Y2 = np.array(Y2)

print "X1=",X1
print "Y1=",Y1
print "X2=",X2
print "Y2=",Y2

#Find the intersections (simple and probably inefficient method):
Xint = [] #intersection X
Yint = [] #intersection Y
Iint = [] #Index in (X1,Y1)-array
Jint = [] #Index in (X2,Y2)-array
for i in xrange(len(X1)-1): #Loop over all X1/Y1-segments
    print "i=",i
    assert X1[i+1] > X1[i]  #strictly growing, never equal
    a1 = (Y1[i+1]-Y1[i])/(X1[i+1]-X1[i])
    b1 = Y1[i]-X1[i]*a1
    for j in xrange(len(X2)-1): #Loop over all X2/Y2-segments
        print "  j=",j
        assert X2[j+1] != X2[j]

        #Special case: endpoints intersect
        if X1[i] == X2[j] and Y1[i]==Y2[j]:
            print "SPECIAL:", X1[i], Y1[i]
            Xint.append(X1[i])
            Yint.append(Y1[i])
            Iint.append(i)
            Jint.append(j)
            continue
            
        a2 = (Y2[j+1]-Y2[j])/(X2[j+1]-X2[j])
        b2 = Y2[j]-X2[j]*a2
        
        if a1==a2:
            #Parallel lines don't intersect
            # (here may be dragons if they are the same...)
            if b1==b2:
                print "WARNING!"
            continue
            
        #Intersection point    
        X = (b2-b1)/(a1-a2)
        Y = a2*X + b2
        
        #Should be between the endpoints of both line segments
        if X > X1[i] and X < X1[i+1] and X > X2[j] and X < X2[j+1]:
            print "FOUND:",X,Y
            Xint.append(X)
            Yint.append(Y)
            Iint.append(i)
            Jint.append(j)

# #Remove double entries due to accepting both endpoints
# if len(Xint) > 0:
#     Xint2 = [Xint[0]]
#     Yint2 = [Yint[0]]
#     Iint2 = [Iint[0]]
#     Jint2 = [Jint[0]]
    
#     i = 0
#     for (X,Y,I,J) in zip(Xint,Yint,Iint,Jint):
#         if i == 0:
#             i = i+1
#             continue
            
#         if X == Xint2[-1]:
#             #Skip if two are the same

#             # This assert might be wrong, 
#             # roundoff errors can cause the calculated
#             # Y-intersections to be *slightly* different
#             assert Yint2[-1] == Y
            
#             continue
#         Xint2.append(X)
#         Yint2.append(Y)
#         Iint2.append(I)
#         Jint2.append(J)
#         i = i+1

#     Xint = Xint2
#     Yint = Yint2
#     Iint = Iint2
#     Jint = Jint2

#Done!
print "Xint =", Xint
print "Yint =", Yint
print "Iint =", Iint
print "Jint =", Jint

#Plot curves and intersections
plt.figure(1)
plt.plot(X1,Y1,'+-')
plt.plot(X2,Y2,'*-')
plt.plot(Xint,Yint,'ro')

#plt.show()
print
print

#Create sub-curves (only for X1/Y1):
plt.figure(2)
plt.plot(X1,Y1,"--o")
plt.plot(X2,Y2,"--")
i = 0
for X,Y in zip(X1,Y1):
    plt.annotate(str(i),xy=(X,Y),xytext=(0,0),textcoords='offset points')
    i = i+1
X1sub = []
Y1sub = []
Xprev = X1[0]
Yprev = Y1[0]
Iprev = 0
for (I,intX,intY) in zip(Iint,Xint,Yint): #Loop over sub-curves of line segments & the corresponding intersection points
    print "I=",I, "Iprev=", Iprev

    X = [Xprev]
    Y = [Yprev]

    #Add intermediate points
    for j in xrange(Iprev+1,I+1):
        print "j=",j
        X.append(X1[j])
        Y.append(Y1[j])
    #Add final point
    X.append(intX)
    Y.append(intY)

    #Add to the list of subsegments
    X1sub.append(X)
    Y1sub.append(Y)

    #Prepare for next point
    Xprev = X[-1]
    Yprev = Y[-1]
    Iprev = I

    print "X_ =", X
    print "Y_ =", Y

    #plot
    plt.plot(X,Y,'+-')
#From the final intersection to the end of the curve
X = [Xprev]
Y = [Yprev]
print "I=",I, "Iprev=", Iprev, "(FINAL)"
for j in xrange(Iprev+1,len(X1)):
    print j
    X.append(X1[j])
    Y.append(Y1[j])

X1sub.append(X)
Y1sub.append(Y)
print "X_ =", X
print "Y_ =", Y
plt.plot(X,Y,'+-')

plt.show()
