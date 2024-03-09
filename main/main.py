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
    twoCheck = 0
    tech1 = ""
    tech2 = ""

    for currentWord in userInput:
        word = difflib.get_close_matches(currentWord, techList['techDatabase'], 4, 0.6)
        ifWord = ''.join(word)
        #print(currentWord)#DEBUG
        if(ifWord == ""):#if user input doesn't match word in json "techDatabase"
            continue
        else:
            ifWord = random.choice(techList['response'])#random choices give back random response from "response" in json
            #adds a json value to the variable, this is so it can be checked later
            #create a better system for this later
            if(twoCheck == 0):
                tech1 = ifWord
                twoCheck += 1
            elif(twoCheck == 1):
                tech2 = ifWord
                twoCheck += 1
    
    if(twoCheck == 2):
        #list differences between specified tech
        print(tech1 + " " + tech2)
        return "I recognize both tech you have specified"
    if(twoCheck == 1):
        #either list what recognized tech has or user adds new tech to database
        return "I only recognize one technology you have specified"
    else:
        #user adds new tech to database
        print("COMPA:I do not recognize the technologies you have specified...")
        print("COMPA:Could you tell me more about " )#should get name of tech user input
        userInput = input("You:")#user inputs more info about said tech
        return "Thank you for sharing this information with me."


#welcome message
print("COMPA:What is your name?")
userInput = input("You:")
print("COMPA:Hello " + userInput + ". I am COMPA, the comparison chatbot.")
print("COMPA:I am in a very early stage of development right now.")
print("COMPA:In the future, you will need to input two technologies for me to compare")
print("COMPA:type \"exit\" to stop the program")

while(userInput != "exit"):
    print("\nCOMPA:What technologies do you wish to compare?")
    userInput = input("You:")
    userInput = userInput.lower()#converts to lowercase
    userInput = userInput.split()
    botResponse = processInput(userInput)
    print("COMPA:" + botResponse)
