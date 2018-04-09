.. _Window.confirm:

================================================
Window.confirm
================================================

   :ref:`Boolean` **confirm** (:ref:`String` **message**, :ref:`Boolean` **noAsDefault**, :ref:`String` **title**)


Parameters
----------

+-----------------+-------------------------------------------------------------------------------------+
| **message**     | The string for the displayed message.                                               |
+-----------------+-------------------------------------------------------------------------------------+
| **noAsDefault** | When true, the No button is the default choice, selected when the user types Enter. |
+-----------------+-------------------------------------------------------------------------------------+
| **title**       | A string to appear as the title of the dialog, if the platform supports a title.    |
+-----------------+-------------------------------------------------------------------------------------+



Description
-----------

Displays a platform-standard dialog containing a short message and two buttons labeled Yes and No.

Returns true if the user clicked Yes, false if the user clicked No.


