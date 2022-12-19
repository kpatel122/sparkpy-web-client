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
   :emphasize-lines: 4,13,30,35
   
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

.. toctree:: 
   :maxdepth: -1
   :hidden: