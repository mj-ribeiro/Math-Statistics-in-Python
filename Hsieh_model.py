# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:18:22 2020

@author: Marcos J Ribeiro
"""
# see this: https://pastebin.com/cvYBvW3B
# The model can be viewed in:  https://drive.google.com/drive/u/0/folders/1MOOHg2woM6B2MCLohTPk-kbIgO5RLbVZ


import numpy as np
import matplotlib.pyplot as plt
import math as mt
from scipy.optimize import minimize
from math import gamma
import itertools as itl
import time





#----------------------- Defining parameters



def par():
    global beta, eta, varphi, theta, rho, i, r, gamma1, phi
    beta = 0.69
    eta = 0.25
    varphi = 0.25
    theta = 3.44
    rho = 0.19
    i = 2
    r = 4
    gamma1 = gamma(1 - (theta*(1 - rho)**(-1)) * (1 - eta)**(-1))
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





#------------------------ Agregate Human capital   (eq 23)

 

def Hf( ):
    taus2()
    global H, E, c1, g, b, a 
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
#            
            H[c, j] = p_ir[c, j]*h_til[c, j] * ( ( (1 - x1[0, c, j])/(1 + x1[1, c, j]) ) * x1[2, c, j] ) ** (eta/(1 - eta)) * E[c]
          
    return H





#----------------------------------------- s - time spent at school   (eq 14)




def sf( ):
    global s
    s = np.zeros((i, 1))
    
    for c in range(i):
        s[c] = (1+ (1-eta)/beta*phi[c])**(-1)                        
    return s




#----------------------------------------- w tilde  (Proposition 1)



def H_trf():
    global H_tr
    H_tr = np.ones((i, r))*0.5
    return H_tr



def w_tilf( ):
    taus2( )
    H_trf( )
    global w_til
    
    w_til = np.ones((i, r))
    
    for c in range(i):
        for j in range(r):
            w_til[c, j] = ( (1 - x1[0, c, j]) / (1 + x1[1, c, j]) ** eta ) * H_tr[c, j]**varphi * x1[2, c, j] * s[c]**phi[c] * (1 - s[c]) ** ( (1- eta) /beta )           

    return w_til





#------------------------------------------ p_ir  (eq 19)
    
        
def p_irf( ):
    global p_ir, p_i, w_r
    w_tilf( )
        
    w_r = w_til**theta
    w_r = w_r.sum(axis = 1) 

    
    p_ir = np.ones((i, r))
    
    for c in range(i):
        for j in range(r):
            p_ir[c, j] = ( w_til[c, j] ) ** theta / w_r[c]
            
    #p_i = np.sum(p_ir)

    p_i = np.sum(p_ir, axis =1) 
    return p_ir
 


# p_ir.sum(axis=1)    # this sum get me a vector with ones


#---------------------------------------  W (eq 27)



def Wf():
    taus2( )
    global W
    W = np.zeros((i, r))
    
    for c in range(i):
        for j in range(r):
            W[c, j] = ((1 - s[c])**(-1/beta))/(1-x1[0, c, j])*gamma1*eta*(w_til[c, j]**theta)**(1/(theta*(1 - eta)))     #        (eq 27)
    return W


 

    
#--------- Simulated data 


def simul():
    global W_t, p_t
    
    W_t = np.array(([0.8, 0.42, 0.33, 0.12], [0.99, 0.22, 0.154, 0.654]))  
    
    p_t = np.array(([0.822, 0.32, 0.132, 0.109], [0.212, 0.453, 0.3524, 0.114]))



#----------------------- Tau's  & w (TPF)

#
    
def taus2():
    global x1, tau_h, tau_w, w
    par()
    #np.random.seed(40)
    
    tau_h = np.random.rand(i, r)
    tau_h[0, :] = 0

    tau_w = np.random.uniform(low=-1, high=1, size=(i,r))
    tau_w[0, : ] = tau_w[0, 0]
    
    w =np.random.uniform(low=0, high=1, size=(i,r))
    w[:, r-1] = 1
    
    x1 = np.array( [tau_w, tau_h, w] )
    
    return x1
    #x0 = x0.reshape(-1, 1)


#
    
def taus():
    global x0, tau_h, tau_w, w
    par()
    #np.random.seed(40)
    
    tau_h = np.ones((i, r))*0.2123
    tau_w = np.ones((i, r))*0.5673
    
    w = np.ones((i, r))*0.1345
    
    x0 = np.array([ [tau_w], [tau_h], [w] ])
    x0 = x0.reshape(3, i, r)
    
    return x0
    #x0 = x0.reshape(-1, 1)





#--------------------- OBJECTIVE FUNCTION

 

def obj(tau):
    global D, tau_w, tau_h, w
    #taus()
    
    tau = tau.reshape((3, i, r))
    tau_w = tau[0]
    tau_h = tau[1]
    w = tau[2]
#    
#    print('tau_w = ', tau_w)    
#    print('  ')
    
    sf()
    w_tilf()
    p_irf()

    Hf()
    Wf()
    simul()
    f1 = np.zeros((i, r))
    f2 = np.zeros((i, r))
    
    
    for c in range(i):
        for j in range(r):
            f1[c, j] = ( (W[c, j] - W_t[c, j]) / W_t[c, j] ) ** 2
            f2[c, j] = ( (p_ir[c, j] - p_t[c, j])  /  p_t[c, j] ) ** 2
    d1 = np.sum(f1)
    d2 = np.sum(f2)
    D = d1 + d2
    
#   D =  np.sum ( ((W - W_t) / W_t)**2  +  ((p_ir - p_t) / p_t)**2 ) 
    #D = np.sum( ( np.dot( (W-W_t), np.linalg.pinv(W_t) ) )**2 + ( np.dot( (p_ir - p_t), np.linalg.pinv(p_t) ) )**2 )
    return D



# pseudo inverse de Moore-Penrose
# restrição do Nelder-Mead
# slsqp   



#----------------------------- OPTIMIZATION Scipy

obj(x1)
taus2()



import scipy.optimize as sp


sp.fmin(obj, x1)



taus2()
obj(x1)


sol = minimize(obj, x1,  method='Nelder-Mead', options={'maxiter':10000})

sol 
sol.fun
sol.x 

taus2()


#--------------------------- OPTIMIZATION Marcos's Algorithm
 

def hsieh(n, t=12):
    global opt, k
    opt = [t]
    k = np.zeros((3, i, r))

    for z in itl.count():
        
        if z < n+1:
            taus2()
            res = obj(x1)
            print(z)
            
            if res < opt[0]:
                opt.remove(opt[0])
                opt.append(res)
                k = x1
        else: 
            break



taus2()
obj(x1)




def calibration(v, t=12):
    
    start = time.time()
    hsieh(v, t)
    end = time.time()
            
    print('\033[1;033m=-'*25)
    print('{:*^50}'.format('Hsieh Model'))
    print('=-'*25)
    print('   ')
    
    print('\033[1;033mElapsed time:', (end - start))
    print('   ')
        

    print(f'tau_w is given by: \n {k[0]}')
    print('   ')

    print(f'tau_h is given by: \n {k[1]}')
    print('   ')

    print(f'w is given by: \n {k[2]}')
    print('   ')

    print(f'The minimun value to D is: {opt}')
    print('   ') 
    
    print('{:*^50}'.format('End of calibration'))



calibration(10000, 20)








#-------------------- Constraints
    


def c1(tau):
    tau = tau.reshape((3, i, r))
    return tau_h[0, :] - 0      
        


def c2(tau):    
    tau = tau.reshape((3, i, r))
    return tau_w[0, : ] - tau_w[0, 0 ]



def c3(tau):
    tau = tau.reshape((3, i, r))
    return w[:, r-1] - 1

        
    


con1 = {'type': 'eq', 'fun':c1}
con2 = {'type': 'eq', 'fun':c2}
con3 = {'type': 'eq', 'fun':c3}


cons = [con2]




 
taus2()
 
sol = minimize(obj, x1, method='SLSQP', options={'maxiter':10e8}, constraints=cons)
sol
 


obj(x0)
sol
















