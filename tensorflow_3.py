# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:25:33 2020

@author: Marcos J Ribeiro
"""


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

tf.reset_default_graph()


a = tf.constant(2, dtype=tf.float32, name='a')

b = tf.constant(3, dtype=tf.float32, name='b')

c = tf.add(a, b)



with tf.Session() as sess:
    writer = tf.summary.FileWriter("D:/Git projects/grafo1", sess.graph)
    saida = sess.run(c)
    
    
print(saida)    

pip install tensorboard-plugin-wit 





