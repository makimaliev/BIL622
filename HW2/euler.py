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
	return (y+x)**2

def y(x):
	return np.tan(x)-x

vx,vy = euler(f, 0, 0, 0.5, 5)

yx = []
for v in vx:
	yx.append(y(v))

dummy, w = euler(f, 0, 0, 0.5, 5)
error_abs = lambda y, w: np.sum(np.abs(y - w))
err = error_abs(yx, w)
print err

for x, y in list(zip(vx, vy))[::1]:
    print("%4.1f %10.16f" % (x, y))
plt.plot(vx, vy, label='approximation')
plt.plot( vx, yx, linestyle='--',label='exact' )
plt.title( "Approximate solution of equation with Euler's method")
plt.xlabel('Value of x') 
plt.ylabel('Value of y')
plt.legend(loc=4)
plt.grid()
plt.savefig( '1_1.eps', fmt='EPS', dpi=100 )
plt.show()
