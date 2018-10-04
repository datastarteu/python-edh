# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:00:20 2017

@author: Pablo Maldonado
"""

# The "compulsory" Hello world program
print("Hello World")


# A Python joke :)
import antigravity

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
 
## Read from file

# Check where we are on the disk
import os
print(os.getcwd())

# You can check your working directory in the upper right corner on Spyder
# (the folder icon)
# All good, my directory is correct
my_data = open('cz_cities.txt','r')
my_data.read() # This opens, reads and closes the file


my_data = open('cz_cities.txt','r')
#
# Loops: Read each line of the file and perform an operation
for line in my_data:
    city, value = line.split(":")
    print("The city is this {0} and the value is {1}".format(city,value))    
my_data.close()

### Loops
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
 
# Example: Calculate the dot product 
# between two vectors

# First, we need to know the length
len(x) # Calculates the length of an object


x = [1,2,3]
y = [4,5,6]
dot_product = 0

for i in range(len(x)):
    #dot_product = dot_product + x[i]*y[i]
    dot_product += x[i]*y[i]
dot_product

# calculate square root
from math import sqrt
sqrt(9)

my_str = "ThIs is a StrinG" 
  ## Write something that calculates number of
  ## capital letters (4)
# HINT: 
# Try to use upper: my_str.upper()    
my_str[3] 
for i in range(len(my_str)):
    print(my_str[i])

#### 
x = [3,0]
y = [0,4]
dist = 0
for i in range(len(x)):
    dist += (x[i]-y[i])**2
dist = sqrt(dist)
dist
 
 
    
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 


















