ScriptUIGraphics.lineTo {#ScriptUIGraphics.lineTo}
=======================

> [Point]{role="ref"} **lineTo** ([Number]{role="ref"} **x**,
> [Number]{role="ref"} **y**)

Parameters
----------

  ------- ----------------------------------------------------------------
  **x**   The X coordinate for the destination point, relative to the
          origin of this element.

  **y**   The Y coordinate for the destination point, relative to the
          origin of this element.
  ------- ----------------------------------------------------------------

Description
-----------

Adds a path segment to the?currentPath.

The line is defined from the?currentPoint?to the specified destination
point. Returns the?Point?object for the destination point, which becomes
the new value of?currentPoint.
