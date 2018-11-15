# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:13:52 2018

@author: pablo
"""

import random
greetings = ('hola', 'hello', 'hi', 'Hi', 'hey!','hey')
questions = ('how are you?','How are you doing?')
responses = ('Okay',"I'm fine")

vocab = {
        greetings:greetings,
        questions:responses
         }


timeout = False

while not timeout:
        for key in vocab.keys():
            userInput = input("Write me something: >>> ")
            if userInput in key:
                resp = random.choice(vocab[key])
                print(resp)
            else:
                print("Sorry, I don't know how to react to that")
                timeout = True
                break