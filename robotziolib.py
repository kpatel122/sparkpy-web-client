from browser import window, aio
#from browser import time
#import datetime
 

MAX_SPEECH = (512 -2)
MAX_MOTOR = 4

CMD_MOTOR_1  =   '0'
CMD_MOTOR_2  =   '1'
CMD_MOTOR_3  =   '2'
CMD_MOTOR_4  =   '3'
CMD_SPEECH   =   's'
CMD_EXPRESSION = 'e'
CMD_MOVEMENT =  'v'
CMD_MOUTH    =  'm'
CMD_EYEBROW  =  'b'
CMD_EYES     =  'y'
CMD_PIN      =  'p'


returnValues = []
res = False


  # sends to the active bluetooth connection 
  # call this function from py files via 
  # import robotziolib as robotzio
  # robotzio.sendToBle("Hello World")
def sendToBle(data):
    window.sendToBle(data)

def waitmillis(millisToWait):

  startmillis = int(round(time.time() * 1000))
  elapsedmillis = 0 #float(startmillis)


  while(elapsedmillis < millisToWait):
    elapsedmillis = (time.time() * 1000) - startmillis

  print(str(millisToWait) + " has elapsed")
     

async def waitForReturn():
  while( checkForReturnValue() == False):
    await aio.sleep(1) #waitmillis(500)


async def callAndWait():

  print("started")
  timer.set_timeout(checkForReturnValue, 1000)
  
  aio.sleep(5000)

  #waitmillis(200)
  print("ended")  

  #while( res == False):
  #  await aio.sleep(1) 


def speak(speech):
   
  if(len(speech) <MAX_SPEECH):
    speakcmd = "s:" + speech
    sendToBle(speakcmd)
  
def blereturn(data):
  global returnValues
  global res

  res = True 
  #print("new BEL Return " + data)
  returnValues.append(data);
  print("blereturn res is set to true ")

def checkForReturnValue():
  global res
  res = (len(returnValues) > 0)

  #window.alert("called check")
  
  f= len(returnValues) > 0
  print("on timer checkForReturnValue() called val is " + str(f))
  return (f)

def sleep(t):
  await aio.sleep(t)


def run(func):
  aio.run(func())


def getResponseValue(response):
  return response.target.value


def init():
  window.blereturn = blereturn




window.blereturn = blereturn


