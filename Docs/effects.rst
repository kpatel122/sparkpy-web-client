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

.. toctree:: 
   :maxdepth: -1
   :hidden: