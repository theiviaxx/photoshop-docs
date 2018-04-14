ScriptUIGraphics.rectPath {#ScriptUIGraphics.rectPath}
=========================

> [Point]{role="ref"} **rectPath** ([Number]{role="ref"} **left**,
> [Number]{role="ref"} **top**, [Number]{role="ref"} **width**,
> [Number]{role="ref"} **height**)

Parameters
----------

  ------------ ----------------------------------------------------------
  **left**     The left coordinate relative to the origin of this
               element.

  **top**      The top coordinate relative to the origin of this element.

  **width**    The width in pixels.

  **height**   The height in pixels.
  ------------ ----------------------------------------------------------

Description
-----------

Defines a rectangular path in the?currentPath?object.

The rectangle can be filled using?fillPath()?or stroked
using?strokePath().Returns the?Point?object for the upper left corner of
the rectangle, which becomes the new value of?currentPoint.
