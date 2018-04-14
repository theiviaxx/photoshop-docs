PDFResampleType {#PDFResampleType}
===============

Description
-----------

Downsampling options when saving as PDF.

### Static Properties

  ------------------------------------------------------------ -------------------------------------------------------
  [NONE\<PDFResampleType.NONE\>]{role="ref"} readonly          Does not downsample.

  [PDFAVERAGE\<PDFResampleType.PDFAVERAGE\>]{role="ref"}       Averages the pixels in a sample area and replaces the
  readonly                                                     entire area with the average pixel color at the
                                                               specified resolution.

  [PDFBICUBIC\<PDFResampleType.PDFBICUBIC\>]{role="ref"}       Uses a weighted average to determine pixel color, which
  readonly                                                     usually yields better results than the simple averaging
                                                               method of downsampling. The slowest but most precise
                                                               method, resulting in the smoothest gradations.

  [PDFSUBSAMPLE\<PDFResampleType.PDFSUBSAMPLE\>]{role="ref"}   Chooses a pixel in the center of the sample area and
  readonly                                                     replaces the entire area with that pixel color;
                                                               significantly reduces conversion time but results in
                                                               images that are less smooth and continuous.
  ------------------------------------------------------------ -------------------------------------------------------

::: {.container .hide}
::: {.toctree}
PDFResampleType/NONE.rst PDFResampleType/PDFAVERAGE.rst
PDFResampleType/PDFSUBSAMPLE.rst PDFResampleType/PDFBICUBIC.rst
:::
:::
