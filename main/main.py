import numpy
import difflib
import random
import json

compare = '{"compareReq": ["compare", "difference", "different", "differentiate", "contrast", "between"], "response": ["res1", "res2", "res3"]}'
compareList = json.loads(compare)
#print(compareList['response'])

def processInput(userInput):
    for currentWord in userInput:
        word = difflib.get_close_matches(currentWord, compareList['compareReq'], 4, 0.6)
        ifWord = ''.join(word)
        if(ifWord == ""):#if user input doesn't match word in json "compareReq"
            continue
        else:
            ifWord = random.choice(compareList['response'])#random choices give back random response from "response" in json
            return ifWord#have this go down into another function?
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
