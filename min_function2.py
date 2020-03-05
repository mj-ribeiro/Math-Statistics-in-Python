# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:46:53 2020

@author: Marcos J Ribeiro
"""

import scipy.optimize as sp
import numpy as np
import matplotlib.pyplot as plt



def f(x):
    return x**2 + x - 3
    


def c1(x):
    return f(x) - 0     


cons = {'type':'ineq', 'fun':c1}
    



x0 = 100

sol = sp.minimize(f, x0, method='SLSQP', constraints=cons)
sol



sol.fun
sol.x


x = np.arange(-50, 50, 0.1)

a = list(map(f, x))



fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(a)





















