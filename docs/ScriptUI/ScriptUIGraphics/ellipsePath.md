ScriptUIGraphics.ellipsePath {#ScriptUIGraphics.ellipsePath}
============================

> [Point]{role="ref"} **ellipsePath** ([Number]{role="ref"} **left**,
> [Number]{role="ref"} **top**, [Number]{role="ref"} **width**,
> [Number]{role="ref"} **height**)

Parameters
----------

  ------------ ------------------------------------------------------------
  **left**     The left coordinate of the region, relative to the origin of
               this element.

  **top**      The top coordinate of the region, relative to the origin of
               this element.

  **width**    The width of the region in pixels.

  **height**   The height of the region in pixels.
  ------------ ------------------------------------------------------------

Description
-----------

Defines an elliptical path within a given rectangular area in
the?currentPath?object, which can be filled using?fillPath()?or stroked
using?strokePath().

Returns a?Point?object for the upper left corner of the area, which is
the new?currentPoint.
