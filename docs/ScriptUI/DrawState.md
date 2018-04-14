DrawState {#DrawState}
=========

Description
-----------

Describes an input state at the time of the triggering
?ScriptUIGraphics.onDraw()?event.

Contains properties that report whether the current control has the
input focus, and the particular mouse button and keypress state. Passed
in as argument to?ScriptUIGraphics.onDraw().

### Properties

  -------------------------------------------------------------------- ---------------------------------
  [altKeyPressed\<DrawState.altKeyPressed\>]{role="ref"} readonly      True if the Alt key is being
                                                                       pressed (in Windows only).

  [capsLockKeyPressed\<DrawState.capsLockKeyPressed\>]{role="ref"}     True if the Caps Lock key is
  readonly                                                             being pressed.

  [cmdKeyPressed\<DrawState.cmdKeyPressed\>]{role="ref"} readonly      True if the Command key is being
                                                                       pressed (in Mac OS only).

  [ctrlKeyPressed\<DrawState.ctrlKeyPressed\>]{role="ref"} readonly    True if the Ctrl key is being
                                                                       pressed.

  [hasFocus\<DrawState.hasFocus\>]{role="ref"} readonly                True if the element has the input
                                                                       focus.

  [leftButtonPressed\<DrawState.leftButtonPressed\>]{role="ref"}       True if the left mouse button is
  readonly                                                             being pressed.

  [middleButtonPressed\<DrawState.middleButtonPressed\>]{role="ref"}   True if the middle mouse button
  readonly                                                             is being pressed.

  [mouseOver\<DrawState.mouseOver\>]{role="ref"} readonly              True if the cursor is hovering
                                                                       over this element.

  [numLockKeyPressed\<DrawState.numLockKeyPressed\>]{role="ref"}       True if the Num Lock key is being
  readonly                                                             pressed.

  [optKeyPressed\<DrawState.optKeyPressed\>]{role="ref"} readonly      True if the Option key is being
                                                                       pressed (in Mac OS only).

  [rightButtonPressed\<DrawState.rightButtonPressed\>]{role="ref"}     True if the right mouse button is
  readonly                                                             being pressed.

  [shiftKeyPressed\<DrawState.shiftKeyPressed\>]{role="ref"} readonly  True if the Shift key is being
                                                                       pressed.
  -------------------------------------------------------------------- ---------------------------------

::: {.container .hide}
::: {.toctree}
DrawState/mouseOver.rst DrawState/leftButtonPressed.rst
DrawState/middleButtonPressed.rst DrawState/rightButtonPressed.rst
DrawState/hasFocus.rst DrawState/shiftKeyPressed.rst
DrawState/ctrlKeyPressed.rst DrawState/cmdKeyPressed.rst
DrawState/optKeyPressed.rst DrawState/altKeyPressed.rst
DrawState/numLockKeyPressed.rst DrawState/capsLockKeyPressed.rst
:::
:::
