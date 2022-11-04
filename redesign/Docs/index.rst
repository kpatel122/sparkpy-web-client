..
   Made with version 5.3.0.
   Install with pip, *do not* use apt
  comment goes here
   *its AltGr '#' for the right kind of speech mark
   Links:
   https://docutils.sourceforge.io/docs/ref/rst/directives.html#images
   https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#comments

   **Images***
   .. image:: Images/ybot.png
   :height: 100px
   :width: 100 px
   :scale: 50 %
   :alt: alternate text
   :align: center

   **Link to anchor point**
   `Hide chat box <Source/sparkpy.html#sparkpy.HideInputBox>`_ 

   **Note box**
   .. note:: hello wordld
..

.. Sparkpy documentation master file, created by
   sphinx-quickstart on Fri Oct 21 13:55:31 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


====================
Welcome to Sparkpy !
====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`


* `Full API Reference <Source/sparkpy.html>`_  

.. to get line numbers back change :linenothreshold: 1 
.. highlight:: python 
   :linenothreshold: 99 

-------------
Introduction
-------------
Sparkpy is a platform to learn and create Python programming projects using interactive 3D graphics.

~~~~~~~
Basics
~~~~~~~

"""""""""""""""""""""
Create an environment
"""""""""""""""""""""
To create a scene an environment is needed ::
   
   import sparkpy

   #create a desert enviroment
   sparkpy.CreateEnvironment('Desert')

.. note::
   A list of all current environments  
   
   ========== ========== =============== ============= ========== ========= =========== 
   \"Desert\" \"Forest\" \"AlienPlanet\" \"GasPlanet\" \"Office\" \"SciFi\" \"Default\"
   ========== ========== =============== ============= ========== ========= ===========

""""""""""""""""""
Create a character
""""""""""""""""""

To create a character, first make an environment then create the character

.. code-block:: python
   :emphasize-lines: 7
   
   import sparkpy

   #create office environment
   sparkpy.CreateEnvironment("Office")

   #create robot character
   sparkpy.CreateCharacter("YBot")

.. note::
   A list of all current characters  
   
   ======= ========= ========= ============ ======== ========  
   \"Amy\" \"Bryce\" \"Lewis\" \"Michelle\" \"YBot\" \"XBot\"   
   ======= ========= ========= ============ ======== ========

""""""""""""""""""""""""""""""""
Character animation
""""""""""""""""""""""""""""""""

Set the animation for a character using  `SetAnimation  <Source/sparkpy.html#sparkpy.SetAnimation>`_ 

.. code-block:: python
   :emphasize-lines: 12,15

   import sparkpy

   #set animation example

   #create office environment
   sparkpy.CreateEnvironment("Office")

   #create robot character
   ybot = sparkpy.CreateCharacter("YBot")

   #set animation to walk
   sparkpy.SetAnimation(ybot, "Walk")

   #set animation speed
   sparkpy.SetAnimationSpeed(ybot, 1)

.. tip:: A list of all available animation names for a given character is shown in the explorer view

   .. image:: Images/animation_names.png
      
 
.. tip:: The speed of the animation can controlled with `SetAnimationSpeed <Source/sparkpy.html#sparkpy.SetAnimationSpeed>`_



""""""""""""""""""""""""""""""""
Character movement
""""""""""""""""""""""""""""""""

A character can be moved using the `Move <Source/sparkpy.html#sparkpy.Move>`_ Method

.. code-block:: python
   :emphasize-lines: 15
   
   import sparkpy

   #move character exaample

   #create office environment
   sparkpy.CreateEnvironment("forest")

   #create robot character at position x=0 y0 z=3
   xbot = sparkpy.CreateCharacter("xbot",0,0,3)

   #set animation to walk
   sparkpy.SetAnimation(xbot, "Walk")

   #move the character for 5 seconds
   sparkpy.Move(xbot,10)
   
.. note:: you will notice that the character's animation continues to play after the movement ends. This is behaviour can resolved using waits [LINK NEEDED] 

""""""""""""""""""""""""""""""""
Character rotation
""""""""""""""""""""""""""""""""

A character can be rotated using the `Rotate <Source/sparkpy.html#sparkpy.Rotate>`_ Method

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #rotate character exaample

   #create office environment
   sparkpy.CreateEnvironment("home")

   #create a character at position 0,0,1
   bryce = sparkpy.CreateCharacter("bryce")

   #rotate 90 degres in 2 seconds, in the counter clockwise direction 
   sparkpy.Rotate(bryce,90, 2, "ccw")


""""""""""""""""""""""""""""""""
Character hide and show
""""""""""""""""""""""""""""""""

A character can be hidden (invisible) using the `Hide <Source/sparkpy.html#sparkpy.Hide>`_ Method

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #hide character exaample

   #create an environment
   sparkpy.CreateEnvironment("forest")

   #create a character at position x=0 y0 z=3
   bryce = sparkpy.CreateCharacter("bryce",0,0,3)

   #character exists but will not be shown in the screen 
   sparkpy.Hide(bryce)

.. note:: A character that is hidden can be shown again using `Show() <Source/sparkpy.html#sparkpy.Show>`_ 

""""""""""""""""""""""""""""""""
Character chat
""""""""""""""""""""""""""""""""

A character can create a chat box using the `Chat() <Source/sparkpy.html#sparkpy.Chat>`_

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #chat example

   #create an environment
   sparkpy.CreateEnvironment("home")

   #create a character
   bryce = sparkpy.CreateCharacter("bryce")

   #create a chat box for 5 seconds
   sparkpy.Chat(bryce, "Hello World", 5)

""""""""""""""""""""""""""""""""
Control character with keyboard
""""""""""""""""""""""""""""""""

To move a character with the keyboard, use the  `SetControlMode()  <Source/sparkpy.html#sparkpy.SetControlMode>`_ method

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #control character with keyboard example

   #create office environment
   sparkpy.CreateEnvironment("Office")

   #create robot character
   ybot = sparkpy.CreateCharacter("YBot")

   #set control mode to keyboard
   sparkpy.SetControlMode(ybot,"keyboard")

~~~~~~~~~~
User Input
~~~~~~~~~~

""""""""""""""""""""""""
Input box (non blocking)
""""""""""""""""""""""""

You can get input from the user using the `ShowInputBox() <Source/sparkpy.html#sparkpy.ShowInputBox>`_
This method accepts a function to call when input has been recieved, the function must accept one parameter which represents the text that was entered in the input box.
You can hide an input box using `HideInputBox() <Source/sparkpy.html#sparkpy.HideInputBox>`_

.. code-block:: python
 
   import sparkpy

   #inputbox example

   #input box handler function
   def InputEntered(inputText):
      
      #print the recieved text
      print("input box recieved " + inputText)

      #once the input has been recieved, do not show the input box anymore
      sparkpy.HideInputBox()

      #set the chat box text to the input
      sparkpy.Chat(michelle, "You said " + inputText)

   #create desert environment test
   sparkpy.CreateEnvironment('desert');

   #create a character
   michelle = sparkpy.CreateCharacter("michelle")
   
   #set the callback function
   sparkpy.SetInputBoxHandler(InputEntered)

   #show input box
   sparkpy.ShowInputBox()
 
   #any code after ShowInputBox() continues to run regardless if text has been entered 
   
.. note:: `ShowInputBox() <Source/sparkpy.html#sparkpy.ShowInputBox>`_ is *asynchronous* (non-blocking) meaning any code *after* the ShowInputBox() will continue
   to run regardless if text has been entered or not. To make input from the user *synchronous* (blocking) meaning any code *after* the ShowInputBox() can only
   be run *after* input has been entered, you can use python input(see below)- though this will block the entire application including any animations and character movement or async await for input event() [LINK NEEDED]

""""""""""""""""""""""""
Input box (blocking)
""""""""""""""""""""""""

.. code-block:: python
   
   import sparkpy
      
   #blocking input call

   #create desert environment test
   sparkpy.CreateEnvironment('desert')

   #create a character
   lewis = sparkpy.CreateCharacter("lewis")
      
   #ask the user for a name, note the entire application will be paused 
   #until a value is entered
   name = input("Please enter your name")

   #output the name to the console
   print("Welcome to sparkpy " + name)

   #create a chat box with the entered text
   sparkpy.Chat(lewis,"Welcome to sparkpy " + name)

~~~~~~~~~~~
Collisions
~~~~~~~~~~~

Collisions can be captured between two characters or primitives, using a callback function set with `SetCollisionHandler() <Source/sparkpy.html#sparkpy.SetCollisionHandler>`_ 
when a collision occurs, the callback function is called. The callback function must have two parameters which will be set to the ids of the two objects that collided

""""""""""""""""""""""""
Collision (non blocking)
""""""""""""""""""""""""

.. code-block:: python

   import sparkpy

   #collision example

   #create collision handler function, the two ids represent the ids of the objects that collided
   def collision(id1,id2):
      print("Collision occured between " + str(id1) + "," + str(id2))

   #assign the collision handler function
   sparkpy.SetCollisionHandler(collision)

   #create an office environment
   sparkpy.CreateEnvironment("Office")

   #create first character
   ybot = sparkpy.CreateCharacter("ybot")

   #create seconf character
   xbot = sparkpy.CreateCharacter("xbot",2,0,0)

   #set control mode to keyboard
   sparkpy.SetControlMode(ybot,"keyboard")

.. note:: `SetCollisionHandler() <Source/sparkpy.html#sparkpy.SetCollisionHandler>`_ is *asynchronous* (non-blocking) meaning any code *after* the SetCollisionHandler() will continue
   to run regardless of if a collision has occured or not. To make collision detection *synchronous* (blocking) meaning any code *after* a collision can only
   be run *after* a collision has occured, use async await for collision event() [LINK NEEDED]


""""""""""""""""""""
Collision (blocking)
""""""""""""""""""""

TODO

~~~~~~
Sounds
~~~~~~

"""""""""""""""""
Environment music
"""""""""""""""""

The `PlaySceneSound() <Source/sparkpy.html#sparkpy.PlaySceneSound>`_ will play background music for the scene. The music will loop by default

.. code-block:: python
   :emphasize-lines: 13
   
   import sparkpy

   #create office environment
   sparkpy.CreateEnvironment("home")

   #create robot character
   xbot = sparkpy.CreateCharacter("xbot")

   #set animation to dancing
   sparkpy.SetAnimation(xbot, "dancing1")

   #play background music, music will loop by default
   sparkpy.PlaySceneSound("funkymusic1")

.. note::
   
   Scene music can be stopped with `StopSceneSound() <Source/sparkpy.html#sparkpy.StopSceneSound>`_  
   The current list of music

   ============== ===============
   \"rockmusic1\" \"funkymusic1\"   
   ============== ===============

""""""""
Sound FX
""""""""

To play a sound effect for a specific character, use `PlayCharacterSound() <Source/sparkpy.html#sparkpy.PlayCharacterSound>`_ 
Sound effects do not loop by default

.. code-block:: python
   :emphasize-lines: 20,31

   import sparkpy

   #simple quiz with sound effects

   bryceid = 0

   #input box handler function
   def ProcessAnswer(answer):

      #print the recieved text
      print("input box recieved " + answer)

      #make the answer case insenstive
      answer = answer.lower()
      
      #check if the answer is correct
      if(answer == "paris"):

         #play an apploause sound effect
         sparkpy.PlayCharacterSound(bryceid, "applause1")

         #let the user know their answer is correct
         sparkpy.Chat(bryceid,"Correct!! ",10)

         #do a victory dance
         sparkpy.SetAnimation(bryceid,"celebration")

      else:

         #play a boo sound effect
         sparkpy.PlayCharacterSound(bryceid, "boo1")

         #let the user know their answer is correct
         sparkpy.Chat(bryceid,"Not correct",10)

         #play a talking animation for the character
         sparkpy.SetAnimation(bryceid,"talking2")

      #once the input has been recieved, do not show the input box anymore
      sparkpy.HideInputBox()


   #create an environment
   sparkpy.CreateEnvironment('home')

   #create a character
   bryceid = sparkpy.CreateCharacter('bryce')

   #play a talking animation for the character
   sparkpy.SetAnimation(bryceid,"talking1")

   #ask the user a question, keep the question on the screen for 20 seconds
   sparkpy.Chat(bryceid,"What's the captial of france? ",20)

   #set the input box callback function
   sparkpy.SetInputBoxHandler(ProcessAnswer)

   #show input box
   sparkpy.ShowInputBox()

.. note::
    
   The current list of sound effects

   +-------------+----------+----------+--------------+
   |\"applause1\"|\"beep1\" |\"beep2\" |\"boo1\"      |
   +-------------+----------+----------+--------------+
   |\"gun1\"     |\"gun2\"  |\"lose1\" |\"lose2\"     |
   +-------------+----------+----------+--------------+
   |\"lose3\"    |\"swipe1\"|\"swipe2\"|\"transport1\"|
   +-------------+----------+----------+--------------+
   |\"win1\"     |\"win2\"  |\"win3\"  |\"bounce1\"   |
   +-------------+----------+----------+--------------+



~~~~~~~~
Effects
~~~~~~~~
""""""""""""""""
Creating effects
""""""""""""""""

The `CreateEffect() <Source/sparkpy.html#sparkpy.CreateEffect>`_ will create a special effect, it's default position is 0
The colour of the effect can be set with `SetEffectColour() <Source/sparkpy.html#sparkpy.SetEffectColour>`_
An effecct can be stopped with `StopEffect() <Source/sparkpy.html#sparkpy.StopEffect>`_

.. code-block:: python

   import sparkpy

   #special effects example

   #create office environment
   sparkpy.CreateEnvironment("office")

   #create a portal effect
   eid=sparkpy.CreateEffect("portal")

   #set colour to red from default
   sparkpy.SetEffectColour(eid,"red")

.. note::
    
   The current list of effects:

   +-------------+
   |\"portal\"   |
   +-------------+

   The current list of colours:

   +-------------+----------+----------+-----------+
   |\"yellow\"   |\"clear\" |\"grey\"  |\"magenta\"|
   +-------------+----------+----------+-----------+
   |\"cyan\"     |\"red\"   |\"black\" |\"white\"  |
   +-------------+----------+----------+-----------+
   |\"blue\"     |\"green\" |          |           |
   +-------------+----------+----------+-----------+

~~~~~
Wait
~~~~~

""""""""""""""""""
Wait for seconds
""""""""""""""""""
To pause your program for a specific amount of time, use *aio.sleep* (see line 22 of the example)
In order to use aio.sleep your program must be written in an *async* function (see line 7 of the example), this function should be called with 
`Run() <Source/sparkpy.html#sparkpy.Run>`_ (see line 28 of the example). Waits are performed using *await aio.sleep()* which is available after an import of the aio module from browser(see line 4 of the example)


.. code-block:: python
   :emphasize-lines: 4,7,22,28
   
   import sparkpy

   #must import aio for await to work
   from browser import aio

   #programs with sleep with be written inside an async function 
   async def main():

      #create office environment
      sparkpy.CreateEnvironment("forest")

      #create robot character at position x=0 y0 z=3
      xbotid = sparkpy.CreateCharacter("xbot",0,0,3)

      #set animation to walk
      sparkpy.SetAnimation(xbotid, "Walk")

      #move the character for 3 seconds
      sparkpy.Move(xbotid,3)

      #sleep for 3 seconds
      await aio.sleep(3)

      #set the animation back to idle 
      sparkpy.SetAnimation(xbotid,"idle")
   
   #run the async function
   sparkpy.Run(main)


""""""""""""""""""""
Wait for collision
""""""""""""""""""""

To pause your program until a collision has occured use *await aio.event(SPARKPY_EVENT, EVENT_COLLISION)* (see line 30 of the example)
In order to use *await aio.event* your program must be written in an *async* function (see line 13 of the example), this function should be called with 
`Run() <Source/sparkpy.html#sparkpy.Run>`_ (see line 35 of the example).  *await aio.event* is available after the aio module is imported from browser (see line 4 of the example)

.. code-block:: python
   :emphasize-lines: 4,13,30,36
   
   import sparkpy

   #must import aio for await to work
   from browser import aio

   #collision example

   #create collision handler function, the two ids represent the ids of the objects that collided
   def collision(id1,id2):
      print("Collision occured between " + str(id1) + "," + str(id2))

   #programs with await must be written inside an async function
   async def main():
      #assign the collision handler function
      sparkpy.SetCollisionHandler(collision)

      #create an office environment
      sparkpy.CreateEnvironment("Office")

      #create first character
      ybot = sparkpy.CreateCharacter("ybot")

      #create seconf character
      xbot = sparkpy.CreateCharacter("xbot",2,0,0)

      #set control mode to keyboard
      sparkpy.SetControlMode(ybot,"keyboard")

      #wait for the collision to occur, no code below this will run until a collision happens
      await aio.event(sparkpy.EVENT, sparkpy.EVENT_COLLISION)

      #this can only run after a collsion event has happened
      sparkpy.Chat(ybot, "I have collided!")
      
   sparkpy.Run(main)

""""""""""""""""""""
Wait for input
""""""""""""""""""""

To pause your program until user has entered text use *await aio.event(SPARKPY_EVENT, EVENT_INPUT)* (see line 21 of the example)
In order to use *await aio.event* your program must be written in an *async* function (see line 7 of the example), this function should be called with 
`Run() <Source/sparkpy.html#sparkpy.Run>`_ (see line 33 of the example).  *await aio.event* is available after the aio module is imported from browser (see line 4 of the example)
Text entered into the input box can be retrieved using `GetInputBoxValue() <Source/sparkpy.html#sparkpy.GetInputBoxValue>`_ (see line 24 of the example). 

.. code-block:: python
   :emphasize-lines: 4,7,21,24, 33

   import sparkpy
   
   #must import aio for await to work
   from browser import aio

   #programs with await must be written inside an async function 
   async def main():
      #create desert environment test
      sparkpy.CreateEnvironment('desert');
         
      #create first character
      ybot = sparkpy.CreateCharacter("ybot")

      #ask the user a question
      sparkpy.Chat(ybot, "Hi, What's your name ? ")

      #show an input box, for the user to enter an answer
      sparkpy.ShowInputBox()

      #wait until text has been entered. Code below this line will not execute until text is entered
      await aio.event(sparkpy.EVENT, sparkpy.EVENT_INPUT)

      #text has been entered, retrieve the value that was entered 
      name = sparkpy.GetInputBoxValue()

      #out message to user, with the value they entered
      sparkpy.Chat(ybot, "Welcome to sparkpy " + name)

      #hide the input box
      sparkpy.HideInputBox()

   #run the async function
   sparkpy.Run(main)

~~~~~~~~~~
Primitives
~~~~~~~~~~

""""""""""""""""""""
Create Primitive
""""""""""""""""""""
Primitives are simple shapes that have no animations attached to them.
To create a primitive use the `CreatePrimitive() <Source/sparkpy.html#sparkpy.CreatePrimitive>`_ method

.. code-block:: python
   :emphasize-lines: 7
   
   import sparkpy

   #create an environment
   sparkpy.CreateEnvironment('forest')

   #make a cube at position x=0 , y=1, z=0
   cubeID = sparkpy.CreatePrimitive('cube',0,1,0)
    
.. note:: The current list of primitive:

   +-------------+-----------+------------+
   |\"sphere\"   |\"capsule\"|\"cylinder\"|
   +-------------+-----------+------------+
   |\"plane\"    |\"quad\"   |\"cube\"    |
   +-------------+-----------+------------+
   
   To hide a created primitive, use the `HidePrimitive() <Source/sparkpy.html#sparkpy.HidePrimitive>`_ method
   To show a previously hidden primitive, use the `ShowPrimitive() <Source/sparkpy.html#sparkpy.ShowPrimitive>`_ method

""""""""""""""""""""
Set Primitive Colour
""""""""""""""""""""
To set the colour of a primitive, use the `SetPrimitiveColour() <Source/sparkpy.html#sparkpy.SetPrimitiveColour>`_ method.
The method accepts the levels of red, green and blue was values between 0-1. The transparancy of a primitive can also be set as a avlue between 0 (fully invisible) to 1 (fully opaque)

.. code-block:: python
   :emphasize-lines: 10
   
   import sparkpy

   #create an environment
   sparkpy.CreateEnvironment('forest')

   #make a cube at position x=0 , y=1, z=0
   cubeID = sparkpy.CreatePrimitive('cube',0,1,0)
   
   #set the colour to red 
   sparkpy.SetPrimitiveColour(cubeID,1,0,0)


""""""""""""""""""""
Destroy Primitive
""""""""""""""""""""
If a primitive is no longer needed in the program `DestroyPrimitive() <Source/sparkpy.html#sparkpy.DestroyPrimitive>`_
will remove the primitive completely

.. code-block:: python
   :emphasize-lines: 10

   import sparkpy

   #create an environment
   sparkpy.CreateEnvironment('forest')

   #make a cube at position x=0 , y=1, z=0
   cubeID = sparkpy.CreatePrimitive('cube',0,1,0)

   #the cube is no longer needed, remove it
   sparkpy.DestroyPrimitive(cubeID)

""""""""""""""""""""""""""
Scale Primitive
""""""""""""""""""""""""""
   
To make a primitive bigger or smaller, use the
`ScalePrimative() <Source/sparkpy.html#sparkpy.ScalePrimative>`_ method

.. code-block:: python
   :emphasize-lines: 10
   
   import sparkpy

   #create an environment
   sparkpy.CreateEnvironment('forest')

   #make a cube at position x=0 , y=1, z=0
   cubeID = sparkpy.CreatePrimitive('cube',0,1,0)

   #double the size of the cube
   sparkpy.ScalePrimative(cubeID, 2)

.. note:: 
   to scale in a specific direction (non-uniform scale), provide the sizes
   of the x,y,z scale when using `ScalePrimitive() <Source/sparkpy.html#sparkpy.ScalePrimative>`_
   
   .. code-block:: python

      import sparkpy

      #make a cube at position x=0 , y=1, z=0
      cubeID = sparkpy.CreatePrimitive('cube',0,1,0)

      #double the size of the cube, along the x and z axis
      sparkpy.ScalePrimative(cubeID, 2,1,2)

""""""""""""""""""""
Rotate Primitive
""""""""""""""""""""
To rotate a primitive, use the `RotatePrimitive() <Source/sparkpy.html#sparkpy.RotatePrimitive>`_ 
by default primitives are rotated around their y (up) axis

.. code-block:: python

      import sparkpy

      #make a cube at position x=0 , y=1, z=0
      cubeID = sparkpy.CreatePrimitive('cube',0,1,0)

      #rotate the cube at a speed of 90 degrees per second
      sparkpy.RotatePrimitive(cubeID, 90)

""""""""""""""""""""
Move Primitive
""""""""""""""""""""
To move a primitive, use the `MovePrimitive() <Source/sparkpy.html#sparkpy.MovePrimitive>`_ method.

.. code-block:: python

      import sparkpy

      #make a cube at position x=0 , y=1, z=0
      cubeID = sparkpy.CreatePrimitive('cube',0,1,0)

      #move the cube to right at a speed of 10 for 2 seconds 
      cubeID = sparkpy.MovePrimitive(cubeID, 2, 10, "right")
    
.. note:: direction values can be:

   +------+--------+--------+---------+
   |\"up\"|\"down\"|\"left\"|\"right\"|
   +------+--------+--------+---------+
    

""""""""""""""""""""
Loop Primitive Move
""""""""""""""""""""
To make a primitive continuously move between two points, use the `LoopPrimitiveMove() <Source/sparkpy.html#sparkpy.LoopPrimitiveMove>`_ 

.. code-block:: python

   #make a cube
   cubeID = sparkpy.CreatePrimitive('cube',0,1,0)
    
   #loop move from right to left and back again for 2 seconds at a speed of 1. 
   sparkpy.LoopPrimitiveMove(cubeID, 2, 1, "right")
 




   

    

