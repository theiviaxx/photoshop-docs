ArtLayer.adjustColorBalance {#ArtLayer.adjustColorBalance}
===========================

> void **adjustColorBalance** (int **shadows**, int **midtones**, int
> **highlights**, bool **preserveLuminosity**)

Parameters
----------

  ------------------------ ---------------------------------------------------------------
  **shadows**              The adjustments for the shadows. The array must include three
                           values (in the range -100 to 100), which represent cyan or red,
                           magenta or green, and yellow or blue, when the document mode is
                           CMYK or RGB.

  **midtones**             The adjustments for the midtones. The array must include three
                           values (in the range -100 to 100), which represent cyan or red,
                           magenta or green, and yellow or blue, when the document mode is
                           CMYK or RGB.

  **highlights**           The adjustments for the highlights. The array must include
                           three values (in the range -100 to 100), which represent cyan
                           or red, magenta or green, and yellow or blue, when the document
                           mode is CMYK or RGB.

  **preserveLuminosity**   If true, luminosity is preserved.
  ------------------------ ---------------------------------------------------------------

Description
-----------

Adjusts the color balance of the layer\'s component channels.
