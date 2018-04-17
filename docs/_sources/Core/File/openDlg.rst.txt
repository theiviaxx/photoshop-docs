.. _File.openDlg:

================================================
File.openDlg
================================================

   :ref:`File` **openDlg** (:ref:`string` **prompt**, any **filter**, bool **multiSelect**)


Parameters
----------

+-----------------+---------------------------------------------------------------------------------+
| **prompt**      | A string containing the prompt text, if the dialog allows a prompt.             |
+-----------------+---------------------------------------------------------------------------------+
| **filter**      | A filter that limits the types of files displayed in the dialog.                |
+-----------------+---------------------------------------------------------------------------------+
| **multiSelect** | When true, the user can select multiple files and the return value is an array. |
+-----------------+---------------------------------------------------------------------------------+



Description
-----------

Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file or files, and creates new File objects to represent the selected files.

Differs from the class method openDialog() in that it presets the current folder to this File object?s parent folder and the current file to this object?s associated file. If the user clicks OK, returns a File or Folder object for the selected file or folder, or an array of objects. If the user cancels, returns null.


