import difflib
import time
import random
import json

with open("commands.json") as commands:
    commandDict = json.load(commands)
with open("responses.json") as responses:
    resDict = json.load(responses)
with open("techDatabase.json") as techDatabase:
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
    print("\nCOMPA:" + tech[0])#show name
    print("COMPA:" + tech[1])#show description
    print("COMPA:Some of " + tech[0] + " strengths are:")
    for pro in tech[2]:
        print("• " + tech[0] + random.choice(resDict['listRes'][0]['proRes']) + pro)#show pros
    print("COMPA:Some of " + tech[0] + " weaknesses are:")
    for con in tech[3]:
        print("• " + tech[0] + random.choice(resDict['listRes'][0]['conRes']) + con)#show cons
    return ""

#compares the differences between the two technologies
def displayingDifferences(tech1, tech2):
    listValues(tech1)
    listValues(tech2)
    similarityCheck = 0
    getNameDiff = difflib.SequenceMatcher(None, tech1[0], tech2[0])
    getNameRatio = getNameDiff.ratio()

    if(getNameRatio >= 0.5):#if both tech have a similar name
        print("COMPA:" + tech1[0] + " and " + tech2[0] + " have similar names.")
        similarityCheck += 1
    for pro in tech1[2]:
        for otherCon in tech2[3]:
            if(pro == otherCon):#if a pro in tech1 is found in tech2 cons
                print("COMPA:" + tech1[0] + random.choice(resDict['compareRes'][0]['proRes']) + pro + " than " + tech2[0])
                similarityCheck += 1
        for otherPro in tech2[2]:
            if(pro == otherPro):#pro both tech have
                print("COMPA:" + tech1[0] + " and " + tech2[0] + random.choice(resDict['compareRes'][0]['equalGoodRes']) + pro)
                similarityCheck += 1
    for con in tech1[3]:
        for otherPro in tech2[2]:
            if(con == otherPro):#if a con in tech1 is found in tech2 pros
                print("COMPA:" + tech1[0] + random.choice(resDict['compareRes'][0]['conRes']) + con + " than " + tech2[0])
                similarityCheck += 1
        for otherCon in tech2[2]:
            if(con == otherCon):#con both tech have
                print("COMPA:" + tech1[0] + " and " + tech2[0] + random.choice(resDict['compareRes'][0]['equalBadRes']) + con)
                similarityCheck += 1
    if(similarityCheck == 0):#no pros or cons or similarities found
        print("COMPA:" + tech1[0] + " and " + tech2[0] + random.choice(resDict['compareRes'][0]['noSimilarityRes']))
    return ""

def createNewData(tech):
    emptyList = []

    print("COMPA:Could you tell me the name of this technology again?")
    userInput = input("You:")
    userInput = userInput.lower() #user input is converted to lower case
    tech.append(userInput) #add a loop to prevent duplicate names
    print("COMPA:Can you give a brief description of this technology.")
    userInput = input("You:")
    tech.append(userInput)#description is not converted to lower case
    print("COMPA:Can you give me an advantage this technology has?")
    userInput = input("You:")
    while True:#checks if the current word some what matchs a word in the json)
        userInput = userInput.lower()
        emptyList.append(userInput)
        print("COMPA:Any other advantages?")
        userInput = input("You:")
        if(difflib.get_close_matches(userInput, commandDict['no'], 4, 0.6)) or difflib.get_close_matches(userInput, commandDict['stop'], 4, 0.6) or (userInput == "-1"):
            tech.append(emptyList)
            break
    emptyList = [] #reusing the list
    print("COMPA:Can you give me one disadvantage this technology suffers from?")
    userInput = input("You:")
    while True:
        userInput = userInput.lower()
        emptyList.append(userInput)
        print("COMPA:Any other disadvantages?")
        userInput = input("You:")
        if(difflib.get_close_matches(userInput, commandDict['no'], 4, 0.6)) or difflib.get_close_matches(userInput, commandDict['stop'], 4, 0.6) or (userInput == "-1"):
            tech.append(emptyList)
            break
    #creating object to append to file
    jsonObj = {
                "name":tech[0],
                "desc":tech[1],
                "pro": tech[2],
                "con": tech[3],
              }
            
    addToDatabase(jsonObj)
    techDict["tech"].append(jsonObj)
    return ""

def processUserInput(userInput):
    for currentWord in userInput:#loops through the user's string input
        word = difflib.get_close_matches(currentWord, commandDict['compare'], 4, 0.6)#checks if the current word some what matchs a word in the json
        ifWord = ''.join(word)
        if (ifWord == ""):#if user input doesn't match word in json "commands"
            continue
        else:
            #stops reading list here and moves into next function
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
                    tech1.append(techItem["desc"])
                    tech1.append(techItem["pro"])
                    tech1.append(techItem["con"])
                    twoCheck += 1
                elif (twoCheck == 1):#second technology matches
                    tech2.append(techItem["name"])
                    tech2.append(techItem["desc"])
                    tech2.append(techItem["pro"])
                    tech2.append(techItem["con"])
                    twoCheck += 1
            else: #if user input doesn't match word in json "techDatabase"
                continue
           
    if (twoCheck == 2):
        #list differences between specified tech
        displayingDifferences(tech1, tech2)
        return ""
    if (twoCheck == 1):
        #either list what recognized tech has or user adds new tech to database
        print("COMPA:I only recognize " + tech1[0] + " but not the other technology you specified.")
        print("COMPA:Would you like me to list the properties of " + tech1[0] + ".")
        print("COMPA:Or could you tell me more about the other technology you specified?")
        userInput = input("You:")#user inputs the name of the tech again 
        if (difflib.get_close_matches(userInput, commandDict['no'], 4, 0.6)) or (userInput == "-1"):#user doesn't give the name (won't be added to database)
            return ""
        elif (difflib.get_close_matches(userInput, commandDict['yes'] + commandDict['list'], 4, 0.6)):
            listValues(tech1)
            return ""
        else:
            createNewData(tech2)
            return "COMPA:Thank you for telling me about this new tech"
    else:
        #user adds new tech to database
        print("COMPA:I do not recognize any of the technologies you have specified...")
        print("COMPA:Could you tell me more about one of them?")
        userInput = input("You:")
        if (difflib.get_close_matches(userInput, commandDict['no'], 4, 0.6)) or (userInput == "-1"):
            return ""
        else:
            createNewData(tech1)
            return "COMPA:Thank you for sharing this information with me."

#welcome message
print("COMPA:What is your name?")
userInput = input("You:")
print("COMPA:Hello " + userInput + ". I am COMPA, the comparison chatbot.")
print("COMPA:I am still in my development stage right now.")
print("COMPA:Please give me the names of two technologies and I will compare them.")
print("COMPA:type \"-1\" to exit the program or to CANCEL a process at anytime in the program")

while(userInput != "-1"):
    print("\nCOMPA:What technologies do you wish to compare?")
    userInput = input("You:")
    if (userInput != "-1"):
        userInput = userInput.lower().split()#converts to lowercase and each word is put into a list
        botResponse = processUserInput(userInput)
        print(botResponse)
    else:
        break