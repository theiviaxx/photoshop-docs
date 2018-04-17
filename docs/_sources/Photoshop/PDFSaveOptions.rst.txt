.. _PDFSaveOptions:

================================================
PDFSaveOptions
================================================


Description
-----------

Options for saving a document in PDF format.






Static Properties
^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`PDFCompatibility<PDFSaveOptions.PDFCompatibility>` readonly             | The PDF version to make the document compatible with.                                                                  |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`PDFStandard<PDFSaveOptions.PDFStandard>` readonly                       | The PDF standard to make the document compatible with.                                                                 |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`alphaChannels<PDFSaveOptions.alphaChannels>` readonly                   | If true, the alpha channels are saved.                                                                                 |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`annotations<PDFSaveOptions.annotations>` readonly                       | If true, the annotations are saved.                                                                                    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`colorConversion<PDFSaveOptions.colorConversion>` readonly               | If true, converts the color profile to the destination profile.                                                        |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`convertToEightBit<PDFSaveOptions.convertToEightBit>` readonly           | If true, converts a 16-bit image to 8-bit for better compatibility with other applications.                            |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`description<PDFSaveOptions.description>` readonly                       | Description of the save options in use.                                                                                |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`destinationProfile<PDFSaveOptions.destinationProfile>` readonly         | Describes the final RGB or CMYK output device, such as a monitor or press standard.                                    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`downSample<PDFSaveOptions.downSample>` readonly                         | The downsample method to use.                                                                                          |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`downSampleSize<PDFSaveOptions.downSampleSize>` readonly                 | The size (in pixels per inch) to downsample images to if they exceed the value specified for 'down sample size limit'. |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`downSampleSizeLimit<PDFSaveOptions.downSampleSizeLimit>` readonly       | Limits downsampling or subsampling to images that exceed this value (in pixels per inch).                              |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`downgradeColorProfile<PDFSaveOptions.downgradeColorProfile>` readonly   | DEPRECATED, ( should the embedded color profile be downgraded to version 2 )                                           |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`embedColorProfile<PDFSaveOptions.embedColorProfile>` readonly           | If true, the color profile is embedded in the document.                                                                |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`embedFonts<PDFSaveOptions.embedFonts>` readonly                         | DEPRECATED. ( embed fonts? Only valid if a text layer is included )                                                    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`embedThumbnail<PDFSaveOptions.embedThumbnail>` readonly                 | If true, includes a small preview image in Acrobat.                                                                    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`encoding<PDFSaveOptions.encoding>` readonly                             | The encoding method to use.                                                                                            |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`interpolation<PDFSaveOptions.interpolation>` readonly                   | DEPRECATED. ( use image interpolation? )                                                                               |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`jpegQuality<PDFSaveOptions.jpegQuality>` readonly                       | The quality of the produced image. Valid only for JPEG-encoded PDF documents. Range: 0 to 12.                          |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`layers<PDFSaveOptions.layers>` readonly                                 | If true, the layers are saved.                                                                                         |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`optimizeForWeb<PDFSaveOptions.optimizeForWeb>` readonly                 | If true, improves performance of PDFs on Web servers.                                                                  |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`outputCondition<PDFSaveOptions.outputCondition>` readonly               | An optional comment field for inserting descriptions of the output condition. The text is stored in the PDF/X file.    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`outputConditionID<PDFSaveOptions.outputConditionID>` readonly           | The identifier for the output condition.                                                                               |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`preserveEditing<PDFSaveOptions.preserveEditing>` readonly               | If true, allows users to reopen the PDF in Photoshop with native Photoshop data intact.                                |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`presetFile<PDFSaveOptions.presetFile>` readonly                         | The preset file to use for settings; overrides other settings.                                                         |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`profileInclusionPolicy<PDFSaveOptions.profileInclusionPolicy>` readonly | If true, shows which profiles to include.                                                                              |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`registryName<PDFSaveOptions.registryName>` readonly                     | The URL where the output condition is registered.                                                                      |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`spotColors<PDFSaveOptions.spotColors>` readonly                         | If true, the spot colors are saved.                                                                                    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`tileSize<PDFSaveOptions.tileSize>` readonly                             | The compression option. Valid only when encoding is JPEG2000.                                                          |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`transparency<PDFSaveOptions.transparency>` readonly                     | DEPRECATED.                                                                                                            |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`useOutlines<PDFSaveOptions.useOutlines>` readonly                       | DEPRECATED. ( use outlines for text? Only valid if vector data is included )                                           |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`vectorData<PDFSaveOptions.vectorData>` readonly                         | DEPRECATED. ( include vector data )                                                                                    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| :ref:`view<PDFSaveOptions.view>` readonly                                     | If true, opens the saved PDF in Acrobat.                                                                               |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      PDFSaveOptions/alphaChannels.rst
      PDFSaveOptions/layers.rst
      PDFSaveOptions/annotations.rst
      PDFSaveOptions/spotColors.rst
      PDFSaveOptions/embedColorProfile.rst
      PDFSaveOptions/downgradeColorProfile.rst
      PDFSaveOptions/transparency.rst
      PDFSaveOptions/interpolation.rst
      PDFSaveOptions/vectorData.rst
      PDFSaveOptions/embedFonts.rst
      PDFSaveOptions/useOutlines.rst
      PDFSaveOptions/encoding.rst
      PDFSaveOptions/jpegQuality.rst
      PDFSaveOptions/presetFile.rst
      PDFSaveOptions/PDFStandard.rst
      PDFSaveOptions/PDFCompatibility.rst
      PDFSaveOptions/description.rst
      PDFSaveOptions/preserveEditing.rst
      PDFSaveOptions/embedThumbnail.rst
      PDFSaveOptions/optimizeForWeb.rst
      PDFSaveOptions/view.rst
      PDFSaveOptions/downSample.rst
      PDFSaveOptions/downSampleSize.rst
      PDFSaveOptions/downSampleSizeLimit.rst
      PDFSaveOptions/tileSize.rst
      PDFSaveOptions/convertToEightBit.rst
      PDFSaveOptions/colorConversion.rst
      PDFSaveOptions/destinationProfile.rst
      PDFSaveOptions/profileInclusionPolicy.rst
      PDFSaveOptions/outputCondition.rst
      PDFSaveOptions/outputConditionID.rst
      PDFSaveOptions/registryName.rst
      

      
      
      
      