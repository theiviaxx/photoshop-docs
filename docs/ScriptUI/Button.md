Button {#Button}
======

Description
-----------

A pushbutton element containing a mouse-sensitive text string.

Calls the?onClick()?callback if the control is clicked or if
its?notify()?method is called.

### Properties

  ----------------------------------------------------- -------------------------------------------------
  [active\<Button.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<Button.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                        this value overrides the alignChildren setting
                                                        for the parent container.

  [bounds\<Button.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                        coordinates.

  [characters\<Button.characters\>]{role="ref"}         A number of characters for which to reserve space
  readonly                                              when calculating the preferred size of the
                                                        element.

  [children\<Button.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<Button.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<Button.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                        the element\'s appearance, in response to
                                                        the?onDraw()?event.

  [helpTip\<Button.helpTip\>]{role="ref"} readonly      The help string that is displayed when the mouse
                                                        hovers over the element.

  [indent\<Button.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                        automatic layout.

  [justify\<Button.justify\>]{role="ref"} readonly      The text justification style.

  [location\<Button.location\>]{role="ref"} readonly    The upper left corner of this element relative to
                                                        its parent.

  [maximumSize\<Button.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                              can be resized.

  [minimumSize\<Button.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                              can be resized.

  [parent\<Button.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<Button.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                              determine the best size for each element.

  [properties\<Button.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                              properties of the container (properties used only
                                                        when the element is created).

  [shortcutKey\<Button.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                              the?onShortcutKey()?callback for this element (in
                                                        Windows only).

  [size\<Button.size\>]{role="ref"} readonly            The current dimensions of this element.

  [text\<Button.text\>]{role="ref"} readonly            The text to display, a localizable string.

  [type\<Button.type\>]{role="ref"} readonly            The element type; \"button\".

  [visible\<Button.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                        hidden.

  [window\<Button.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<Button.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                              top-level parent window.
  ----------------------------------------------------- -------------------------------------------------

### Methods

  ----------------------------------------------------------------- ----------------------------------------
  [addEventListener\<Button.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                          particular type of event occuring in
                                                                    this element.

  [dispatchEvent\<Button.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                    this target.

  [hide\<Button.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<Button.notify\>]{role="ref"} readonly                    Sends a notification message, simulating
                                                                    the specified user interaction event.

  [removeEventListener\<Button.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                          particular type of event occuring in
                                                                    this element.

  [show\<Button.show\>]{role="ref"} readonly                        Shows this element.
  ----------------------------------------------------------------- ----------------------------------------

### Events

  ----------------------------------------------------- ------------------------------------------------
  [onActivate\<Button.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                              the element acquires the keyboard focus.

  [onClick\<Button.onClick\>]{role="ref"} readonly      An event-handler callback function, called when
                                                        the element has been clicked

  [onDeactivate\<Button.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                              the element loses the keyboard focus.

  [onDraw\<Button.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                        the window is about to be drawn.

  [onShortcutKey\<Button.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                              the element\'s shortcutKey sequence is typed in
                                                        the active window.
  ----------------------------------------------------- ------------------------------------------------

::: {.container .hide}
::: {.toctree}
Button/characters.rst Button/justify.rst Button/text.rst
Button/active.rst Button/shortcutKey.rst Button/graphics.rst
Button/visible.rst Button/bounds.rst Button/location.rst
Button/maximumSize.rst Button/minimumSize.rst Button/preferredSize.rst
Button/size.rst Button/windowBounds.rst Button/alignment.rst
Button/children.rst Button/properties.rst Button/enabled.rst
Button/helpTip.rst Button/indent.rst Button/parent.rst Button/window.rst
Button/type.rst

Button/notify.rst Button/show.rst Button/hide.rst
Button/addEventListener.rst Button/removeEventListener.rst
Button/dispatchEvent.rst

Button/onActivate.rst Button/onDeactivate.rst Button/onDraw.rst
Button/onClick.rst Button/onShortcutKey.rst
:::
:::
