#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:36:47 2017

@author: pablo
"""
# Writing functions: Calculating the dot product
def dot_product(x,y):
	assert len(x)==len(y)
	tot = 0
	for i in range(len(x)):
		tot += x[i]*y[i]
	return tot

# Generating white noise
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(100)
plt.plot(x)
plt.show()

# Anonymous functions
square = lambda x: x**2
square(2)

from scipy.integrate import quad
quad(lambda x: x**3, 0,1)

