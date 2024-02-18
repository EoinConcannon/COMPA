import random

print("test")#test

userInput = input("Please enter something: ")

uniqueResponse = random.randint(1,4)

if(uniqueResponse == 1):
  print("You input \"" + userInput + "\"")

elif(uniqueResponse == 2):
  print(userInput + " " + userInput + " " + userInput + " " + userInput + " " + userInput)

elif(uniqueResponse == 3):
  print(("Your input was... " + userInput)[::-1])

elif(uniqueResponse == 4):
  print("The random number was " + str(uniqueResponse))

else:
  print ("ERROR")