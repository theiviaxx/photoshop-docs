.. _Intent.ABSOLUTECOLORIMETRIC:

================================================
Intent.ABSOLUTECOLORIMETRIC
================================================

   int **ABSOLUTECOLORIMETRIC**


Description
-----------

Aims to maintain color accuracy at the expense of preserving relationships between colors and is suitable for proofing to simulate the output of a particular device. This intent is particularly useful for previewing how paper color affects printed colors.

Leaves colors that fall inside the destination gamut unchanged. Out of gamut colors are clipped. No scaling of colors to destination white point is performed.