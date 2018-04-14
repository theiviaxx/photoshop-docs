.. _Folder.selectDlg:

================================================
Folder.selectDlg
================================================

   :ref:`Folder` **selectDlg** (:ref:`string` **prompt**)


Parameters
----------

+------------+-------------------------------------------------+
| **prompt** | The prompt text, if the dialog allows a prompt. |
+------------+-------------------------------------------------+



Description
-----------

Opens the built-in platform-specific file-browsing dialog, and creates a new File or Folder object for the selected file or folder.

Differs from the class method selectDialog() in that it preselects this folder. If the user clicks OK, returns a File or Folder object for the selected file or folder. If the user cancels, returns null.


