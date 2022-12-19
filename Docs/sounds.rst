"""""""""""""""""
Background music
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

""""""""""""""""""""
Character sound FX
""""""""""""""""""""
 
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


.. toctree:: 
   :maxdepth: -1
   :hidden: