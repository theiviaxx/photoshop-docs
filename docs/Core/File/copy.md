File.copy {#File.copy}
=========

> bool **copy** ([string]{role="ref"} **target**)

Parameters
----------

  ------------ ---------------------------------------------------------------
  **target**   A string with the URI path to the target location, or a File
               object that references the target location.
  ------------ ---------------------------------------------------------------

Description
-----------

Copies this object?s referenced file to the specified target location.

Resolves any aliases to find the source file. If a file exists at the
target location, it is overwritten. Returns true if the copy was
successful.
