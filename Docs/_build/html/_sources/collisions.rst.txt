""""""""""""""""""""""""
Collision (non blocking)
""""""""""""""""""""""""

Collisions can be captured between two characters or primitives, using a callback function set with `SetCollisionHandler() <Source/sparkpy.html#sparkpy.SetCollisionHandler>`_ 
when a collision occurs, the callback function is called. The callback function must have two parameters which will be set to the ids of the two objects that collided.
To retrieve a character object from the ids, use `GetCharacterFromID() <Source/sparkpy.html#sparkpy.GetCharacterFromID>`_


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
   be run *after* a collision has occured, use async await for `collision event() <wait.html#wait-for-collision>`_ 

 
""""""""""""""""""""
Collision (blocking)
""""""""""""""""""""

`See wait for collision <wait.html#wait-for-collision>`_ 

.. toctree:: 
   :maxdepth: -1
   :hidden: