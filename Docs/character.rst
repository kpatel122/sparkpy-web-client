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
         
.. note:: you will notice that the character's animation continues to play after the movement ends. This is behaviour can resolved using  `waits <wait.html#wait-for-seconds>`_ 

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

""""""""""""""""""""""""""""""""""""""""""""
Control character with keyboard 3rd Person
""""""""""""""""""""""""""""""""""""""""""""

To move a character with the keyboard, use the  `ControlMode()  <Source/sparkpy.html#sparkpy.Character.ControlMode>`_ method
A character can be controlled in third person mode using 'third_person' as the SetControlMode parameter

.. code-block:: python
   :emphasize-lines: 12
   
   import sparkpy

   #control character with keyboard example

   #create an environment
   sparkpy.Environment("Forest")

   #create robot character
   robot = sparkpy.Character("YBot")

   #set control mode to keyboard
   robot.ControlMode("third_person")

.. toctree:: 
   :maxdepth: -1
   :hidden:
