from math import sqrt
from matplotlib import pyplot as plt
 
def rk4(f, x0, y0, x1, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + h, y - k1 + 2 * k2)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + 4 * k2 + k3) / 6
    return vx, vy
 
def f(x,y):
	return (1-2*x)/y**2

vx,vy = rk4(f, 0, 1, 1.0, 10)
for x, y in list(zip(vx, vy))[::1]:
    print("%4.1f %10.16f" % (x, y))
plt.plot(vx, vy, label='approximation' )
plt.title( "Approximate solution of equation with Runge-Kutta method 3")
plt.xlabel('Value of x') 
plt.ylabel('Value of y')
plt.legend(loc=4)
plt.grid()
plt.savefig( '2_2.eps', fmt='EPS', dpi=100 )
plt.show()
