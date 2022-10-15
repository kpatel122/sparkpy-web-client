import pysparklib as pyspark


#create collision handler function
def collision(id1,id2):
    print("Handled " + str(id1) + "," + str(id2))

#assign the collision handler function
pyspark.SetCollisionHandler(collision)

#create an office environment
pyspark.CreateEnvironment("Office")

#create first character
uid = pyspark.CreateCharacter("YBot2")

#create seconf character
uid2 = pyspark.CreateCharacter("XBot2",2,0,0)

#control character by keyboard
pyspark.SetControlMode(uid,"keyboard")  
