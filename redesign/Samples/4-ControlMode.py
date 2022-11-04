import sparkpy

#control character with keyboard example

#create office environment
sparkpy.CreateEnvironment("office")

#create robot character
ybot = sparkpy.CreateCharacter("YBot")

#set control mode to keyboard
sparkpy.SetControlMode(ybot,"keyboard")
