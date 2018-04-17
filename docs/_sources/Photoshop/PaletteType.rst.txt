.. _PaletteType:

================================================
PaletteType
================================================


Description
-----------



The palette type for converting an image to indexed color.




Static Properties
^^^^^^^^^^^^^^^^^

+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`EXACT<PaletteType.EXACT>` readonly                       | The palette uses the exact colors appearing in the RGB image; available only if the image uses 256 or fewer colors.                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`LOCALADAPTIVE<PaletteType.LOCALADAPTIVE>` readonly       | Creates a palette by sampling the colors from the spectrum appearing most commonly in the image.                                                             |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`LOCALPERCEPTUAL<PaletteType.LOCALPERCEPTUAL>` readonly   | Creates a custom palette by giving priority to colors for in the image which the human eye has greater sensitivity.                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`LOCALSELECTIVE<PaletteType.LOCALSELECTIVE>` readonly     | Creates a color table similar to the Perceptual color table, but favoring broad areas of color in the image and the preservation of web colors.              |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`MACOSPALETTE<PaletteType.MACOSPALETTE>` readonly         | The Mac OS default 8-bit palette, whch is based on a uniform sampling of RGB colors.                                                                         |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`MASTERADAPTIVE<PaletteType.MASTERADAPTIVE>` readonly     | Creates a palette by sampling the colors from the spectrum appearing most commonly in a group of open images that share the same color palette.              |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`MASTERPERCEPTUAL<PaletteType.MASTERPERCEPTUAL>` readonly | Creates a custom palette by giving priority to colors in a group of open images with the same color palette for which the human eye has greater sensitivity. |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`MASTERSELECTIVE<PaletteType.MASTERSELECTIVE>` readonly   | Creates a color table similar to the Master Perceptual color table, but favoring broad areas of color and the preservation of web colors.                    |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PREVIOUSPALETTE<PaletteType.PREVIOUSPALETTE>` readonly   | Uses the custom palette from the previous conversion, making it easy to convert several images with the same custom palette.                                 |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`UNIFORM<PaletteType.UNIFORM>` readonly                   | Creates a palette by uniformly sampling colors from the RGB color cube.                                                                                      |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`WEBPALETTE<PaletteType.WEBPALETTE>` readonly             | The 216-color palette that web browsers, regardless of platform, use to display images on a monitor limited to 256 colors.                                   |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`WINDOWSPALETTE<PaletteType.WINDOWSPALETTE>` readonly     | The Windows system's default 8-bit palette, whch is based on a uniform sampling of RGB colors.                                                               |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      PaletteType/EXACT.rst
      PaletteType/MACOSPALETTE.rst
      PaletteType/WINDOWSPALETTE.rst
      PaletteType/WEBPALETTE.rst
      PaletteType/UNIFORM.rst
      PaletteType/LOCALPERCEPTUAL.rst
      PaletteType/LOCALSELECTIVE.rst
      PaletteType/LOCALADAPTIVE.rst
      PaletteType/MASTERPERCEPTUAL.rst
      PaletteType/MASTERSELECTIVE.rst
      PaletteType/MASTERADAPTIVE.rst
      PaletteType/PREVIOUSPALETTE.rst
      

      
      
      
      