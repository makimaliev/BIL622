import numpy as np
from math import tan
from matplotlib import pyplot as plt

def mod_euler( f, x0, y0, x1, n):
	h = (x1-x0)/float(n)
	t = np.arange(x0, x1+h, h )
	w = np.zeros((n+1,))
	t[0] = x0
	w[0] = y0
	for i in range(1,n+1):              # apply Modified Euler Method
		f1 = f( t[i-1], w[i-1] )
		f2 = f( t[i], w[i-1] + h * f1 )
		w[i] = w[i-1] + h * ( f1 + f2 ) / 2.0
		t[i] = x0 + i * h
	return t,w

def f(x, y):
	return (1+y)/tan(x)

vx,vy = mod_euler(f, 1.0, 1, 10, 10)
for x, y in list(zip(vx, vy))[::1]:
    print("%4.1f %10.16f" % (x, y))
plt.plot(vx, vy, label='approximation' )
#plt.plot( t, y(t), label='exact' )
plt.title( "Approximate solution of equation with Modified Euler method 1")
plt.xlabel('Value of x') 
plt.ylabel('Value of y')
plt.legend(loc=4)
plt.grid()
plt.savefig( '5_1.eps', fmt='EPS', dpi=100 )
plt.show()
