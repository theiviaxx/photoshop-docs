.. _ColorReductionType:

================================================
ColorReductionType
================================================


Description
-----------



The color reduction algorithm.




Static Properties
^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`ADAPTIVE<ColorReductionType.ADAPTIVE>` readonly       | Samples color from the spectrum appearing most commonly in the image.                                                                                                                                |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`BLACKWHITE<ColorReductionType.BLACKWHITE>` readonly   | Uses a set palette of colors.                                                                                                                                                                        |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`CUSTOM<ColorReductionType.CUSTOM>` readonly           | Uses a color palette that is created or modified by the user. If you open an existing GIF or PNG-8 file, it will have a custom color palette.                                                        |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`GRAYSCALE<ColorReductionType.GRAYSCALE>` readonly     | Uses a set palette of colors.                                                                                                                                                                        |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`MACINTOSH<ColorReductionType.MACINTOSH>` readonly     | Uses a set palette of colors.                                                                                                                                                                        |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PERCEPTUAL<ColorReductionType.PERCEPTUAL>` readonly   | Gives priority to colors for which the human eye has greater sensitivity.                                                                                                                            |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`RESTRICTIVE<ColorReductionType.RESTRICTIVE>` readonly | Uses the standard 216-color color table common to Windows and Mac OS 8-bit (256-color or web-safe palette); ensures that no browser dither is applied when the image is displayed using 8-bit color. |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`SELECTIVE<ColorReductionType.SELECTIVE>` readonly     | Gives priority to broad areas of color and the preservation of web colors; usually produces images with the greatest color integrity.                                                                |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`WINDOWS<ColorReductionType.WINDOWS>` readonly         | Uses a set palette of colors.                                                                                                                                                                        |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      ColorReductionType/PERCEPTUAL.rst
      ColorReductionType/SELECTIVE.rst
      ColorReductionType/ADAPTIVE.rst
      ColorReductionType/RESTRICTIVE.rst
      ColorReductionType/CUSTOM.rst
      ColorReductionType/BLACKWHITE.rst
      ColorReductionType/GRAYSCALE.rst
      ColorReductionType/MACINTOSH.rst
      ColorReductionType/WINDOWS.rst
      

      
      
      
      