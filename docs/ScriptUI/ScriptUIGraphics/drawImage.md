ScriptUIGraphics.drawImage {#ScriptUIGraphics.drawImage}
==========================

> void **drawImage** ([ScriptUIImage]{role="ref"} **image**,
> [Number]{role="ref"} **left**, [Number]{role="ref"} **top**,
> [Number]{role="ref"} **width**, [Number]{role="ref"} **height**)

Parameters
----------

  ------------ ----------------------------------------------------------------
  **image**    The image to draw.

  **left**     The left coordinate of the region, relative to the origin of
               this element.

  **top**      The top coordinate of the region, relative to the origin of this
               element.

  **width**    The width in pixels. If provided, the image is stretched or
               shrunk to fit. If omitted, uses the original image width.

  **height**   The height in pixels. If provided, the image is stretched or
               shrunk to fit. If omitted, uses the original image height.
  ------------ ----------------------------------------------------------------

Description
-----------

Draws an image within a given region of the element.

Uses the version of the image that is appropriate to the element\'s
current state.
