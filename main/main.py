import numpy
import difflib
import random
import json

greeting = '["Hello", "Hi", "Howdy", "Hello :)", "Hallo"]'
greet = json.dumps(greeting)
#print(greet)

def processInput(userInput):
    x = print(difflib.get_close_matches(userInput, greet))
    y = ''.join(x)
    return y

print("COMPA:What is your name?")
userInput = input("You:")
print("COMPA:Hello " + userInput + ". I am COMPA, the comparison chatbot.")
print("COMPA:I am in a very early stage of development right now.")
print("COMPA:In the future, you will need to input two technologies for me to compare")
print("COMPA:type \"exit\" to stop the program\n")

while(userInput != "exit"):
    userInput = input("You:")
    userInput = userInput.lower()#converts to lowercase
    print("COMPA:" + processInput(userInput))
