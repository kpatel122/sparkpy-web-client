import pysparklib as pyspark

#create office environment
pyspark.CreateEnvironment("Office")

#create robot character
ybot = pyspark.CreateCharacter("YBot2")

#set control mode to keyboard
pyspark.SetControlMode(ybot,"keyboard") 
