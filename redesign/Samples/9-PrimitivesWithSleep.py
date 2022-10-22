import sparkpy

#import aio for sleep calls
from browser import aio

#wait for events example
 
#sleep needs to be in async functions
async def main():
    
    #create environment
    sparkpy.CreateEnvironment('Office')
    
    #make a cube
    cubeID = sparkpy.CreatePrimitive('cube',0,1,0)
    
    #set it's colour to red
    sparkpy.SetPrimitiveColour(cubeID,1,0,0)
    
    #rotate around y axis
    sparkpy.RotatePrimitive(cubeID,100)
    
    #loop move from left to right
    sparkpy.LoopPrimitiveMove(cubeID, 2, 2, "right")
    
    #wait for 4 seconds
    await aio.sleep(4)
    
    #stop moving the cube
    sparkpy.StopPrimitiveMove(cubeID)
    
    
    #change the colour to blue
    sparkpy.SetPrimitiveColour(cubeID,0,0,1)
 
   
#functions with sleep must be called through run   
sparkpy.run(main)
