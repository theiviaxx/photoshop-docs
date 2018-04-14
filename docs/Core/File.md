File {#File}
====

Description
-----------

Represents a file in the local file system in a platform-independent
manner.

### Properties

  ----------------------------------------------- --------------------------------------------------
  [absoluteURI\<File.absoluteURI\>]{role="ref"}   The full path name for the referenced file in URI
  readonly                                        notation.

  [alias\<File.alias\>]{role="ref"} readonly      If true, the object refers to a file system alias
                                                  or shortcut.

  [created\<File.created\>]{role="ref"} readonly  The creation date of the referenced file, or null
                                                  if the object does not refer to a file on disk.

  [creator\<File.creator\>]{role="ref"} readonly  In Mac OS, the file creator as a four-character
                                                  string. In Windows or UNIX, value is \"????\".

  [displayName\<File.displayName\>]{role="ref"}   The localized name of the referenced file, without
  readonly                                        the path specification.

  [encoding\<File.encoding\>]{role="ref"}         Gets or sets the encoding for subsequent
  readonly                                        read/write operations.

  [eof\<File.eof\>]{role="ref"} readonly          When true, a read attempt caused the current
                                                  position to be at the end of the file, or the file
                                                  is not open.

  [error\<File.error\>]{role="ref"} readonly      A string containing a message describing the most
                                                  recent file system error.

  [exists\<File.exists\>]{role="ref"} readonly    If true, this object refers to a file or
                                                  file-system alias that actually exists in the file
                                                  system.

  [fsName\<File.fsName\>]{role="ref"} readonly    The platform-specific full path name for the
                                                  referenced file.

  [fullName\<File.fullName\>]{role="ref"}         The full path name for the referenced file in URI
  readonly                                        notation.

  [hidden\<File.hidden\>]{role="ref"} readonly    When true, the file is not shown in the
                                                  platform-specific file browser.

  [length\<File.length\>]{role="ref"} readonly    The size of the file in bytes.

  [lineFeed\<File.lineFeed\>]{role="ref"}         How line feed characters are written in the file
  readonly                                        system.

  [modified\<File.modified\>]{role="ref"}         The date of the referenced file\'s last
  readonly                                        modification, or null if the object does not refer
                                                  to a file on the disk.

  [name\<File.name\>]{role="ref"} readonly        The file name portion of the absolute URI for the
                                                  referenced file, without the path specification.

  [parent\<File.parent\>]{role="ref"} readonly    The Folder object for the folder that contains
                                                  this file.

  [path\<File.path\>]{role="ref"} readonly        The path portion of the absolute URI for the
                                                  referenced file, without the file name.

  [readonly\<File.readonly\>]{role="ref"}         When true, prevents the file from being altered or
  readonly                                        deleted.

  [relativeURI\<File.relativeURI\>]{role="ref"}   The path name for the object in URI notation,
  readonly                                        relative to the current folder.

  [type\<File.type\>]{role="ref"} readonly        The file type as a four-character string.
  ----------------------------------------------- --------------------------------------------------

### Static Properties

  ----------------------------- ------------------------------
  [fs\<File.fs\>]{role="ref"}   The name of the file system.
  readonly                      
  ----------------------------- ------------------------------

### Constructors

  --------------------------------- --------------------------------------------------
  [File\<File.File\>]{role="ref"}   Creates and returns a new File object referring to
  readonly                          a given file system location.
  --------------------------------- --------------------------------------------------

### Methods

  ----------------------------------------------------- --------------------------------------------------------
  [changePath\<File.changePath\>]{role="ref"} readonly  Changes the path specification of the referenced file.

  [close\<File.close\>]{role="ref"} readonly            Closes this open file.

  [copy\<File.copy\>]{role="ref"} readonly              Copies this object?s referenced file to the specified
                                                        target location.

  [createAlias\<File.createAlias\>]{role="ref"}         Makes this file a file-system alias or shortcut to the
  readonly                                              specified file.

  [execute\<File.execute\>]{role="ref"} readonly        Executes or opens this file using the appropriate
                                                        application, as if it had been double-clicked in a file
                                                        browser.

  [getRelativeURI\<File.getRelativeURI\>]{role="ref"}   Retrieves and returns the path for this file, relative
  readonly                                              to the specified base path, in URI notation.

  [open\<File.open\>]{role="ref"} readonly              Opens the referenced file for subsequent read/write
                                                        operations. The method resolves any aliases to find the
                                                        file.

  [openDlg\<File.openDlg\>]{role="ref"} readonly        Opens the built-in platform-specific file-browsing
                                                        dialog, in which the user can select an existing file or
                                                        files, and creates new File objects to represent the
                                                        selected files.

  [read\<File.read\>]{role="ref"} readonly              Reads the contents of the file, starting at the current
                                                        position.

  [readch\<File.readch\>]{role="ref"} readonly          Reads a single text character from the file at the
                                                        current position.

  [readln\<File.readln\>]{role="ref"} readonly          Reads a single line of text from the file at the current
                                                        position.

  [remove\<File.remove\>]{role="ref"} readonly          Deletes the file associated with this object from disk
                                                        immediately, without moving it to the system trash.

  [rename\<File.rename\>]{role="ref"} readonly          Renames the associated file.

  [resolve\<File.resolve\>]{role="ref"} readonly        Attempts to resolve the file-system alias or shortcut
                                                        that this object refers to.

  [saveDlg\<File.saveDlg\>]{role="ref"} readonly        Opens the built-in platform-specific file-browsing
                                                        dialog, in which the user can select an existing file
                                                        location to which to save information, and creates a new
                                                        File object to represent the selected file.

  [seek\<File.seek\>]{role="ref"} readonly              Seeks to a given position in the file.

  [tell\<File.tell\>]{role="ref"} readonly              Retrieves the current position as a byte offset from the
                                                        start of the file.

  [toSource\<File.toSource\>]{role="ref"} readonly      Creates and returns a serialized string representation
                                                        of this object.

  [toString\<File.toString\>]{role="ref"} readonly      Converts this object to a string.

  [write\<File.write\>]{role="ref"} readonly            Writes the specified text to the file at the current
                                                        position.

  [writeln\<File.writeln\>]{role="ref"} readonly        Writes a string to the file at the current position and
                                                        appends a line-feed sequence.
  ----------------------------------------------------- --------------------------------------------------------

### Static Methods

  --------------------------------------------------------------- -----------------------------------------
  [decode\<File.decode\>]{role="ref"} readonly                    Decodes a UTF-8 encoded string as
                                                                  required by RFC 2396, and returns the
                                                                  decoded string.

  [encode\<File.encode\>]{role="ref"} readonly                    Encodes a string as required by RFC 2396,
                                                                  and returns the encoded string.

  [isEncodingAvailable\<File.isEncodingAvailable\>]{role="ref"}   Reports whether a given encoding is
  readonly                                                        available.

  [openDialog\<File.openDialog\>]{role="ref"} readonly            Opens a dialog so the user can select one
                                                                  or more files to open.

  [saveDialog\<File.saveDialog\>]{role="ref"} readonly            Opens a dialog so the user can select a
                                                                  file name to save to.
  --------------------------------------------------------------- -----------------------------------------

::: {.container .hide}
::: {.toctree}
File/alias.rst File/created.rst File/error.rst File/exists.rst
File/fsName.rst File/fullName.rst File/absoluteURI.rst
File/relativeURI.rst File/modified.rst File/name.rst
File/displayName.rst File/path.rst File/parent.rst File/type.rst
File/creator.rst File/hidden.rst File/readonly.rst File/lineFeed.rst
File/length.rst File/encoding.rst File/eof.rst

File/fs.rst

File/resolve.rst File/rename.rst File/remove.rst File/changePath.rst
File/getRelativeURI.rst File/execute.rst File/openDlg.rst
File/saveDlg.rst File/toString.rst File/toSource.rst
File/createAlias.rst File/open.rst File/close.rst File/read.rst
File/readch.rst File/readln.rst File/write.rst File/writeln.rst
File/seek.rst File/tell.rst File/copy.rst

File/encode.rst File/decode.rst File/isEncodingAvailable.rst
File/openDialog.rst File/saveDialog.rst

File/File.rst
:::
:::
