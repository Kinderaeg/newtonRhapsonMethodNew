from sympy import *

x = Symbol("x")
f = x**2+x-2
d = diff(f,x)
iterations = 10
x0 = -4
xn = x0
xn1 = 0


def newton(xn, fun, der, maxIter, curIter):
    xn1 = xn-fun.evalf(subs={x: xn})/d.evalf(subs={x: xn})
    print(xn1)
    if curIter <= maxIter:
        return newton(xn1, fun, der, maxIter, curIter +1)
    return xn1

