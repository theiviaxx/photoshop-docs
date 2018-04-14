File.createAlias {#File.createAlias}
================

> void **createAlias** ([string]{role="ref"} **path**)

Parameters
----------

  ---------- --------------------------------------------------
  **path**   A string containing the path of the target file.
  ---------- --------------------------------------------------

Description
-----------

Makes this file a file-system alias or shortcut to the specified file.

The referenced file for this object must not yet exist on disk. Returns
true if the operation was successful.
