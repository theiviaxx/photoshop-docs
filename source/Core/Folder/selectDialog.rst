.. _Folder.selectDialog:

================================================
Folder.selectDialog
================================================

   :ref:`Folder` **selectDialog** (:ref:`string` **prompt**)


Parameters
----------

+------------+-------------------------------------------------+
| **prompt** | The prompt text, if the dialog allows a prompt. |
+------------+-------------------------------------------------+



Description
-----------

Opens the built-in platform-specific file-browsing dialog, and creates a new File or Folder object for the selected file or folder.

Differs from the object method selectDlg() in that it does not preselect a folder. If the user clicks OK, returns a File or Folder object for the selected file or folder. If the user cancels, returns null.


