.. _BitmapConversionType:

================================================
BitmapConversionType
================================================


Description
-----------



The quality of an image converted to bitmap mode.




Static Properties
^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`CUSTOMPATTERN<BitmapConversionType.CUSTOMPATTERN>` readonly     | Simulates the effect of printing a grayscale image through a custom halftone screen. This method lets you apply a screen texture, such as a wood grain, to an image. To use this option, you must first define a pattern.                                |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`DIFFUSIONDITHER<BitmapConversionType.DIFFUSIONDITHER>` readonly | Applies a random pattern that is usually less noticeable than pattern dither. The dither effects are diffused across adjacent pixels. If you select this algorithm, specify a dither percentage to control the amount of dithering applied to the image. |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`HALFTHRESHOLD<BitmapConversionType.HALFTHRESHOLD>` readonly     | 50% Threshold.                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`HALFTONESCREEN<BitmapConversionType.HALFTONESCREEN>` readonly   | Lets you convert a grayscale image to simulated halftone dots.                                                                                                                                                                                           |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PATTERNDITHER<BitmapConversionType.PATTERNDITHER>` readonly     | Applies a halftone-like square pattern to determine the value of pixels.                                                                                                                                                                                 |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      BitmapConversionType/HALFTHRESHOLD.rst
      BitmapConversionType/PATTERNDITHER.rst
      BitmapConversionType/DIFFUSIONDITHER.rst
      BitmapConversionType/HALFTONESCREEN.rst
      BitmapConversionType/CUSTOMPATTERN.rst
      

      
      
      
      