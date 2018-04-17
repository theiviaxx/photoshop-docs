.. _BatchOptions:

================================================
BatchOptions
================================================


Description
-----------

Options to specify when running a Batch command.






Static Properties
^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`destination<BatchOptions.destination>` readonly                 | The type of destination for the processed files.                                                                                       |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`destinationFolder<BatchOptions.destinationFolder>` readonly     | The folder location for the processed files. Valid only when 'destination' = folder.                                                   |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`errorFile<BatchOptions.errorFile>` readonly                     | The file in which to log errors encountered. To display errors on the screen and stop batch processing when errors occur, leave blank. |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`fileNaming<BatchOptions.fileNaming>` readonly                   | A list of file naming options. Maximum: 6.                                                                                             |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`macintoshCompatible<BatchOptions.macintoshCompatible>` readonly | If true, the final file names are Macintosh compatible.                                                                                |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`overrideOpen<BatchOptions.overrideOpen>` readonly               | If true, overrides action open commands.                                                                                               |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`overrideSave<BatchOptions.overrideSave>` readonly               | If true, overrides save as action steps with the specified destination.                                                                |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`startingSerial<BatchOptions.startingSerial>` readonly           | The starting serial number to use in naming files.                                                                                     |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`suppressOpen<BatchOptions.suppressOpen>` readonly               | If true, suppresses file open options dialogs.                                                                                         |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`suppressProfile<BatchOptions.suppressProfile>` readonly         | If true, suppresses color profile warnings.                                                                                            |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`unixCompatible<BatchOptions.unixCompatible>` readonly           | If true, the final file names are Unix compatible.                                                                                     |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowsCompatible<BatchOptions.windowsCompatible>` readonly     | If true, the final file names are Windows compatible.                                                                                  |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      BatchOptions/overrideOpen.rst
      BatchOptions/suppressOpen.rst
      BatchOptions/suppressProfile.rst
      BatchOptions/destination.rst
      BatchOptions/destinationFolder.rst
      BatchOptions/overrideSave.rst
      BatchOptions/fileNaming.rst
      BatchOptions/startingSerial.rst
      BatchOptions/windowsCompatible.rst
      BatchOptions/macintoshCompatible.rst
      BatchOptions/unixCompatible.rst
      BatchOptions/errorFile.rst
      

      
      
      
      