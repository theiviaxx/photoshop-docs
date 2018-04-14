StaticText {#StaticText}
==========

Description
-----------

A text label that the user cannot change.

### Properties

  --------------------------------------------------------- ------------------------------------------------
  [active\<StaticText.active\>]{role="ref"} readonly        Always false. This element cannot have input
                                                            focus.

  [alignment\<StaticText.alignment\>]{role="ref"} readonly  The alignment style for this element. If
                                                            defined, this value overrides the alignChildren
                                                            setting for the parent container.

  [bounds\<StaticText.bounds\>]{role="ref"} readonly        The boundaries of the element, in
                                                            parent-relative coordinates.

  [characters\<StaticText.characters\>]{role="ref"}         A number of characters for which to reserve
  readonly                                                  space when calculating the preferred size of the
                                                            element.

  [children\<StaticText.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<StaticText.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<StaticText.graphics\>]{role="ref"} readonly    The graphics object that can be used to
                                                            customize the element\'s appearance, in response
                                                            to the?onDraw()?event.

  [helpTip\<StaticText.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                            hovers over the element.

  [indent\<StaticText.indent\>]{role="ref"} readonly        The number of pixels to indent the element
                                                            during automatic layout.

  [justify\<StaticText.justify\>]{role="ref"} readonly      The text justification style.

  [location\<StaticText.location\>]{role="ref"} readonly    The upper left corner of this element relative
                                                            to its parent.

  [maximumSize\<StaticText.maximumSize\>]{role="ref"}       The maximum height and width to which the
  readonly                                                  element can be resized.

  [minimumSize\<StaticText.minimumSize\>]{role="ref"}       The minimum height and width to which the
  readonly                                                  element can be resized.

  [parent\<StaticText.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<StaticText.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                  determine the best size for each element.

  [properties\<StaticText.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                  properties of the container (properties used
                                                            only when the element is created).

  [shortcutKey\<StaticText.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                                  the?onShortcutKey()?callback for this element
                                                            (in Windows only).

  [size\<StaticText.size\>]{role="ref"} readonly            The current dimensions of this element.

  [text\<StaticText.text\>]{role="ref"} readonly            The text to display, a localizable string.

  [type\<StaticText.type\>]{role="ref"} readonly            The element type, \"statictext\".

  [visible\<StaticText.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                            hidden.

  [window\<StaticText.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<StaticText.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                  top-level parent window.
  --------------------------------------------------------- ------------------------------------------------

### Methods

  --------------------------------------------------------------------- ---------------------------------------
  [addEventListener\<StaticText.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                              particular type of event occuring in
                                                                        this element.

  [dispatchEvent\<StaticText.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                        this target.

  [hide\<StaticText.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<StaticText.notify\>]{role="ref"} readonly                    Sends a notification message,
                                                                        simulating the specified user
                                                                        interaction event.

  [removeEventListener\<StaticText.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                              particular type of event occuring in
                                                                        this element.

  [show\<StaticText.show\>]{role="ref"} readonly                        Shows this element.
  --------------------------------------------------------------------- ---------------------------------------

### Events

  --------------------------------------------------------- -----------------------------------------------
  [onDraw\<StaticText.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                            the window is about to be drawn.

  [onShortcutKey\<StaticText.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                                  the element\'s shortcutKey sequence is typed in
                                                            the active window.
  --------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
StaticText/characters.rst StaticText/justify.rst StaticText/text.rst
StaticText/active.rst StaticText/shortcutKey.rst StaticText/graphics.rst
StaticText/visible.rst StaticText/bounds.rst StaticText/location.rst
StaticText/maximumSize.rst StaticText/minimumSize.rst
StaticText/preferredSize.rst StaticText/size.rst
StaticText/windowBounds.rst StaticText/alignment.rst
StaticText/children.rst StaticText/properties.rst StaticText/enabled.rst
StaticText/helpTip.rst StaticText/indent.rst StaticText/parent.rst
StaticText/window.rst StaticText/type.rst

StaticText/notify.rst StaticText/show.rst StaticText/hide.rst
StaticText/addEventListener.rst StaticText/removeEventListener.rst
StaticText/dispatchEvent.rst

StaticText/onDraw.rst StaticText/onShortcutKey.rst
:::
:::
