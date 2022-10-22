import sparkpy

#special effects example

#create office environment
sparkpy.CreateEnvironment("Office")

#create a portal effect
eid=sparkpy.CreateEffect("portal")

#set colour to red from default
sparkpy.SetEffectColour(eid,"red")
