.. _File.saveDlg:

================================================
File.saveDlg
================================================

   :ref:`File` **saveDlg** (:ref:`string` **prompt**, any **filter**)


Parameters
----------

+------------+-----------------------------------------------------------------------------------+
| **prompt** | A string containing the prompt text, if the dialog allows a prompt.               |
+------------+-----------------------------------------------------------------------------------+
| **filter** | In Windows only, a filter that limits the types of files displayed in the dialog. |
+------------+-----------------------------------------------------------------------------------+



Description
-----------

Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file location to which to save information, and creates a new File object to represent the selected file.

Differs from the class method saveDialog() in that it presets the current folder to this File object?s parent folder and the file to this object?s associated file. If the user clicks OK, returns a File object for the selected file. If the user cancels, returns null.


