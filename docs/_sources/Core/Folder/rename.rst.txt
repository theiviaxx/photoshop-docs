.. _Folder.rename:

================================================
Folder.rename
================================================

   bool **rename** (:ref:`string` **newName**)


Parameters
----------

+-------------+------------------------------------------------+
| **newName** | The new folder name, with no path information. |
+-------------+------------------------------------------------+



Description
-----------

Renames the associated folder.

Does not resolve aliases, but renames the referenced alias or shortcut file itself. Returns true if the folder was successfully renamed.


