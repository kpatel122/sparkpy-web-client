import sparkpy

#collision example

#create collision handler function
def collision(id1,id2):
    print("Handled " + str(id1) + "," + str(id2))

#assign the collision handler function
sparkpy.SetCollisionHandler(collision)

#create an office environment
sparkpy.CreateEnvironment("Office")

#create first character
uid = sparkpy.CreateCharacter("YBot")

#create seconf character
uid2 = sparkpy.CreateCharacter("XBot",2,0,0)

#control character by keyboard
sparkpy._SetControlMode(uid,"keyboard")
