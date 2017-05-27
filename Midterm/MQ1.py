#  Solves a Cauchy problem for a 2nd order ODE by Euler's method
#		y" + 1/5y'+3.125y = 0, y(0) = 0, y'(0) = 1
#  Equivalent problem: y[1] = y, y[2] = y'
#     y[1]' =  y[2],   y[1](0) = 0
#     y[2]' = -3.125y[1]-1/5y[2],   y[2](0) = 1
#----------------------------------------------------------------------------
from math import *
from ode import *
from matplotlib import pyplot as plt

def Func(t, y, f):                                 # Right-hand sides of ODEs
	f[1] =  y[2]
	f[2] = -3.125*y[1]-1/5*y[2]

# main

y0 = 0; dy0 = 1                         # initial values => y(t) = sin(t)
tmax = 10e0                                                      # time span
ht = 0.1e0                                                       # step size

n = 2                                              # number of 1st order ODEs
nt = int(tmax/ht + 0.5) + 1                            # number of time steps
y = [0]*(n+1)                                           # solution components

out = open("ode.txt","w")                                  # open output file
out.write("      t         y1        y2\n")

t = 0e0
y_1 = []
y_2 = []

y[1] = y0; y[2] = dy0                                        # initial values
out.write(("{0:10.5f}{1:10.5f}{2:10.5f}\n"). \
          format(t,y[1],y[2]))

y_1.append(y[1])
y_2.append(y[2])

while (t+ht <= tmax):                                      # propagation loop
   Euler(t,ht,y,n,Func)
   t += ht
	
   y_1.append(y[1])
   y_2.append(y[2])

   out.write(("{0:10.5f}{1:10.5f}{2:10.5f}\n"). \
             format(t,y[1],y[2]))
out.close()

plt.plot(y_1, y_2)
plt.title( "Euler method")
plt.xlabel('Value of y[1]') 
plt.ylabel('Value of y[2]')
plt.legend(loc=4)
plt.grid()
plt.savefig( '1_1.eps', fmt='EPS', dpi=100 )
plt.show()
