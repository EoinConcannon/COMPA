import numpy
import difflib
import random
import json

compareCmds = open("compareCmds.json")
listCmds = open("listCmds.json")
techDatabase = open("techDatabase.json")

compareDict = json.load(compareCmds)
listDict = json.load(listCmds)
techDict = json.load(techDatabase)

#add to json file
def addToDatabase(newObj, filename='techDatabase.json'):
    with open(filename,'r+') as file:
        filedata = json.load(file)
        filedata["tech"].append(newObj)
        file.seek(0)
        json.dump(filedata, file, indent = 4)

#list object values
def listValues(tech):
    print("\nCOMPA:" + tech[0] + " was released " + tech[1])
    print("COMPA:" + tech[0] + " has " + tech[2])
    print("COMPA:" + tech[0] + " has " + tech[3])
    return ""

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
    return "COMPA:I don't understand"

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
        print("\nCOMPA:" + tech1[0] + " was released " + tech1[1] + " while " + tech2[0] + " was release on " + tech2[1])
        print("COMPA:" + tech1[0] + " has " + tech1[2] + " while " + tech2[0] + " has " + tech2[2])
        print("COMPA:" + tech1[0] + " has " + tech1[3] + " while " + tech2[0] + " has " + tech2[3])
        return "I recognize both tech you have specified"
    if (twoCheck == 1):
        #either list what recognized tech has or user adds new tech to database
        #add a delay to each print?
        print("COMPA:I only recognize " + tech1[0] + " but not the other technology you specified")
        print("COMPA:Would you like me to list the properties of " + tech1[0])
        print("COMPA:Or could you tell me more about the other technology you specified?")
        userInput = input("You:")#user inputs the name of the tech again 
        if (userInput == "-1"):#user doesn't give the name (won't be added to database)
            return "exiting" #do something about this
        elif (difflib.get_close_matches(userInput, listDict['listCMD'], 4, 0.6)):
            listValues(tech1)
            return ""
        else:
            print("COMPA:Could you tell me the name of this technology again?")
            userInput = input("You:")
            userInput = userInput.lower() #user input is converted to lower case
            tech2.append(userInput) #add a loop to prevent duplicate names
            print("COMPA:Could you give me the date of when it was released?")
            userInput = input("You:")
            tech2.append(userInput)
            print("COMPA:Can you give me some additional information about this technology?")
            userInput = input("You:")
            userInput = userInput.lower()
            tech2.append(userInput)
            print("COMPA:Can you give me one final piece of information about this technology?")
            userInput = input("You:")
            userInput = userInput.lower()
            tech2.append(userInput)

            #creating object to append to file
            jsonObj = {
                        "name":tech2[0],
                        "date": tech2[1],
                        "stat1": tech2[2],
                        "stat2": tech2[3]
                      }
            
            addToDatabase(jsonObj)
            techDict["tech"].append(jsonObj)

            #techList["response"] = userInput#description of tech added to database (this will be improved upon after changing how the json is structured)
            return "COMPA:Thank you for telling me about this new tech"
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
print("COMPA:I am still in my development stage right now.")
print("COMPA:Please give me the names of two technologies and I will compare them.")
print("COMPA:type \"-1\" to stop the program or to CANCEL at anytime in the program")

while(userInput != "-1"):
    print("\nCOMPA:What technologies do you wish to compare?")
    userInput = input("You:")
    if (userInput != "-1"):
        userInput = userInput.lower()#converts to lowercase
        userInput = userInput.split()#user's input converted to a list
        botResponse = processInput(userInput)
        print("COMPA:" + botResponse)
