RawFormatOpenOptions {#RawFormatOpenOptions}
====================

Description
-----------

Options that can be specified when opening a document in RAW format.

### Static Properties

  ----------------------------------------------------------------------------- ---------------------------------------------------
  [bitsPerChannel\<RawFormatOpenOptions.bitsPerChannel\>]{role="ref"} readonly  The number of bits for each channel. Valid values:
                                                                                8 or 16.

  [byteOrder\<RawFormatOpenOptions.byteOrder\>]{role="ref"} readonly            The order in which bytes will be read. Valid only
                                                                                when \'bits per channel\' = 16.

  [channelNumber\<RawFormatOpenOptions.channelNumber\>]{role="ref"} readonly    The number of channels in the image. Valid only
                                                                                when \'bits per channel\' = 16. Range: 1 to 56.

  [headerSize\<RawFormatOpenOptions.headerSize\>]{role="ref"} readonly          The number of bytes of information that will appear
                                                                                in the file before actual image information begins;
                                                                                that is, the number of zeroes inserted at the
                                                                                beginning of the file as placeholders. Range: 0 to
                                                                                1919999.

  [height\<RawFormatOpenOptions.height\>]{role="ref"} readonly                  The image height (in pixels)

  [interleaveChannels\<RawFormatOpenOptions.interleaveChannels\>]{role="ref"}   If true, color values are stored sequentially.
  readonly                                                                      

  [retainHeader\<RawFormatOpenOptions.retainHeader\>]{role="ref"} readonly      If true, the header is retained when saving.

  [width\<RawFormatOpenOptions.width\>]{role="ref"} readonly                    The image width (in pixels)
  ----------------------------------------------------------------------------- ---------------------------------------------------

::: {.container .hide}
::: {.toctree}
RawFormatOpenOptions/height.rst RawFormatOpenOptions/width.rst
RawFormatOpenOptions/channelNumber.rst
RawFormatOpenOptions/interleaveChannels.rst
RawFormatOpenOptions/bitsPerChannel.rst
RawFormatOpenOptions/byteOrder.rst RawFormatOpenOptions/headerSize.rst
RawFormatOpenOptions/retainHeader.rst
:::
:::
