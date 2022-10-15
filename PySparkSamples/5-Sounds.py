import pysparklib as pyspark

#create a office backgroung
pyspark.CreateEnvironment("Office")

#play background music
pyspark.PlaySceneSound("rockmusic1|0.1|true");

#create a scene character
uid = pyspark.CreateCharacter("YBot2")

#play a sound clip
pyspark.PlayCharacterSound(uid,"applause1")
