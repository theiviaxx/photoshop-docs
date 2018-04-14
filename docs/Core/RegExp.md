RegExp {#RegExp}
======

Description
-----------

Wraps a regular expression.

### Static Properties

  --------------------------------------------------- ------------------------------------
  [\$1\<RegExp.\$1\>]{role="ref"} readonly            The matched subexpression \#1.

  [\$2\<RegExp.\$2\>]{role="ref"} readonly            The matched subexpression \#2.

  [\$3\<RegExp.\$3\>]{role="ref"} readonly            The matched subexpression \#3.

  [\$4\<RegExp.\$4\>]{role="ref"} readonly            The matched subexpression \#4.

  [\$5\<RegExp.\$5\>]{role="ref"} readonly            The matched subexpression \#5.

  [\$6\<RegExp.\$6\>]{role="ref"} readonly            The matched subexpression \#6.

  [\$7\<RegExp.\$7\>]{role="ref"} readonly            The matched subexpression \#7.

  [\$8\<RegExp.\$8\>]{role="ref"} readonly            The matched subexpression \#8.

  [\$9\<RegExp.\$9\>]{role="ref"} readonly            The matched subexpression \#9.

  [global\<RegExp.global\>]{role="ref"} readonly      Indicates whether the match is a
                                                      global match.

  [ignoreCase\<RegExp.ignoreCase\>]{role="ref"}       Indicates whether the match is not
  readonly                                            case sensitive.

  [input\<RegExp.input\>]{role="ref"} readonly        The original input string.

  [lastMatch\<RegExp.lastMatch\>]{role="ref"}         The last match.
  readonly                                            

  [lastParen\<RegExp.lastParen\>]{role="ref"}         The value of the last matched
  readonly                                            subexpression.

  [leftContext\<RegExp.leftContext\>]{role="ref"}     The string before the match.
  readonly                                            

  [multiline\<RegExp.multiline\>]{role="ref"}         Indicates whether the match matches
  readonly                                            multiple lines.

  [rightContext\<RegExp.rightContext\>]{role="ref"}   The string after the match.
  readonly                                            
  --------------------------------------------------- ------------------------------------

### Constructors

  --------------------------------------- ----------------------------------------------------
  [RegExp\<RegExp.RegExp\>]{role="ref"}   Creates and returns a new RegExp object set to the
  readonly                                value of the argument converted to a regular
                                          expression.
  --------------------------------------- ----------------------------------------------------

### Methods

  ------------------------------------------- ------------------------------------------------
  [compile\<RegExp.compile\>]{role="ref"}     Compiles a string to a regular expression.
  readonly                                    Returns true if the compilation was successful.

  [exec\<RegExp.exec\>]{role="ref"} readonly  Execute a regular expression.

  [test\<RegExp.test\>]{role="ref"} readonly  Execute a regular expression, and return true if
                                              there is a match.

  [toString\<RegExp.toString\>]{role="ref"}   Converts this RegExp object to a string.
  readonly                                    
  ------------------------------------------- ------------------------------------------------

::: {.container .hide}
::: {.toctree}
RegExp/\$1.rst RegExp/\$2.rst RegExp/\$3.rst RegExp/\$4.rst
RegExp/\$5.rst RegExp/\$6.rst RegExp/\$7.rst RegExp/\$8.rst
RegExp/\$9.rst RegExp/lastMatch.rst RegExp/lastParen.rst
RegExp/leftContext.rst RegExp/rightContext.rst RegExp/global.rst
RegExp/ignoreCase.rst RegExp/multiline.rst RegExp/input.rst

RegExp/toString.rst RegExp/compile.rst RegExp/exec.rst RegExp/test.rst

RegExp/RegExp.rst
:::
:::
