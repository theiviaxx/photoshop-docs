.. _GIFSaveOptions:

================================================
GIFSaveOptions
================================================


Description
-----------

Options for saving a document in GIF format.






Static Properties
^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`colors<GIFSaveOptions.colors>` readonly                           | The number of colors in palette. Not valid for all palette types.                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`dither<GIFSaveOptions.dither>` readonly                           | The type of dither.                                                                                                                      |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`ditherAmount<GIFSaveOptions.ditherAmount>` readonly               | The amount of dither. Valid only when 'dither type' is diffusion. Range: 1 to 100.                                                       |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`forced<GIFSaveOptions.forced>` readonly                           | The type of colors to force into the color palette.                                                                                      |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`interlaced<GIFSaveOptions.interlaced>` readonly                   | If true, rows are interlaced.                                                                                                            |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`matte<GIFSaveOptions.matte>` readonly                             | The color to use to fill anti-aliased edges adjacent to transparent areas of the image. Default: white.                                  |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`palette<GIFSaveOptions.palette>` readonly                         | The type of palette to use.                                                                                                              |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preserveExactColors<GIFSaveOptions.preserveExactColors>` readonly | If true, protects colors in the image that contain entries in the color table from being dithered. Valid only when 'dither' = diffusion. |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`transparency<GIFSaveOptions.transparency>` readonly               | If true, preserves transparent ares of the image during GIF conversion.                                                                  |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      GIFSaveOptions/colors.rst
      GIFSaveOptions/dither.rst
      GIFSaveOptions/ditherAmount.rst
      GIFSaveOptions/forced.rst
      GIFSaveOptions/interlaced.rst
      GIFSaveOptions/matte.rst
      GIFSaveOptions/palette.rst
      GIFSaveOptions/preserveExactColors.rst
      GIFSaveOptions/transparency.rst
      

      
      
      
      