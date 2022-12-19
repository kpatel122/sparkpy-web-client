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


Indices and tables
==================

* :ref:`genindex`

* `Full API Reference <Source/sparkpy.html>`_  


-------------
Introduction
-------------
Sparkpy is a platform to learn and create Python programming projects using interactive 3D graphics.

:doc:`environment`
    How to make a background environment

.. Hidden TOCs

.. toctree::
   :caption: Environments 
   :maxdepth: -1
   :hidden:

   environment

:doc:`character`
   Creating and animating characters

.. Hidden TOCs

.. toctree::
   :caption: Characters 
   :maxdepth: -1
   :hidden:

   character

:doc:`input`
    User input

.. Hidden TOCs

.. toctree::
   :caption: Input 
   :maxdepth: -1
   :hidden:

   input

:doc:`collisions`
    Detecting collisions between characters and objects

.. Hidden TOCs

.. toctree::
   :caption: Collisions 
   :maxdepth: -1
   :hidden:

   collisions

:doc:`sounds`
    Making sounds

.. Hidden TOCs

.. toctree::
   :caption: Sounds 
   :maxdepth: -1
   :hidden:

   sounds

:doc:`effects`
    Special effects

.. Hidden TOCs

.. toctree::
   :caption: Effects 
   :maxdepth: -1
   :hidden:

   effects

:doc:`wait`
    Pausing your program and waiting for events

.. Hidden TOCs

.. toctree::
   :caption: Wait 
   :maxdepth: -1
   :hidden:

   wait

:doc:`primitives`
    Creating different primitive shapes

.. Hidden TOCs

.. toctree::
   :caption: Primitives 
   :maxdepth: -1
   :hidden:

   primitives

:doc:`trails`
    Trails is sparkpy's implementation of the Logo programming similiar to python turtles using 3D graphics

.. Hidden TOCs

.. toctree::
   :caption: LOGO programming with Trails 
   :maxdepth: -1
   :hidden:

   trails
