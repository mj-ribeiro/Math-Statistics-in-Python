# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:05:09 2020

@author: Marcos J Ribeiro
"""

import sympy as sp
sp.init_printing()


#----------- Define variables and functions


x = sp.Symbol('x')

y, z = sp.symbols('y, z')


f = sp.Function('f')


#------------ create a function


g = x**2+ y**4 + 2*z
g                      # see function g


h = 5*x + 3*y - z
h


#------------ evaluate the function in a point


t = 3*x**2 + 2*x + 1

t.subs(x, 2)

print(t.subs(x, 2))


h = 5*x + 3*y**2 - z**5
h
h.subs( [(x,2), (y,4), (z, 1)])  # function with more than one variable




#------------- simplify expressions


f = (x**2 - x - 6)/ (x**2 - 3*x)

f.simplify()


f = (x**2 - x)**2*(3*x - 2)**3
f.simplify()
f.expand()          # expand function f


#------------- factoring

t = 3*x**4 - 36*x**3 + 99*x**2 - 6*x - 144
t.factor()


#---------- calculus


y = (sp.sin(x))**2 * sp.exp(2*x)

z = sp.diff(y, x)  # derivative of y

z.subs(x, 3.2)




f = x**2* sp.sin(x**2)

g = sp.integrate(f, (x, 0, 5))
g.evalf()



f = x**2 + 2*x + 1
z = sp.integrate(f, (x, 1, 2))
z.evalf()

sp.plot(f)   # plot f


#------------ solve equations 


y = sp.Eq(x**3 + 15*x**2, 3*x - 10)
t = sp.solve(y)
t[0].evalf()

for s in t:
    print(s.evalf())


#------------ solve system

x, y, z = sp.symbols('x, y, z')

eq1 = sp.Eq(x + y + z, 0)
eq2 = sp.Eq(2*x - y - z, 10)
eq3 = sp.Eq( y + 2*z, 5)

sp.solve([eq1, eq2, eq3], [x, y, z])



#----------------- Solve Differential equation

f = sp.Function('f')

y = sp.dsolve(sp.Derivative(f(x), x)-x*sp.cos(x), f(x))
y

sp.integrate(x*sp.cos(x))  # same answer


#----------------- matrix algebra

# solve system Ax = b

A = sp.Matrix([[1, 2, 5], [3, 1, 6], [1, 0, 3]])

A.shape
A.det()
A.eigenvals()
A.eigenvects()


b = sp.Matrix([1, 0, -2])
b

A.inv()*b # solution





#----------------


# end




































