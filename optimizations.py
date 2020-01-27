# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:20:14 2020

@author: Marcos Ribeiro
"""


import numpy as np 


#------------------- Econometric Modelling with Time Series Specification, Estimation and Testing:
#                                               Charpter 3


#------------------- Exponential distribution


#--------- Simulation using Newthon Rhapson


y = [3.5, 1, 1.5]

theta, tol = 1, 0.00001
g = -1/theta + 2/theta**2   # gradient

while g > tol:
    g = -1/theta + np.mean(y)/theta**2
    h = 1/theta**2 - 4/theta**3   # hessian
    theta = theta - g/h
    print('\033[1;033mtheta =', theta)
    


#--------- Simulation using Method Scoring
    
    

y = [3.5, 1, 1.5]

theta, tol = 1, 0.00001
g = -1/theta + 2/theta**2


while g>tol:
    g = -1/theta + np.mean(y)/theta**2
    i = 1/theta**2
    theta = theta + g/i
    print('\033[1;033mtheta=', theta)



#----------------------------- Simulation using BHHH
    
    
import time as tm

y = [3.5, 1, 1.5]
   
theta, tol = 1, 0.000001
g = -1/theta + 2/theta**2

n = len(y)    


c = 0
while g > tol:
    g = -1/theta + 2/theta**2

    for i in y:
        j += 1/n*(-1/theta + i/theta**2)**2    
        #print(j)
        
    theta = theta + g/j
    tm.sleep(2)
    print('\033[1;033mtheta = ', theta)
    c += 1
    
## BHHH demora mais convergir
    
     
    
#----------------------- Weibull distribution with NR   
    
    
from math import log as ln    
    
y_1 = [ 0.293, 0.589, 1.374, 0.954, 0.608, 1.199, 1.464, 0.383, 1.743, 0.022,
0.719, 0.949, 1.888, 0.754, 0.873, 0.515, 1.049, 1.506, 1.090, 1.644]
    


theta = np.array([[0.5], 
                  [1.5]])


def quad(x):
    return x**theta[1,0]


def quad2(x):
    return x**theta[1,0]*ln(x)


def quad3(x):
    return x**theta[1,0]*ln(x)**2

def quad4(x):
    return ln(x)

       
n = len(y_1)

def compute_g():
    return np.array([[1/theta[0,0] - 1/n*np.sum(list(map(quad,y_1))) ],
            [1/theta[1,0] + 1/n*np.sum(np.log(y_1)) - theta[0,0]/n*np.sum(list(map(quad2,y_1)))]])

    
def compute_h():    
    return np.array([[-1/theta[0,0]**2, -1/n*np.sum(list(map(quad2,y_1)))], 
    [-1/n*np.sum(list(map(quad2,y_1))), -1/theta[1,0]**2 - theta[0,0]/n*np.sum(list(map(quad3, y_1)))]])

    
tol = 1e-30


g = compute_g() 

def compute_Lt():
    return np.log(theta[0,0]) + np.log(theta[1,0]) + (theta[1,0] - 1 )*1/n* np.sum(list(map(quad4, y_1))) - theta[0,0]/n*np.sum(list(map(quad, y_1)))         


#---------------------------- OPTIMIZATION

while (g > tol).all():    
    g = compute_g()
    h = compute_h()
    theta = theta - np.dot(np.linalg.inv(h), g)
    L_t = compute_Lt()
    print('\033[1;033mtheta =', theta)
    print('L_t = ', L_t)





                                                                    
               







    
    
    
    
    
    
    
    
    