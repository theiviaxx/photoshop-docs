PresentationOptions {#PresentationOptions}
===================

Description
-----------

Options for the PDF presentation command.

### Static Properties

  ---------------------------------------------------------------------- --------------------------------------------
  [PDFFileOptions\<PresentationOptions.PDFFileOptions\>]{role="ref"}     Options for creating the PDF file.
  readonly                                                               

  [autoAdvance\<PresentationOptions.autoAdvance\>]{role="ref"} readonly  If true, the presentation auto advances.

  [includeFilename\<PresentationOptions.includeFilename\>]{role="ref"}   If true, includes the file name for the
  readonly                                                               image.

  [interval\<PresentationOptions.interval\>]{role="ref"} readonly        The amount of time (in seconds) before auto
                                                                         advancing the view. Valid only when \'auto
                                                                         advance\' is true. Range: 1 to 60.

  [loop\<PresentationOptions.loop\>]{role="ref"} readonly                If true, the presentation loops after the
                                                                         last page.

  [magnification\<PresentationOptions.magnification\>]{role="ref"}       The magnification type when viewing the
  readonly                                                               image.

  [presentation\<PresentationOptions.presentation\>]{role="ref"}         If true, the file type is presentation. If
  readonly                                                               false, the file type is Multi-Page document.

  [transition\<PresentationOptions.transition\>]{role="ref"} readonly    The image transition type.
  ---------------------------------------------------------------------- --------------------------------------------

::: {.container .hide}
::: {.toctree}
PresentationOptions/presentation.rst PresentationOptions/autoAdvance.rst
PresentationOptions/interval.rst PresentationOptions/loop.rst
PresentationOptions/transition.rst PresentationOptions/magnification.rst
PresentationOptions/includeFilename.rst
PresentationOptions/PDFFileOptions.rst
:::
:::
