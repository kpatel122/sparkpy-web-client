import sparkpy

#special effects example

#create office environment
sparkpy.CreateEnvironment("Office")

x = 0 #x position 
y = -1 #y position
z= 0 #z position

#create a portal effect
eid=sparkpy.CreateEffect("portal",x,y,z)

#set colour to red from default
sparkpy.SetEffectColour(eid,"red")
