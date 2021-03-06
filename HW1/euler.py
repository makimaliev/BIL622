import numpy as np
from matplotlib import pyplot as plt

def euler( f, x0, y0, x1, n):
	# determine step-size
	h = (x1-x0)/float(n)  
	# create mesh                         
	t = np.arange(x0, x1+h, h )
	# initialize w               
	w = np.zeros((n+1,))
	# set initial values                     
	t[0] = x0
	w[0] = y0   
	# apply Euler's method                       
	for i in range(1,n+1):                       
		w[i] = w[i-1] + h * f(t[i-1], w[i-1])
		t[i] = x0 + i * h
	return t,w

def f(x,y):
	return (y**2-y)/x**2
	#return (x*y**2+x)/(y-x**2*y)

vx,vy = euler(f, 1, 0, 10, 10)
for x, y in list(zip(vx, vy))[::1]:
    print("%4.1f %10.16f" % (x, y))
plt.plot(vx, vy, label='approximation' )
plt.title( "Euler's Method Example")
plt.xlabel('Value of x') 
plt.ylabel('Value of y')
plt.legend(loc=4)
plt.grid()
plt.savefig( '1_1.eps', fmt='EPS', dpi=100 )
plt.show()
