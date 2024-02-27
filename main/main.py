import numpy
import consoleColour as cc

print("COMPA:What is your name?")
userInput = input("You:")
print("COMPA:Hello " + userInput + ". I am COMPA, the comparison chatbot.")
print("COMPA:I am in a very early stage of development right now.")
print("COMPA:In the future, you will need to input two technologies for me to compare")
print("COMPA:type \"exit\" to stop the program\n")

while(userInput != "exit"):
    userInput = input("You:")
    userInput = userInput.lower()#converts to lowercase
    print(cc.ct.WARNING + "COMPA:" + cc.ct.ENDC +  userInput)

#currently in colourTest branch check the git repo to go back