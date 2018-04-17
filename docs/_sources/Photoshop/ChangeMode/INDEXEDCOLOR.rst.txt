.. _ChangeMode.INDEXEDCOLOR:

================================================
ChangeMode.INDEXEDCOLOR
================================================

   int **INDEXEDCOLOR**


Description
-----------

Indexed color, in which the number of colors in the image is reduced to at most 256, the standard number of colors supported by the GIF and PNG-8 formats and many multimedia applications.

This conversion reduces file size by deleting color information from the image. To convert to indexed color, you must start with an image that is 8 bits per channel and in either Grayscale or RGB mode.