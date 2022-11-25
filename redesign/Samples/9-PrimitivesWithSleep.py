import sparkpy

#import aio for sleep calls
from browser import aio

#wait for events example
 
#sleep needs to be in async functions
async def main():
    
    #create environment
    sparkpy.CreateEnvironment('Office')
    
    #make a cube
    cubeID = sparkpy._CreatePrimitive('cube',0,1,0)
    
    #set it's colour to red
    sparkpy._SetPrimitiveColour(cubeID,1,0,0)
    
    #rotate around y axis
    sparkpy._RotatePrimitive(cubeID,100)
    
    #loop move from left to right
    sparkpy._LoopPrimitiveMove(cubeID, 2, 2, "right")
    
    #wait for 4 seconds
    await aio.sleep(4)
    
    #stop moving the cube
    sparkpy._StopPrimitiveMove(cubeID)
    
    
    #change the colour to blue
    sparkpy._SetPrimitiveColour(cubeID,0,0,1)
 
   
#functions with sleep must be called through run   
sparkpy.Run(main)
