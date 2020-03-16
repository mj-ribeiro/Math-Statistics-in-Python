# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:52:58 2020

@author: Marcos J Ribeiro
"""




def pib(c0, c1, t0=0, t1=0, t=0, b0=0, b1=0, i=0):
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
    
    g = 150
    i = 150   
    
    y = ( 1/(1 - c1 + c1*t1) )*( c0 + i + g - c1*t0 - c1*t)
    
    if t == 0:
        T = t0 + t1*y
    else:
        T = t
        
    if i == 0:
        I = b0 + b1*y
    else:
        I = i
        
    print('\033[1;033m')
    print('     ')
    print('{:*^40}'.format('Multiplicador da renda'))
    print(f'\033[1;033mA renda de equilíbrio é igual a: {y:.2f}')
    print(f'Os impostos são iguais a: {T:.2f}')
    print(f'Os investimento são iguais a: {I:.2f}')
    print(f'A renda disponível é igual a: {(y-T):.2f}')
    print(f'O multiplicador é igual a: {( 1/(1 - c1 + c1*t1) ):.2f}')
    print(f'O consumo será: {(c0 +c1*y):.2f}')
    print('  ')
    print('{:*^40}'.format('Fim do programa'))
            


pib(160, 0.6, 0, 0, 100, 120, 0.8, 0)

















