.. _Folder.remove:

================================================
Folder.remove
================================================

   bool **remove** ()




Description
-----------

Deletes the folder associated with this object from disk immediately, without moving it to the system trash.

Folders must be empty before they can be deleted. Does not resolve aliases; instead, deletes the referenced alias or shortcut file itself. Returns true if the file was successfully removed. IMPORTANT: Cannot be undone. It is recommended that you prompt the user for permission before deleting.


