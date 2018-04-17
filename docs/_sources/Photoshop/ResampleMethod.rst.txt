.. _ResampleMethod:

================================================
ResampleMethod
================================================


Description
-----------



The method to use to resample the image.




Static Properties
^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`AUTOMATIC<ResampleMethod.AUTOMATIC>` readonly               |                                                                                                                                                           |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`BICUBIC<ResampleMethod.BICUBIC>` readonly                   | Uses a weighted average to determine pixel color, which usually yields better results than the simple averageing method of downsampling.                  |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`BICUBICAUTOMATIC<ResampleMethod.BICUBICAUTOMATIC>` readonly |                                                                                                                                                           |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`BICUBICSHARPER<ResampleMethod.BICUBICSHARPER>` readonly     | A good method for reducing the size of an image based on Bicubic interpolation with enhanced sharpening. Maintains the detail in a resampled image.       |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`BICUBICSMOOTHER<ResampleMethod.BICUBICSMOOTHER>` readonly   | A good method for enlarging images based on Bicubic interpolation but designed to produce smoother results.                                               |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`BILINEAR<ResampleMethod.BILINEAR>` readonly                 | Averages the pixels in a sample area and replaces the entire area with the average pixel color at the specified resolution. Same as average downsampling. |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`NEARESTNEIGHBOR<ResampleMethod.NEARESTNEIGHBOR>` readonly   | Chooses a pixel in the center of the sample area and replaces the entire area with that pixel color. Same as subsampling.                                 |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`NONE<ResampleMethod.NONE>` readonly                         | Does not resample.                                                                                                                                        |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PRESERVEDETAILS<ResampleMethod.PRESERVEDETAILS>` readonly   |                                                                                                                                                           |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      ResampleMethod/NONE.rst
      ResampleMethod/NEARESTNEIGHBOR.rst
      ResampleMethod/BILINEAR.rst
      ResampleMethod/BICUBIC.rst
      ResampleMethod/BICUBICSHARPER.rst
      ResampleMethod/BICUBICSMOOTHER.rst
      ResampleMethod/BICUBICAUTOMATIC.rst
      ResampleMethod/AUTOMATIC.rst
      ResampleMethod/PRESERVEDETAILS.rst
      

      
      
      
      