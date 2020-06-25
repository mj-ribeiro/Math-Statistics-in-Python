# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:48:20 2020

@author: Marcos J Ribeiro
"""
from scipy import optimize 

#------ Scipy


def f(X):
    return -X[0] * X[1] * X[2]


def g(X):
    return 2 * (X[0]*X[1] + X[1] * X[2] + X[2] * X[0]) - 1


constraint = dict(type='eq', fun=g)
result = optimize.minimize(f, [0.5, 1, 1.5], 
                           method='SLSQP',
                           constraints=[constraint])


help(ipopt)
###### PyOpt


import ipopt



dic = {'am': '\033[1;033m'}



print('{} olá mundo '.format(dic['am']))




v = [1, 2, 4]

list(map(lambda x: x**2, v))


from numba import vectorize

@vectorize
def vec(x):
    return x**2


v = np.array((1, 2, 4, 200))

vec(v)



