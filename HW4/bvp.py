#!/usr/bin/env python

"""A variety of methods to solve ODE boundary value problems.

AUTHOR:
    Jonathan Senning <jonathan.senning@gordon.edu>
    Gordon College
    Based Octave functions written in the spring of 1999
    Python version: October-November 2008
"""

import numpy

#-----------------------------------------------------------------------------

def shoot( f, a, b, z1, z2, t, tol ):
    """Implements the shooting method to solve second order BVPs

    USAGE:
        y = shoot(f, a, b, z1, z2, t, tol)

    INPUT:
        f     - function dy/dt = f(y,t).  Since we are solving a second-
                order boundary-value problem that has been transformed
                into a first order system, this function should return a
                1x2 array with the first entry equal to y and the second
                entry equal to y'.
        a     - solution value at the left boundary: a = y(t[0]).
        b     - solution value at the right boundary: b = y(t[n-1]).
        z1    - first initial estimate of y'(t[0]).
        z1    - second initial estimate of y'(t[0]).
        t     - array of n time values to determine y at.
        tol   - allowable tolerance on right boundary: | b - y[n-1] | < tol

    OUTPUT:
        y     - array of solution function values corresponding to the
                values in the supplied array t.

    NOTE:
        This function assumes that the second order BVP has been converted to
        a first order system of two equations.  The secant method is used to
        refine the initial values of y' used for the initial value problems.
    """

    from diffeq import rk4

    max_iter = 25   # Maximum number of shooting iterations

    n = len( t )    # Determine the size of the arrays we will generate

    # Compute solution to first initial value problem (IVP) with y'(a) = z1.
    # Because we are using the secant method to refine our estimates of z =
    # y', we don't really need all the solution of the IVP, just the last
    # point of it -- this is saved in w1.

    y = rk4( f, [a,z1], t )
    w1 = y[n-1,0]

    print "%2d: z = %10.3e, error = %10.3e" % ( 0, z1, b - w1 )

    # Begin the main loop.  We will compute the solution of a second IVP and
    # then use the both solutions to refine our estimate of y'(a).  This
    # second solution then replaces the first and a new "second" solution is
    # generated.  This process continues until we either solve the problem to
    # within the specified tolerance or we exceed the maximum number of
    # allowable iterations.

    for i in xrange( max_iter ):

        # Solve second initial value problem, using y'(a) = z2.  We need to
        # retain the entire solution vector y since if y(t(n)) is close enough
        # to b for us to stop then the first column of y becomes our solution
        # vector.

        y = rk4( f, [a,z2], t )
        w2 = y[n-1,0]

        print "%2d: z = %10.3e, error = %10.3e" % ( i+1, z2, b - w2 )

        # Check to see if we are done...
    
        if abs( b - w2 ) < tol:
            break

        # Compute the new approximations to the initial value of the first
        # derivative.  We compute z2 using a linear fit through (z1,w1) and
        # (z2,w2) where w1 and w2 are the estimates at t=b of the initial
        # value problems solved above with y1'(a) = z1 and y2'(a) = z2.  The
        # new value for z1 is the old value of z2.

        #z1, z2 = ( z2, z1 + ( z2 - z1 ) / ( w2 - w1 ) * ( b - w1 ) )
        z1, z2 = ( z2, z2 + ( z2 - z1 ) / ( w2 - w1 ) * ( b - w2 ) )
        w1 = w2

    # All done.  Check to see if we really solved the problem, and then return
    # the solution.

    if abs( b - w2 ) >= tol:
        print "\a**** ERROR ****"
        print "Maximum number of iterations (%d) exceeded" % max_iter
        print "Returned values may not have desired accuracy"
        print "Error estimate of returned solution is %e" % ( b - w2 )

    return y[:,0]

if __name__ == "__main__":

    import math
    from pylab import *

    # Solves x'' = x + 4exp(t), x(0)=1, x(1/2) = 2exp(1/2) using the shooting method.

    # Set up interval.  We will solve the problem for both n=64 and n=128.

    a = 2
    b = 9
    n1 = 10
    #n2 = 128
    t1 = linspace( a, b, n1 )
    #t2 = linspace( a, b, n2 )

    # Compute exact solutions.  The transpose of the solution is taken because
    # both the finite difference function fd() and the shooting method function
    # shoot() return nx1 vectors rather than 1xn vectors.

    #def exact(t):
        #return exp(t) * ( 1 + 2 * t )
  
    #x1 = exact( t1 )
    #x2 = exact( t2 )

    # Compute shooting method solutions

    def f(x,t):
        return array( [x[1], (3*t**3+t*x[0])/t**2] )
  
    xs1 = shoot( f, 2, 9, 1.0, 10.0, t1, 1e-5 )
    #xs2 = shoot( f, 2, 9, 1.0, 10.0, t2, 1e-5 )

    # Prepare for display; set interactive mode to true so each plot
    # is shown as it is generated

    interactive( True )

    for p1, p2 in list(zip(t1, xs1))[::1]:
    	print("%4.1f %10.16f" % (p1, p2))

    # Plot solutions

    #plot( t1, xs1, 'ro', t2, xs2, 'b-' )
    plot( t1, xs1, 'ro')
    title( 'Shooting Method' )
    xlabel( "t" )
    ylabel( "x" )
    #legend( ( '%3d points' % n1, '%3d points' % n2 ), loc='lower right' )
    savefig( '1_2.eps', fmt='EPS', dpi=100 )
    draw()
    z = raw_input( "Press ENTER to quit..." )

