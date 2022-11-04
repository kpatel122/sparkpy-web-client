import sparkpy

#set animation example

#create office environment
sparkpy.CreateEnvironment("office")

#create robot character
ybot = sparkpy.CreateCharacter("YBot")

#set animation to walk
sparkpy.SetAnimation(ybot, "Walk")

#set animation speed
sparkpy.SetAnimationSpeed(ybot, 1)
