import sparkpy

#create a trails object
t = sparkpy.Trails()

t.PenColour("green")

#move the trails object forward by a distance of 1 unit
#then turn left by 90 degrees. Repeat 4 times.
t.Forward(1)
t.Left(90)

t.Forward(1)
t.Left(90)

t.Forward(1)
t.Left(90)

t.Forward(1)
t.Left(90)