# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:14:38 2020

@author: Marcos J Ribeiro

"""
# Martin - cap 15



def cor():
    return print('\033[1;033m')


cor()
print("{:*^80s}".format("KALMAN FILTER")) 



import numpy as np

y = np.array([-0.680, 0.67, 0.012, -0.39, -1.477])

def par():
    global lamb, phi, sigma_u, sigma_n
    lamb= 1
    phi = 0.8
    sigma_u = 0.5**2
    sigma_n =  1
    


par()




n = len(y)

s = np.zeros(n+1)
p =  np.zeros(n+1)

p[0] = 1/(1-phi**2)
p

mu = np.zeros(n)
v = np.zeros(n)


s_up = np.zeros(n)
p_up = np.zeros(n)


 

for i in range(n):
    #observation
    
    mu[i] = lamb * s[i]
    v[i]  = lamb**2 * p[i] + sigma_u 
    
    #updating
    
    s_up[i] = s[i] + (lamb*p[i])/v[i] *(y[i]-mu[i])
    p_up[i] = p[i] - (lamb**2*p[i]**2)/v[i]

    #prediction
    
    s[i+1] = phi*s_up[i] 
    p[i+1] = phi**2*p_up[i] + 1
    
    
    
# Resultado
    
from time import sleep as slp

cor()
print("{:*^40s}".format("KALMAN FILTER")) 
print('-='*20)
print('S_t|t-1 {:>30}'.format('P_t|t-1'))
print('-='*20)
for i in range(len(s)):  
    #slp(1)      
    print(f'{s[i]:.<31.4f} {p[i]:.4f}')
print('*'*40)
 



# dicas de prints ver: https://www.geeksforgeeks.org/python-format-function/















    
    
    
    
    
    
    