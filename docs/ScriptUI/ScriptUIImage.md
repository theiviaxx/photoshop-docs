ScriptUIImage {#ScriptUIImage}
=============

Description
-----------

Encapsulates a set of images that can be drawn into a control.

Different images can reflect the current state, such as a dimmed version
for a disabled control. Create with the?newImage()?method. Passed as an
argument to?drawImage().

### Properties

  -------------------------------------------------- -------------------------------------------
  [format\<ScriptUIImage.format\>]{role="ref"}       The image format. One of: resource, JPEG,
  readonly                                           GIF, TIFF, PNG, or PICT (Macintosh).

  [name\<ScriptUIImage.name\>]{role="ref"} readonly  The image name. Either the file name, or
                                                     the resource name.

  [pathname\<ScriptUIImage.pathname\>]{role="ref"}   The full path to the file that contains the
  readonly                                           image.

  [size\<ScriptUIImage.size\>]{role="ref"} readonly  The image size in pixels.
  -------------------------------------------------- -------------------------------------------

::: {.container .hide}
::: {.toctree}
ScriptUIImage/format.rst ScriptUIImage/name.rst
ScriptUIImage/pathname.rst ScriptUIImage/size.rst
:::
:::
