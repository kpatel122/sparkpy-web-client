import sparkpy

#control character with keyboard example

#create office environment
sparkpy.Environment("office")

#create robot character
robot = sparkpy.Character("YBot")

#set control mode to keyboard
robot.ControlMode("keyboard")
