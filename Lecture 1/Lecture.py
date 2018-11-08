# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:00:20 2017

@author: Pablo Maldonado
"""

# The "compulsory" Hello world program
print("Hello World")

###########################
### Data types
###########################
## What kind of stuff can we work with?

# First tipe: Boolean
x = True
y = 100 < 10
y
x*y
x+y

# Numeric data (integers and floats)

a = 1
b = 2
a+b
a*b
a/b
c, d = 2.5, 10.0
c
d

# Complex numbers
z = complex(1,2)
z

# Strings
x = "I am a string"
y = "... and I am a string too"

# Tells us the type of the object
type(x)

x+y
x*2

'test '*2
"test "*2

###########################
### Containers
###########################
# These are objects that contain other objects. 

# List
x = [1,'a',2.0]
x
x[0]
x[2]
x[-1]
x[-2]

x[0]  = 'pablo'
x # The new list is now modified

#  Tuple
y = (1,'a',2.0)
y
type(y)
y[0]
y[0] = 'something' # Error! You can not overwrite tuples

# Unpacking: Storing the information of an object in different parts

names = ('Juan', 'Pablo','Maldonado') 
first_name, second_name, last_name = names
first_name

# Parse a string into a list
single_line = 'pablo,maldonado,zizkov'
my_data = single_line.split(',')
my_data
 
# put it again together
new_single_line = ','.join(my_data)
new_single_line
 
# Dictionaries
d = {'name':'Pablo', 'last_name':'M'}
type(d)
d['name']
d['last_name']
d['address']
 

###########################
### Loops and list comprehension
###########################

x_vals = [1,2,3,4,5]
for x in x_vals:
    print(x*x)

# Sum of squares
x_vals
total = 0 
for x in x_vals:
    total = total + x*x
total

# The Python way: Using list comprehension!
sum([x*x for x in x_vals])

# List comprehension is a very useful way of doing loops "faster"
[x*x for x in x_vals]

# Ranges of numbers:
my_vals = range(1,20)    

# Run the following. What does it print?
for i in my_vals:
    print(i)

my_vals

# Calculating squares in two different ways
sum([x*x for x in my_vals])
sum([x**2 for x in my_vals])    
 
# Example: Calculate the distance between two vectors

#### 
from math import sqrt

x = [3,0]
y = [0,4]
dist = 0
for i in range(len(x)):
    dist += (x[i]-y[i])**2
dist = sqrt(dist)
dist

# How can we re-write this?


def my_dist(x,y):
    dist2 = sum([(x[i]-y[i])**2 for i in range(len(x))])
    dist = sqrt(dist2)
    return dist
    
    
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 


















