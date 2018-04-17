.. _ScriptUIGraphics.rectPath:

================================================
ScriptUIGraphics.rectPath
================================================

   :ref:`Point` **rectPath** (:ref:`Number` **left**, :ref:`Number` **top**, :ref:`Number` **width**, :ref:`Number` **height**)


Parameters
----------

+------------+-------------------------------------------------------------+
| **left**   | The left coordinate relative to the origin of this element. |
+------------+-------------------------------------------------------------+
| **top**    | The top coordinate relative to the origin of this element.  |
+------------+-------------------------------------------------------------+
| **width**  | The width in pixels.                                        |
+------------+-------------------------------------------------------------+
| **height** | The height in pixels.                                       |
+------------+-------------------------------------------------------------+



Description
-----------

Defines a rectangular path in the?currentPath?object.

The rectangle can be filled using?fillPath()?or stroked using?strokePath().Returns the?Point?object  for the upper left corner of the rectangle, which becomes the new value of?currentPoint.


