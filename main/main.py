import numpy
import difflib
import random
import json

compareCmds = open("compareCmds.json")
techDatabase = open("techDatabase.json")

compareDict = json.load(compareCmds)
techDict = json.load(techDatabase)

def processInput(userInput):
    for currentWord in userInput:#loops through the user's string input
        word = difflib.get_close_matches(currentWord, compareDict['compareCMD'], 4, 0.6)#checks if the current word some what matchs a word in the json
        ifWord = ''.join(word)
        if (ifWord == ""):#if user input doesn't match word in json "compareCMD"
            continue
        else:
            #stops reading list here
            #moves into next function
            ifWord = compareTech(userInput)
            return ifWord
    return "I don't understand"

def compareTech(userInput):
    #checkers to make sure tech user has input is valid and matches the json
    twoCheck = 0
    tech1 = []
    tech2 = []

    for currentWord in userInput:
        for techItem in techDict["tech"]:
            for key, value in techItem.items(): #change this after 1.0 release
                ifWord = ""
                if (key != "name"):
                    continue

                if (currentWord == value):#if user's input matches the key's name value
                    ifWord = value #better way of doing this (relating to check)
                    
                if (ifWord == ""):#if user input doesn't match word in json "techDatabase"
                    continue
                else:
                    #ifWord = random.choice()#random choices give back random response from "response" in json
                    #adds a json value to a list, this is so it can be used for comparison
                    if (twoCheck == 0):#first technology matches
                        tech1.append(ifWord)
                        tech1.append(techItem["date"])
                        tech1.append(techItem["stat1"])
                        tech1.append(techItem["stat2"])
                        twoCheck += 1
                    elif (twoCheck == 1):#second technology matches
                        tech2.append(ifWord)
                        tech2.append(techItem["date"])
                        tech2.append(techItem["stat1"])
                        tech2.append(techItem["stat2"])
                        twoCheck += 1
        
    if (twoCheck == 2):
        #list differences between specified tech
        #improve this later
        #better definition for what tech COULD be
        print("\n" + tech1[0] + " was released " + tech1[1] + " while " + tech2[0] + " was release on " + tech2[1])
        print(tech1[0] + " has " + tech1[2] + " while " + tech2[0] + " has " + tech2[2])
        print(tech1[0] + " has " + tech1[3] + " while " + tech2[0] + " has " + tech2[3])
        return "I recognize both tech you have specified"
    if (twoCheck == 1):
        #either list what recognized tech has or user adds new tech to database
        #add a delay to each print?
        print("I only recognize " + tech1[0] + " but not the other technology you specified")
        print("Would you like me to list the properties of " + tech1[0])
        print("Or could you tell me more about the other technology you specified?")
        userInput = input("You:")#user inputs the name of the tech again 
        if (userInput == "-1"):#user doesn't give the name (won't be added to database)
            return "exiting"
        else:
            print("Could you tell me the name of this technology again?")
            userInput = input("You:")
            #techList.append(userInput)#name of tech added to database
            #print(techList)
            print("Could you give me the date of when it was released?")
            userInput = input("You:")
            print("Can you give me some additional information about this technology?")
            userInput = input("You:")
            #techList["response"] = userInput#description of tech added to database (this will be improved upon after changing how the json is structured)
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
        botResponse = processInput(userInput)
        print("COMPA:" + botResponse)
