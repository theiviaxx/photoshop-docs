ScriptUI {#ScriptUI}
========

Description
-----------

A global class containing central information about ScriptUI. Not
instantiable.

### Static Properties

  ------------------------------------------------------------- -----------------------------------------------
  [Alignment\<ScriptUI.Alignment\>]{role="ref"} readonly        Collects the enumerated values that can be used
                                                                in the alignment and alignChildren properties
                                                                of controls and containers.

  [FontStyle\<ScriptUI.FontStyle\>]{role="ref"} readonly        Collects the enumerated values that can be used
                                                                as the style argument to
                                                                the?ScriptUI.newFont()?method.

  [applicationFonts\<ScriptUI.applicationFonts\>]{role="ref"}   The font constants defined by the host
  readonly                                                      application.

  [compatibility\<ScriptUI.compatibility\>]{role="ref"}         An object whose properties are the names of
  readonly                                                      compatability modes supported by the host
                                                                application.

  [coreVersion\<ScriptUI.coreVersion\>]{role="ref"} readonly    A string containing the internal version number
                                                                of the ScriptUI module.

  [environment\<ScriptUI.environment\>]{role="ref"} readonly    An object whose properties define attributes of
                                                                the environment in which ScriptUI operates.

  [events\<ScriptUI.events\>]{role="ref"} readonly              An object whose properties and methods provide
                                                                access to objects used in the ScriptUI event
                                                                system.

  [frameworkName\<ScriptUI.frameworkName\>]{role="ref"}         A string containing the name of the UI
  readonly                                                      component framework with which this version of
                                                                ScriptUI is compatible.

  [version\<ScriptUI.version\>]{role="ref"} readonly            A string containing the version number of the
                                                                ScriptUI component framework
  ------------------------------------------------------------- -----------------------------------------------

### Static Methods

  ----------------------------------------------------------- --------------------------------------------
  [getResourceText\<ScriptUI.getResourceText\>]{role="ref"}   Finds and returns the resource for a given
  readonly                                                    text string from the host application\'s
                                                              resource data.

  [newFont\<ScriptUI.newFont\>]{role="ref"} readonly          Creates a new font object for use in text
                                                              controls and titles.

  [newImage\<ScriptUI.newImage\>]{role="ref"} readonly        Loads a new image from resources or disk
                                                              files into an image object.
  ----------------------------------------------------------- --------------------------------------------

::: {.container .hide}
::: {.toctree}
ScriptUI/applicationFonts.rst ScriptUI/compatibility.rst
ScriptUI/coreVersion.rst ScriptUI/environment.rst ScriptUI/events.rst
ScriptUI/frameworkName.rst ScriptUI/version.rst ScriptUI/Alignment.rst
ScriptUI/FontStyle.rst

ScriptUI/getResourceText.rst ScriptUI/newImage.rst ScriptUI/newFont.rst
:::
:::
