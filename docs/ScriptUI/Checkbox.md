Checkbox {#Checkbox}
========

Description
-----------

A dual-state control showing a box that has a checkmark when
the?value?is true, and is empty when the?value?is false.

Calls the?onClick()?callback if the control is clicked or if
its?notify()?method is called.

### Properties

  ------------------------------------------------------- -------------------------------------------------
  [active\<Checkbox.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<Checkbox.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                          this value overrides the alignChildren setting
                                                          for the parent container.

  [bounds\<Checkbox.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                          coordinates.

  [characters\<Checkbox.characters\>]{role="ref"}         A number of characters for which to reserve space
  readonly                                                when calculating the preferred size of the
                                                          element.

  [children\<Checkbox.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<Checkbox.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<Checkbox.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                          the element\'s appearance, in response to
                                                          the?onDraw()?event.

  [helpTip\<Checkbox.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                          hovers over the element.

  [indent\<Checkbox.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                          automatic layout.

  [justify\<Checkbox.justify\>]{role="ref"} readonly      The default text justification style for child
                                                          text elements.

  [location\<Checkbox.location\>]{role="ref"} readonly    The upper left corner of this element relative to
                                                          its parent.

  [maximumSize\<Checkbox.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                                can be resized.

  [minimumSize\<Checkbox.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                                can be resized.

  [parent\<Checkbox.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<Checkbox.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                determine the best size for each element.

  [properties\<Checkbox.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                properties of the item (properties used only when
                                                          the element is created).

  [shortcutKey\<Checkbox.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                                the?onShortcutKey()?callback for this element (in
                                                          Windows only).

  [size\<Checkbox.size\>]{role="ref"} readonly            The current dimensions of this element.

  [text\<Checkbox.text\>]{role="ref"} readonly            The text to display, a localizable string.

  [type\<Checkbox.type\>]{role="ref"} readonly            The element type; \"checkbox\".

  [value\<Checkbox.value\>]{role="ref"} readonly          The selection state of the control.

  [visible\<Checkbox.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                          hidden.

  [window\<Checkbox.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<Checkbox.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                top-level parent window.
  ------------------------------------------------------- -------------------------------------------------

### Methods

  ------------------------------------------------------------------- ----------------------------------------
  [addEventListener\<Checkbox.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                            particular type of event occuring in
                                                                      this element.

  [dispatchEvent\<Checkbox.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                      this target.

  [hide\<Checkbox.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<Checkbox.notify\>]{role="ref"} readonly                    Sends a notification message, simulating
                                                                      the specified user interaction event.

  [removeEventListener\<Checkbox.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                            particular type of event occuring in
                                                                      this element.

  [show\<Checkbox.show\>]{role="ref"} readonly                        Shows this element.
  ------------------------------------------------------------------- ----------------------------------------

### Events

  ------------------------------------------------------- -----------------------------------------------
  [onActivate\<Checkbox.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                the element acquires the keyboard focus.

  [onClick\<Checkbox.onClick\>]{role="ref"} readonly      An event-handler callback function, called when
                                                          the element has been clicked.

  [onDeactivate\<Checkbox.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                                the element loses the keyboard focus.

  [onDraw\<Checkbox.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                          the window is about to be drawn.

  [onShortcutKey\<Checkbox.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                                the element\'s?shortcutKey?sequence is typed in
                                                          the active window.
  ------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
Checkbox/value.rst Checkbox/characters.rst Checkbox/justify.rst
Checkbox/text.rst Checkbox/active.rst Checkbox/shortcutKey.rst
Checkbox/graphics.rst Checkbox/visible.rst Checkbox/bounds.rst
Checkbox/location.rst Checkbox/maximumSize.rst Checkbox/minimumSize.rst
Checkbox/preferredSize.rst Checkbox/size.rst Checkbox/windowBounds.rst
Checkbox/alignment.rst Checkbox/children.rst Checkbox/properties.rst
Checkbox/enabled.rst Checkbox/helpTip.rst Checkbox/indent.rst
Checkbox/parent.rst Checkbox/window.rst Checkbox/type.rst

Checkbox/notify.rst Checkbox/show.rst Checkbox/hide.rst
Checkbox/addEventListener.rst Checkbox/removeEventListener.rst
Checkbox/dispatchEvent.rst

Checkbox/onActivate.rst Checkbox/onDeactivate.rst Checkbox/onDraw.rst
Checkbox/onClick.rst Checkbox/onShortcutKey.rst
:::
:::
