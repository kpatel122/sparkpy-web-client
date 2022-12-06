import sparkpy

#create a trails object
t = sparkpy.Trails()

#set colour to red
colours = ["red","green","blue","yellow"]

#move the trails object forward by a distance of 1 unit
#then turn left by 90 degrees. Repeat 4 times using a loop.

for i in range(0,4):
    #get the next colour from the colours list
    t.PenColour(colours[i])
    t.Forward(1)
    t.Left(90)
    