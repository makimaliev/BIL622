from math import sqrt
from math import tan
from matplotlib import pyplot as plt
 
def rk4(x, y, u, n, h):
	while(x<n):
		m1 = u
		k1 = 2*x*u/(x**2+1)
		m2 = u + (h/2.)*k1
		x_2 = x + (h/2.)
		y_2 = y + (h/2.)+m1
		u_2 = m2
		k2 = 2*x_2*u_2/(x_2**2+1)
		m3 = u + (h/2.)*k2
		x_3 = x + (h/2.)
		y_3 = y + (h/2.) * m2
		u_3 = m3
		k3 = 2*x_3*u_3/(x_3**2+1)
		m4 = u + h * k3
		x_4 = x+h
		y_4 = x+h*m3
		u_4 = m4
		k4 = 2*x_4*u_4/(x_4**2+1)
		x = x + h
		y = y + (h/6.)*(m1+(2.*m2)+(2.*m3) + m4)
		u = u + (h/6.)*(k1+(2.*k2)+(2.*k3) + k4)
		print x,y
		return x,y
 
def y(x):
	return -x**3+3*x+1

vx,vy = rk4(0.0,1.0,3.0,1.0,0.2)
print vx, vy

#for x, y in list(zip(vx, vy))[::1]:
    #print("%4.1f %10.16f" % (x, y))
plt.plot(vx, vy, label='approximation' )
plt.plot( vx, y(vx), linestyle='--',label='exact' )
plt.title( "Approximate solution of equation with Runge-Kutta method 4")
plt.xlabel('Value of x') 
plt.ylabel('Value of y')
plt.legend(loc=4)
plt.grid()
plt.savefig( '1_1.eps', fmt='EPS', dpi=100 )
plt.show()
