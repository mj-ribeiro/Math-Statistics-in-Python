# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:52:58 2020

@author: Marcos J Ribeiro
"""




def pib(c0, c1, g, t0=0, t1=0, t=0, b0=0, b1=0, i=0):
    '''
    c0: consumo autônomo
    c1: propensão marginal a consumir
    t0: tributo autônomo
    t1: propensão a tributar
    t: tributos
    b0: confiança nos negócios
    b1: propensão a investir
    i: investimento
    '''
    global y        
    
    y = ( 1/(1 - c1 + c1*t1 - b1) )*(c0 - c1*t0 + b0 + g + i - c1*t)

     
    if t == 0:
        T = t0 + t1*y
    else:
        T = t
        
    if i == 0:
        I = b0 + b1*y
    else:
        I = i
    
         
    print('\033[1;033m')    
    print('{:*^40}'.format('Multiplicador da renda'))
    print('     ')
    print(f'\033[1;033mA renda de equilíbrio é igual a: {y:.2f}')
    print(f'Os impostos são iguais a: {T:.2f}')
    print(f'Os investimento são iguais a: {I:.2f}')
    print(f'A renda disponível é igual a: {(y-T):.2f}')
    print(f'O multiplicador é igual a: {( 1/(1 - c1 + c1*t1 - b1) ):.2f}')
    print(f'O consumo será: {(c0 +c1*(y-T)):.2f}')
    print('  ')
    print('{:*^40}'.format('Fim do programa'))
            


pib(c0=179, c1=0.4, t=100, b0=120, b1=0.2, i=0, g=110)


pib(c0=160, c1=0.4, t=110, i=140, g=100)



