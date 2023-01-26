import sparkpy

#play sound example

#create office environment
environment = sparkpy.Environment("home")

#create robot character
robot = sparkpy.Character("xbot")

#set animation to dancing
robot.SetAnimation("dancing1")

#play background music, music will loop by default
environment.PlaySound("funkymusic1")
