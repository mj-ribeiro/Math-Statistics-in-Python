# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:52:05 2020

@author: Marcos J Ribeiro
"""

import plotnine

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


a = tf.constant([9, 7, 3, 1], name='a')
b = tf.constant([2, 0, 1, 4], name='b')


s = a + b 


with tf.Session() as sess:
    soma = sess.run(s)
    print(soma)
    
    


#--- Complex numbers


x = tf.constant([[-2.25 + 4.75j], [-3.25 + 5.75j]])

with tf.Session() as sess:    
    k1 = sess.run(tf.abs(x))
    print(k1)





    
#----- Matrix


m1 = tf.constant([[1, 2, 4], [4, 0, 9], [1, 1, 5]], name='m1')
m2 = tf.constant([[3, 2, 21], [7, 3, 9], [1, 1, 5]], name='m1')

s2 = tf.add(m1,m2)

with tf.Session() as sess:
    soma2 = sess.run(s2)
    print(soma2)











