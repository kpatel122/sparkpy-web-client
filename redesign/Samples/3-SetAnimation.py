import sparkpy

#set animation example

#create office environment
sparkpy.CreateEnvironment("Office")

#create robot character
ybot = sparkpy.CreateCharacter("YBot2")

#set animation to walk
sparkpy.SetAnimation(ybot, "Walk")

#set animation speed
sparkpy.SetAnimationSpeed(ybot, 1)
