.. _File.openDialog:

================================================
File.openDialog
================================================

   :ref:`File` **openDialog** (:ref:`string` **prompt**, any **filter**, bool **multiSelect**)


Parameters
----------

+-----------------+---------------------------------------------------------------------------------+
| **prompt**      | The prompt text, displayed if the dialog allows a prompt.                       |
+-----------------+---------------------------------------------------------------------------------+
| **filter**      | A filter that limits the types of files displayed in the dialog.                |
+-----------------+---------------------------------------------------------------------------------+
| **multiSelect** | When true, the user can select multiple files and the return value is an array. |
+-----------------+---------------------------------------------------------------------------------+



Description
-----------

Opens a dialog so the user can select one or more files to open.

Opens the built-in platform-specific file-browsing dialog in which a user can select an existing file or multiple files, and creates new File objects to represent the selected files. If the user clicks OK, returns a File object for the selected file, or an array of objects if multiple files are selected. If the user cancels, returns null.


