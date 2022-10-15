import pysparklib as pyspark

#import aio for sleep calls
from browser import aio

 
#sleep needs to be in async functions
async def main():
    
    #create environment
    pyspark.CreateEnvironment('Office')
    
    #make a cube
    cubeID = pyspark.CreatePrimitive('cube',0,1,0)
    
    #set it's colour to red
    pyspark.SetPrimitiveColour(cubeID,1,0,0)
    
    #rotate around y axis
    pyspark.RotatePrimitive(cubeID,100)
    
    #loop move from left to right
    pyspark.LoopPrimitiveMove(cubeID, 2, 2, "right")
    
    #wait for 4 seconds
    await aio.sleep(4)
    
    #stop moving the cube
    pyspark.StopPrimitiveMove(cubeID)
    
    
    #change the colour to blue
    pyspark.SetPrimitiveColour(cubeID,0,0,1)
 
   
#functions with sleep must be called through run   
pyspark.run(main) 
