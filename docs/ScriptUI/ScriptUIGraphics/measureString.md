ScriptUIGraphics.measureString {#ScriptUIGraphics.measureString}
==============================

> [Dimension]{role="ref"} **measureString** ([String]{role="ref"}
> **text**, [ScriptUIFont]{role="ref"} **font**, [Number]{role="ref"}
> **boundingWidth**)

Parameters
----------

  ------------------- -----------------------------------------------------
  **text**            The text string to measure.

  **font**            The font to use. Default is the?font?value in this
                      object.

  **boundingWidth**   The bounding width.
  ------------------- -----------------------------------------------------

Description
-----------

Calculates the size needed to display a string using the given font.

Returns a?Dimension?object that contains the height and width of the
string in pixels.
