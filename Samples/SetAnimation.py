import sparkpy

#set animation example

#create office environment
sparkpy.Environment("office")

#create robot character
robot = sparkpy.Character("YBot")

#set animation to walk
robot.SetAnimation("Walk")
