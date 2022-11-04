import sparkpy

#play sound example

#create a office backgroung
sparkpy.CreateEnvironment("office")

#play background music
sparkpy.PlaySceneSound("rockmusic1");

#create a scene character
uid = sparkpy.CreateCharacter("YBot")

#play a sound clip
sparkpy.PlayCharacterSound(uid,"applause1")
