import sparkpy

#play sound example

#create a office backgroung
sparkpy.CreateEnvironment("Office")

#play background music
sparkpy.PlaySceneSound("rockmusic1|0.1|true");

#create a scene character
uid = sparkpy.CreateCharacter("YBot2")

#play a sound clip
sparkpy.PlayCharacterSound(uid,"applause1")
