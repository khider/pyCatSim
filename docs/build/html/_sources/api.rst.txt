.. _api:

PyCatSim User API
===================

PyCatSim, like a lot of other Python packages, follows an object-oriented design. It sounds fancy, but it really is `quite simple <https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/>`_. What this means for you is that we've gone through the trouble of coding up a lot of methods that apply in various situations - so you don't have to worry about that.
These situations are described in classes, the beauty of which is called "inheritance" (see link above). Basically, it allows to define methods that will automatically apply to your use case, as long as you put your data within one of those classes.
A major advantage of object-oriented design is that you, the user, can harness the power of PyCatSim in very few lines of code through the user API without ever having to get your hands dirty with our code (unless you want to, of course).
The flipside is that any user would do well to understand PyCatSim classes, what they are intended for, and what methods they support.

The following describes the various classes that undergird the PyCatsim edifice.

Cat (pyCatSim.Cat)
""""""""""""""""""

.. autoclass:: pyCatSim.api.cat.Cat
   :members:

Owner (pyCatSim.Owner)
""""""""""""""""""""""

.. autoclass:: pyCatSim.api.human.Owner
   :members:


