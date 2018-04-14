Application {#Application}
===========

Description
-----------

The Adobe Photoshop application object, which contains all other Adobe
Photoshop objects.

This is the root of the object model, and provides access to all other
objects. To access the properties and methods, you can use the
pre-defined global variable app. For example: var currentDoc =
app.activeDocument;

### Properties

  ---------------------------------------------------------------------------- ------------------------------------------------
  [activeDocument\<Application.activeDocument\>]{role="ref"} readonly          The frontmost document.

  [backgroundColor\<Application.backgroundColor\>]{role="ref"} readonly        The default background color (used to paint,
                                                                               fill, and stroke selections).

  [build\<Application.build\>]{role="ref"} readonly                            The build number of Adobe Photoshop application.

  [colorSettings\<Application.colorSettings\>]{role="ref"} readonly            The name of the selected color setting\'s set.

  [currentTool\<Application.currentTool\>]{role="ref"} readonly                Name of the current tool.

  [displayDialogs\<Application.displayDialogs\>]{role="ref"} readonly          The dialog mode for the document, which
                                                                               indicates whether or not Photoshop displays
                                                                               dialogs when the script runs.

  [documents\<Application.documents\>]{role="ref"} readonly                    The collection of open documents.

  [fonts\<Application.fonts\>]{role="ref"} readonly                            The fonts installed on this system.

  [foregroundColor\<Application.foregroundColor\>]{role="ref"} readonly        The default foreground color (used to paint,
                                                                               fill, and stroke selections).

  [freeMemory\<Application.freeMemory\>]{role="ref"} readonly                  The amount of unused memory available to
                                                                               Photoshop.

  [locale\<Application.locale\>]{role="ref"} readonly                          The language locale of the application.

  [macintoshFileTypes\<Application.macintoshFileTypes\>]{role="ref"} readonly  A list of the image file types Photoshop can
                                                                               open.

  [measurementLog\<Application.measurementLog\>]{role="ref"} readonly          The log of measurements taken.

  [name\<Application.name\>]{role="ref"} readonly                              The application name.

  [notifiers\<Application.notifiers\>]{role="ref"} readonly                    The notifiers currently configured (in the
                                                                               Scripts Events Manager menu in the application).

  [notifiersEnabled\<Application.notifiersEnabled\>]{role="ref"} readonly      If true, notifiers are enabled.

  [parent\<Application.parent\>]{role="ref"} readonly                          The object\'s container.

  [path\<Application.path\>]{role="ref"} readonly                              The full path of the location of the Adobe
                                                                               Photoshop application.

  [playbackDisplayDialogs\<Application.playbackDisplayDialogs\>]{role="ref"}   The dialog mode for playback mode, which
  readonly                                                                     indicates whether or not Photoshop displays
                                                                               dialogs in playback mode.

  [playbackParameters\<Application.playbackParameters\>]{role="ref"} readonly  The playback options, which indicate the speed
                                                                               at which Photoshop plays actions.

  [preferences\<Application.preferences\>]{role="ref"} readonly                The application preference settings (equivalent
                                                                               to selecting Edit \> Preferences in the Adobe
                                                                               Photoshop application in Windows or Photoshop \>
                                                                               Preferences in Mac OS).

  [preferencesFolder\<Application.preferencesFolder\>]{role="ref"} readonly    The full path to the preferences folder.

  [recentFiles\<Application.recentFiles\>]{role="ref"} readonly                Files in the Recent Files list.

  [scriptingBuildDate\<Application.scriptingBuildDate\>]{role="ref"} readonly  The build date of the scripting interface.

  [scriptingVersion\<Application.scriptingVersion\>]{role="ref"} readonly      The version of the Scripting interface.

  [systemInformation\<Application.systemInformation\>]{role="ref"} readonly    System information of the host application and
                                                                               machine.

  [typename\<Application.typename\>]{role="ref"} readonly                      The class name of the object.

  [version\<Application.version\>]{role="ref"} readonly                        The version of Adobe Photoshop application that
                                                                               you are running.

  [windowsFileTypes\<Application.windowsFileTypes\>]{role="ref"} readonly      A list of the image file extensions Photoshop
                                                                               can open.
  ---------------------------------------------------------------------------- ------------------------------------------------

### Methods

  -------------------------------------------------------------------------- -------------------------------------------------------
  [batch\<Application.batch\>]{role="ref"} readonly                          Runs the batch automation routine; analogous to using
                                                                             the Batch command in Photoshop.

  [beep\<Application.beep\>]{role="ref"} readonly                            Alerts the user.

  [bringToFront\<Application.bringToFront\>]{role="ref"} readonly            Makes Photoshop the active application.

  [changeProgressText\<Application.changeProgressText\>]{role="ref"}         Changes the text that appears in the progress window.
  readonly                                                                   

  [charIDToTypeID\<Application.charIDToTypeID\>]{role="ref"} readonly        Converts from a four character code to a runtime ID.

  [doAction\<Application.doAction\>]{role="ref"} readonly                    Plays the specified action from the Actions palette.

  [doForcedProgress\<Application.doForcedProgress\>]{role="ref"} readonly    Performs a task with a progress bar. Forces progress
                                                                             bar to display, ignoring the normal heuristics that
                                                                             keep it from showing unnecessarily (e.g. during very
                                                                             short tasks). Other progress APIs must be called
                                                                             periodically to update the progress bar and allow
                                                                             cancelling.

  [doProgress\<Application.doProgress\>]{role="ref"} readonly                Performs a task with a progress bar. Other progress
                                                                             APIs must be called periodically to update the progress
                                                                             bar and allow cancelling.

  [doProgressSegmentTask\<Application.doProgressSegmentTask\>]{role="ref"}   Sections off a portion of the unused progress bar for
  readonly                                                                   execution of a subtask. Returns false on cancel. Use
                                                                             when iterating a list of tasks with unequal run times.

  [doProgressSubTask\<Application.doProgressSubTask\>]{role="ref"} readonly  Sections off a portion of the unused progress bar for
                                                                             execution of a subtask. Returns false on cancel. Use
                                                                             when iterating a simple list of tasks with equal run
                                                                             times.

  [doProgressTask\<Application.doProgressTask\>]{role="ref"} readonly        Sections off a portion of the unused progress bar for
                                                                             execution of a subtask. Returns false on cancel.

  [eraseCustomOptions\<Application.eraseCustomOptions\>]{role="ref"}         Removes the specified user objects from the Photoshop
  readonly                                                                   registry.

  [executeAction\<Application.executeAction\>]{role="ref"} readonly          Plays an ActionManager event.

  [executeActionGet\<Application.executeActionGet\>]{role="ref"} readonly    Obtains an action descriptor.

  [featureEnabled\<Application.featureEnabled\>]{role="ref"} readonly        If true, the specified feature is enabled.

  [getCustomOptions\<Application.getCustomOptions\>]{role="ref"} readonly    Retrieves user objects from the Photoshop registry for
                                                                             the ID with value key.

  [isQuicktimeAvailable\<Application.isQuicktimeAvailable\>]{role="ref"}     Returns true if Quicktime is installed.
  readonly                                                                   

  [load\<Application.load\>]{role="ref"} readonly                            Loads a support document.

  [makeContactSheet\<Application.makeContactSheet\>]{role="ref"} readonly    Creates a contact sheet from multiple files.

  [makePDFPresentation\<Application.makePDFPresentation\>]{role="ref"}       Creates a PDF presentation file.
  readonly                                                                   

  [makePhotoGallery\<Application.makePhotoGallery\>]{role="ref"} readonly    DEPRECATED. Creates a web photo gallery.

  [makePhotomerge\<Application.makePhotomerge\>]{role="ref"} readonly        DEPRECATED. Merges multiple files into one, user
                                                                             interaction required.

  [makePicturePackage\<Application.makePicturePackage\>]{role="ref"}         Creates a picture package from multiple files.
  readonly                                                                   

  [open\<Application.open\>]{role="ref"} readonly                            Opens the specified document file(s).

  [openDialog\<Application.openDialog\>]{role="ref"} readonly                Uses the Photoshop open dialog to select files.

  [purge\<Application.purge\>]{role="ref"} readonly                          Purges one or more caches.

  [putCustomOptions\<Application.putCustomOptions\>]{role="ref"} readonly    Save user objects in the Photoshop registry.

  [refresh\<Application.refresh\>]{role="ref"} readonly                      Pauses the script until the application refreshes.

  [refreshFonts\<Application.refreshFonts\>]{role="ref"} readonly            Force the font list to get refreshed.

  [runMenuItem\<Application.runMenuItem\>]{role="ref"} readonly              Run a menu item.

  [showColorPicker\<Application.showColorPicker\>]{role="ref"} readonly      Display color picker dialog. Returns false if dialog is
                                                                             cancelled, true otherwise.

  [stringIDToTypeID\<Application.stringIDToTypeID\>]{role="ref"} readonly    Converts from a string ID to a runtime ID.

  [system\<Application.system\>]{role="ref"} readonly                        Perform a system call.

  [togglePalettes\<Application.togglePalettes\>]{role="ref"} readonly        Toggle palette visibility.

  [toolSupportsBrushes\<Application.toolSupportsBrushes\>]{role="ref"}       Check if the specified tool supports brushes.
  readonly                                                                   

  [typeIDToCharID\<Application.typeIDToCharID\>]{role="ref"} readonly        Converts from a runtime ID to a character ID.

  [typeIDToStringID\<Application.typeIDToStringID\>]{role="ref"} readonly    Converts from a runtime ID to a string ID.

  [updateProgress\<Application.updateProgress\>]{role="ref"} readonly        Updates the progress bar started by doProgress. Use for
                                                                             manual non-task based progress updating. Returns false
                                                                             on cancel.
  -------------------------------------------------------------------------- -------------------------------------------------------

::: {.container .hide}
::: {.toctree}
Application/parent.rst Application/typename.rst
Application/colorSettings.rst Application/activeDocument.rst
Application/name.rst Application/path.rst Application/preferences.rst
Application/scriptingVersion.rst Application/freeMemory.rst
Application/version.rst Application/displayDialogs.rst
Application/foregroundColor.rst Application/backgroundColor.rst
Application/playbackParameters.rst
Application/playbackDisplayDialogs.rst Application/notifiersEnabled.rst
Application/windowsFileTypes.rst Application/macintoshFileTypes.rst
Application/preferencesFolder.rst Application/locale.rst
Application/documents.rst Application/fonts.rst
Application/notifiers.rst Application/scriptingBuildDate.rst
Application/recentFiles.rst Application/build.rst
Application/systemInformation.rst Application/measurementLog.rst
Application/currentTool.rst

Application/toolSupportsBrushes.rst Application/doProgress.rst
Application/doForcedProgress.rst Application/changeProgressText.rst
Application/doProgressTask.rst Application/doProgressSegmentTask.rst
Application/doProgressSubTask.rst Application/updateProgress.rst
Application/togglePalettes.rst Application/doAction.rst
Application/load.rst Application/open.rst Application/purge.rst
Application/makePhotoGallery.rst Application/makePDFPresentation.rst
Application/makePhotomerge.rst Application/makeContactSheet.rst
Application/makePicturePackage.rst Application/batch.rst
Application/bringToFront.rst Application/refresh.rst
Application/refreshFonts.rst Application/putCustomOptions.rst
Application/getCustomOptions.rst Application/eraseCustomOptions.rst
Application/featureEnabled.rst Application/openDialog.rst
Application/runMenuItem.rst Application/system.rst
Application/executeAction.rst Application/executeActionGet.rst
Application/stringIDToTypeID.rst Application/typeIDToStringID.rst
Application/charIDToTypeID.rst Application/typeIDToCharID.rst
Application/beep.rst Application/isQuicktimeAvailable.rst
Application/showColorPicker.rst
:::
:::
