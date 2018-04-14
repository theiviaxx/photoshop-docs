IconButton {#IconButton}
==========

Description
-----------

A mouse-sensitive pushbutton that displays an image instead of text.

Calls the?onClick()?callback if the control is clicked or if
its?notify()?method is called.

### Properties

  --------------------------------------------------------- ------------------------------------------------
  [active\<IconButton.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<IconButton.alignment\>]{role="ref"} readonly  The alignment style for this element. If
                                                            defined, this value overrides the alignChildren
                                                            setting for the parent container.

  [bounds\<IconButton.bounds\>]{role="ref"} readonly        The boundaries of the element, in
                                                            parent-relative coordinates.

  [children\<IconButton.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<IconButton.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<IconButton.graphics\>]{role="ref"} readonly    The graphics object that can be used to
                                                            customize the element\'s appearance, in response
                                                            to the?onDraw()?event.

  [helpTip\<IconButton.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                            hovers over the element.

  [image\<IconButton.image\>]{role="ref"} readonly          The image object that defines the image to be
                                                            drawn.

  [indent\<IconButton.indent\>]{role="ref"} readonly        The number of pixels to indent the element
                                                            during automatic layout.

  [location\<IconButton.location\>]{role="ref"} readonly    The upper left corner of this element relative
                                                            to its parent.

  [maximumSize\<IconButton.maximumSize\>]{role="ref"}       The maximum height and width to which the
  readonly                                                  element can be resized.

  [minimumSize\<IconButton.minimumSize\>]{role="ref"}       The minimum height and width to which the
  readonly                                                  element can be resized.

  [parent\<IconButton.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<IconButton.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                  determine the best size for each element.

  [properties\<IconButton.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                  properties of the container (properties used
                                                            only when the element is created).

  [shortcutKey\<IconButton.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                                  the?onShortcutKey()?callback for this element
                                                            (in Windows only).

  [size\<IconButton.size\>]{role="ref"} readonly            The current dimensions of this element.

  [type\<IconButton.type\>]{role="ref"} readonly            The element type; \"iconbutton\".

  [visible\<IconButton.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                            hidden.

  [window\<IconButton.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<IconButton.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                  top-level parent window.
  --------------------------------------------------------- ------------------------------------------------

### Methods

  --------------------------------------------------------------------- ---------------------------------------
  [addEventListener\<IconButton.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                              particular type of event occuring in
                                                                        this element.

  [dispatchEvent\<IconButton.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                        this target.

  [hide\<IconButton.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<IconButton.notify\>]{role="ref"} readonly                    Sends a notification message,
                                                                        simulating the specified user
                                                                        interaction event.

  [removeEventListener\<IconButton.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                              particular type of event occuring in
                                                                        this element.

  [show\<IconButton.show\>]{role="ref"} readonly                        Shows this element.
  --------------------------------------------------------------------- ---------------------------------------

### Events

  --------------------------------------------------------- -----------------------------------------------
  [onActivate\<IconButton.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                  the element acquires the keyboard focus.

  [onClick\<IconButton.onClick\>]{role="ref"} readonly      An event-handler callback function, called when
                                                            the element has been clicked.

  [onDeactivate\<IconButton.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                                  the element loses the keyboard focus.

  [onDraw\<IconButton.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                            the window is about to be drawn.

  [onShortcutKey\<IconButton.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                                  the element\'s shortcutKey sequence is typed in
                                                            the active window.
  --------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
IconButton/image.rst IconButton/active.rst IconButton/shortcutKey.rst
IconButton/graphics.rst IconButton/visible.rst IconButton/bounds.rst
IconButton/location.rst IconButton/maximumSize.rst
IconButton/minimumSize.rst IconButton/preferredSize.rst
IconButton/size.rst IconButton/windowBounds.rst IconButton/alignment.rst
IconButton/children.rst IconButton/properties.rst IconButton/enabled.rst
IconButton/helpTip.rst IconButton/indent.rst IconButton/parent.rst
IconButton/window.rst IconButton/type.rst

IconButton/notify.rst IconButton/show.rst IconButton/hide.rst
IconButton/addEventListener.rst IconButton/removeEventListener.rst
IconButton/dispatchEvent.rst

IconButton/onActivate.rst IconButton/onDeactivate.rst
IconButton/onDraw.rst IconButton/onClick.rst
IconButton/onShortcutKey.rst
:::
:::
