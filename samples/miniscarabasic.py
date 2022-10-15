import roboarmlib as robotzio

def Reset():
    robotzio.setShoulder(0)
    robotzio.setElbow(0)
    robotzio.setArm(0)

Reset()
robotzio.setShoulder(-90);
robotzio.setElbow(45);
robotzio.setArm(150);
