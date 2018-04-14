.. _File:

================================================
File
================================================


Description
-----------

Represents a file in the local file system in a platform-independent manner.




Properties
^^^^^^^^^^

+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`absoluteURI<File.absoluteURI>` readonly | The full path name for the referenced file in URI notation.                                                      |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`alias<File.alias>` readonly             | If true, the object refers to a file system alias or shortcut.                                                   |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`created<File.created>` readonly         | The creation date of the referenced file, or null if the object does not refer to a file on disk.                |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`creator<File.creator>` readonly         | In Mac OS, the file creator as a four-character string. In Windows or UNIX, value is "????".                     |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`displayName<File.displayName>` readonly | The localized name of the referenced file, without the path specification.                                       |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`encoding<File.encoding>` readonly       | Gets or sets the encoding for subsequent read/write operations.                                                  |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`eof<File.eof>` readonly                 | When true, a read attempt caused the current position to be at the end of the file, or the file is not open.     |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`error<File.error>` readonly             | A string containing a message describing the most recent file system error.                                      |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`exists<File.exists>` readonly           | If true, this object refers to a file or file-system alias that actually exists in the file system.              |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`fsName<File.fsName>` readonly           | The platform-specific full path name for the referenced file.                                                    |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`fullName<File.fullName>` readonly       | The full path name for the referenced file in URI notation.                                                      |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`hidden<File.hidden>` readonly           | When true, the file is not shown in the platform-specific file browser.                                          |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`length<File.length>` readonly           | The size of the file in bytes.                                                                                   |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`lineFeed<File.lineFeed>` readonly       | How line feed characters are written in the file system.                                                         |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`modified<File.modified>` readonly       | The date of the referenced file's last modification, or null if the object does not refer to a file on the disk. |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`name<File.name>` readonly               | The file name portion of the absolute URI for the referenced file, without the path specification.               |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<File.parent>` readonly           | The Folder object for the folder that contains this file.                                                        |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`path<File.path>` readonly               | The path portion of the absolute URI for the referenced file, without the file name.                             |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`readonly<File.readonly>` readonly       | When true, prevents the file from being altered or deleted.                                                      |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`relativeURI<File.relativeURI>` readonly | The path name for the object in URI notation, relative to the current folder.                                    |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`type<File.type>` readonly               | The file type as a four-character string.                                                                        |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+

Static Properties
^^^^^^^^^^^^^^^^^

+-----------------------------+------------------------------+
| :ref:`fs<File.fs>` readonly | The name of the file system. |
+-----------------------------+------------------------------+


Constructors
^^^^^^^^^^^^

+---------------------------------+----------------------------------------------------------------------------------+
| :ref:`File<File.File>` readonly | Creates and returns a new File object referring to a given file system location. |
+---------------------------------+----------------------------------------------------------------------------------+


Methods
^^^^^^^

+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`changePath<File.changePath>` readonly         | Changes the path specification of the referenced file.                                                                                                                                                        |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`close<File.close>` readonly                   | Closes this open file.                                                                                                                                                                                        |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`copy<File.copy>` readonly                     | Copies this object?s referenced file to the specified target location.                                                                                                                                        |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`createAlias<File.createAlias>` readonly       | Makes this file a file-system alias or shortcut to the specified file.                                                                                                                                        |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`execute<File.execute>` readonly               | Executes or opens this file using the appropriate application, as if it had been double-clicked in a file browser.                                                                                            |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`getRelativeURI<File.getRelativeURI>` readonly | Retrieves and returns the path for this file, relative to the specified base path, in URI notation.                                                                                                           |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`open<File.open>` readonly                     | Opens the referenced file for subsequent read/write operations. The method resolves any aliases to find the file.                                                                                             |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`openDlg<File.openDlg>` readonly               | Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file or files, and creates new File objects to represent the selected files.                              |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`read<File.read>` readonly                     | Reads the contents of the file, starting at the current position.                                                                                                                                             |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`readch<File.readch>` readonly                 | Reads a single text character from the file at the current position.                                                                                                                                          |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`readln<File.readln>` readonly                 | Reads a single line of text from the file at the current position.                                                                                                                                            |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`remove<File.remove>` readonly                 | Deletes the file associated with this object from disk immediately, without moving it to the system trash.                                                                                                    |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`rename<File.rename>` readonly                 | Renames the associated file.                                                                                                                                                                                  |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`resolve<File.resolve>` readonly               | Attempts to resolve the file-system alias or shortcut that this object refers to.                                                                                                                             |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`saveDlg<File.saveDlg>` readonly               | Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file location to which to save information, and creates a new File object to represent the selected file. |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`seek<File.seek>` readonly                     | Seeks to a given position in the file.                                                                                                                                                                        |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`tell<File.tell>` readonly                     | Retrieves the current position as a byte offset from the start of the file.                                                                                                                                   |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`toSource<File.toSource>` readonly             | Creates and returns a serialized string representation of this object.                                                                                                                                        |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`toString<File.toString>` readonly             | Converts this object to a string.                                                                                                                                                                             |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`write<File.write>` readonly                   | Writes the specified text to the file at the current position.                                                                                                                                                |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`writeln<File.writeln>` readonly               | Writes a string to the file at the current position and appends a line-feed sequence.                                                                                                                         |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Static Methods
^^^^^^^^^^^^^^

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| :ref:`decode<File.decode>` readonly                           | Decodes a UTF-8 encoded string as required by RFC 2396, and returns the decoded string. |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| :ref:`encode<File.encode>` readonly                           | Encodes a string as required by RFC 2396, and returns the encoded string.               |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| :ref:`isEncodingAvailable<File.isEncodingAvailable>` readonly | Reports whether a given encoding is available.                                          |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| :ref:`openDialog<File.openDialog>` readonly                   | Opens a dialog so the user can select one or more files to open.                        |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| :ref:`saveDialog<File.saveDialog>` readonly                   | Opens a dialog so the user can select a file name to save to.                           |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+




.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      File/alias.rst
      File/created.rst
      File/error.rst
      File/exists.rst
      File/fsName.rst
      File/fullName.rst
      File/absoluteURI.rst
      File/relativeURI.rst
      File/modified.rst
      File/name.rst
      File/displayName.rst
      File/path.rst
      File/parent.rst
      File/type.rst
      File/creator.rst
      File/hidden.rst
      File/readonly.rst
      File/lineFeed.rst
      File/length.rst
      File/encoding.rst
      File/eof.rst
      
      File/fs.rst
      

      File/resolve.rst
      File/rename.rst
      File/remove.rst
      File/changePath.rst
      File/getRelativeURI.rst
      File/execute.rst
      File/openDlg.rst
      File/saveDlg.rst
      File/toString.rst
      File/toSource.rst
      File/createAlias.rst
      File/open.rst
      File/close.rst
      File/read.rst
      File/readch.rst
      File/readln.rst
      File/write.rst
      File/writeln.rst
      File/seek.rst
      File/tell.rst
      File/copy.rst
      
      File/encode.rst
      File/decode.rst
      File/isEncodingAvailable.rst
      File/openDialog.rst
      File/saveDialog.rst
      
      
      File/File.rst
      