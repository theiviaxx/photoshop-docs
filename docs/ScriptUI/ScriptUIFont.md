ScriptUIFont {#ScriptUIFont}
============

Description
-----------

Encapsulates the qualities of a font used to draw text into a control.

Create with the?newFont()?method.Used as a value of?font. Passed as an
argument to?drawString()?and?measureString().

### Properties

  ----------------------------------------------------- --------------------------------------------------
  [family\<ScriptUIFont.family\>]{role="ref"} readonly  The font family name.

  [name\<ScriptUIFont.name\>]{role="ref"} readonly      The complete font name, consisting of the family
                                                        and style, if specified.

  [size\<ScriptUIFont.size\>]{role="ref"} readonly      The font point size.

  [style\<ScriptUIFont.style\>]{role="ref"} readonly    The font style. One of the constants
                                                        in?ScriptUIGraphics.FontStyle.

  [substitute\<ScriptUIFont.substitute\>]{role="ref"}   The name of a substitution font, a fallback font
  readonly                                              to substitute for this font if the requested font
                                                        family or style is not available.
  ----------------------------------------------------- --------------------------------------------------

::: {.container .hide}
::: {.toctree}
ScriptUIFont/family.rst ScriptUIFont/name.rst ScriptUIFont/size.rst
ScriptUIFont/style.rst ScriptUIFont/substitute.rst
:::
:::
