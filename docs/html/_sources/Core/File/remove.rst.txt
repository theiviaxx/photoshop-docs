.. _File.remove:

================================================
File.remove
================================================

   bool **remove** ()




Description
-----------

Deletes the file associated with this object from disk immediately, without moving it to the system trash.

Does not resolve aliases; instead, deletes the referenced alias or shortcut file itself. Returns true if the file was successfully removed. IMPORTANT: Cannot be undone. It is recommended that you prompt the user for permission before deleting.


