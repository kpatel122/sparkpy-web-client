import sparkpy

#third person character control

#create environment
sparkpy.Environment("alienplanet")

#create character
lewis = sparkpy.Character("lewis")

#set control mode to keyboard
lewis.ControlMode("third_person")
