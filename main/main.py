import numpy
import difflib
import random
import json

compareCMD = '{"compareCMD": ["compare", "difference", "different", "differentiate", "contrast", "between"]}'
compareList = json.loads(compareCMD)
tech = '{"techDatabase": ["tech1", "tech2", "tech3", "tech4"], "response": ["res1", "res2", "res3"]}'
#create a better structure for tech JSON e.g. (Tech1: stat1 = 3525, stat2 = 6426) should be easy to work with/display
techList = json.loads(tech)

def processInput(userInput):
    for currentWord in userInput:
        word = difflib.get_close_matches(currentWord, compareList['compareCMD'], 4, 0.6)
        ifWord = ''.join(word)
        #print(currentWord)#DEBUG
        if(ifWord == ""):#if user input doesn't match word in json "compareCMD"
            continue
        else:
            #stops reading list here
            #moves into next function
            ifWord = compareTech(userInput)
            return ifWord
    return "I don't understand"

def compareTech(userInput):
    for currentWord in userInput:
        word = difflib.get_close_matches(currentWord, techList['techDatabase'], 4, 0.6)
        ifWord = ''.join(word)
        #print(currentWord)#DEBUG
        if(ifWord == ""):#if user input doesn't match word in json "techDatabase"
            continue
        else:
            ifWord = random.choice(techList['response'])#random choices give back random response from "response" in json
            return ifWord
    return "I don't understand"

#welcome message
print("COMPA:What is your name?")
userInput = input("You:")
print("COMPA:Hello " + userInput + ". I am COMPA, the comparison chatbot.")
print("COMPA:I am in a very early stage of development right now.")
print("COMPA:In the future, you will need to input two technologies for me to compare")
print("COMPA:type \"exit\" to stop the program\n")

while(userInput != "exit"):
    userInput = input("You:")
    userInput = userInput.lower()#converts to lowercase
    userInput = userInput.split()
    botResponse = processInput(userInput)
    print("COMPA:" + botResponse)
