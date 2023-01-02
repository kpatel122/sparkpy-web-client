import sparkpy
import random

#create a trails object
t = sparkpy.Trails()

#set colour to red
colours = ["red","green","blue","yellow"]

#move the trails object forward by a distance of 1 unit
#then turn left by 90 degrees. Repeat 4 times using a loop.



for i in range(0,6):
    t.PenSize(0.2)
    #get the next colour from the colours list
    rand = random.randint(0,3)
    print(rand)
    t.PenColour(colours[rand])
    t.Forward(0.2)
    t.Left(60)

