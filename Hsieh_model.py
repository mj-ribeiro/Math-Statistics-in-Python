# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:18:22 2020

@author: Marcos J Ribeiro
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt
from scipy.optimize import minimize
from math import gamma


#----------------------- Defining parameters

def par():
    global beta, eta, varphi, theta, rho, i, r, gamma1
    beta = 0.69
    eta = 0.25
    varphi = 0.25
    theta = 3.44
    rho = 0.19
    i = 2
    r = 4
    gamma1 = gamma(1 - (theta*(1 - rho)**(-1)) * (1 - eta)**(-1))


par()





phi = [0.138, 0.174]





#------------------------ h_til



def h_tilf( ):
    global h_til
    
    sf( )

    h_til = np.zeros((i, r))
    for c in range(i):
        for j in range(r):    
            h_til[c, j] = ( 1 ** varphi * s[c]**phi[c] * eta**eta )**(1 - eta)**(-1) 

    return h_til


h_tilf()



#------------------------ Agregate Human capital   (eq 21)

 

def Hf( ):
    global H, E, c1
    h_tilf( )
    
    a = 1/ theta* ( 1 - rho )
    b = 1/ ( 1 - eta )
    
    g = gamma(1 - a * b)
              
    
    H = np.zeros((i, r))
    c1 = np.zeros(i)
    E = np.zeros(i)
    
    for c in range(i):               
            
            c1[c] = ( 1/p_i[c] )**(b / eta)
            E[c] = c1[c] * g
            
            for j in range(r): 
            
                H[c, j] = p_ir[c, j]*h_til[c, j] * ( ( (1 - tau_w[c, j])/(1 + tau_h[c, j]) ) * w[c, j] ) ** (eta/(1 - eta)) * E[c]
          
    return H



Hf( )
 

#----------------------------------------- s - time spent at school   (eq 14)


def sf( ):
    global s
    s = np.zeros((i, 1))
    
    for c in range(i):
        s[c] = (1+ (1-eta)/beta*phi[c])**(-1)                        
    return s


sf()


#----------------------------------------- w tilde


def w_tilf( ):
    global w_til
    
    w_til = np.ones((i, r))
    
    for c in range(i):
        for j in range(r):
            w_til[c, j] = ( (1 - tau_w[c, j]) / (1 + tau_h[c, j]) ** eta ) * 1**varphi * w[c, j] * s[c]**phi[c] * (1 - s[c]) ** ( (1- eta) /beta )           
    
    return w_til


# tenho que colocar o H_tr aqui no lugar do 1
    
w_tilf( )


#------------------------------------------ p_ir
    
        
def p_irf( ):
    global p_ir, p_i
    w_tilf( )
    w_r = w_til.sum(axis = 0) 
    
    w_r = list(map(lambda x: x**theta, w_r))
    
    p_ir = np.ones((i, r))
    
    for c in range(i):
        for j in range(r):
            p_ir[c, j] = ( w_til[c, j] ) ** theta / w_r[j]
            
    #p_i = np.sum(p_ir)

    p_i = np.sum(p_ir, axis =1) 
    return p_ir




#---------------------------------------  W (eq 27)


def Wf():
    global W
    W = np.zeros((i, r))
    
    for c in range(i):
        for j in range(r):
            W[c, j] = ((1 - s[c])**(-1/beta))/(1-tau_w[c, j])*gamma1*eta*(w_til[c, j]**theta)**(1/(theta*(1 - eta)))     #        (eq 27)
    return W



Wf()



#--------- Simulated data 



np.random.seed(3)
W_t = np.random.rand(i, r)   # simulated W - I get this in PNAD


np.random.seed(3)
p_t = np.random.rand(i, r)




#----------------------- Tau's  & w (TPF)


np.random.seed(4)

tau_h = np.random.rand(i, r)
tau_w = np.random.rand(i, r)

w = np.random.rand(i, r)




tau1 = [tau_w, tau_h, w]
tau1 = np.array(tau)




#--------------------- OBJECTIVE



def obj(tau):
    
    tau_w = tau[0]
    tau_h = tau[1]
    w = tau[2]        
    
    Hf()
    sf()
    w_tilf()
    p_irf()
    Wf()
    
    return np.sum(( (W - W_t) / W_t ) ** 2 + ( (p_ir - p_t) / p_t )**2 )
    
   



obj(tau1)


sol = minimize(obj, tau, method='Nelder-Mead', options={'maxiter':10e10})

sol.fun
sol.x

 
 

 

 





















