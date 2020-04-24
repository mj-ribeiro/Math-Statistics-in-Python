# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:36:56 2020

@author: Marcos J Ribeiro
"""

#------- Questão 8

def dm(x, y, m_s, I=0):
    '''
    x: componente da demanda de moeda
    y: renda nominal 
    m_s: oferta de moeda
    I: tx de juros
    '''
    
    if I != 0:
        i = I
        
    else:
        i = x - (m_s/y)
    
    M_s = y*(x - i)
    print('\033[1;033m')
    print(f'A taxa de juros de equilíbrio será: {i:.2%}')
    print(f'A demanda por moeda em equilíbrio será {M_s:.2f}')
    
 
    
dm(0.5, 150, 45, I=0)



#-------- Questão 9
 

def bacen(x0, x1, theta, c, h_s, y):
    '''
    x0  e x1: parâmetros da demanda por moeda
    theta: coeficiente de reservas
    c: proporção fixa de moeda em espécie
    h_s: oferta de moeda do Bacen
    y: renda nominal
    '''
    i = - h_s/(x1*y*(c+theta*(1 - c))) + x0/x1            
    m_d = y*(x0 -x1*i)

    mult = 1/(c + theta*(1 - c))
    m_s = h_s*mult
     
    print('\033[1;033m')
    print(f' A taxa de juros de equilíbrio é: {i:.2%}')
    print(f'O multiplicador será: {mult:.2f}')
    print(f'A demanda total de moeda será: {m_d:.2f}')
    print(f'A oferta total de moeda será: {m_s:.2f}')


bacen(0.75, 6, 0.15, 0, 18, 1200)
 


#-------------




import numpy as np
import matplotlib.pyplot as plt


#----------  Questão 10 (e)

##### CURVA IS

# quanto maior o multiplicador, mais elástico será a IS


i = np.arange(0, 20, 0.1)

b0 = 20000

b1 = (1/0.8)   #soma 0.2
b2 = (1/0.2)   #soma 0.8
b3 = (1/0.05) #soma 0.95 

y1 = b0 - b1*i
y2 = b0 - b2*i
y3 = b0 - b3*i

fig, ax = plt.subplots(figsize=(8,6))
#ax.set_xlim(19000, 21000)
ax.plot(y1, i, 'b--', label='c1+b1=0,2')
ax.plot(y2, i, 'g-', label='c1+b1=0,8')
ax.plot(y3, i, 'r-.', label='c1+b1=0,95')
plt.axhline(y=5, color='r', linestyle='-')
plt.axhline(y=7.5, color='r', linestyle='-')
plt.rc('axes', titlesize=20)     # fontsize of the axes title
plt.rc('axes', labelsize=25)    # fontsize of the x and y labels
ax.set_title('Curva IS')
ax.set_xlabel('Y')
ax.set_ylabel('i')
ax.legend()



#-----------Questão 11 c

###### CURVA LM


m_d = 100
y = np.arange(0, 1000, 5)
d1_1 = 0.2
d1_2 = 2

d2 = 0.7

i_1 = d1_1/d2*y - m_d/d2
i_2 = d1_2/d2*y - m_d/d2



fig, ax = plt.subplots(figsize=(12,8))
ax.plot(y, i_1, 'b--', label='d1_1 = 0.2')
ax.plot(y, i_2, 'g-', label='d1_2 = 0.5')
plt.rc('axes', titlesize=20)     # fontsize of the axes title
plt.rc('axes', labelsize=20)    # fontsize of the x and y labels
ax.set_title('Curva LM')
ax.set_xlabel('Y')
ax.set_ylabel('i')
ax.legend()




################ IS-LM



def is_lm(x0, x1, m_s, c0, c1, t, b0, b1, b2, g):
    '''
    x0: parâmetro da demanda de moeda
    x1: parâmetro da demanda de moeda
    m_s: demanda de moeda
    c0: consumo autônomo
    c1: propensão marginal a consumir
    b0: investimento autônomo
    b1: propensão marginal a investir
    b2: investimento em função da taxa de juros
    g: gastos do governo
    '''
    M = 1/(1 - c1 - b1 + b2* (x0/x1) )
    
    y = M * (c0 - c1*t + b0 + b2*(m_s/x1) + g)
    
    i = ( x0/x1 )*y - m_s/x1
    
    C = c0 + c1*(y - t)
    
    I = b0 + b1*y - b2*i
    
    print('\033[1;033m')
    print('{:*^40}'.format(' IS-LM '))
    print('  ')
    print(f'O Multiplicador é: {M:.2f}')
    print(f'O consumo é dado por: {C:.2f}')
    print(f'O investimento é dado por: {I:.2f}')
    print(f'O produto de equilíbrio é: {y:.2f}')
    print(f'A taxa de juros de equilíbrio é: {i:.2%}')
    print('  ')
    print('{:*^40}'.format(' Fim do Programa! '))
    



is_lm(0.5, 5000, 2000, 300, 0.25, 500, 3000, 0.2, 1000, 200)
    







































