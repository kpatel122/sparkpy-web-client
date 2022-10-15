import roboarmlib as robotzio
from browser import document,aio 


async def main():
    
    app = document["appdata"]
    
    for i in range(0,4):
        robotzio.setShoulder(90);
        await aio.event(app, "finishedMovement")
        robotzio.setShoulder(0);
        await aio.sleep(4)
        
    print('Finished')

robotzio.run(main)