Document.print {#Document.print}
==============

> void **print** ([SourceSpaceType]{role="ref"} **sourceSpace**,
> [string]{role="ref"} **printSpace**, [Intent]{role="ref"} **intent**,
> bool **blackPointCompensation**)

Parameters
----------

  ---------------------------- ------------------------------------------------------------
  **sourceSpace**              The color space for the source.

  **printSpace**               The color space for the printer. Can be \"nothing\" (meaning
                               same as source); one of the working spaces or Lab color; or
                               a string specifying a color space. Default: nothing.

  **intent**                   The color conversion intent.

  **blackPointCompensation**   If true, black point compensation is used.
  ---------------------------- ------------------------------------------------------------

Description
-----------

Prints the document.
