import sparkpy

#import aio for sleep calls
from browser import aio

#wait for events example
 
#sleep needs to be in async functions
async def main():
    
    #create environment
    sparkpy.Environment('Office')
    
    #make a cube
    cube = sparkpy.Primitive('cube',0,1,0)
    
    #set it's colour to red
    cube.SetColour(1,0,0)
    
    #rotate around y axis
    cube.Rotate(100)
    
    #loop move from left to right
    cube.LoopMove(2, 2, "right")
    
    #wait for 4 seconds
    await aio.sleep(4)
    
    #stop moving the cube
    cube.StopMove()
    
    
    #change the colour to blue
    cube.SetColour(0,0,1)
 
   
#functions with sleep must be called through run   
sparkpy.Run(main)
