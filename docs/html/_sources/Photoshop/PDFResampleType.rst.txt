.. _PDFResampleType:

================================================
PDFResampleType
================================================


Description
-----------



Downsampling options when saving as PDF.




Static Properties
^^^^^^^^^^^^^^^^^

+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`NONE<PDFResampleType.NONE>` readonly                 | Does not downsample.                                                                                                                                                                                                |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PDFAVERAGE<PDFResampleType.PDFAVERAGE>` readonly     | Averages the pixels in a sample area and replaces the entire area with the average pixel color at the specified resolution.                                                                                         |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PDFBICUBIC<PDFResampleType.PDFBICUBIC>` readonly     | Uses a weighted average to determine pixel color, which usually yields better results than the simple averaging method of downsampling. The slowest but most precise method, resulting in the smoothest gradations. |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PDFSUBSAMPLE<PDFResampleType.PDFSUBSAMPLE>` readonly | Chooses a pixel in the center of the sample area and replaces the entire area with that pixel color; significantly reduces conversion time but results in images that are less smooth and continuous.               |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      PDFResampleType/NONE.rst
      PDFResampleType/PDFAVERAGE.rst
      PDFResampleType/PDFSUBSAMPLE.rst
      PDFResampleType/PDFBICUBIC.rst
      

      
      
      
      