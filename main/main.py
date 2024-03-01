import numpy
import difflib
import random
import json

greeting = '{"greetings": ["Hello", "Hi", "Howdy", "Hello :)", "Hallo"]}'
greet = json.loads(greeting)
#print(greet['greetings'])

def processInput(userInput):
    x = difflib.get_close_matches(userInput, greet['greetings'], 2, 0.5)
    y = ''.join(x)
    if(y == ""):
        y = "no response"
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
    botResponse = processInput(userInput)
    print("COMPA:" + botResponse)
