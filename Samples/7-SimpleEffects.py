import sparkpy

#special effects example

#create office environment
sparkpy.Environment("Office")

x = 0 #x position 
y = -1 #y position
z= 0 #z position

#create a portal effect
portalEffect=sparkpy.Effect("portal",x,y,z)

#set colour to red from default
portalEffect.SetColour("red")
