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
   be run *after* input has been entered, you can use python input(see below)- though this will block the entire application including any animations and character movement or `async await for input event(). <wait.html#wait-for-input>`_

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

.. toctree:: 
   :maxdepth: -1
   :hidden: