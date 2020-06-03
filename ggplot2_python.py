# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:02:02 2020

@author: Marcos J Ribeiro
"""

import plotnine
from plotnine import *
from plotnine.data import mpg
%matplotlib inline

(ggplot(mpg)         # defining what data to use
 + aes(x='class')    # defining what variable to use
 + geom_bar(size=20) # defining the type of plot to use
)


(ggplot(mpg)
 + aes(x='displ', y='hwy', color='class')
 + geom_point()
 + labs(title='Engine Displacement vs. Highway Miles per Gallon', x='Engine Displacement, in Litres', y='Highway Miles per Gallon')
)
