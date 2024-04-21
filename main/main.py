import difflib
import time
import random
import json

commands = open("commands.json")
responses = open("responses.json")
techDatabase = open("techDatabase.json")

commandDict = json.load(commands)
resDict = json.load(responses)
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
    print("\nCOMPA:" + tech[0] + random.choice(resDict['listRes'][0]['dateRes']) + tech[1])
    print("COMPA:" + tech[0] + random.choice(resDict['listRes'][0]['statRes']) + tech[2])
    print("COMPA:" + tech[0] + random.choice(resDict['listRes'][0]['statRes']) + tech[3])
    return ""

def processInput(userInput):
    for currentWord in userInput:#loops through the user's string input
        word = difflib.get_close_matches(currentWord, commandDict['compare'], 4, 0.6)#checks if the current word some what matchs a word in the json
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
    #twoCheck ensures that tech user has input is valid and matches the json
    twoCheck = 0
    tech1 = []
    tech2 = []

    for currentWord in userInput:
        for techItem in techDict["tech"]:
            if (currentWord == techItem["name"]):#if user's input matches the key's name value
                if (twoCheck == 0):#first technology matches
                    tech1.append(techItem["name"])
                    tech1.append(techItem["date"])
                    tech1.append(techItem["stat1"])
                    tech1.append(techItem["stat2"])
                    twoCheck += 1
                elif (twoCheck == 1):#second technology matches
                    tech2.append(techItem["name"])
                    tech2.append(techItem["date"])
                    tech2.append(techItem["stat1"])
                    tech2.append(techItem["stat2"])
                    twoCheck += 1
            else: #if user input doesn't match word in json "techDatabase"
                continue
           
    if (twoCheck == 2):
        #list differences between specified tech
        print("\nCOMPA:" + tech1[0] + " was released " + tech1[1] + " while " + tech2[0] + " was release on " + tech2[1])
        print("COMPA:" + tech1[0] + " has " + tech1[2] + " while " + tech2[0] + " has " + tech2[2])
        print("COMPA:" + tech1[0] + " has " + tech1[3] + " while " + tech2[0] + " has " + tech2[3])
        return "I recognize both tech you have specified"
    if (twoCheck == 1):
        #either list what recognized tech has or user adds new tech to database
        print("COMPA:I only recognize " + tech1[0] + " but not the other technology you specified")
        print("COMPA:Would you like me to list the properties of " + tech1[0])
        print("COMPA:Or could you tell me more about the other technology you specified?")
        userInput = input("You:")#user inputs the name of the tech again 
        if (userInput == "-1"):#user doesn't give the name (won't be added to database)
            return "exiting" #do something about this
        elif (difflib.get_close_matches(userInput, commandDict['list'], 4, 0.6)):
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

            return "COMPA:Thank you for telling me about this new tech"
    else:
        #user adds new tech to database
        print("COMPA:I do not recognize the technologies you have specified...")
        print("COMPA:Could you tell me more about both of them" )#should get name of tech user input
        userInput = input("You:")#user inputs more info about said tech
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
        print("COMPA:" + botResponse)#check on this later
