import sparkpy

#advanced special effects

#create environment
sparkpy.Environment("Office")

#cube position
x=0
y=-1 #move to the floor
z=0
scale = 2 # make the portal twice as normal

#create portal effect
bigPortal=sparkpy.Effect("portal",x,y,z,scale)

#set the colour
bigPortal.SetColour("green","white")
