import sparkpy

#basic quiz
#instructions
#walk into the red character to get a question
#enter answer into the input box

def InputEntered(inputText):
    if(inputText.lower() == "paris"):
        bryce.Chat("Correct!! ")
        bryce.SetAnimation("Celebration")
    else:
        bryce.Chat("Wrong")
        bryce.SetAnimation("Talking1")

#create collision handler function
def collision(id1,id2):
     
    if(bryce.GetId() == id1 or bryce.GetId() == id2):
        bryce.Chat("Whats the capital of france? ")
        sparkpy.ShowInputBox()

#assign the collision handler function
sparkpy.SetCollisionHandler(collision)
sparkpy.SetInputBoxHandler(InputEntered)

sparkpy.Environment("gasplanet");
lewis = sparkpy.Character("lewis");
bryce = sparkpy.Character("bryce",1,0,2);

lewis.ControlMode("third_person")