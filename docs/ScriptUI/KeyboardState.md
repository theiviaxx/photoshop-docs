KeyboardState {#KeyboardState}
=============

Description
-----------

Reports the active state of the keyboard.

Access through the?ScriptUI.environment.keyboardState?property. Query
the properties of this object at any time to determine the current key
that is down and any modifiers that are pressed.

### Properties

  -------------------------------------------------- ----------------------------------------------
  [altKey\<KeyboardState.altKey\>]{role="ref"}       True if the Alt or Option key is pressed.
  readonly                                           

  [ctrlKey\<KeyboardState.ctrlKey\>]{role="ref"}     True if the Ctrl key is pressed.
  readonly                                           

  [keyName\<KeyboardState.keyName\>]{role="ref"}     A string containing the name of the currently
  readonly                                           pressed key, such as \"a\", or an empty
                                                     string.

  [metaKey\<KeyboardState.metaKey\>]{role="ref"}     True if the Cmd key (in Mac OS) or Windows key
  readonly                                           (in Windows) is pressed.

  [shiftKey\<KeyboardState.shiftKey\>]{role="ref"}   True if the Shift key is pressed.
  readonly                                           
  -------------------------------------------------- ----------------------------------------------

::: {.container .hide}
::: {.toctree}
KeyboardState/keyName.rst KeyboardState/shiftKey.rst
KeyboardState/ctrlKey.rst KeyboardState/altKey.rst
KeyboardState/metaKey.rst
:::
:::
