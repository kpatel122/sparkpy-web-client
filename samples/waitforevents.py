import roboarmlib as robotzio
from browser import document,aio 

def Reset():
    robotzio.setShoulder(0);
    print("called reset")

async def main():
    
    app = document["appdata"]
    
    for i in range(0,4):
        robotzio.setShoulder(90);
        await aio.event(app, "finishedMovement")
        Reset()    
        await aio.sleep(4)
        
    print('Finished')

robotzio.run(main)