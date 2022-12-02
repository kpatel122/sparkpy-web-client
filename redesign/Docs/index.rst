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
To create a scene an `Environment() <Source/sparkpy.html#sparkpy.Environment>`_ object is needed ::
   
   import sparkpy

   #create a desert enviroment
   sparkpy.Environment('desert')

.. note::
   A list of all current environments  
   
   ========== ========== =============== ============= ========== ========= =========== 
   \"Desert\" \"Forest\" \"AlienPlanet\" \"GasPlanet\" \"Office\" \"SciFi\" \"Default\"
   ========== ========== =============== ============= ========== ========= ===========

""""""""""""""""""
Create a character
""""""""""""""""""

To create a character, first make an environment then create a `Character() <Source/sparkpy.html#sparkpy.Character>`_ object

.. code-block:: python
   :emphasize-lines: 7
   
   import sparkpy

   #create office environment
   sparkpy.Environment("Office")

   #create robot character
   sparkpy.Character("YBot")

.. note::
   A list of all current characters  
   
   ======= ========= ========= ============ ======== ========  
   \"Amy\" \"Bryce\" \"Lewis\" \"Michelle\" \"YBot\" \"XBot\"   
   ======= ========= ========= ============ ======== ========

""""""""""""""""""""""""""""""""
Character animation
""""""""""""""""""""""""""""""""

Set the animation for a character using  `SetAnimation()  <Source/sparkpy.html#sparkpy.Character.SetAnimation>`_ 

.. code-block:: python
   :emphasize-lines: 12,15

   import sparkpy

   #set animation example

   #create office environment
   sparkpy.Environment("Office")

   #create robot character
   robot = sparkpy.Character("YBot")

   #set animation to walk
   robot.SetAnimation("Walk")

   #set animation speed
   robot.SetAnimationSpeed(1)

.. tip:: A list of all available animation names for a given character is shown in the explorer view

   .. image:: Images/animation_names.png
      
 
.. tip:: The speed of the animation can controlled with `SetAnimationSpeed() <Source/sparkpy.html#sparkpy.Character.SetAnimationSpeed>`_



""""""""""""""""""""""""""""""""
Character movement
""""""""""""""""""""""""""""""""

A character can be moved using the `Move() <Source/sparkpy.html#sparkpy.Character.Move>`_ Method

.. code-block:: python
   :emphasize-lines: 15
   
   import sparkpy

   #move character exaample

   #create office environment
   sparkpy.Environment("forest")

   #create robot character at position x=0 y0 z=5
   robot = sparkpy.Character("xbot",0,0,5)

   #set animation to walk
   robot.SetAnimation("Walk")

   #move the robot for 5 seconds
   robot.Move(5)
   
.. note:: you will notice that the character's animation continues to play after the movement ends. This is behaviour can resolved using waits [LINK NEEDED] 

""""""""""""""""""""""""""""""""
Character rotation
""""""""""""""""""""""""""""""""

A character can be rotated using the `Rotate() <Source/sparkpy.html#sparkpy.Character.Rotate>`_ Method

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #rotate character exaample

   #create office environment
   sparkpy.Environment("home")

   #create a character at position 0,0,1
   bryce = sparkpy.Character("bryce")

   #rotate left 90 degres in 2 seconds 
   bryce.Rotate(90, 2, "left")

""""""""""""""""""""""""""""""""
Character scale
""""""""""""""""""""""""""""""""

A character can be scaled using the `Scale() <Source/sparkpy.html#sparkpy.Character.Scale>`_ Method

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #scale character example

   #create office environment
   sparkpy.Environment("office")

   #create a character
   robot = sparkpy.Character("Ybot")

   #shrink the robot to half the size 
   robot.Scale(0.5)


""""""""""""""""""""""""""""""""
Character hide and show
""""""""""""""""""""""""""""""""

A character can be hidden (invisible) using the `Hide() <Source/sparkpy.html#sparkpy.Character.Hide>`_ Method

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #hide character exaample

   #create an environment
   sparkpy.Environment("forest")

   #create a character at position x=0 y0 z=3
   bryce = sparkpy.Character("bryce",0,0,3)

   #character exists but will not be shown in the screen 
   bryce.Hide()

.. note:: A character that is hidden can be shown again using `Show() <Source/sparkpy.html#sparkpy.Character.Show>`_ 

""""""""""""""""""""""""""""""""
Character chat
""""""""""""""""""""""""""""""""

A character can create a chat box using the `Chat() <Source/sparkpy.html#sparkpy.Character.Chat>`_

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #chat example

   #create an environment
   sparkpy.Environment("home")

   #create a character
   bryce = sparkpy.Character("bryce")

   #create a chat box for 5 seconds
   bryce.Chat("Hello World", 5)

""""""""""""""""""""""""""""""""
Control character with keyboard
""""""""""""""""""""""""""""""""

To move a character with the keyboard, use the  `ControlMode()  <Source/sparkpy.html#sparkpy.Character.ControlMode>`_ method
A character can be controlled in third person mode using 'third_person' as the SetControlMode parameter

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #control character with keyboard example

   #create office environment
   sparkpy.Environment("Office")

   #create robot character
   robot = sparkpy.Character("YBot")

   #set control mode to keyboard
   robot.ControlMode("keyboard")



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
      michelle.Chat("You said " + inputText)

   #create desert environment test
   sparkpy.Environment('desert')

   #create a character
   michelle = sparkpy.Character("michelle")
   
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
   sparkpy.Environment('desert')

   #create a character
   lewis = sparkpy.Character("lewis")
      
   #ask the user for a name, note the entire application will be paused 
   #until a value is entered
   name = input("Please enter your name")

   #output the name to the console
   print("Welcome to sparkpy " + name)

   #create a chat box with the entered text
   lewis.Chat("Welcome to sparkpy " + name)

~~~~~~~~~~~
Collisions
~~~~~~~~~~~

Collisions can be captured between two characters or primitives, using a callback function set with `SetCollisionHandler() <Source/sparkpy.html#sparkpy.SetCollisionHandler>`_ 
when a collision occurs, the callback function is called. The callback function must have two parameters which will be set to the ids of the two objects that collided.
To retrieve a character object from the ids, use `GetCharacterFromID() <Source/sparkpy.html#sparkpy.GetCharacterFromID>`_

""""""""""""""""""""""""
Collision (non blocking)
""""""""""""""""""""""""

.. code-block:: python

   import sparkpy

   import sparkpy

   #collision example

   #create collision handler function
   def collision(id1,id2):
      print("Handled " + str(id1) + "," + str(id2))
      collidedCharacter = sparkpy.GetCharacterFromID(id1)
      collidedCharacter.Chat("I collided")

   #assign the collision handler function
   sparkpy.SetCollisionHandler(collision)

   #create an office environment
   sparkpy.Environment("Office")

   #create first character
   robot1 = sparkpy.Character("YBot")
   

   #create seconf character
   robot2 = sparkpy.Character("XBot",2,0,0)

   #control character by keyboard
   robot1.ControlMode("keyboard")

.. note:: `SetCollisionHandler() <Source/sparkpy.html#sparkpy.SetCollisionHandler>`_ is *asynchronous* (non-blocking) meaning any code *after* the SetCollisionHandler will continue
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
 
The `PlaySound() <Source/sparkpy.html#sparkpy.Environment.PlaySound>`_ will play background music for the scene environment. The music will loop by default

.. code-block:: python
   :emphasize-lines: 13
   
   import sparkpy

   #create office environment
   environment = sparkpy.Environment("home")

   #create robot character
   xbot = sparkpy.Character("xbot")

   #set animation to dancing
   xbot.SetAnimation("dancing1")

   #play background music, music will loop by default
   environment.PlaySound("funkymusic1")

.. note::
   
   Scene music can be stopped with `StopSound() <Source/sparkpy.html#sparkpy.Environment.StopSound>`_  
   The current list of music

   ============== ===============
   \"rockmusic1\" \"funkymusic1\"   
   ============== ===============

""""""""
Sound FX
""""""""
 
To play a sound effect for a specific character, use `PlaySound() <Source/sparkpy.html#sparkpy.Character.PlaySound>`_ 
Sound effects do not loop by default

.. code-block:: python
   :emphasize-lines: 19,30

   import sparkpy

   #simple quiz with sound effects
   bryce = None

   #input box handler function
   def ProcessAnswer(answer):

      #print the recieved text
      print("input box recieved " + answer)

      #make the answer case insenstive
      answer = answer.lower()
      
      #check if the answer is correct
      if(answer == "paris"):

         #play an apploause sound effect
         bryce.PlaySound("applause1")

         #let the user know their answer is correct
         bryce.Chat("Correct!! ",10)

         #do a victory dance
         bryce.SetAnimation("celebration")

      else:

         #play a boo sound effect
         bryce.PlaySound("boo1")

         #let the user know their answer is correct
         bryce.Chat("Not correct",10)

         #play a talking animation for the character
         bryce.SetAnimation("talking2")

      #once the input has been recieved, do not show the input box anymore
      sparkpy.HideInputBox()

   #create an environment
   sparkpy.Environment('home')

   #create a character
   bryce = sparkpy.Character('bryce')

   #play a talking animation for the character
   bryce.SetAnimation("talking1")

   #ask the user a question, keep the question on the screen for 20 seconds
   bryce.Chat("What's the captial of france? ",20)

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
 
The `Effect() <Source/sparkpy.html#sparkpy.Effect>`_ object will create a special effect, it's default position is 0
The colour of the effect can be set with `SetColour() <Source/sparkpy.html#sparkpy.Effect.SetColour>`_
An effect can be stopped with `Stop() <Source/sparkpy.html#sparkpy.Effect.Stop>`_

.. code-block:: python

   import sparkpy

   #special effects example

   #create office environment
   sparkpy.Environment("Office")

   x = 0 #x position 
   y = -1 #y position
   z= 0 #z position

   #create a portal effect
   portal=sparkpy.Effect("portal",x,y,z)

   #set colour to red from default
   portal.SetColour("red")


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
To pause your program for a specific amount of time, use *aio.sleep* 
In order to use aio.sleep your program must be written in an *async* function, this function should be called with 
`Run() <Source/sparkpy.html#sparkpy.Run>`_ (see last line of example). Waits are performed using *await aio.sleep()* which is available after an import of the aio module from browser


.. code-block:: python
   :emphasize-lines: 4,7,22,28
   
   import sparkpy

   #must import aio for await to work
   from browser import aio

   #programs with sleep with be written inside an async function 
   async def main():

      #create office environment
      sparkpy.Environment("forest")

      #create robot character at position x=0 y0 z=3
      xbot = sparkpy.Character("xbot",0,0,3)

      #set animation to walk
      xbot.SetAnimation("Walk")

      #move the character for 3 seconds
      xbot.Move(3)

      #sleep for 3 seconds
      await aio.sleep(3)

      #set the animation back to idle 
      xbot.SetAnimation("idle")
   
   #run the async function
   sparkpy.Run(main)


""""""""""""""""""""
Wait for collision
""""""""""""""""""""

To pause your program until a collision has occured use *await aio.event(SPARKPY_EVENT, EVENT_COLLISION)* 
In order to use *await aio.event* your program must be written in an *async* function , this function should be called with 
`Run() <Source/sparkpy.html#sparkpy.Run>`_ .  *await aio.event* is available after the aio module is imported from browser 

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
      sparkpy.Environment("Office")

      #create first character
      ybot = sparkpy.Character("ybot")

      #create seconf character
      xbot = sparkpy.Character("xbot",2,0,0)

      #set control mode to keyboard
      ybot.ControlMode("keyboard")

      #wait for the collision to occur, no code below this will run until a collision happens
      await aio.event(sparkpy.EVENT, sparkpy.EVENT_COLLISION)

      #this can only run after a collsion event has happened
      ybot.Chat("I have collided!")
      
   sparkpy.Run(main)

""""""""""""""""""""
Wait for input
""""""""""""""""""""

To pause your program until user has entered text use *await aio.event(SPARKPY_EVENT, EVENT_INPUT)* 
In order to use *await aio.event* your program must be written in an *async* function , this function should be called with 
`Run() <Source/sparkpy.html#sparkpy.Run>`_ .  *await aio.event* is available after the aio module is imported from browser
Text entered into the input box can be retrieved using `GetInputBoxValue() <Source/sparkpy.html#sparkpy.GetInputBoxValue>`_ . 

.. code-block:: python
   :emphasize-lines: 4,7,21,24, 33

   import sparkpy
   
   #must import aio for await to work
   from browser import aio

   #programs with await must be written inside an async function 
   async def main():
      #create desert environment test
      sparkpy.Environment('desert');
         
      #create first character
      ybot = sparkpy.Character("ybot")

      #ask the user a question
      ybot.Chat("Hi, What's your name ? ")

      #show an input box, for the user to enter an answer
      sparkpy.ShowInputBox()

      #wait until text has been entered. Code below this line will not execute until text is entered
      await aio.event(sparkpy.EVENT, sparkpy.EVENT_INPUT)

      #text has been entered, retrieve the value that was entered 
      name = sparkpy.GetInputBoxValue()

      #out message to user, with the value they entered
      ybot.Chat("Welcome to sparkpy " + name)

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
To create a primitive use the `Primitive() <Source/sparkpy.html#sparkpy.Primitive>`_ object

.. code-block:: python
   :emphasize-lines: 7
   
   import sparkpy

   #create an environment
   sparkpy.Environment('office')

   #make a cube at position x=0 , y=0, z=0
   cube = sparkpy.Primitive('cube',0,0,0)
    
.. note:: The current list of primitive:

   +-------------+-----------+------------+
   |\"sphere\"   |\"capsule\"|\"cylinder\"|
   +-------------+-----------+------------+
   |\"plane\"    |\"quad\"   |\"cube\"    |
   +-------------+-----------+------------+
   
   To hide a created primitive, use the `Hide() <Source/sparkpy.html#sparkpy.Primitive.Hide>`_ method
   To show a previously hidden primitive, use the `Show() <Source/sparkpy.html#sparkpy.Primitive.Show>`_ method

""""""""""""""""""""
Set Primitive Colour
""""""""""""""""""""
To set the colour of a primitive, use the `SetColour() <Source/sparkpy.html#sparkpy.Primitive.SetColour>`_ method.
The method accepts the levels of red, green and blue was values between 0-1. The transparancy of a primitive can also be set as a avlue between 0 (fully invisible) to 1 (fully opaque)

.. code-block:: python
   :emphasize-lines: 10
   
   import sparkpy

   #create an environment
   sparkpy.Environment('forest')

   #make a cube at position x=0 , y=0, z=0
   cube = sparkpy.Primitive('cube',0,0,0)
   
   #set the colour to red (1=Red, 0=Blue, 0=Green)
   cube.SetColour(1,0,0) #1=Red, 0=Blue, 0=Green


""""""""""""""""""""
Destroy Primitive
""""""""""""""""""""
If a primitive is no longer needed in the program `Destroy() <Source/sparkpy.html#sparkpy.Primitive.Destroy>`_
will remove the primitive completely

.. code-block:: python
   :emphasize-lines: 10

   import sparkpy

   #must import aio for await to work
   from browser import aio

   #programs with await with be written inside an async function 
   async def main():

      #create an environment
      sparkpy.Environment('forest')

      #make a cube at position x=0 , y=1, z=0
      cube = sparkpy.Primitive('cube',0,1,0)

      #sleep for 3 seconds
      await aio.sleep(3)

      #the cube is no longer needed, remove it
      cube.Destroy()

   #run main
   sparkpy.Run(main)

""""""""""""""""""""""""""
Scale Primitive
""""""""""""""""""""""""""
   
To make a primitive bigger or smaller, use the
`Scale() <Source/sparkpy.html#sparkpy.Primitive.Scale>`_ method

.. code-block:: python
   :emphasize-lines: 10
   
   import sparkpy

   #create an environment
   sparkpy.Environment('forest')

   #make a cube at position x=0 , y=1, z=0
   cube = sparkpy.Primitive('cube',0,1,0)

   #double the size of the cube
   cube.Scale(2)

.. note:: 
   to scale in a specific direction (non-uniform scale), provide the sizes
   of the x,y,z when using `ScaleNonUniform() <Source/sparkpy.html#sparkpy.Primitive.ScaleNonUniform>`_
   
   .. code-block:: python
      :emphasize-lines: 10

      import sparkpy

      #create an environment
      sparkpy.Environment('forest')

      #make a cube at position x=0 , y=1, z=0
      cube = sparkpy.Primitive('cube',0,1,0)

      #double the size of the cube, along the x and z axis
      cube.ScaleNonUniform(2,1,2)

""""""""""""""""""""
Rotate Primitive
""""""""""""""""""""
To rotate a primitive, use the `Rotate() <Source/sparkpy.html#sparkpy.Primitive.Rotate>`_ 
by default primitives are rotated around their y (up) axis

.. code-block:: python
   :emphasize-lines: 10

   import sparkpy
      
   #create an environment
   sparkpy.Environment('office')

   #make a cube at position x=0 , y=1, z=0
   cube = sparkpy.Primitive('cube',0,1,0)

   #rotate the cube at a speed of 90 degrees per second
   cube.Rotate(90)

""""""""""""""""""""
Move Primitive
""""""""""""""""""""
To move a primitive, use the `Move() <Source/sparkpy.html#sparkpy.Primitive.Move>`_ method.

.. code-block:: python
   :emphasize-lines: 10

   import sparkpy

   #create an environment
   sparkpy.Environment('office')

   #make a cube at position x=0 , y=1, z=0
   cube = sparkpy.Primitive('cube',0,1,0)

   #move the cube to right at a speed of 4 for 1 seconds
   cube.Move(1, 4, "right")
    
.. note:: direction values can be:

   +------+--------+--------+---------+
   |\"up\"|\"down\"|\"left\"|\"right\"|
   +------+--------+--------+---------+
    

""""""""""""""""""""
Loop Primitive Move
""""""""""""""""""""
To make a primitive continuously move between two points, use the `LoopMove() <Source/sparkpy.html#sparkpy.Primitive.LoopMove>`_ 

.. code-block:: python
   :emphasize-lines: 10

   import sparkpy

   #create an environment
   sparkpy.Environment('office')

   #make a cube
   cube = sparkpy.Primitive('cube',0,1,0)
    
   #loop move from right to left and back again for 2 seconds at a speed of 1. 
   cube.LoopMove(2, 1, "right")
 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
LOGO programming with Trails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Trails is sparkpy's implementation of the Logo programming similiar to python turtles using 3D graphics

""""""""""""""""""""
Create Trails
""""""""""""""""""""

To start using trails create a `Trails() <Source/sparkpy.html#sparkpy.Trails>`_ Object 

.. code-block:: python

   import sparkpy

   #create a trails object
   t = sparkpy.Trails()

""""""""""""""""""""
Movement
""""""""""""""""""""

To move a trails character, use `Forward() <Source/sparkpy.html#sparkpy.Trails.Forward>`_ and `Backward() <Source/sparkpy.html#sparkpy.Trails.Backward>`_  

.. code-block:: python

   import sparkpy

   #create a trails object
   t = sparkpy.Trails()

   #move the trails object forward by a distance of 1 unit
   t.Forward(1)

""""""""""""""""""""
Rotation
""""""""""""""""""""
To rotate a trails character, use `Right() <Source/sparkpy.html#sparkpy.Trails.Right>`_ and `Left() <Source/sparkpy.html#sparkpy.Trails.Left>`_

.. code-block:: python
   :emphasize-lines: 10

   import sparkpy

   #create a trails character
   t = sparkpy.Trails()

   #move the trails character forward by a distance of 1 unit
   t.Forward(1)

   #turn left by 90 degrees
   t.Left(90)

   #move the trails character forward by a distance of 1 unit
   t.Forward(1)

""""""""""""""""""""
Pen Up & Pen Down
""""""""""""""""""""
To stop leaving trails as the character moves use `PenUp() <Source/sparkpy.html#sparkpy.Trails.PenUp>`_. To resume trails use `PenDown() <Source/sparkpy.html#sparkpy.Trails.PenDown>`_  
    
.. code-block:: python
   :emphasize-lines: 15,24

   import sparkpy

   #draw 2 parallel lines

   #create a trails character
   t = sparkpy.Trails()

   #move the trails character forward by a distance of 1 unit
   t.Forward(1)

   #turn left by 90 degrees
   t.Left(90)

   #stop trails effect
   t.PenUp()

   #move the trails character forward by a distance of 0.5 unit
   t.Forward(0.5)

   #turn left
   t.Left(90)

   #resume trails effect
   t.PenDown()

   #move the trails character forward by a distance of 1 unit
   t.Forward(1)

""""""""""""""""""""
Trail Colour
""""""""""""""""""""
To set the colour of the trail, use `PenColour <Source/sparkpy.html#sparkpy.Trails.PenColour>`_

.. code-block:: python
   :emphasize-lines: 7

   import sparkpy

   #create a trails character
   t = sparkpy.Trails()

   #set the trail colour to blue
   t.PenColour("blue")

   #move the trails character forward by a distance of 1 unit
   t.Forward(1)

   #turn left by 90 degrees
   t.Left(90)

   #move the trails character forward by a distance of 1 unit
   t.Forward(1)

.. note:: A full list of colours can be found at `Creating effects <index.html#creating-effects>`_


""""""""""""""""""""
Trail Size
""""""""""""""""""""

The size of the trail can be set using `PenSize() <Source/sparkpy.html#sparkpy.Trails.PenSize>`_


.. code-block:: python
   :emphasize-lines: 16

   import sparkpy

   #create a trails character
   t = sparkpy.Trails()

   #move the trails character forward by a distance of 1 unit
   t.Forward(1)

   #turn left by 90 degrees
   t.Left(90)

   #change the colour to blue
   t.PenColour("blue")

   #make the trail half the size
   t.PenSize(0.5)

   #move the trails character forward by a distance of 1 unit
   t.Forward(1)
