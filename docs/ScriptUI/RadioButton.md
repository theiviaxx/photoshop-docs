RadioButton {#RadioButton}
===========

Description
-----------

A dual-state control, grouped with other radiobuttons, of which only one
can be in the selected state.

Shows the selected state when?value=true, empty when?value=false. Calls
the?onClick()?callback if the control is clicked or if
its?notify()?method is called.

### Properties

  ---------------------------------------------------------- ------------------------------------------------
  [active\<RadioButton.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<RadioButton.alignment\>]{role="ref"} readonly  The alignment style for this element. If
                                                             defined, this value overrides the alignChildren
                                                             setting for the parent container.

  [bounds\<RadioButton.bounds\>]{role="ref"} readonly        The boundaries of the element, in
                                                             parent-relative coordinates.

  [characters\<RadioButton.characters\>]{role="ref"}         A number of characters for which to reserve
  readonly                                                   space when calculating the preferred size of the
                                                             element.

  [children\<RadioButton.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<RadioButton.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<RadioButton.graphics\>]{role="ref"} readonly    The graphics object that can be used to
                                                             customize the element\'s appearance, in response
                                                             to the?onDraw?event.

  [helpTip\<RadioButton.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                             hovers over the element.

  [indent\<RadioButton.indent\>]{role="ref"} readonly        The number of pixels to indent the element
                                                             during automatic layout.

  [justify\<RadioButton.justify\>]{role="ref"} readonly      The default text justification style for child
                                                             text elements.

  [location\<RadioButton.location\>]{role="ref"} readonly    The upper left corner of this element relative
                                                             to its parent.

  [maximumSize\<RadioButton.maximumSize\>]{role="ref"}       The maximum height and width to which the
  readonly                                                   element can be resized.

  [minimumSize\<RadioButton.minimumSize\>]{role="ref"}       The minimum height and width to which the
  readonly                                                   element can be resized.

  [parent\<RadioButton.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<RadioButton.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                   determine the best size for each element.

  [properties\<RadioButton.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                   properties of the container (properties used
                                                             only when the element is created).

  [shortcutKey\<RadioButton.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                                   the?onShortcutKey()?callback for this element
                                                             (in Windows only).

  [size\<RadioButton.size\>]{role="ref"} readonly            The current dimensions of this element.

  [text\<RadioButton.text\>]{role="ref"} readonly            The label text for this button, a localizable
                                                             string.

  [type\<RadioButton.type\>]{role="ref"} readonly            The element type; \"radiobutton\".

  [value\<RadioButton.value\>]{role="ref"} readonly          The selection state of this button, selected
                                                             when true.

  [visible\<RadioButton.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                             hidden.

  [window\<RadioButton.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<RadioButton.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                   top-level parent window.
  ---------------------------------------------------------- ------------------------------------------------

### Methods

  ---------------------------------------------------------------------- ---------------------------------------
  [addEventListener\<RadioButton.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                               particular type of event occuring in
                                                                         this element.

  [dispatchEvent\<RadioButton.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                         this target.

  [hide\<RadioButton.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<RadioButton.notify\>]{role="ref"} readonly                    Sends a notification message,
                                                                         simulating the specified user
                                                                         interaction event.

  [removeEventListener\<RadioButton.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                               particular type of event occuring in
                                                                         this element.

  [show\<RadioButton.show\>]{role="ref"} readonly                        Shows this element.
  ---------------------------------------------------------------------- ---------------------------------------

### Events

  ---------------------------------------------------------- -----------------------------------------------
  [onActivate\<RadioButton.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                   the element acquires the keyboard focus.

  [onClick\<RadioButton.onClick\>]{role="ref"} readonly      An event-handler callback function, called when
                                                             the element has been clicked.

  [onDeactivate\<RadioButton.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                                   the element loses the keyboard focus.

  [onDraw\<RadioButton.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                             the window is about to be drawn.

  [onShortcutKey\<RadioButton.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                                   the element\'s?shortcutKey?sequence is typed in
                                                             the active window.
  ---------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
RadioButton/value.rst RadioButton/characters.rst RadioButton/justify.rst
RadioButton/text.rst RadioButton/active.rst RadioButton/shortcutKey.rst
RadioButton/graphics.rst RadioButton/visible.rst RadioButton/bounds.rst
RadioButton/location.rst RadioButton/maximumSize.rst
RadioButton/minimumSize.rst RadioButton/preferredSize.rst
RadioButton/size.rst RadioButton/windowBounds.rst
RadioButton/alignment.rst RadioButton/children.rst
RadioButton/properties.rst RadioButton/enabled.rst
RadioButton/helpTip.rst RadioButton/indent.rst RadioButton/parent.rst
RadioButton/window.rst RadioButton/type.rst

RadioButton/notify.rst RadioButton/show.rst RadioButton/hide.rst
RadioButton/addEventListener.rst RadioButton/removeEventListener.rst
RadioButton/dispatchEvent.rst

RadioButton/onActivate.rst RadioButton/onDeactivate.rst
RadioButton/onDraw.rst RadioButton/onClick.rst
RadioButton/onShortcutKey.rst
:::
:::
