BitmapConversionType.DIFFUSIONDITHER {#BitmapConversionType.DIFFUSIONDITHER}
====================================

> int **DIFFUSIONDITHER**

Description
-----------

Applies a random pattern that is usually less noticeable than pattern
dither. The dither effects are diffused across adjacent pixels. If you
select this algorithm, specify a dither percentage to control the amount
of dithering applied to the image.

May cause detectable seams to appear across slice boundaries. Linking
slices diffuses the dither pattern across all linked slices, and
eliminates the seams.
