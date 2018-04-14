String {#String}
======

Description
-----------

A character string. Each character is adressable by index.

### Properties

  --------------------------------------- ---------------------------
  [length\<String.length\>]{role="ref"}   The length of the string.
  readonly                                
  --------------------------------------- ---------------------------

### Constructors

  --------------------------------------- --------------------------------------------
  [String\<String.String\>]{role="ref"}   Returns a string representation of the value
  readonly                                given as an argument.
  --------------------------------------- --------------------------------------------

### Methods

  ------------------------------------------------------------- ------------------------------------------------
  [anchor\<String.anchor\>]{role="ref"} readonly                Returns a string consisting of this string
                                                                enclosed in a \<a\> tag.

  [big\<String.big\>]{role="ref"} readonly                      Returns a string consisting of this string
                                                                enclosed in a \<big\> tag.

  [blink\<String.blink\>]{role="ref"} readonly                  Returns a string consisting of this string
                                                                enclosed in a \<blink\> tag.

  [bold\<String.bold\>]{role="ref"} readonly                    Returns a string consisting of this string
                                                                enclosed in a \<b\> tag.

  [charAt\<String.charAt\>]{role="ref"} readonly                Returns the character at the specified index.

  [charCodeAt\<String.charCodeAt\>]{role="ref"} readonly        Returns the Unicode value of the character at
                                                                the given index.

  [concat\<String.concat\>]{role="ref"} readonly                If necessary, converts the one or more given
                                                                values to strings.

  [fixed\<String.fixed\>]{role="ref"} readonly                  Returns a string consisting of this string
                                                                enclosed in a \<tt\> tag.

  [fontcolor\<String.fontcolor\>]{role="ref"} readonly          Returns a string consisting of this string
                                                                enclosed in a \<font\> tag.

  [fontsize\<String.fontsize\>]{role="ref"} readonly            Returns a string consisting of this string
                                                                enclosed in a \<font\> tag.

  [indexOf\<String.indexOf\>]{role="ref"} readonly              Returns the index within the string of the first
                                                                occurrence of the specified string, starting the
                                                                search at fromIndex if provided.

  [italics\<String.italics\>]{role="ref"} readonly              Returns a string consisting of this string
                                                                enclosed in a \<i\> tag.

  [lastIndexOf\<String.lastIndexOf\>]{role="ref"} readonly      Returns the index within the string of the last
                                                                occurrence of the specified value.

  [link\<String.link\>]{role="ref"} readonly                    Returns a string consisting of this string
                                                                enclosed in a \<a\> tag.

  [localeCompare\<String.localeCompare\>]{role="ref"} readonly  Performs a localized comparison of two strings.

  [match\<String.match\>]{role="ref"} readonly                  Matches a string against a regular expression.

  [replace\<String.replace\>]{role="ref"} readonly              

  [search\<String.search\>]{role="ref"} readonly                

  [slice\<String.slice\>]{role="ref"} readonly                  Extracts a substring of the given string and
                                                                returns it as a new string.

  [small\<String.small\>]{role="ref"} readonly                  Returns a string consisting of this string
                                                                enclosed in a \<small\> tag.

  [split\<String.split\>]{role="ref"} readonly                  Splits a string into a group of substrings,
                                                                places those strings in an array, and returns
                                                                the array.

  [strike\<String.strike\>]{role="ref"} readonly                Returns a string consisting of this string
                                                                enclosed in a \<strike\> tag.

  [sub\<String.sub\>]{role="ref"} readonly                      Returns a string consisting of this string
                                                                enclosed in a \<sub\> tag.

  [substr\<String.substr\>]{role="ref"} readonly                Returns a string containing the characters
                                                                beginning at the specified index, start, through
                                                                the specified number of characters.

  [substring\<String.substring\>]{role="ref"} readonly          Returns a substring of the given string by
                                                                extracting characters from indexA up to but not
                                                                including indexB.

  [sup\<String.sup\>]{role="ref"} readonly                      Returns a string consisting of this string
                                                                enclosed in a \<sup\> tag.

  [toLocaleLowerCase\<String.toLocaleLowerCase\>]{role="ref"}   Returns a new string which contains all the
  readonly                                                      characters of the original string converted to
                                                                lowercase (localized).

  [toLocaleUpperCase\<String.toLocaleUpperCase\>]{role="ref"}   Returns a new string which contains all the
  readonly                                                      characters of the original string converted to
                                                                uppercase (localized).

  [toLowerCase\<String.toLowerCase\>]{role="ref"} readonly      Returns a new string which contains all the
                                                                characters of the original string converted to
                                                                lowercase.

  [toSource\<String.toSource\>]{role="ref"} readonly            Creates a string representation of this object
                                                                that can be fed back to?eval()?to re-create an
                                                                object. Works only with built-in classes.

  [toString\<String.toString\>]{role="ref"} readonly            Returns itself.

  [toUpperCase\<String.toUpperCase\>]{role="ref"} readonly      Returns a new string which contains all the
                                                                characters of the original string converted to
                                                                uppercase.

  [valueOf\<String.valueOf\>]{role="ref"} readonly              Returns itself.
  ------------------------------------------------------------- ------------------------------------------------

### Static Methods

  --------------------------------------------------- ---------------------------------------------
  [fromCharCode\<String.fromCharCode\>]{role="ref"}   Returns a string created by concatenation one
  readonly                                            or more characters specified as ASCII values.
  --------------------------------------------------- ---------------------------------------------

::: {.container .hide}
::: {.toctree}
String/length.rst

String/toString.rst String/toSource.rst String/valueOf.rst
String/charAt.rst String/charCodeAt.rst String/concat.rst
String/indexOf.rst String/lastIndexOf.rst String/slice.rst
String/toLowerCase.rst String/toUpperCase.rst
String/toLocaleLowerCase.rst String/toLocaleUpperCase.rst
String/localeCompare.rst String/match.rst String/replace.rst
String/search.rst String/split.rst String/substr.rst
String/substring.rst String/anchor.rst String/big.rst String/blink.rst
String/bold.rst String/fixed.rst String/fontcolor.rst
String/fontsize.rst String/italics.rst String/link.rst String/small.rst
String/strike.rst String/sub.rst String/sup.rst

String/fromCharCode.rst

String/String.rst
:::
:::
