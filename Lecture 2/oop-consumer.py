# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:15:41 2018

@author: pablo
"""

# CLASSES: 

class Person:
    # Class constructor
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age
    
    # Method: function that exists inside the 
    # class only.
    def is_underage(self):
        return self.age <18
            
    
   p1 = Person('Jan',30)
   p1.name # Retrieve the value of attributes
   p1.age
   
   
import numpy as np
class Consumer:
    def __init__(self, w, p):
        self.wealth = w
        self.propensity = p # spending probability
        
    def earn(self,salary):
        self.wealth += salary
   
    def spend(self,amount):
        if amount >= self.wealth:
            print('Poverty alert')
        else:
            if np.random.rand() < self.propensity:
                self.wealth -= amount
            
savers = [Consumer(500, 0.1) for _ in range(100)]
shopaholics = [Consumer(500, 0.9) for _ in range(100)]

savers_after_spend = [s.spend(50+5*np.random.randn()) for s in savers]
savers_final_wealth = [s.wealth for s in savers]
savers_final_wealth

import matplotlib.pyplot as plt
plt.hist(savers_final_wealth)









   
   
   
   
   
   
   
   
   
   
   