#  Solves a Cauchy problem for a 2nd order ODE by Euler's method
#     y" + y = 0,   y(0) = y0, y'(0) = y0'
#		y" + 1/5y'+3.125y = 0, y(0) = 0, y'(0) = 1
#  Equivalent problem: y[1] = y, y[2] = y'
#     y[1]' =  y[2],   y[1](0) = 0
#     y[2]' = -3.125y[1]-1/5y[2],   y[2](0) = 1
#----------------------------------------------------------------------------
from math import *
from ode import *
#from matplotlib import pyplot as plt
from graphlib import *

def Func(t, y, f):                                 # Right-hand sides of ODEs
	f[1] =  y[2]
	f[2] = -3.125*y[1]-1/5*y[2]

# main

y0 = 0; dy0 = 1                         # initial values => y(t) = sin(t)
tmax = 100e0                                                      # time span
ht = 0.05e0                                                       # step size

n = 2                                              # number of 1st order ODEs
nt = int(tmax/ht + 0.5) + 1                            # number of time steps
y = [0]*(n+1)                                           # solution components

out = open("ode.txt","w")                                  # open output file
out.write("      t         y1        y2      check\n")

t = 0e0
y[1] = y0; y[2] = dy0                                        # initial values
out.write(("{0:10.5f}{1:10.5f}{2:10.5f}{3:10.5f}\n"). \
          format(t,y[1],y[2],y[1]*y[1]+y[2]*y[2]))

while (t+ht <= tmax):                                      # propagation loop
   Euler(t,ht,y,n,Func)
   t += ht

   out.write(("{0:10.5f}{1:10.5f}{2:10.5f}{3:10.5f}\n"). \
             format(t,y[1],y[2],y[1]*y[1]+y[2]*y[2]))
out.close()

Plot(y1,y2,nt,"red",2,0.10,0.45,0.15,0.85,"y","y'","Euler method")
