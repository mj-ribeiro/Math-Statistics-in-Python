# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:47:58 2020

@author: Marcos J Ribeiro
"""

#----------------  HODRICK PRESCOT FILTER


import matplotlib.pyplot as plt
import numpy as np



# F matrix
            

x = np.zeros((24, 24), dtype=np.int)
for i, v in enumerate((1,-4,6,-4,1)):
    np.fill_diagonal(x[2:,i:], v)




x[0: 1, 0:3 ] = [1, -2, 1]
x[1: 2, 0:4 ] = [ -2,	5,	-4,	1] 
x[22:23, 20:24] = [1, -4, 5, -2]
x[23:24, 21:24] =  [1, -2, 1 ]


# y matrix

y = np.array([97051.10, 96289, 95142, 94531.1, 94658.8, 
              94231.5, 92569.7, 92450.2, 90496.1, 89392.3,
              87682.5, 88809.0,88244.4, 86276.7, 86262.4,
              84917,84985.7,82437.3,80183, 82053.8, 77734.9,
              71863, 72241.2, 69227.1])


F = x
    
I = np.identity(24)

lamb = 1600



#--- calculate trend


T = np.dot(np.linalg.inv((lamb*F + I)), y)


# calculate cycle

C = y - T


#--------------- graph

fig, ax = plt.subplots(1,2, figsize=(16,8))
ax[0].plot(y, label='PIB')
ax[0].plot(T, label='Trend')
ax[0].legend()
ax[1].plot(C,'b--', label='Cycle' )
ax[1].legend()














