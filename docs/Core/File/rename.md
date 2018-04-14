File.rename {#File.rename}
===========

> bool **rename** ([string]{role="ref"} **newName**)

Parameters
----------

  ------------- ----------------------------------------------
  **newName**   The new file name, with no path information.
  ------------- ----------------------------------------------

Description
-----------

Renames the associated file.

Does not resolve aliases, but renames the referenced alias or shortcut
file itself. Returns true if the file was successfully renamed.
