import sparkpy

#play sound example

#create office environment
sparkpy.CreateEnvironment("home")

#create robot character
xbot = sparkpy.CreateCharacter("xbot")

#set animation to dancing
sparkpy.SetAnimation(xbot, "dancing1")

#play background music, music will loop by default
sparkpy.PlaySceneSound("funkymusic1")
