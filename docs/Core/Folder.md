Folder {#Folder}
======

Description
-----------

Represents a file-system folder or directory in a platform-independent
manner.

### Properties

  ------------------------------------------------- --------------------------------------------------
  [absoluteURI\<Folder.absoluteURI\>]{role="ref"}   The full path name for the referenced folder in
  readonly                                          URI notation.

  [alias\<Folder.alias\>]{role="ref"} readonly      When true, the object refers to a file system
                                                    alias or shortcut.

  [created\<Folder.created\>]{role="ref"} readonly  The creation date of the referenced folder, or
                                                    null if the object does not refer to a folder on
                                                    disk.

  [displayName\<Folder.displayName\>]{role="ref"}   The localized name portion of the absolute URI for
  readonly                                          the referenced folder, without the path
                                                    specification.

  [error\<Folder.error\>]{role="ref"} readonly      A message describing the most recent file system
                                                    error.

  [exists\<Folder.exists\>]{role="ref"} readonly    When true, this object refers to a folder that
                                                    currently exists in the file system.

  [fsName\<Folder.fsName\>]{role="ref"} readonly    The platform-specific name of the referenced
                                                    folder as a full path name.

  [fullName\<Folder.fullName\>]{role="ref"}         The full path name for the referenced folder in
  readonly                                          URI notation. .

  [modified\<Folder.modified\>]{role="ref"}         The date of the referenced folder\'s last
  readonly                                          modification, or null if the object does not refer
                                                    to a folder on disk.

  [name\<Folder.name\>]{role="ref"} readonly        The folder name portion of the absolute URI for
                                                    the referenced file, without the path
                                                    specification.

  [parent\<Folder.parent\>]{role="ref"} readonly    TThe Folder object for the folder that contains
                                                    this folder, or null if this object refers to the
                                                    root folder of a volume.

  [path\<Folder.path\>]{role="ref"} readonly        The path portion of the object absolute URI for
                                                    the referenced file, without the folder name.

  [relativeURI\<Folder.relativeURI\>]{role="ref"}   The path name for the referenced folder in URI
  readonly                                          notation, relative to the current folder.
  ------------------------------------------------- --------------------------------------------------

### Static Properties

  ------------------------------------------------- -------------------------------------------------------
  [appData\<Folder.appData\>]{role="ref"} readonly  The folder containing the application data for all
                                                    users.

  [appPackage\<Folder.appPackage\>]{role="ref"}     In Mac OS, a Folder object for the folder containing
  readonly                                          the bundle of the running application.

  [commonFiles\<Folder.commonFiles\>]{role="ref"}   A Folder object for the folder containing common files
  readonly                                          for all programs installed by the user.

  [current\<Folder.current\>]{role="ref"} readonly  A Folder object for the current folder.

  [desktop\<Folder.desktop\>]{role="ref"} readonly  A Folder object for the folder that contains the user?s
                                                    desktop.

  [fs\<Folder.fs\>]{role="ref"} readonly            The name of the current file system.

  [myDocuments\<Folder.myDocuments\>]{role="ref"}   A folder pointing to the user\'s My Documents folder.
  readonly                                          

  [startup\<Folder.startup\>]{role="ref"} readonly  A Folder object for the folder containing the
                                                    executable image of the running application.

  [system\<Folder.system\>]{role="ref"} readonly    A Folder object for the folder containing the operating
                                                    system files.

  [temp\<Folder.temp\>]{role="ref"} readonly        A Folder object for the default folder for temporary
                                                    files.

  [trash\<Folder.trash\>]{role="ref"} readonly      A Folder object for the folder containing deleted
                                                    items. On Windows, the trash folder is a virtual folder
                                                    containing a database; therefore, the property value is
                                                    null on Windows.

  [userData\<Folder.userData\>]{role="ref"}         A Folder object for the folder containing the user\'s
  readonly                                          application data.
  ------------------------------------------------- -------------------------------------------------------

### Constructors

  --------------------------------------- ------------------------------------------------
  [Folder\<Folder.Folder\>]{role="ref"}   Creates and returns a new Folder object
  readonly                                referring to a given file-system location.
  --------------------------------------- ------------------------------------------------

### Methods

  ------------------------------------------------------- --------------------------------------------------
  [changePath\<Folder.changePath\>]{role="ref"} readonly  Changes the path specification of the referenced
                                                          folder.

  [create\<Folder.create\>]{role="ref"} readonly          Creates a folder at the location given by this
                                                          object\'s?path?property.

  [execute\<Folder.execute\>]{role="ref"} readonly        Opens this folder in the platform-specific file
                                                          browser (as if it had been double-clicked in the
                                                          file browser).

  [getFiles\<Folder.getFiles\>]{role="ref"} readonly      Retrieves the contents of this folder, filtered by
                                                          the supplied mask.

  [getRelativeURI\<Folder.getRelativeURI\>]{role="ref"}   Retrieves and returns the path for this file,
  readonly                                                relative to the specified base path, in URI
                                                          notation.

  [remove\<Folder.remove\>]{role="ref"} readonly          Deletes the folder associated with this object
                                                          from disk immediately, without moving it to the
                                                          system trash.

  [rename\<Folder.rename\>]{role="ref"} readonly          Renames the associated folder.

  [resolve\<Folder.resolve\>]{role="ref"} readonly        Attempts to resolve the file-system alias or
                                                          shortcut that this object refers to.

  [selectDlg\<Folder.selectDlg\>]{role="ref"} readonly    Opens the built-in platform-specific file-browsing
                                                          dialog, and creates a new File or Folder object
                                                          for the selected file or folder.

  [toSource\<Folder.toSource\>]{role="ref"} readonly      Creates and returns a serialized string
                                                          representation of this object.

  [toString\<Folder.toString\>]{role="ref"} readonly      Converts this object to a string.
  ------------------------------------------------------- --------------------------------------------------

### Static Methods

  ----------------------------------------------------------------- -----------------------------------------------
  [decode\<Folder.decode\>]{role="ref"} readonly                    Decodes a UTF-8 encoded string as required by
                                                                    RFC 2396, and returns the decoded string.

  [encode\<Folder.encode\>]{role="ref"} readonly                    Encodes a string as required by RFC 2396, and
                                                                    returns the encoded string.

  [isEncodingAvailable\<Folder.isEncodingAvailable\>]{role="ref"}   Reports whether a given encoding is available.
  readonly                                                          

  [selectDialog\<Folder.selectDialog\>]{role="ref"} readonly        Opens the built-in platform-specific
                                                                    file-browsing dialog, and creates a new File or
                                                                    Folder object for the selected file or folder.
  ----------------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
Folder/alias.rst Folder/created.rst Folder/error.rst Folder/exists.rst
Folder/fsName.rst Folder/fullName.rst Folder/absoluteURI.rst
Folder/relativeURI.rst Folder/modified.rst Folder/name.rst
Folder/displayName.rst Folder/path.rst Folder/parent.rst

Folder/fs.rst Folder/current.rst Folder/startup.rst
Folder/appPackage.rst Folder/system.rst Folder/trash.rst Folder/temp.rst
Folder/userData.rst Folder/appData.rst Folder/commonFiles.rst
Folder/myDocuments.rst Folder/desktop.rst

Folder/resolve.rst Folder/rename.rst Folder/remove.rst
Folder/changePath.rst Folder/getRelativeURI.rst Folder/execute.rst
Folder/toString.rst Folder/toSource.rst Folder/selectDlg.rst
Folder/getFiles.rst Folder/create.rst

Folder/encode.rst Folder/decode.rst Folder/isEncodingAvailable.rst
Folder/selectDialog.rst

Folder/Folder.rst
:::
:::
