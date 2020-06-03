# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:43:23 2020

@author: Marcos J Ribeiro
"""

#-- libraries

import rope
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


tf.__version__

a = tf.Variable(0.41)


init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(a.eval())

p = tf.placeholder(tf.float32, [1,1])


#---- constants

v1 = tf.constant(2) 
v2 = tf.constant(3)


print(v1)


s = v1 + v2

type(s)

s


with tf.Session() as sess:
    s1 = sess.run(s)


#---- strings

t1 =  tf.constant('texto 1 ')

t2 =  tf.constant('texto 2')


with tf.Session() as sess:
    con = sess.run(t1 + t2)



print(con)



#----- Variables

v3 = tf.constant(15, name= 'v3')
v3

s2 = tf.Variable(v3 + 5, name='s2')

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    k = sess.run(s2)

k



vec = tf.constant([1, 5, 6], name='vec')

s4 = tf.Variable(vec + 4, name='s4')

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    svec = sess.run(s4)
    print(svec)


























