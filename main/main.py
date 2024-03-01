import numpy
import difflib
import random
import json

compare = '{"compareReq": ["compare", "difference", "different", "differentiate", "contrast", "between"], "response": ["res1", "res2", "res3"]}'
compareList = json.loads(compare)
#print(compareList['response'])

def processInput(userInput):
    x = difflib.get_close_matches(userInput, compareList['compareReq'], 4, 0.6)
    y = ''.join(x)
    if(y == ""):#if user input doesn't match word in json "compareReq"
        y = "what"
    else:
        y = random.choice(compareList['response'])#random choices give back random response from "response" in json
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
