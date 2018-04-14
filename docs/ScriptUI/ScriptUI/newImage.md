ScriptUI.newImage {#ScriptUI.newImage}
=================

> [ScriptUIImage]{role="ref"} **newImage** ([String]{role="ref"}
> **normal**, [String]{role="ref"} **disabled**, [String]{role="ref"}
> **pressed**, [String]{role="ref"} **rollover**)

Parameters
----------

  -------------- ------------------------------------------------------------
  **normal**     The resource name or the disk file path to the image used
                 for the normal state.

  **disabled**   The resource name, or the disk file path to the image used
                 for the disabled state.

  **pressed**    The resource name, or the file-system path to the image used
                 for the pressed state.

  **rollover**   The resource name, or the file-system path to the image used
                 for the rollover state.
  -------------- ------------------------------------------------------------

Description
-----------

Loads a new image from resources or disk files into an image object.

Creates a new global image object for use in controls that can display
images, loading the associated images from the specified resources or
image files.
