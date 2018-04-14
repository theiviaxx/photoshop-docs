Folder.getFiles {#Folder.getFiles}
===============

> [Array]{role="ref"} **getFiles** (any **mask**)

Parameters
----------

  ---------- -------------------------------------------------------------
  **mask**   A search mask for file names, specified as a string or a
             function.
  ---------- -------------------------------------------------------------

Description
-----------

Retrieves the contents of this folder, filtered by the supplied mask.

Returns an array of File and Folder objects, or null if this object\'s
referenced folder does not exist.
