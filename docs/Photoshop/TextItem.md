TextItem {#TextItem}
========

Description
-----------

The text object contained in an art layer.

### Properties

  ----------------------------------------------------------------------------- ----------------------------------------------------
  [alternateLigatures\<TextItem.alternateLigatures\>]{role="ref"} readonly      If true, alternate ligatures are used.

  [antiAliasMethod\<TextItem.antiAliasMethod\>]{role="ref"} readonly            The method of anti-aliasing to use.

  [autoKerning\<TextItem.autoKerning\>]{role="ref"} readonly                    Options for auto kerning.

  [autoLeadingAmount\<TextItem.autoLeadingAmount\>]{role="ref"} readonly        The percentage to use for auto leading. Range: 0.01
                                                                                to 5000.00.

  [baselineShift\<TextItem.baselineShift\>]{role="ref"} readonly                The amount of baseline offset of text.

  [capitalization\<TextItem.capitalization\>]{role="ref"} readonly              The case of the text.

  [color\<TextItem.color\>]{role="ref"} readonly                                The text color.

  [contents\<TextItem.contents\>]{role="ref"} readonly                          The actual text in the layer.

  [desiredGlyphScaling\<TextItem.desiredGlyphScaling\>]{role="ref"} readonly    The desired amount (as a percentage) to scale the
                                                                                horizontal size of the text letters. Range: 50 -
                                                                                200; at 100, the width of characters is not scaled.
                                                                                Valid only for justified text.

  [desiredLetterScaling\<TextItem.desiredLetterScaling\>]{role="ref"} readonly  The amount of space (as a percentage) between
                                                                                letters. Range: 100 - 500; at 0, no space is added
                                                                                between letters. Valid only for justified text.

  [desiredWordScaling\<TextItem.desiredWordScaling\>]{role="ref"} readonly      The amount (as a percentage) of space between words.
                                                                                Range: 0 -1000; at 100, no additional space is added
                                                                                between words. Valid only for justified text.

  [direction\<TextItem.direction\>]{role="ref"} readonly                        The text orientation.

  [fauxBold\<TextItem.fauxBold\>]{role="ref"} readonly                          If true, faux bold is used.

  [fauxItalic\<TextItem.fauxItalic\>]{role="ref"} readonly                      If true, faux italic is used.

  [firstLineIndent\<TextItem.firstLineIndent\>]{role="ref"} readonly            The amount to indent the first line of paragraphs.
                                                                                Range: -1296 to 1296.

  [font\<TextItem.font\>]{role="ref"} readonly                                  The text face of the character.

  [hangingPuntuation\<TextItem.hangingPuntuation\>]{role="ref"} readonly        If true, uses Roman hanging punctuation.

  [height\<TextItem.height\>]{role="ref"} readonly                              The height of the bounding box for paragraph text.

  [horizontalScale\<TextItem.horizontalScale\>]{role="ref"} readonly            Character scaling (horizontal) in proportion to
                                                                                horizontal scale. Range: 0 - 1000 as a percentage.

  [hyphenLimit\<TextItem.hyphenLimit\>]{role="ref"} readonly                    The maximum number of consecutive lines that can end
                                                                                with a hyphenated word.

  [hyphenateAfterFirst\<TextItem.hyphenateAfterFirst\>]{role="ref"} readonly    The number of letters after which hyphenation in
                                                                                word wrap is allowed. Range: 1 to 15.

  [hyphenateBeforeLast\<TextItem.hyphenateBeforeLast\>]{role="ref"} readonly    The number of letters before which hyphenation in
                                                                                word wrap is allowed. Range: 1 to 15.

  [hyphenateCapitalWords\<TextItem.hyphenateCapitalWords\>]{role="ref"}         If true, capitalized words can be hyphenated.
  readonly                                                                      

  [hyphenateWordsLongerThan\<TextItem.hyphenateWordsLongerThan\>]{role="ref"}   The minimum number of letters a word must have in
  readonly                                                                      order for hyphenation in word wrap to be allowed.
                                                                                Range: 2 to 25.

  [hyphenation\<TextItem.hyphenation\>]{role="ref"} readonly                    If true, hyphenation is used.

  [hyphenationZone\<TextItem.hyphenationZone\>]{role="ref"} readonly            The distance at the end of a line that will cause a
                                                                                word to break in unjustified type. Range: 0 - 720
                                                                                picas.

  [justification\<TextItem.justification\>]{role="ref"} readonly                The paragraph justification.

  [kind\<TextItem.kind\>]{role="ref"} readonly                                  The type of text.

  [language\<TextItem.language\>]{role="ref"} readonly                          The language.

  [leading\<TextItem.leading\>]{role="ref"} readonly                            The leading amount.

  [leftIndent\<TextItem.leftIndent\>]{role="ref"} readonly                      The amount to indent text from the left. Range:
                                                                                -1296 to 1296.

  [ligatures\<TextItem.ligatures\>]{role="ref"} readonly                        If true, ligatures are used.

  [maximumGlyphScaling\<TextItem.maximumGlyphScaling\>]{role="ref"} readonly    The maximum amount (as a percentage) to scale the
                                                                                horizontal size of the text letters. Range: 50 -
                                                                                200; at 100, the width of characters is not scaled.
                                                                                Valid only for justified text.

  [maximumLetterScaling\<TextItem.maximumLetterScaling\>]{role="ref"} readonly  The maximum amount (as a percentage) of space
                                                                                between letters. Range: 100 - 500; at 0, no space is
                                                                                added between letters. Valid only for justified
                                                                                text.

  [maximumWordScaling\<TextItem.maximumWordScaling\>]{role="ref"} readonly      The maximum amount (as a percentage) of space
                                                                                between words (0 -1000; at 100, no additional space
                                                                                is added between words). Valid only for justified
                                                                                text.

  [minimumGlyphScaling\<TextItem.minimumGlyphScaling\>]{role="ref"} readonly    The minimum amount (as a percentage) to scale the
                                                                                horizontal size of the text letters. Range: 50 -
                                                                                200; at 100, the width of characters is not scaled.
                                                                                Valid only for justified text.

  [minimumLetterScaling\<TextItem.minimumLetterScaling\>]{role="ref"} readonly  The minimum amount of space (as a percentage)
                                                                                between letters. Range: 100 to 500; at 0, no space
                                                                                is added between letters. Valid only for justified
                                                                                text.

  [minimumWordScaling\<TextItem.minimumWordScaling\>]{role="ref"} readonly      The minimum amount (as a percentage) of space
                                                                                between words. Range: 0 -1000; at 100, no additional
                                                                                space is added between words. Valid only for
                                                                                justified text.

  [noBreak\<TextItem.noBreak\>]{role="ref"} readonly                            If true, words are not allowed to break at the end
                                                                                of a line. When enacted on large amounts of
                                                                                consecutive characters, can prevent word wrap and
                                                                                thus may prevent some text from appearing on the
                                                                                screen.

  [oldStyle\<TextItem.oldStyle\>]{role="ref"} readonly                          If true, old style is used.

  [parent\<TextItem.parent\>]{role="ref"} readonly                              The object\'s container.

  [position\<TextItem.position\>]{role="ref"} readonly                          The position of the origin for the text. The array
                                                                                must contain two values. Setting this property is
                                                                                basically equivalent to clicking the text tool at a
                                                                                point in the document to create the point of origin
                                                                                for text.

  [rightIndent\<TextItem.rightIndent\>]{role="ref"} readonly                    The amount to indent text from the right. Range:
                                                                                -1296 to 1296.

  [size\<TextItem.size\>]{role="ref"} readonly                                  The font size in points.

  [spaceAfter\<TextItem.spaceAfter\>]{role="ref"} readonly                      The amount of space after each paragraph. Range:
                                                                                -1296 to 1296.

  [spaceBefore\<TextItem.spaceBefore\>]{role="ref"} readonly                    The amount of space before each paragraph. Range:
                                                                                -1296 to 1296.

  [strikeThru\<TextItem.strikeThru\>]{role="ref"} readonly                      The strike through option to use.

  [textComposer\<TextItem.textComposer\>]{role="ref"} readonly                  The text composing engine to use.

  [tracking\<TextItem.tracking\>]{role="ref"} readonly                          The amount of uniform spacing between multiple
                                                                                characters. Range: -1000 to 10000.

  [typename\<TextItem.typename\>]{role="ref"} readonly                          The class name of the object.

  [underline\<TextItem.underline\>]{role="ref"} readonly                        Options for underlining the text.

  [useAutoLeading\<TextItem.useAutoLeading\>]{role="ref"} readonly              If true, uses the font\'s built-in leading
                                                                                information.

  [verticalScale\<TextItem.verticalScale\>]{role="ref"} readonly                Character scaling (vertical) in proportion to
                                                                                horizontal scale. Range: 0 - 1000 as a percentage.

  [warpBend\<TextItem.warpBend\>]{role="ref"} readonly                          The warp bend percentage. Range: -100 to 100.

  [warpDirection\<TextItem.warpDirection\>]{role="ref"} readonly                The warp direction.

  [warpHorizontalDistortion\<TextItem.warpHorizontalDistortion\>]{role="ref"}   The warp horizontal distortion percentage. Range:
  readonly                                                                      -100 to 100.

  [warpStyle\<TextItem.warpStyle\>]{role="ref"} readonly                        The style of warp.

  [warpVerticalDistortion\<TextItem.warpVerticalDistortion\>]{role="ref"}       The warp vertical distortion percentage. Range: -100
  readonly                                                                      to 100.

  [width\<TextItem.width\>]{role="ref"} readonly                                The width of the bounding box for paragraph text.
  ----------------------------------------------------------------------------- ----------------------------------------------------

### Methods

  --------------------------------------------------------- ----------------------------------------------
  [convertToShape\<TextItem.convertToShape\>]{role="ref"}   Converts the text object and its containing
  readonly                                                  layer to a fill layer with the text changed to
                                                            a clipping path.

  [createPath\<TextItem.createPath\>]{role="ref"} readonly  Creates a clipping path from the outlines of
                                                            the actual text items (such as letters or
                                                            words).
  --------------------------------------------------------- ----------------------------------------------

::: {.container .hide}
::: {.toctree}
TextItem/parent.rst TextItem/typename.rst TextItem/antiAliasMethod.rst
TextItem/autoKerning.rst TextItem/color.rst TextItem/useAutoLeading.rst
TextItem/tracking.rst TextItem/verticalScale.rst
TextItem/horizontalScale.rst TextItem/baselineShift.rst
TextItem/contents.rst TextItem/font.rst TextItem/leading.rst
TextItem/ligatures.rst TextItem/alternateLigatures.rst
TextItem/oldStyle.rst TextItem/position.rst TextItem/direction.rst
TextItem/size.rst TextItem/fauxBold.rst TextItem/fauxItalic.rst
TextItem/capitalization.rst TextItem/strikeThru.rst
TextItem/underline.rst TextItem/language.rst TextItem/noBreak.rst
TextItem/kind.rst TextItem/justification.rst TextItem/leftIndent.rst
TextItem/firstLineIndent.rst TextItem/rightIndent.rst
TextItem/spaceBefore.rst TextItem/spaceAfter.rst
TextItem/hangingPuntuation.rst TextItem/textComposer.rst
TextItem/hyphenation.rst TextItem/minimumGlyphScaling.rst
TextItem/desiredGlyphScaling.rst TextItem/maximumGlyphScaling.rst
TextItem/minimumLetterScaling.rst TextItem/desiredLetterScaling.rst
TextItem/maximumLetterScaling.rst TextItem/minimumWordScaling.rst
TextItem/desiredWordScaling.rst TextItem/maximumWordScaling.rst
TextItem/autoLeadingAmount.rst TextItem/hyphenateWordsLongerThan.rst
TextItem/hyphenateAfterFirst.rst TextItem/hyphenateBeforeLast.rst
TextItem/hyphenLimit.rst TextItem/hyphenationZone.rst
TextItem/hyphenateCapitalWords.rst TextItem/width.rst
TextItem/height.rst TextItem/warpStyle.rst TextItem/warpDirection.rst
TextItem/warpBend.rst TextItem/warpHorizontalDistortion.rst
TextItem/warpVerticalDistortion.rst

TextItem/createPath.rst TextItem/convertToShape.rst
:::
:::
