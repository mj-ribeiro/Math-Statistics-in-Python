# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:15:33 2020

@author: Marcos J Ribeiro
"""
################  Optimization with scipy



import numpy as np
from scipy.optimize import minimize



def f(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1*x4*(x1+x2+x3)+x3



def c1(x):
    return x[0]*x[1]*x[2]*x[3]-25



def c2(x):
    sq = 40
    for i in range(4):
        sq = sq - x[i]**2
    return sq


x0 = [1, 5, 5, 1]
print(f(x0))



b = (1.0, 5.0)
bnds = (b, b, b, b)


con1 = {'type': 'ineq', 'fun':c1}
con2 = {'type': 'eq', 'fun':c2}
cons = [con1, con2]


sol = minimize(f, x0, method='SLSQP', \
               bounds=bnds, constraints=cons)


sol.fun
sol.x









