import numpy
import difflib
import random
import json

compareCmds = open("compareCmds.json")
techDatabase = open("techDatabase.json")

#create a better structure for tech JSON e.g. (Tech1: stat1 = 3525, stat2 = 6426) should be easy to work with/display
compareList = json.load(compareCmds)
techList = json.load(techDatabase)

def processInput(
        userInput):
    for currentWord in userInput:#loops through the user's string input
        word = difflib.get_close_matches(currentWord, compareList['compareCMD'], 4, 0.6)#checks if the current word some what matchs a word in the json
        ifWord = ''.join(word)
        #print(currentWord)#DEBUG
        if (ifWord == ""):#if user input doesn't match word in json "compareCMD"
            continue
        else:
            #stops reading list here
            #moves into next function
            ifWord = compareTech(userInput)
            return ifWord
    return "I don't understand"

def compareTech(
        userInput):
    #checkers to make sure tech user has input is valid and matches the json
    twoCheck = 0
    tech1 = ""
    tech2 = ""
    ifWord = ""

    for currentWord in userInput:
        for key, value in techDatabase.item():#??????????????????
            #if key == "name":
            word = difflib.get_close_matches(currentWord, techList[i]['name'], 4, 0.6)
            print(word)
            ifWord = ''.join(word)
        
        #print(currentWord)#DEBUG
        if (ifWord == ""):#if user input doesn't match word in json "techDatabase"
            continue
        else:
            ifWord = random.choice(techList[1]['name'])#random choices give back random response from "response" in json
            #adds a json value to the variable, this is so it can be checked later
            #create a better system for this later
            if (twoCheck == 0):#first technology matches
                tech1 = ifWord
                twoCheck += 1
            elif (twoCheck == 1):#second technology matches
                tech2 = ifWord
                twoCheck += 1
    
    if (twoCheck == 2):
        #list differences between specified tech
        print(tech1 + " " + tech2)
        return "I recognize both tech you have specified"
    if (twoCheck == 1):
        #either list what recognized tech has or user adds new tech to database
        print("I only recognize one technology you have specified but not the other")
        print("Could you tell me the name of this technology again?")
        userInput = input("You:")#user inputs the name of the tech again 
        if (userInput == "-1"):#user doesn't give the name (won't be added to database)
            return "exiting"
        else:
            techList.append(userInput)#name of tech added to database
            #print(techList)
            print("Can you give me some additional information about this technology?")
            userInput = input("You:")
            techList["response"] = userInput#description of tech added to database (this will be improved upon after changing how the json is structured)
            return "Thank you for telling me about this new tech"
    else:
        #user adds new tech to database
        print("COMPA:I do not recognize the technologies you have specified...")
        print("COMPA:Could you tell me more about both of them" )#should get name of tech user input
        #userInput = input("You:")#user inputs more info about said tech
        return "Thank you for sharing this information with me."


#welcome message
print("COMPA:What is your name?")
userInput = input("You:")
print("COMPA:Hello " + userInput + ". I am COMPA, the comparison chatbot.")
print("COMPA:I am in a very early stage of development right now.")
print("COMPA:In the future, you will need to input two technologies for me to compare")
print("COMPA:type \"-1\" to stop the program or to CANCEL at anytime in the program")

while(userInput != "-1"):
    print("\nCOMPA:What technologies do you wish to compare?")
    userInput = input("You:")
    if (userInput != "-1"):
        userInput = userInput.lower()#converts to lowercase
        userInput = userInput.split()#user's input converted to a list
        print(techList) #unlabelled json python / https://realpython.com/python-dicts/
        botResponse = processInput(userInput)
        print("COMPA:" + botResponse)
