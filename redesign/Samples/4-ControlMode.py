import sparkpylib as sparkpy

#control character with keyboard example

#create office environment
sparkpy.CreateEnvironment("Office")

#create robot character
ybot = sparkpy.CreateCharacter("YBot2")

#set control mode to keyboard
sparkpy.SetControlMode(ybot,"keyboard")
