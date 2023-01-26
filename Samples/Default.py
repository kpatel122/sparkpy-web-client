import sparkpy

#hello world example

#create environment
sparkpy.Environment("forest")

#create robot character
robot = sparkpy.Character("YBot")

#set talking animation
robot.SetAnimation("Talking1")

#create a speech box
robot.Chat("Hello World")