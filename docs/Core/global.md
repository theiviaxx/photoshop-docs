global
======

Description
-----------

The global methods and properties for ExtendScript.

### Properties

  --------------------------------------------- ---------------------------------------------------
  [Infinity\<global.Infinity\>]{role="ref"}     The Infinity global property is a predefined
  readonly                                      variable with the value for infinity.

  [NaN\<global.NaN\>]{role="ref"} readonly      The NaN global property is a predefined variable
                                                with the value NaN (Not-a-Number), as specified by
                                                the IEEE-754 standard.

  [undefined\<global.undefined\>]{role="ref"}   This global property is a predefined variable with
  readonly                                      the value for an undefined value.
  --------------------------------------------- ---------------------------------------------------

### Methods

  ----------------------------------------------------------------------- ----------------------------------------
  [alert\<global.alert\>]{role="ref"} readonly                            Displays an alert box

  [confirm\<global.confirm\>]{role="ref"} readonly                        Displays an alert box with Yes and No
                                                                          buttons; returns true for Yes

  [decodeURI\<global.decodeURI\>]{role="ref"} readonly                    Decodes a string created
                                                                          with?encodeURI().

  [decodeURIComponent\<global.decodeURIComponent\>]{role="ref"} readonly  Decodes a string created
                                                                          with?encodeURIComponent().

  [encodeURI\<global.encodeURI\>]{role="ref"} readonly                    Encodes a string after RFC2396.

  [encodeURIComponent\<global.encodeURIComponent\>]{role="ref"} readonly  Encodes a string after RFC2396.

  [escape\<global.escape\>]{role="ref"} readonly                          Creates a URL-encoded string from
                                                                          aString.

  [eval\<global.eval\>]{role="ref"} readonly                              Evaluates its argument as a JavaScript
                                                                          script, and returns the result of
                                                                          evaluation.

  [isFinite\<global.isFinite\>]{role="ref"} readonly                      Evaluates an expression and reports
                                                                          whether the result is a finite number.

  [isNaN\<global.isNaN\>]{role="ref"} readonly                            Evaluates an expression and reports
                                                                          whether the result is \"Not-a-Number\"
                                                                          (NaN).

  [isXMLName\<global.isXMLName\>]{role="ref"} readonly                    Returns true if the supplied string is a
                                                                          valid XML name.

  [localize\<global.localize\>]{role="ref"} readonly                      Localizes a ZString-encoded string and
                                                                          merges additional arguments into the
                                                                          string.

  [parseFloat\<global.parseFloat\>]{role="ref"} readonly                  Extracts a floating-point number from a
                                                                          string.

  [parseInt\<global.parseInt\>]{role="ref"} readonly                      Extracts an integer from a string.

  [prompt\<global.prompt\>]{role="ref"} readonly                          Displays a dialog allowing the user to
                                                                          enter text

  [setDefaultXMLNamespace\<global.setDefaultXMLNamespace\>]{role="ref"}   Defines the default XML namespace.
  readonly                                                                

  [unescape\<global.unescape\>]{role="ref"} readonly                      Translates URL-encoded string into a
                                                                          regular string, and returns that string.

  [uneval\<global.uneval\>]{role="ref"} readonly                          Creates a source code representation of
                                                                          the supplied argument, and returns it as
                                                                          a string.
  ----------------------------------------------------------------------- ----------------------------------------

::: {.container .hide}
::: {.toctree}
global/NaN.rst global/Infinity.rst global/undefined.rst

global/encodeURI.rst global/encodeURIComponent.rst global/decodeURI.rst
global/decodeURIComponent.rst global/escape.rst global/eval.rst
global/uneval.rst global/isFinite.rst global/isNaN.rst
global/parseInt.rst global/parseFloat.rst global/unescape.rst
global/localize.rst global/isXMLName.rst
global/setDefaultXMLNamespace.rst global/alert.rst global/confirm.rst
global/prompt.rst
:::
:::
