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

To create a character, first make an environment then create the character ::
   
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

Set the animation for a character using  `SetAnimation  <Source/sparkpy.html#sparkpy.SetAnimation>`_ The speed of the animation can controlled with `SetAnimationSpeed <Source/sparkpy.html#sparkpy.SetAnimationSpeed>`_ ::

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

