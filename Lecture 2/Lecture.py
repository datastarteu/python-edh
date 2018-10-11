#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:36:47 2017

@author: pablo
"""

# NUMPY
import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"	


a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"


# SLICING
A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = A[:2,1:3]
							 
# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(A[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(A[0, 1])   # Prints "77"
	

	
	
# MATPLOTLIB
# Plotting the sine function
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()  # You must call plt.show() to make graphics appear.

# Sine and cosine
# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()
	
# Generating white noise
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(100)
plt.plot(x)
plt.show()

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()



# SCIPY
# Anonymous functions
square = lambda x: x**2
square(2)

from scipy.integrate import quad
quad(lambda x: x**3, 0,1)


# A histogram an the shape of the distribution
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
q = beta(5, 5) # Beta(a, b), with a = b = 5
obs = q.rvs(2000) # 2000 observations
grid = np.linspace(0.01, 0.99, 100)
fig, ax = plt.subplots()
ax.hist(obs, bins=40, normed=True)
ax.plot(grid, q.pdf(grid), 'k-', linewidth=2)
fig.show()


##########################
## EXERCISE: Employment simulation
##########################

'''
Using US unemployment data, Hamilton [Ham05] estimated the stochastic matrix
P =
0.971 0.029 0
0.145 0.778 0.077
0 0.508 0.492

where
• the frequency is monthly
• the first state represents “normal growth”
• the second state represents “mild recession”
• the third state represents “severe recession”
For example, the matrix tells us that when the state is normal growth, the state will again be
normal growth next month with probability 0.97


Assuming an initial employment distribution (0.

- What is the long term equilibrium? Does it change with different initial state?

Hint: np.dot(P,x) where x is the distribution
'''







# A Python joke :)
import antigravity
