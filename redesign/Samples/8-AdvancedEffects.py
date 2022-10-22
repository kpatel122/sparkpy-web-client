import sparkpy

#advanced special effects

#create environment
sparkpy.CreateEnvironment("Office")

#cube position
x=0
y=0
z=0
scale = 2 # make the portal twice as normal

#create portal effect
eid=sparkpy.CreateEffect("portal",x,y,z,scale)

#set the colour
sparkpy.SetEffectColour(eid,"green","white")
