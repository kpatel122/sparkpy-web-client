import sparkpy
import random

#number guessing game

#set the maximum value of the answer
maxAnswer = 10

#generate a random number
answer = random.randint(1,maxAnswer)

#input box handler function
def GuessEntered(guessValue):
    if( int(guessValue) == answer ):
        lewis.Chat("Correct!")
        lewis.SetAnimation("celebration")
        #once the input has been recieved, do not show the input box anymore
        sparkpy.HideInputBox()
    else:
        lewis.Chat("Wrong Try again")
        lewis.SetAnimation("talking1")

        
#create an environment
sparkpy.Environment("GasPlanet")

#create a character
lewis = sparkpy.Character("lewis")

lewis.Chat("Guess a number between 1 and " + str(maxAnswer))

#set the callback function
sparkpy.SetInputBoxHandler(GuessEntered)

#show input box
sparkpy.ShowInputBox()



    