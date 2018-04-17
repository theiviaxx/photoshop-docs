.. _ChangeMode.MULTICHANNEL:

================================================
ChangeMode.MULTICHANNEL
================================================

   int **MULTICHANNEL**


Description
-----------

Image with multiple color channels.

Uses 256 levels of gray in each channel. Useful for specialized printing. Color channels in the original image become spot color channels in the converted image. A CMYK image converted to Multichannel mode creates cyan, magenta, yellow, and black spot channels. An RGB image converted Multichannel mode creates cyan, magenta, and yellow spot channels. The new grayscale information is based on the color values of the pixels in each channel. Multichannel mode images can be saved in Photoshop, Photoshop 2.0, Photoshop Raw, or Photoshop DCS 2.0 format. To export a multichannel image, save it in Photoshop DCS 2.0 format.