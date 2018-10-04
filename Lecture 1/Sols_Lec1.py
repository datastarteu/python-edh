#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:55:30 2017

@author: pablo
"""

# 1.a Write a function to calculate the inner product between two vectors.
x = [1,2,3]
y = [4,5,6]

def inner(x,y):
    acc = 0
    for i in range(len(x)):
        acc += x[i]*y[i]
    return acc

inner(x,y)        

# 1.b How many even integers are there between 1 and 99?
sum([x % 2 for x in range(100)])

# 1.c Count the number of elements in a list of tuples that have both coordinates even.
test_vals = [(2,5),(4,2),(9,8), (12,11)]
tot = 0
for p in test_vals:
    if p[0] % 2 == 0 and p[1] % 2 == 0:
        tot += 1
print(tot)      

# 2 How can we calculate how many capital letters are in a string?
test = 'testStrinG'
cnt =0
for letter in test:
    if letter == letter.upper():
        cnt +=1
print('There are {0} capital letters'.format(cnt))

# 3 Given a value and a list of coefficients, evaluate the polynomial determined by such coefficients.
def poly(x,coeffs):
    val = 0
    for i, coeff in enumerate(coeffs):
        val += coeff*x**i
    return val

poly(1,[1,2,1])

# 4
def triangle(n):
    for i in range(1,n+1):
        print('* '*i)

triangle(5)      

#5 Write a function to calculate factorial(n)

def factorial(n):
    acc = 1
    for i in range(1,n+1):
        acc *= i
    return acc

factorial(4)