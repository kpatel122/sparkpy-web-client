import sparkpy

#collision example

#create collision handler function
def collision(id1,id2):
    print("Handled " + str(id1) + "," + str(id2))
    collidedCharacter = sparkpy.GetCharacterFromID(id1)
    collidedCharacter.Chat("I collided")

#assign the collision handler function
sparkpy.SetCollisionHandler(collision)

#create an office environment
sparkpy.Environment("Office")

#create first character
robot1 = sparkpy.Character("YBot")
 

#create seconf character
robot2 = sparkpy.Character("XBot",2,0,0)

#control character by keyboard
robot1.ControlMode("keyboard")
