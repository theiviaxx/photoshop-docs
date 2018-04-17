.. _Intent:

================================================
Intent
================================================


Description
-----------



The color conversion intent.




Static Properties
^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`ABSOLUTECOLORIMETRIC<Intent.ABSOLUTECOLORIMETRIC>` readonly | Aims to maintain color accuracy at the expense of preserving relationships between colors and is suitable for proofing to simulate the output of a particular device. This intent is particularly useful for previewing how paper color affects printed colors. |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PERCEPTUAL<Intent.PERCEPTUAL>` readonly                     | Gives priority to colors for which the human eye has greater sensitivity.                                                                                                                                                                                       |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`RELATIVECOLORIMETRIC<Intent.RELATIVECOLORIMETRIC>` readonly | Compares the extreme highlight of the source color space to that of the destination color space and shifts all colors accordingly. Out of gamut colors are shifted to the closest reproducible color in the destination color space.                            |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`SATURATION<Intent.SATURATION>` readonly                     | Tries to produce vivid colors in an image at the expense of color accuracy.                                                                                                                                                                                     |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      Intent/PERCEPTUAL.rst
      Intent/SATURATION.rst
      Intent/RELATIVECOLORIMETRIC.rst
      Intent/ABSOLUTECOLORIMETRIC.rst
      

      
      
      
      