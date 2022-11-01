#reference: https://docs.unity3d.com/Manual/webgl-interactingwithbrowserscripting.html

from browser import document,window,bind,aio
import traceback

PARAM_DELIMINATOR = '|' #unity SendMessage only accepts one parameter so pack multiple params with this deliminator, unity uses the same character to unpack the values

#enviroment return
VALID_ENVIROMENT = 1
INVALID_ENVIROMENT = 0

#character returns
INVALID_CHARACTER = 0

#sound returns
FAILURE = 0
NO_SOUND_CLIP = 2

unityInstance = window.unint
pysparkClass = "Main" #the name of the unity class that contains the lib methods

CollisionHandler = None #collision function pointer
InputHandler     = None #input bix function pointer

#unity events div name
SPARKPY_EVENT = "unity_events"

#event names set in Unity Plugins/pyslib.jslib
EVENT_COLLISION = "Collision"
EVENT_INPUT = "InputText"


#must map to unity C# public enum  AppPrimitiveType
PRIMITIVE_SPHERE = 0
PRIMITIVE_CAPSULE = 1
PRIMITIVE_CYLINDER = 2
PRIMITIVE_CUBE = 3
PRIMITIVE_PLANE = 4
PRIMITIVE_QUAD = 5

#primitive returns
INVALID_PRIMITIVE = 0

#map strings to primitives
primativeMap = {"sphere": PRIMITIVE_SPHERE, "capsule": PRIMITIVE_CAPSULE,
                "cylinder": PRIMITIVE_CYLINDER, "cube": PRIMITIVE_CUBE,
                "plane": PRIMITIVE_PLANE, "quad": PRIMITIVE_QUAD}

#primitive move directions
UP = 0
DOWN=1
LEFT=2
RIGHT=3
FORWARD=4,
BACKWARD=5

#map strings to directions
directionMap = {"up": UP, "down": DOWN,
                "left": LEFT, "right": RIGHT,
                "forward": FORWARD, "backward": BACKWARD}

#valid special effectnames
specialEffectNames = ["portal"]

#must map to unity C# public enum  AppColour
COLOUR_YELLOW = 0
COLOUR_CLEAR = 1
COLOUR_GREY = 2
COLOUR_MAGENTA = 3
COLOUR_CYAN = 4
COLOUR_RED = 5
COLOUR_BLACK = 6
COLOUR_WHITE = 7
COLOUR_BLUE = 8
COLOUR_GREEN = 9

colourMap = {"yellow": COLOUR_YELLOW, "clear": COLOUR_CLEAR, "grey": COLOUR_GREY, "magenta": COLOUR_MAGENTA,
            "cyan": COLOUR_CYAN, "red": COLOUR_RED,"black": COLOUR_BLACK, "white": COLOUR_WHITE,
            "blue": COLOUR_BLUE, "green": COLOUR_GREEN}

@bind(document[SPARKPY_EVENT], EVENT_INPUT)
def InputTextHook(ev):
    #call the input text box handler
    #check if the handler has been set
    if(InputHandler != None):
        InputHandler(ev.detail) #call the function handler

def SetInputBoxHandler(handler):
    '''Assigns a function to handle input box 
    
    :param handler: the function to handle the when input box text is entered, signature should have 1 string parameter that gets set to the input box text e.g. InputHandler(msg)
    :type handler: function pointer
    
    :return: None
    
    '''
    global InputHandler
    InputHandler = handler

@bind(document[SPARKPY_EVENT], EVENT_COLLISION)
def ColiisionHook(ev):
    if(CollisionHandler != None): #Collision handler is set with SetCollisionHandler call
        CollisionHandler(ev.detail.uid1,ev.detail.uid2) #call the user defined function handler

def SetCollisionHandler(handler):
    '''Creates assigns a function to handle collision, the function should accept two parameters which are the uids on which the collisions occured
    
    :param handler: the function to handle the collision, signature should have two parameters for the collision uids e.g. handlerFunction(uid1,uid2)
    :type handler: function pointer
    
    :return: None
    
    '''
    global CollisionHandler
    CollisionHandler = handler

def ErrorMsg(method, msg):
    print("ERROR: " + method + ": " + str(msg))

def ResetScene():
    '''Resets the scene- removes environment and all characters
    '''
    #note this function is implicitly called in the webpage on the play button
    #title="run code" id="run" type="button" aria-label="run_code" onclick="unityRestScene()
    
    #reset the collision handler
    global CollisionHandler
    CollisionHandler = None 
    
    #call unity function
    unityInstance.SendMessage(pysparkClass, "ResetScene")

def CreateEnvironment(environmentName, location=0):
    '''Creates an scene environment

    :param environmentName: The environment name to create
    :type environmentName: string
    
    :param location: The location of the environment
    :type location: int, optional, defaults to 0
    
    :return: None
    '''
    methodName = "CreateEnvironment" #used for error messages
    
    #data type checks
    try:
        environmentNameString = str(environmentName)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter environment name was not a string. environmentName=" +environmentName)
        return 0

    try:
        locationInt = int(location)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter location value was not an integer. location=" + location)
        return 0
    #create parameter string
    params = environmentNameString + PARAM_DELIMINATOR + str(locationInt)
    
    #call the unity function
    unityInstance.SendMessage(pysparkClass, "CreateEnvironment",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    if(result!=VALID_ENVIROMENT):
        ErrorMsg(methodName, "\'" + environmentName + "\' does not exist")
    
    return result

def CreateCharacter(characterName,x=0,y=0,z=0):
    '''Creates an scene character

    :param characterName: The name of the character to create
    :type characterName: string
    
    :return: characterID (int)- unique ID of the character
    '''
    #create parameter string
    params = characterName + PARAM_DELIMINATOR + str(x) + PARAM_DELIMINATOR + str(y) + PARAM_DELIMINATOR + str(z)
    
    #call unity function
    unityInstance.SendMessage(pysparkClass, "CreateSceneObject",params)

    #get the return value from the unity function
    result = int(document["unity_return_values"].value)

    #check success or failure
    if(result == INVALID_CHARACTER):
        ErrorMsg("CreateCharacter", "\'" +characterName + "\' does not exist")

    return result
   
def SetAnimationSpeed(characterID, speed):
    '''Sets the animation speed for the charcter

    :param characterID: The characterID to set
    :type characterID: int

    :param speed: The speed of the animation
    :type speed: float 
    
    :return: 1 on success or 0 on failure  
    '''
    methodName = "SetAnimationSpeed"

    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
    try:
        animSpeed = float(speed)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter speed was not a float. speed=\'"+ str(speed) + "\'")
        return 0
    
    #create parameter string
    params = str(characterID) + PARAM_DELIMINATOR + str(animSpeed)

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "SetAnimationSpeed",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result

def SetAnimation(characterID, animationName, resetTrigger = False):
    '''Sets the animation for the charcter

    :param characterID: The characterID to set the snimation for
    :type characterID: int
    
    :param animationName: The name of the animation
    :type animationName: string
    
    :param resetTrigger: unity animation trigger reset
    :type resetTrigger: bool, defaults to False 
    
    :return: 1 on success or 0 on failure 
    '''

    methodName = "SetAnimation" #used for error messages

    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
    try:
        animation = str(animationName)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter animationName was not a string. animationName=\'"+ animationName + "\'")
        return 0
    try:
        trigger = bool(resetTrigger)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter resetTrigger was not a bool. resetTrigger=\'"+ str(resetTrigger) + "\'")
        return 0
    
    #create parameter string
    params = str(characterID) + PARAM_DELIMINATOR + str(animationName) + PARAM_DELIMINATOR + str(resetTrigger)

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "SetAnimation",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result

def SetControlMode(characterID, mode):
    '''Sets the control mode for the charcter as either 'script' or 'keyboard'

    :param characterID: The characterID to set
    :type characterID: int
    
    :param mode: 'script'- control through move, rotate etc. 'keyboard'- control through a,w,d,s & space (3rd person control)
    :type mode: string 
    
    :return: 1 on success or 0 on failure

    '''
    methodName = "SetControlMode"
    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
    try:
        animation = str(mode)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter mode was not a string. mode=\'"+ mode + "\'")
        return 0

    mode = mode.lower()

    #map the string to the unity enum value
    SCRIPT = 0
    KEYBOARD = 1
    modeEnum = 0 

    if mode == "keyboard":
        modeEnum = KEYBOARD
    elif mode == "script":
        modeEnum = SCRIPT
    else:
        ErrorMsg(methodName,"parameter mode has invalid value mode=\'"+ mode + "\'. Valid values are \'script\' or \'keyboard\'")
        return 0

    #create parameter string
    params = str(characterID) + PARAM_DELIMINATOR + str(modeEnum)

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "SetControlMode",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result

def Show(characterID):
    '''Sets the character to be visible

    :param characterID: The characterID to set
    :type characterID: int
    
    :return: 1 on success or 0 on failure 
    
    '''
    methodName = "Show"
    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
     
    #create parameter string
    params = str(characterID)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "Show",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result
    
def Hide(characterID):
    '''Sets the character to be invisible

    :param characterID: The characterID to set
    :type characterID: int
    
    :return: 1 on success or 0 on failure 
    
    '''
    methodName = "Hide"

    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
     
    #create parameter string
    params = str(characterID)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "Hide",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result 

def Rotate(characterID, degrees, seconds, direction = "cw"):

    '''rotates a character to degrees in seconds. direction is cw (clockwise) or ccw (counter clockwise)

    :param characterID: The characterID to rotate
    :type characterID: int
    
    :param degrees: how many degrees to rotate
    :type degrees: float
    
    :param seconds: how long the character rotates for in seconds
    :type seconds: float
    
    :param direction: which direction to rotate- cw or ccw
    :type direction: string defaults to cw
    
    :return: 1 on success or 0 on failure 
    '''

    methodName = "Rotate" #used for error messages

    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
    try:
        secondsToReachTarget = float(seconds)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter seconds was not a float. seconds=\'"+ seconds + "\'")
        return 0
    try:
        targetDegrees = float(degrees)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter degrees was not a float. degrees=\'"+ str(degrees) + "\'")
        return 0

    direction = direction.lower()

    #map the string to the unity enum value
    CW = 1
    CCW = 2
    dirEnum = CW 

    if direction == "cw":
        dirEnum = CW
    elif direction == "ccw":
        dirEnum = CCW
    else:
        ErrorMsg(methodName,"parameter direction has invalid value direction=\'"+ direction + "\'. Valid values are \'cw\' or \'ccw\'")
        return 0

    #create parameter string
    params = str(characterID) + PARAM_DELIMINATOR + str(secondsToReachTarget) + PARAM_DELIMINATOR + str(targetDegrees) + PARAM_DELIMINATOR+ str(dirEnum)

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "Rotate",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result

def Move(characterID, seconds, speed=1):
    '''moves a character forward at 'speed' for 'seconds'

    :param characterID: The characterID to rotate
    :type characterID: int
    
    :param seconds: how long the character moves for in seconds
    :type seconds: float
    
    :param speed: how fast to move, defaults to 1
    :type speed: float
    
    :return: 1 on success or 0 on failure 
    '''
    methodName = "Move" #used for error messages

    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
    try:
        secondsToReachTarget = float(seconds)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter seconds was not a float. seconds=\'"+ seconds + "\'")
        return 0
    try:
        moveSpeed = float(speed)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter speed was not a float. speed=\'"+ str(speed) + "\'")
        return 0

    #create parameter string
    params = str(characterID) + PARAM_DELIMINATOR + str(secondsToReachTarget) + PARAM_DELIMINATOR + str(moveSpeed)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "Move",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result

#TODO add hide chat

def Chat(characterID, text, seconds):
    '''Displays a chat box above the character with 'text' for 'seconds'

    :param characterID: The characterID to rotate
    :type characterID: int

    :param text: the text for the chat box
    :type text: string

    :param seconds: how long to show the chat bubble for in seconds
    :type seconds: float

    :return: 0 on failure or 1 on success

    .. code-block:: python
        :linenos:
        
        #https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#showing-code-examples
        print('hello world')
    '''

    methodName = "ChatBubble" #used for error messages

    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
    try:
        textToShow = str(text)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter text was not a string. text=\'", text ,"\'")
        return 0
    try:
        secondsToShow = float(seconds)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter seconds was not a float. seconds=\'"+ str(seconds) + "\'")
        return 0

    #create parameter string
    params = str(characterID) + PARAM_DELIMINATOR + str(textToShow) + PARAM_DELIMINATOR + str(secondsToShow)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "ChatBubble",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result

#examples of input retrival can be found at samples/InputMethods.py
def ShowInputBox():
    '''Shows an input box, event with enetered text will be triggered on div id 'UNITY_EVENTS_DIV'. 'UNITY_EVENTS_DIV.value' will also hold the result of the text entered  
    '''
    unityInstance.SendMessage(pysparkClass, "ShowInputBox")

def GetInputBoxValue():
    ''' Retrurns the text of an input box, should only be used after *await aio.event(SPARKPY_EVENT, EVENT_INPUT)* 
     :return: text of input box 
    '''
    return document[SPARKPY_EVENT].value

def HideInputBox():
    '''Hides an input box 
    '''
    unityInstance.SendMessage(pysparkClass, "HideInputBox")

def PlaySceneSound(clipname, volume = 1.0 ,loop = True):
    '''Plays Scene audio clip. Mainly used for background music 

    :param clipname: name of the sound clip to play
    :type clipname: string
    
    :param volume: the volume of the clip
    :type volume: float optional, defaults to 1
    
    :param loop: whether to loop back to the beginning of the clip when finished
    :type loop: bool optional, defaults to True
    
    :return: 1 on success or 0 on failure 
    '''

    methodName = "PlaySceneSound" #used for error messages

    #data type checks
    try:
        clip = str(clipname)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter clipname was not a string. clipname=\'", clipname ,"\'")
        return 0
    try:
        vol = float(volume)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter volume was not a float. volume=\'"+ str(volume) + "\'")
        return 0
    try:
        looped = bool(loop)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter loop was not a float. loop=\'"+ str(loop) + "\'")
        return 0

    #create parameter string
    params = str(clip) + PARAM_DELIMINATOR + str(vol) + PARAM_DELIMINATOR + str(looped)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "PlayBackgroundSound",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == FAILURE):
        ErrorMsg(methodName," Invalid sound clip name. clipname=\'"+ str(clipname) + "\'")

    return result

def StopSceneSound():
    '''Stops the scene's audio clip
    '''
    #call the unity function
    unityInstance.SendMessage(pysparkClass, "StopBackgroundSound")
    
def PlayCharacterSound(characterID, clipname, volume = 1.0 ,loop = False):
    '''Plays character audio clip.   

    :param clipname: name of the sound clip to play
    :type clipname: string
    
    :param volume: the volume of the clip
    :type volume: float, defaults to 1 (0-lowest 1-highest)
    
    :param loop: whether to loop back to the beginning of the clip when finished
    :type loop: bool optional, defaults to False
    
    :return: 1 on success or 0 on failure
    '''

    methodName = "PlayCharacterSound" #used for error messages

    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
    try:
        clip = str(clipname)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter clipname was not a string. clipname=\'", clipname ,"\'")
        return 0
    try:
        vol = float(volume)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter volume was not a float. volume=\'"+ str(volume) + "\'")
        return 0
    try:
        looped = bool(loop)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter loop was not a float. loop=\'"+ str(loop) + "\'")
        return 0

    #create parameter string
    params = str(characterID) + PARAM_DELIMINATOR + str(clip) + PARAM_DELIMINATOR + str(vol) + PARAM_DELIMINATOR + str(looped)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "PlayCharacterSound",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == NO_SOUND_CLIP):
        ErrorMsg(methodName," Invalid sound clip name. clipname=\'"+ str(clipname) + "\'")
    elif(result == FAILURE):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")
    
    return result

def StopCharacterSound(characterID):
    '''Stops the character's sound clip playing

    :param characterID: The characterID to stop audio for
    :type characterID: int
    
    :return: 1 on success or 0 on failure 
    
    '''
    methodName = "StopCharacterSound"

    #data type checks
    try:
        uid = int(characterID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter characterID was not an int. characterID=\'"+ str(characterID) + "\'")
        return 0
     
    #create parameter string
    params = str(characterID)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "StopCharacterSound",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_CHARACTER):
        ErrorMsg(methodName,"Invalid characterID. characterID=\'"+ str(characterID) + "\'")

    return result

 

def CreatePrimitive(primitiveType, x=0, y=0, z=0):
    '''Creates a scene primitive

    :param primitiveType: the type of primitive to create
    :type primitiveType: string- values can be:sphere,capsule,cylinder,cube,plane, quad
    
    :param x: x position
    :type x: float optional, defaults to 0
    
    :param y: y position
    :type y: float optional, defaults to 0
    
    :param z: z position
    :type z: float optional, defaults to 0
    
    :return: int primitiveID- unique ID of the primitive
    '''
    methodName = "CreatePrimitive"
    primitiveType = primitiveType.lower()

    #check for valid primitive
    if primitiveType not in primativeMap:
        ErrorMsg(methodName,"Invalid primitive type. type=\'"+ str(type) + "\'")
        return 0
    
    #data type checks
    try:
        x = float(x)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter x was not a float. x=\'"+ str(x) + "\'")
        return 0
    try:
        y = float(y)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter y was not a float. y=\'"+ str(y) + "\'")
        return 0
    try:
        z = float(z)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter y was not a float. y=\'"+ str(y) + "\'")
        return 0

    primitiveType = primativeMap[primitiveType]

    #create parameter string
    params = str(primitiveType) + PARAM_DELIMINATOR + str(x) + PARAM_DELIMINATOR + str(y) + PARAM_DELIMINATOR + str(z) 

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "CreatePrimitive",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    return result


def RotatePrimitive(primitiveID,speedY, speedX=0,speedZ=0):
    '''Rotates primitive around it's x, y z axis

    :param primitiveID: the id of the primitive to rotate
    :type primitiveID: int
    
    :param speedY: how fast to rotate around the Y axis
    :type speedY: int 
    
    :param speedX: how fast to rotate around the X axis
    :type speedX: int optional, defualts to 0
    
    :param speedZ: how fast to rotate around the z axis
    :type speedZ: int optional, defualts to 0
    
    :return: 1 on success or 0 on failure
    '''
    methodName = "RotatePrimitive"

    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"primitiveID was not a primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0
    try:
        speedX = int(speedX)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter speedX was not an int. speedX=\'"+ str(speedX) + "\'")
        return 0
    try:
        speedY = int(speedY)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter speedY was not an int. speedY=\'"+ str(speedY) + "\'")
        return 0
    try:
        speedZ = int(speedZ)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter speedZ was not an int. speedZ=\'"+ str(speedZ) + "\'")
        return 0

    #create parameter string
    params = str(primitiveID) + PARAM_DELIMINATOR + str(speedX) + PARAM_DELIMINATOR + str(speedY) + PARAM_DELIMINATOR + str(speedZ)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "RotatePrimitive",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check if the character was valid
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result


def MovePrimitive(primitiveID, seconds, speed, direction):
    '''moves a primitive for 'seconds' at a rate of 'speed' in 'direction'

    :param primitiveID: primitiveID  
    :type primitiveID: int
    
    :param seconds: how long the primitive moves for in seconds
    :type seconds: float
    
    :param speed: how fast to move 
    :type speed: float
    
    :param direction: which direction to move the primitive 
    :type direction: string, values#; 'up','down','left','right','forward','backward'
    
    :return: 1 on success or 0 on failure 
    '''
    methodName = "MovePrimitive"
    direction = direction.lower()

    #check for valid primitive
    if direction not in directionMap:
        ErrorMsg(methodName,"Invalid direction. type=\'"+ str(direction) + "\'")
        return 0
    
    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0
    try:
        seconds = float(seconds)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter seconds was not a float. seconds=\'"+ str(seconds) + "\'")
        return 0
    try:
        speed = float(speed)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter speed was not a float. speed=\'"+ str(speed) + "\'")
        return 0
    
    #create parameter string
    params = str(primitiveID) + PARAM_DELIMINATOR + str(seconds) + PARAM_DELIMINATOR + str(speed) + PARAM_DELIMINATOR + str(directionMap[direction]) 

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "MovePrimitive",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    #return result
    return 0

def LoopPrimitiveMove(primitiveID, seconds, speed, direction):
    '''loop moves a primitive for 'seconds' at a rate of 'speed' in 'direction' and then back to its original position again
    
    :param primitiveID: primitiveID  
    :type primitiveID: int
    
    :param seconds: how long the primitive moves for in seconds
    :type seconds: float
    
    :param speed: how fast to move 
    :type speed: float
    
    :param direction: which direction to move the primitive 
    :type direction: string, values#; 'up','down','left','right','forward','backward'
    
    :return: 0 on failure or 1 on success
    '''
    methodName = "LoopPrimitiveMove"
    direction = direction.lower()

    #check for valid primitive
    if direction not in directionMap:
        ErrorMsg(methodName,"Invalid direction. type=\'"+ str(direction) + "\'")
        return 0
    
    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0
    try:
        seconds = float(seconds)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter seconds was not a float. seconds=\'"+ str(seconds) + "\'")
        return 0
    try:
        speed = float(speed)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter speed was not a float. speed=\'"+ str(speed) + "\'")
        return 0
    
    #create parameter string
    params = str(primitiveID) + PARAM_DELIMINATOR + str(seconds) + PARAM_DELIMINATOR + str(speed) + PARAM_DELIMINATOR + str(directionMap[direction]) 

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "LoopPrimitiveMove",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result



def StopPrimitiveRotation(primitiveID):
    '''stops a rotating primitive
    
    :param primitiveID: primitiveID  
    :type primitiveID: int
    
    :return: 1 on success, 0 on failure 
    
    '''
    methodName = "StopPrimitiveRotation"

    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "StopPrimitiveRotation",primitiveID)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result

def StopPrimitiveMove(primitiveID):
    '''stops a moving primitive

    :param primitiveID: primitiveID
    :type primitiveID: int  
    
    :return: 1 on success, 0 on failure
    
    '''
    methodName = "StopPrimitiveMove"
    
    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "StopPrimitiveMove",int(primitiveID))

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result

def HidePrimitive(primitiveID):
    '''hides a primitive

    :param primitiveID: primitiveID
    :type primitiveID: int 
    
    :return: 1 on success, 0 on failure
    '''
    methodName = "HidePrimitive"
    
    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "HidePrimitive",primitiveID)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result

def ShowPrimitive(primitiveID):
    '''shows a primitive
    
    :param primitiveID: primitiveID
    :type primitiveID: int 

    :return: 1 on success, 0 on failure
    '''
    methodName = "ShowPrimitive"
    
    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "ShowPrimitive",primitiveID)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result

def DestroyPrimitive(primitiveID):
    '''destroys a primitive

    :param primitiveID: primitiveID
    :type primitiveID: int 
    
    :return: 1 on success, 0 on failure
    '''
    methodName = "DestroyPrimitive"
    
    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0


    print("Destroy called")

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "DestroyPrimitive",primitiveID)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result

def BoundsCheckInc(value,min,max): #inclusive boundary check
    return ((float(value) >= float(min) ) and (float(value)<=float(max)))

def SetPrimitiveColour(primitiveID, red, green,blue,alpha=1):
    '''sets the colour of a primitive

    :param primitiveID: primitiveID  
    :type primitiveID: int
    
    :param red: the red value of the colour (0-1)
    :type red: float
    
    :param green: the green value of the colour (0-1)
    :type green: float
    
    :param blue: the blue value of the colour (0-1)
    :type alhpa: float
    
    :param alpha: alpha(transparaency) value of the colour (0-1)
    :type alpha: float optional, defaults to 1
    
    :return: 1 on success, 0 on failure
    '''
    methodName = "SetPrimitiveColour"
    
    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0
    try:
        red = float(red)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter red was not a float. red=\'"+ str(red) + "\'")
        return 0
    try:
        green = float(green)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter green was not a float. green=\'"+ str(green) + "\'")
        return 0
    try:
        blue = float(blue)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter blue was not a float. blue=\'"+ str(blue) + "\'")
        return 0
    try:
        alpha = float(alpha)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter alpha was not a alpha. alpha=\'"+ str(alpha) + "\'")
        return 0

    #boundary check
    if(BoundsCheckInc(red,0,1)==False):
        ErrorMsg(methodName,"Parameter red can have a value between 0 and 1. red value is \'"+str(red)+"\'")
        return 0
    if(BoundsCheckInc(green,0,1)==False):
        ErrorMsg(methodName,"Parameter green can have a value between 0 and 1. green value is \'"+str(green)+"\'")
        return 0
    if(BoundsCheckInc(blue,0,1)==False):
        ErrorMsg(methodName,"Parameter blue can have a value between 0 and 1. blue value is \'"+str(blue)+"\'")
        return 0
    if(BoundsCheckInc(alpha,0,1)==False):
        ErrorMsg(methodName,"Parameter alpha can have a value between 0 and 1. alpha value is \'"+str(alpha)+"\'")
        return 0


     #create parameter string
    params = str(primitiveID) + PARAM_DELIMINATOR + str(red) + PARAM_DELIMINATOR + str(green) + PARAM_DELIMINATOR + str(blue) + PARAM_DELIMINATOR + str(alpha) 

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "SetPrimitiveColour",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result

def ScalePrimative(primitiveID,size):
    '''uniform primative scale

    :param primitiveID: primitiveID  
    :type primitiveID: int
    
    :param size: size of scale
    :type size: float
    
    '''
    #wrapper call
    result = ScalePrimative(primitiveID,size,size,size)
    return result



def ScalePrimative(primitiveID,x,y,z):
    '''non-uniform primative scale
    
    :param primitiveID: primitiveID  
    :type primitiveID: int
    
    :param x: x axis scale
    :type x: float
    
    :param y: y axis scale
    :type y: float
    
    :param z: z axis scale
    :type z: float
    
    :return: 1 on success,0 on failure
    '''

    methodName = "ScalePrimative"
    
    #data type checks
    try:
        primitiveID = int(primitiveID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter primitiveID was not a int. primitiveID=\'"+ str(primitiveID) + "\'")
        return 0
    try:
        x = float(x)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter x was not a float. x=\'"+ str(x) + "\'")
        return 0
    try:
        y = float(y)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter y was not a float. y=\'"+ str(y) + "\'")
        return 0
    try:
        z = float(z)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter z was not a float. z=\'"+ str(z) + "\'")
        return 0
    
     #create parameter string
    params = str(primitiveID) + PARAM_DELIMINATOR + str(x) + PARAM_DELIMINATOR + str(y) + PARAM_DELIMINATOR + str(z)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "ScalePrimative",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid primitiveID. primitiveID=\'"+ str(primitiveID) + "\'")

    return result


def CreateEffect(effectName, x=0, y=0, z=0,scale=1):
    '''Creates a special effect

    :param effectName: the name of the effect
    :type effectName: string- valid values are stored in specialEffectNames
    
    :param x: x position
    :type x: float optional, defaults to 0
    
    :param y: y position
    :type y: float optional, defaults to 0
    
    :param z: z position
    :type z: float optional, defaults to 0
    
    :param scale: scale(size) of the effect
    :type scale: float optional, defaults to 1
    
    :return: int -effectID, unique ID of the effect
    '''
    methodName = "CreateEffect"
    effectName = effectName.lower()

    #check for valid primitive
    if effectName not in specialEffectNames:
        ErrorMsg(methodName,"Invalid effect name. name=\'"+ str(type) + "\'")
        return 0
    
    #data type checks
    try:
        x = float(x)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter x was not a float. x=\'"+ str(x) + "\'")
        return 0
    try:
        y = float(y)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter y was not a float. y=\'"+ str(y) + "\'")
        return 0
    try:
        z = float(z)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter z was not a float. z=\'"+ str(z) + "\'")
        return 0
    try:
        scale = float(scale)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter scale was not a float. scale=\'"+ str(scale) + "\'")
        return 0
    
    #create parameter string
    params = effectName + PARAM_DELIMINATOR + str(x) + PARAM_DELIMINATOR + str(y) + PARAM_DELIMINATOR + str(z) + PARAM_DELIMINATOR + str(scale)

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "CreateEffect",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    return result

def StopEffect(effectID):
    '''stops an effect

    :param effectID: effectID
    :type effectID: int 
    
    :return: 1 on success, 0 on failure
    '''
    methodName = "StopEffect"
    
    #data type checks
    try:
        effectID = int(effectID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter effectID was not a int. effectID=\'"+ str(effectID) + "\'")
        return 0

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "StopEffect",effectID)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    #check result
    if(result == INVALID_PRIMITIVE):
        ErrorMsg(methodName,"Invalid effectID. effectID=\'"+ str(effectID) + "\'")

    return result



def SetEffectColour(effectID, startColour,endColour="white"):
    '''sets the effect colour, valid colours: 'yellow','clear','grey','magenta','cyan','red','black','white','blue' & 'green'
    
    :param effectID: the ID of the effect
    :type effectID: int 
    
    :param startColour: start colour of the effect
    :type startColour: string 
    
    :param endColour: start colour of the effect
    :type endColour: string optional, defaults to white 
    
    :return: 1 on success, 0 on failure
    '''
    methodName = "SetEffectColour"
    
    #change colour values to lowercase
    startColour = startColour.lower()
    endColour = endColour.lower()

    #check for valid colour values
    if startColour not in colourMap:
        ErrorMsg(methodName,"Invalid startColour. startColour=\'"+startColour+"\'")
        return 0
    if endColour not in colourMap:
        ErrorMsg(methodName,"Invalid endColour. endColour=\'"+endColour+"\'")
        return 0
    
    #data type checks
    try:
        effectID = int(effectID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter effectID was not a int, effectID=\'"+ str(effectID) + "\'")
        return 0
    
    #create parameter string
    
    startColourString = str(colourMap[startColour])
    endColourString = str(colourMap[endColour])
    
    #params = str(effectID) + PARAM_DELIMINATOR + str(colourMap[startColour]) + PARAM_DELIMINATOR + str(colourMap[endColour])
    
    #print("start colour " + str(colourMap[startColour]) + " end colour " + str(colourMap[endColour]))
    
    params = str(effectID) + PARAM_DELIMINATOR + startColourString + PARAM_DELIMINATOR + endColourString 

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "SetEffectColour",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    return result

def CreateParentChild(parentID, childID):
    '''creates parent-child relationship

    :param parentID: the ID of the parent
    :type parentID: int 
    
    :param childID: the ID of the child
    :type childID: int 
    
    :return: 1 on success, 0 on failure

    '''
    methodName = "SetParentChild"

    #data type checks
    try:
        parentID = int(parentID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter parentID was not a int, parentID=\'"+ str(parentID) + "\'")
        return 0
    try:
        childID = int(childID)
    except (ValueError, TypeError):
        ErrorMsg(methodName,"parameter childID was not a int, childID=\'"+ str(childID) + "\'")
        return 0
    
    #create parameter string
    params = str(parentID) + PARAM_DELIMINATOR + str(childID)  

    #call the unity function
    unityInstance.SendMessage(pysparkClass, "CreateParentChild",params)

    #check the return value(unity function modifies this div's value to store the return value)
    result = int(document["unity_return_values"].value)

    return result

async def Sleep(t):
  await aio.sleep(t)


def Run(func):
    ''' 
    Runs an async function which allows waits to be used

    :param func: the async function to run
    :type func: async function

    :return: None

    '''
    aio.run(func())




