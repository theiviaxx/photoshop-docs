File.saveDialog {#File.saveDialog}
===============

> [File]{role="ref"} **saveDialog** ([string]{role="ref"} **prompt**,
> any **filter**)

Parameters
----------

  ------------ -------------------------------------------------------------
  **prompt**   The prompt text, displayed if the dialog allows a prompt.

  **filter**   In Windows only, a filter that limits the types of files
               displayed in the dialog.
  ------------ -------------------------------------------------------------

Description
-----------

Opens a dialog so the user can select a file name to save to.

Opens the built-in platform-specific file-browsing dialog in which a
user can select an existing file location to which to save information,
and creates a new File object to represent the selected file location.
If the user clicks OK, returns a File object for the selected file
location. If the user cancels, returns null.
