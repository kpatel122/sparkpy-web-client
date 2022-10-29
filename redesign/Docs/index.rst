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
 
.. highlight:: python 
   :linenothreshold: 1

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
   ybot = sparkpy.CreateCharacter("YBot2")

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
   ybot = sparkpy.CreateCharacter("xbot",0,0,3)

   #set animation to walk
   sparkpy.SetAnimation(ybot, "Walk")

   #move the character for 5 seconds
   sparkpy.Move(ybot,5)
   
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

   #create robot character at position x=0 y0 z=3
   bryce = sparkpy.CreateCharacter("bryce",0,0,3)

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

A character can create a chat box using the `Chat <Source/sparkpy.html#sparkpy.Hide>`_ Chat

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
Input box
""""""""""""""""""""""""""""""""

A character can create a chat box using the `Chat <Source/sparkpy.html#sparkpy.Hide>`_ Chat

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #textbox example

   #input box handler function
   def InputEntered(msg):
      
      #print the recieved text
      print("recieved " + msg)

   #create desert environment test
   sparkpy.CreateEnvironment('desert');
   
   #show input box
   sparkpy.ShowInputBox()
   
   #set the callback function
   sparkpy.SetInputBoxHandler(InputEntered)


""""""""""""""""""""""""""""""""
Control character with keyboard
""""""""""""""""""""""""""""""""

To move a character with the keyboard, use the  `SetControlMode  <Source/sparkpy.html#sparkpy.SetControlMode>`_ method ::
   
   import sparkpy

   #control character with keyboard example

   #create office environment
   sparkpy.CreateEnvironment("Office")

   #create robot character
   ybot = sparkpy.CreateCharacter("YBot")

   #set control mode to keyboard
   sparkpy.SetControlMode(ybot,"keyboard")

