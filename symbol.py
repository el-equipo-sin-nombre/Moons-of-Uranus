#!/usr/bin/env python3

from sympy import *

x = Symbol("x")

formulae = 'x^3+1.0+sin(x)/x + exp(1/x)'
y = sympify(formulae)

velocity = y.diff(x)
acceleration = velocity.diff(x)

#print(y)
#print(yprime)

f = lambdify(x,acceleration, "numpy")
#f1 = lambdify(x,yprime, "numpy")

x0 = 1.5
y0 = f(x0)
#y1 = f1(x0)
print(y0)
