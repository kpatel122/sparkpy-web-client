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

.. note:: A full list of colours can be found at `Creating effects <effects.html#creating-effects>`_


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

.. toctree:: 
   :maxdepth: -1
   :hidden: