import numpy as np
import matplotlib.pyplot as plt
 
# limits: 0.0 <= t <= 2.0
a = 0.0
b = 0.9
 
# steps
N = 10
 
# step-size
h = (b-a)/N
 
# initial value: y(0.0) = 0.5
IV = (0.0,1.0)
 
# ordinary differential equation
def f( t, y ):
	 return (t*y**2+t)/(y-t**2*y)
    #return y - t**2 + 1
 
# make arrays to hold t, and y
t = np.arange( a, b+h, h )
w = np.zeros((N+1,))
 
# set the initial values
t[0], w[0] = IV
 
# apply Euler's method
for i in range(1,N+1):
    w[i] = w[i-1] + h * f( t[i-1], w[i-1] )
     
plt.plot( t, w, label='approximation' )
plt.title( "Approximate solution of equation with Euler's Method")
plt.xlabel('Value of x') 
plt.ylabel('Value of y')
plt.legend(loc=4)
plt.grid()
plt.savefig( '1.eps', fmt='EPS', dpi=100 )
