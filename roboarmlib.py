from browser import window,document,aio 

 

def run(func):
  aio.run(func())

def setShoulder(angle):
  window.unint.SendMessage('MainObj', 'SetShoulder',angle)

def setElbow(angle):
  window.unint.SendMessage('MainObj', 'SetElbow',angle)

def setArm(distance):
  window.unint.SendMessage('MainObj', 'SetArmSlide',distance)