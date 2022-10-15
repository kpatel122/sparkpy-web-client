import pysparklib as pyspark

#create office environment
pyspark.CreateEnvironment("Office")

#create a portal effect
eid=pyspark.CreateEffect("portal")

#set colour to red from default
pyspark.SetEffectColour(eid,"red")  
