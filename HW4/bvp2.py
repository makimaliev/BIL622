#	y''+ (x-1)y'+ 3.125y = 4x$\\
#	y(0) = 1
#	y(1) = 1.368
#	y1' = y2
#	y2' = 4x-(x-1)y2 - 3.125y1


#	x^2*y''-x*y' = 3*x^3
#	y(1) = 2
#	y(2) = 9
#	y1' = y2
#	y2' = 4x-(x-1)y2 - 3.125y1



import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def fun(x, y, p):
	x = p[0]
	return np.vstack((y[1], 4*x-(x-1)*y[1] - 3.125*y[0]))

def bc(ya, yb, p):
	k = p[0]
	return np.array([ya[0], yb[0], ya[1] - k])

x = np.linspace(0, 1, 5)
y = np.zeros((2, x.size))
y[0, 1] = 1
y[0, 3] = 1.3

sol = solve_bvp(fun, bc, x, y, p=[5])
print sol.p[0]

x_plot = np.linspace(0, 1, 100)
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
#plt.savefig( '1_2.eps', fmt='EPS', dpi=100 )
plt.show()
