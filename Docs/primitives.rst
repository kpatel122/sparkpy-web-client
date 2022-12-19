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


.. toctree:: 
   :maxdepth: -1
   :hidden: