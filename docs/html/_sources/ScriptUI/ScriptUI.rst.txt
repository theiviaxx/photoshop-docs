.. _ScriptUI:

================================================
ScriptUI
================================================


Description
-----------

A global class containing central information about ScriptUI. Not instantiable.






Static Properties
^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`Alignment<ScriptUI.Alignment>` readonly               | Collects the enumerated values that can be used in the alignment and alignChildren properties of controls and containers. |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`FontStyle<ScriptUI.FontStyle>` readonly               | Collects the enumerated values that can be used as the style argument to the?ScriptUI.newFont()?method.                   |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`applicationFonts<ScriptUI.applicationFonts>` readonly | The font constants defined by the host application.                                                                       |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`compatibility<ScriptUI.compatibility>` readonly       | An object whose properties are the names of compatability modes supported by the host application.                        |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`coreVersion<ScriptUI.coreVersion>` readonly           | A string containing the internal version number of the ScriptUI module.                                                   |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`environment<ScriptUI.environment>` readonly           | An object whose properties define attributes of the environment in which ScriptUI operates.                               |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`events<ScriptUI.events>` readonly                     | An object whose properties and methods provide access to objects used in the ScriptUI event system.                       |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`frameworkName<ScriptUI.frameworkName>` readonly       | A string containing the name of the UI component framework with which this version of ScriptUI is compatible.             |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| :ref:`version<ScriptUI.version>` readonly                   | A string containing the version number of the ScriptUI component framework                                                |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+







Static Methods
^^^^^^^^^^^^^^

+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`getResourceText<ScriptUI.getResourceText>` readonly | Finds and returns the resource for a given text string from the host application's resource data. |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`newFont<ScriptUI.newFont>` readonly                 | Creates a new font object for use in text controls and titles.                                    |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`newImage<ScriptUI.newImage>` readonly               | Loads a new image from resources or disk files into an image object.                              |
+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+




.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      ScriptUI/applicationFonts.rst
      ScriptUI/compatibility.rst
      ScriptUI/coreVersion.rst
      ScriptUI/environment.rst
      ScriptUI/events.rst
      ScriptUI/frameworkName.rst
      ScriptUI/version.rst
      ScriptUI/Alignment.rst
      ScriptUI/FontStyle.rst
      

      
      ScriptUI/getResourceText.rst
      ScriptUI/newImage.rst
      ScriptUI/newFont.rst
      
      
      