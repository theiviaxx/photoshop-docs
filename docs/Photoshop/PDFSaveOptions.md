PDFSaveOptions {#PDFSaveOptions}
==============

Description
-----------

Options for saving a document in PDF format.

### Static Properties

  ------------------------------------------------------------------------------- ------------------------------------------
  [PDFCompatibility\<PDFSaveOptions.PDFCompatibility\>]{role="ref"} readonly      The PDF version to make the document
                                                                                  compatible with.

  [PDFStandard\<PDFSaveOptions.PDFStandard\>]{role="ref"} readonly                The PDF standard to make the document
                                                                                  compatible with.

  [alphaChannels\<PDFSaveOptions.alphaChannels\>]{role="ref"} readonly            If true, the alpha channels are saved.

  [annotations\<PDFSaveOptions.annotations\>]{role="ref"} readonly                If true, the annotations are saved.

  [colorConversion\<PDFSaveOptions.colorConversion\>]{role="ref"} readonly        If true, converts the color profile to the
                                                                                  destination profile.

  [convertToEightBit\<PDFSaveOptions.convertToEightBit\>]{role="ref"} readonly    If true, converts a 16-bit image to 8-bit
                                                                                  for better compatibility with other
                                                                                  applications.

  [description\<PDFSaveOptions.description\>]{role="ref"} readonly                Description of the save options in use.

  [destinationProfile\<PDFSaveOptions.destinationProfile\>]{role="ref"} readonly  Describes the final RGB or CMYK output
                                                                                  device, such as a monitor or press
                                                                                  standard.

  [downSample\<PDFSaveOptions.downSample\>]{role="ref"} readonly                  The downsample method to use.

  [downSampleSize\<PDFSaveOptions.downSampleSize\>]{role="ref"} readonly          The size (in pixels per inch) to
                                                                                  downsample images to if they exceed the
                                                                                  value specified for \'down sample size
                                                                                  limit\'.

  [downSampleSizeLimit\<PDFSaveOptions.downSampleSizeLimit\>]{role="ref"}         Limits downsampling or subsampling to
  readonly                                                                        images that exceed this value (in pixels
                                                                                  per inch).

  [downgradeColorProfile\<PDFSaveOptions.downgradeColorProfile\>]{role="ref"}     DEPRECATED, ( should the embedded color
  readonly                                                                        profile be downgraded to version 2 )

  [embedColorProfile\<PDFSaveOptions.embedColorProfile\>]{role="ref"} readonly    If true, the color profile is embedded in
                                                                                  the document.

  [embedFonts\<PDFSaveOptions.embedFonts\>]{role="ref"} readonly                  DEPRECATED. ( embed fonts? Only valid if a
                                                                                  text layer is included )

  [embedThumbnail\<PDFSaveOptions.embedThumbnail\>]{role="ref"} readonly          If true, includes a small preview image in
                                                                                  Acrobat.

  [encoding\<PDFSaveOptions.encoding\>]{role="ref"} readonly                      The encoding method to use.

  [interpolation\<PDFSaveOptions.interpolation\>]{role="ref"} readonly            DEPRECATED. ( use image interpolation? )

  [jpegQuality\<PDFSaveOptions.jpegQuality\>]{role="ref"} readonly                The quality of the produced image. Valid
                                                                                  only for JPEG-encoded PDF documents.
                                                                                  Range: 0 to 12.

  [layers\<PDFSaveOptions.layers\>]{role="ref"} readonly                          If true, the layers are saved.

  [optimizeForWeb\<PDFSaveOptions.optimizeForWeb\>]{role="ref"} readonly          If true, improves performance of PDFs on
                                                                                  Web servers.

  [outputCondition\<PDFSaveOptions.outputCondition\>]{role="ref"} readonly        An optional comment field for inserting
                                                                                  descriptions of the output condition. The
                                                                                  text is stored in the PDF/X file.

  [outputConditionID\<PDFSaveOptions.outputConditionID\>]{role="ref"} readonly    The identifier for the output condition.

  [preserveEditing\<PDFSaveOptions.preserveEditing\>]{role="ref"} readonly        If true, allows users to reopen the PDF in
                                                                                  Photoshop with native Photoshop data
                                                                                  intact.

  [presetFile\<PDFSaveOptions.presetFile\>]{role="ref"} readonly                  The preset file to use for settings;
                                                                                  overrides other settings.

  [profileInclusionPolicy\<PDFSaveOptions.profileInclusionPolicy\>]{role="ref"}   If true, shows which profiles to include.
  readonly                                                                        

  [registryName\<PDFSaveOptions.registryName\>]{role="ref"} readonly              The URL where the output condition is
                                                                                  registered.

  [spotColors\<PDFSaveOptions.spotColors\>]{role="ref"} readonly                  If true, the spot colors are saved.

  [tileSize\<PDFSaveOptions.tileSize\>]{role="ref"} readonly                      The compression option. Valid only when
                                                                                  encoding is JPEG2000.

  [transparency\<PDFSaveOptions.transparency\>]{role="ref"} readonly              DEPRECATED.

  [useOutlines\<PDFSaveOptions.useOutlines\>]{role="ref"} readonly                DEPRECATED. ( use outlines for text? Only
                                                                                  valid if vector data is included )

  [vectorData\<PDFSaveOptions.vectorData\>]{role="ref"} readonly                  DEPRECATED. ( include vector data )

  [view\<PDFSaveOptions.view\>]{role="ref"} readonly                              If true, opens the saved PDF in Acrobat.
  ------------------------------------------------------------------------------- ------------------------------------------

::: {.container .hide}
::: {.toctree}
PDFSaveOptions/alphaChannels.rst PDFSaveOptions/layers.rst
PDFSaveOptions/annotations.rst PDFSaveOptions/spotColors.rst
PDFSaveOptions/embedColorProfile.rst
PDFSaveOptions/downgradeColorProfile.rst PDFSaveOptions/transparency.rst
PDFSaveOptions/interpolation.rst PDFSaveOptions/vectorData.rst
PDFSaveOptions/embedFonts.rst PDFSaveOptions/useOutlines.rst
PDFSaveOptions/encoding.rst PDFSaveOptions/jpegQuality.rst
PDFSaveOptions/presetFile.rst PDFSaveOptions/PDFStandard.rst
PDFSaveOptions/PDFCompatibility.rst PDFSaveOptions/description.rst
PDFSaveOptions/preserveEditing.rst PDFSaveOptions/embedThumbnail.rst
PDFSaveOptions/optimizeForWeb.rst PDFSaveOptions/view.rst
PDFSaveOptions/downSample.rst PDFSaveOptions/downSampleSize.rst
PDFSaveOptions/downSampleSizeLimit.rst PDFSaveOptions/tileSize.rst
PDFSaveOptions/convertToEightBit.rst PDFSaveOptions/colorConversion.rst
PDFSaveOptions/destinationProfile.rst
PDFSaveOptions/profileInclusionPolicy.rst
PDFSaveOptions/outputCondition.rst PDFSaveOptions/outputConditionID.rst
PDFSaveOptions/registryName.rst
:::
:::
