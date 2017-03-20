from matplotlib import pyplot as plt
import numpy as np

#	y"=f(x,y,y')
#	Create two differential equations
#	y'=u
#	u'=f(x,y,u)

#	Example
#	(x^2+1)y"-2xy'=0; y(0)=1;y'(0)=3

#	y"=2xy'/(x^2+1) or the f(x,y,y')
#	u'=2xu/(x^2+1) or the f(x,y,u)

x = 0.0
y = 1.0
u = 3.0

h = 0.2
vx=[]
vy=[]

print "x   ", "y"
print("%4.1f %10.16f" % (x, y))

while(x<1.0):
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
	vx.append(x)
	vy.append(y)

def y(x):
	return -x**3+3*x+1

yx = []
for v in vx:
	yx.append(y(v))

def error_abs(v,w):
	total_err = 0
	for i in range(0,len(v)):
		total_err = total_err + np.abs(v[i]-w[i]) 
	return total_err

for x, y in list(zip(vx, vy))[::1]:
    print("%4.1f %10.16f" % (x, y))
plt.plot(vx, vy, label='approximation' )
plt.plot( vx, yx, linestyle='--',label='exact' )
plt.title( "Approximate solution of equation with Runge-Kutta method 4")
plt.xlabel('Value of x') 
plt.ylabel('Value of y')
plt.legend(loc=4)
plt.grid()
plt.savefig( '1_1.eps', fmt='EPS', dpi=100 )
plt.show()

err = error_abs(yx, vy)
print err
