Preferences {#Preferences}
===========

Description
-----------

Options to define for the preferences property of the application
object, basically equivalent to selecting Edit \> Preferences (Windows)
or Photoshop \> Preferences in the Adobe Photoshop application.

### Properties

  ------------------------------------------------------------------------------------ ------------------------------------------
  [additionalPluginFolder\<Preferences.additionalPluginFolder\>]{role="ref"} readonly  The path to the additional plug-in folder.
                                                                                       Valid only when \'use additional plugin
                                                                                       folder\' = true.

  [appendExtension\<Preferences.appendExtension\>]{role="ref"} readonly                Save files with extensions on Windows.

  [askBeforeSavingLayeredTIFF\<Preferences.askBeforeSavingLayeredTIFF\>]{role="ref"}   If true, asks the user to verify layer
  readonly                                                                             preservation options when saving a file in
                                                                                       TIFF format.

  [autoUpdateOpenDocuments\<Preferences.autoUpdateOpenDocuments\>]{role="ref"}         If true, automatically updates open
  readonly                                                                             documents.

  [beepWhenDone\<Preferences.beepWhenDone\>]{role="ref"} readonly                      If true, alerts the user when a process
                                                                                       finishes.

  [colorChannelsInColor\<Preferences.colorChannelsInColor\>]{role="ref"} readonly      If true, displays component channels in
                                                                                       the Channels palette in color.

  [colorPicker\<Preferences.colorPicker\>]{role="ref"} readonly                        The color picker to use.

  [columnGutter\<Preferences.columnGutter\>]{role="ref"} readonly                      The gutter of columns (in points)

  [columnWidth\<Preferences.columnWidth\>]{role="ref"} readonly                        The width of columns (in points)

  [createFirstSnapshot\<Preferences.createFirstSnapshot\>]{role="ref"} readonly        If true, automatically makes the first
                                                                                       snapshot when a new document is created.

  [dynamicColorSliders\<Preferences.dynamicColorSliders\>]{role="ref"} readonly        If true, dynamic color sliders appear in
                                                                                       the Color palette.

  [editLogItems\<Preferences.editLogItems\>]{role="ref"} readonly                      Options for edit log items.

  [exportClipboard\<Preferences.exportClipboard\>]{role="ref"} readonly                If true, retains Adobe Photoshop contents
                                                                                       on the clipboard after you exit the
                                                                                       application.

  [fontPreviewSize\<Preferences.fontPreviewSize\>]{role="ref"} readonly                Show font previews in the type tool font
                                                                                       menus.

  [fullSizePreview\<Preferences.fullSizePreview\>]{role="ref"} readonly                If true, shows the image preview as a full
                                                                                       size image.

  [gamutWarningOpacity\<Preferences.gamutWarningOpacity\>]{role="ref"} readonly        The opacity (as a percentage) of the
                                                                                       warning color for out-of-gamut colors.
                                                                                       Range: 0 to 100.

  [gridSize\<Preferences.gridSize\>]{role="ref"} readonly                              The size of grid squares.

  [gridStyle\<Preferences.gridStyle\>]{role="ref"} readonly                            The formatting style for non-printing grid
                                                                                       lines.

  [gridSubDivisions\<Preferences.gridSubDivisions\>]{role="ref"} readonly              The value by which to subdivide the grid.

  [guideStyle\<Preferences.guideStyle\>]{role="ref"} readonly                          The formatting style for non-printing
                                                                                       guide lines.

  [iconPreview\<Preferences.iconPreview\>]{role="ref"} readonly                        If true, shows the image preview as a
                                                                                       thumbnail.

  [imageCacheForHistograms\<Preferences.imageCacheForHistograms\>]{role="ref"}         If true, shows the current image cache
  readonly                                                                             used to create the histogram.

  [imageCacheLevels\<Preferences.imageCacheLevels\>]{role="ref"} readonly              The number of images to hold in the cache.
                                                                                       Range: 1 to 8.

  [imagePreviews\<Preferences.imagePreviews\>]{role="ref"} readonly                    The behavior mode to use when saving
                                                                                       files.

  [interpolation\<Preferences.interpolation\>]{role="ref"} readonly                    The method to use to assign color values
                                                                                       to any new pixels created when an image is
                                                                                       resampled or resized.

  [keyboardZoomResizesWindows\<Preferences.keyboardZoomResizesWindows\>]{role="ref"}   If true, automatically resizes the window
  readonly                                                                             when zooming in or out using keyboard
                                                                                       shortcuts.

  [macOSThumbnail\<Preferences.macOSThumbnail\>]{role="ref"} readonly                  If true, creates a thumbnail when saving
                                                                                       the image in Mac OS.

  [maxRAMuse\<Preferences.maxRAMuse\>]{role="ref"} readonly                            Maximum percentage of available RAM used
                                                                                       by Photoshop.

  [maximizeCompatibility\<Preferences.maximizeCompatibility\>]{role="ref"} readonly    The behavior to use to check whether to
                                                                                       maximize compatibility when opening Adobe
                                                                                       Photoshop (PSD) files.

  [nonLinearHistory\<Preferences.nonLinearHistory\>]{role="ref"} readonly              If true, allows non-linear history.

  [numberOfHistoryStates\<Preferences.numberOfHistoryStates\>]{role="ref"} readonly    The number of history states to preserve.
                                                                                       Range: 1 to 100.

  [otherCursors\<Preferences.otherCursors\>]{role="ref"} readonly                      The type of pointer to use.

  [paintingCursors\<Preferences.paintingCursors\>]{role="ref"} readonly                The type of pointer to use.

  [parent\<Preferences.parent\>]{role="ref"} readonly                                  The object\'s container.

  [pixelDoubling\<Preferences.pixelDoubling\>]{role="ref"} readonly                    If true, halves the resolution or (doubles
                                                                                       the size of pixels) to make previews
                                                                                       display more quickly.

  [pointSize\<Preferences.pointSize\>]{role="ref"} readonly                            The point/pica size.

  [recentFileListLength\<Preferences.recentFileListLength\>]{role="ref"} readonly      The number of items in the recent file
                                                                                       list. Range: 0 to 30.

  [rulerUnits\<Preferences.rulerUnits\>]{role="ref"} readonly                          The unit that the scripting system uses
                                                                                       when receiving and returning values.

  [saveLogItems\<Preferences.saveLogItems\>]{role="ref"} readonly                      Options for saving the history items.

  [saveLogItemsFile\<Preferences.saveLogItemsFile\>]{role="ref"} readonly              File to save the history log.

  [savePaletteLocations\<Preferences.savePaletteLocations\>]{role="ref"} readonly      If true, makes new palette locations the
                                                                                       default location.

  [showAsianTextOptions\<Preferences.showAsianTextOptions\>]{role="ref"} readonly      If true, Asian text options are displayed
                                                                                       in the Paragraph palette.

  [showEnglishFontNames\<Preferences.showEnglishFontNames\>]{role="ref"} readonly      If true, Asian font names are listed in
                                                                                       English.

  [showSliceNumber\<Preferences.showSliceNumber\>]{role="ref"} readonly                If true, displays slice numbers in the
                                                                                       document window when using the Slice tool.

  [showToolTips\<Preferences.showToolTips\>]{role="ref"} readonly                      If true, pop-up definitions are displayed
                                                                                       on mouseover.

  [smartQuotes\<Preferences.smartQuotes\>]{role="ref"} readonly                        If true, curly quote marks are used.

  [textFontSize\<Preferences.textFontSize\>]{role="ref"} readonly                      Size of the small font used in panels and
                                                                                       dialogs.

  [typeUnits\<Preferences.typeUnits\>]{role="ref"} readonly                            The unit type-size that the numeric inputs
                                                                                       are assumed to represent.

  [typename\<Preferences.typename\>]{role="ref"} readonly                              The class name of the object.

  [useAdditionalPluginFolder\<Preferences.useAdditionalPluginFolder\>]{role="ref"}     If true, uses an additional folder for
  readonly                                                                             compatible plug-ins stored with a
                                                                                       different application.

  [useDiffusionDither\<Preferences.useDiffusionDither\>]{role="ref"} readonly          If true, uses diffusion dither.

  [useHistoryLog\<Preferences.useHistoryLog\>]{role="ref"} readonly                    Turn on and off the history logging.

  [useLowerCaseExtension\<Preferences.useLowerCaseExtension\>]{role="ref"} readonly    If true, the file extension is lowercase.

  [useShiftKeyForToolSwitch\<Preferences.useShiftKeyForToolSwitch\>]{role="ref"}       If true, enables cycling through a set of
  readonly                                                                             hidden tools.

  [useVideoAlpha\<Preferences.useVideoAlpha\>]{role="ref"} readonly                    If true, enables Adobe Photoshop to send
                                                                                       transparency information to your
                                                                                       computer?s video board. (Requires hardware
                                                                                       support.)

  [windowsThumbnail\<Preferences.windowsThumbnail\>]{role="ref"} readonly              If true, creates a thumbnail when saving
                                                                                       the image in Windows. (Requires hardware
                                                                                       support.)
  ------------------------------------------------------------------------------------ ------------------------------------------

::: {.container .hide}
::: {.toctree}
Preferences/parent.rst Preferences/typename.rst
Preferences/colorPicker.rst Preferences/interpolation.rst
Preferences/exportClipboard.rst Preferences/showToolTips.rst
Preferences/keyboardZoomResizesWindows.rst
Preferences/autoUpdateOpenDocuments.rst
Preferences/showAsianTextOptions.rst Preferences/beepWhenDone.rst
Preferences/dynamicColorSliders.rst Preferences/savePaletteLocations.rst
Preferences/showEnglishFontNames.rst
Preferences/useShiftKeyForToolSwitch.rst Preferences/textFontSize.rst
Preferences/numberOfHistoryStates.rst
Preferences/createFirstSnapshot.rst Preferences/nonLinearHistory.rst
Preferences/smartQuotes.rst Preferences/imagePreviews.rst
Preferences/iconPreview.rst Preferences/fullSizePreview.rst
Preferences/macOSThumbnail.rst Preferences/windowsThumbnail.rst
Preferences/appendExtension.rst Preferences/useLowerCaseExtension.rst
Preferences/askBeforeSavingLayeredTIFF.rst
Preferences/maximizeCompatibility.rst
Preferences/recentFileListLength.rst
Preferences/colorChannelsInColor.rst Preferences/useDiffusionDither.rst
Preferences/pixelDoubling.rst Preferences/paintingCursors.rst
Preferences/otherCursors.rst Preferences/gridSize.rst
Preferences/useVideoAlpha.rst Preferences/gamutWarningOpacity.rst
Preferences/rulerUnits.rst Preferences/typeUnits.rst
Preferences/columnWidth.rst Preferences/columnGutter.rst
Preferences/pointSize.rst Preferences/guideStyle.rst
Preferences/gridStyle.rst Preferences/gridSubDivisions.rst
Preferences/showSliceNumber.rst
Preferences/useAdditionalPluginFolder.rst
Preferences/additionalPluginFolder.rst Preferences/imageCacheLevels.rst
Preferences/imageCacheForHistograms.rst Preferences/maxRAMuse.rst
Preferences/useHistoryLog.rst Preferences/saveLogItems.rst
Preferences/editLogItems.rst Preferences/saveLogItemsFile.rst
Preferences/fontPreviewSize.rst
:::
:::
