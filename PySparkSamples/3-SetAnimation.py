import pysparklib as pyspark

#create office environment
pyspark.CreateEnvironment("Office")

#create robot character
ybot = pyspark.CreateCharacter("YBot2")

#set animation to walk
pyspark.SetAnimation(ybot, "Walk")

#set animation speed
pyspark.SetAnimationSpeed(ybot, 1) 
