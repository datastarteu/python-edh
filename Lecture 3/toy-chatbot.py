# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:43:20 2018

@author: pablo
"""

import random

# ELIZA: http://www.manifestation.com/neurotoys/eliza.php3
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]

while True:
        userInput = input(">>> ")
        if userInput in greetings:
                random_greeting = random.choice(greetings)
                print(random_greeting)
        elif userInput in question:
                random_response = random.choice(responses)
                print(random_response)
        else:
                print("I did not understand what you said")

                
                
# Make it talk!
import pyttsx3
engine = pyttsx3.init()
engine.say("I love Prague")
engine.runAndWait()


# EXERCISE: 

# 1. Rewrite the code above as a class. What are the methods and attributes?

# 2. Can you make your bot do more interesting stuff? Tell you the weather, 
# google something for you, or open youtube?
import webbrowser
my_query = "rain in Spain"
webbrowser.open_new("www.google.com/search?q="+my_query)

my_video = "saturday night live"
webbrowser.open_new("https://www.youtube.com/results?search_query="+my_video)
