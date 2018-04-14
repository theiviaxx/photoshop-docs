Document.saveAs {#Document.saveAs}
===============

> void **saveAs** ([File]{role="ref"} **saveIn**, any **options**, bool
> **asCopy**, [MacExtensionType]{role="ref"} **extensionType**)

Parameters
----------

  ------------------- --------------------------------------------------------------
  **saveIn**          The file to save to, specified as a string containing the full
                      file path or an alias. If not specified, the document is saved
                      to its existing file.

  **options**         Options for the specified file type.

  **asCopy**          Saves the document as a copy, leaving the original open.

  **extensionType**   Appends the specified extension to the file name.
  ------------------- --------------------------------------------------------------

Description
-----------

Saves the document with the specified save options.
