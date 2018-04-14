BatchOptions {#BatchOptions}
============

Description
-----------

Options to specify when running a Batch command.

### Static Properties

  ----------------------------------------------------------------------- ----------------------------------------------
  [destination\<BatchOptions.destination\>]{role="ref"} readonly          The type of destination for the processed
                                                                          files.

  [destinationFolder\<BatchOptions.destinationFolder\>]{role="ref"}       The folder location for the processed files.
  readonly                                                                Valid only when \'destination\' = folder.

  [errorFile\<BatchOptions.errorFile\>]{role="ref"} readonly              The file in which to log errors encountered.
                                                                          To display errors on the screen and stop batch
                                                                          processing when errors occur, leave blank.

  [fileNaming\<BatchOptions.fileNaming\>]{role="ref"} readonly            A list of file naming options. Maximum: 6.

  [macintoshCompatible\<BatchOptions.macintoshCompatible\>]{role="ref"}   If true, the final file names are Macintosh
  readonly                                                                compatible.

  [overrideOpen\<BatchOptions.overrideOpen\>]{role="ref"} readonly        If true, overrides action open commands.

  [overrideSave\<BatchOptions.overrideSave\>]{role="ref"} readonly        If true, overrides save as action steps with
                                                                          the specified destination.

  [startingSerial\<BatchOptions.startingSerial\>]{role="ref"} readonly    The starting serial number to use in naming
                                                                          files.

  [suppressOpen\<BatchOptions.suppressOpen\>]{role="ref"} readonly        If true, suppresses file open options dialogs.

  [suppressProfile\<BatchOptions.suppressProfile\>]{role="ref"} readonly  If true, suppresses color profile warnings.

  [unixCompatible\<BatchOptions.unixCompatible\>]{role="ref"} readonly    If true, the final file names are Unix
                                                                          compatible.

  [windowsCompatible\<BatchOptions.windowsCompatible\>]{role="ref"}       If true, the final file names are Windows
  readonly                                                                compatible.
  ----------------------------------------------------------------------- ----------------------------------------------

::: {.container .hide}
::: {.toctree}
BatchOptions/overrideOpen.rst BatchOptions/suppressOpen.rst
BatchOptions/suppressProfile.rst BatchOptions/destination.rst
BatchOptions/destinationFolder.rst BatchOptions/overrideSave.rst
BatchOptions/fileNaming.rst BatchOptions/startingSerial.rst
BatchOptions/windowsCompatible.rst BatchOptions/macintoshCompatible.rst
BatchOptions/unixCompatible.rst BatchOptions/errorFile.rst
:::
:::
