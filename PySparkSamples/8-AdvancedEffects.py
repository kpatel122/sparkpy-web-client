import pysparklib as pyspark

#create environment
pyspark.CreateEnvironment("Office")

#cube position
x=0
y=0
z=0
scale = 2 # make the portal twice as normal

#create portal effect
eid=pyspark.CreateEffect("portal",x,y,z,scale)

#set the colour
pyspark.SetEffectColour(eid,"green","white") 
