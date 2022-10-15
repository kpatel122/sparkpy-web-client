#brython sample that sends a ble message and then waits beofre moving on


import robotziolib as robotzio

from browser import document,aio  

async def main():
	print('started')
	
	bt = document["blerec"]
    robotzio.speak("Hello World")
    
    val = await aio.event(bt, "bleReceived")
    v = robotzio.getResponseValue(val)
    
    print("got ble value " + v)
    
    print("now i have finished")

aio.run(main())