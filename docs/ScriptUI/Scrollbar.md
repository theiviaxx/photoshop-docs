Scrollbar {#Scrollbar}
=========

Description
-----------

A scrollbar with a draggable scroll indicator and stepper buttons to
move the indicator.

The scrollbar control has a horizontal orientation if the width is
greater than the height at creation time, or vertical if its height is
greater than its width. Calls the?onChange()?callback after the position
of the indicator is changed or if its?notify()?method is called. Calls
the?onChanging()?callback repeatedly while the user is moving the
indicator. Scrollbars are often created with an
associated?EditText?field to display the current value of the scrollbar,
and to allow setting the scrollbar\'s position to a specific value.

### Properties

  -------------------------------------------------------- -------------------------------------------------
  [active\<Scrollbar.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<Scrollbar.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                           this value overrides the alignChildren setting
                                                           for the parent container.

  [bounds\<Scrollbar.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                           coordinates.

  [children\<Scrollbar.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<Scrollbar.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<Scrollbar.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                           the element\'s appearance, in response to
                                                           the?onDraw()?event.

  [helpTip\<Scrollbar.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                           hovers over the element.

  [indent\<Scrollbar.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                           automatic layout.

  [jumpdelta\<Scrollbar.jumpdelta\>]{role="ref"} readonly  The amount to increment or decrement a scrollbar
                                                           indicator\'s position when the user clicks ahead
                                                           or behind the moveable element.

  [location\<Scrollbar.location\>]{role="ref"} readonly    The upper left corner of this element relative to
                                                           its parent.

  [maximumSize\<Scrollbar.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                                 can be resized.

  [maxvalue\<Scrollbar.maxvalue\>]{role="ref"} readonly    The maximum value allowed in the value property.

  [minimumSize\<Scrollbar.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                                 can be resized.

  [minvalue\<Scrollbar.minvalue\>]{role="ref"} readonly    The minimum value allowed in the value property.

  [parent\<Scrollbar.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<Scrollbar.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                 determine the best size for each element.

  [properties\<Scrollbar.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                 properties of the container (properties used only
                                                           when the element is created).

  [shortcutKey\<Scrollbar.shortcutKey\>]{role="ref"}       The key sequence that invokes the
  readonly                                                 ?onShortcutKey()?callback for this element (in
                                                           Windows only).

  [size\<Scrollbar.size\>]{role="ref"} readonly            The current dimensions of this element.

  [stepdelta\<Scrollbar.stepdelta\>]{role="ref"} readonly  The amount by which to increment or decrement a
                                                           scrollbar element\'s position when the user
                                                           clicks a stepper button.

  [type\<Scrollbar.type\>]{role="ref"} readonly            The element type, \"scrollbar\".

  [value\<Scrollbar.value\>]{role="ref"} readonly          The current position of the indicator.

  [visible\<Scrollbar.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                           hidden.

  [window\<Scrollbar.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<Scrollbar.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                 top-level parent window.
  -------------------------------------------------------- -------------------------------------------------

### Methods

  -------------------------------------------------------------------- ---------------------------------------
  [addEventListener\<Scrollbar.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                             particular type of event occuring in
                                                                       this element.

  [dispatchEvent\<Scrollbar.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                       this target.

  [hide\<Scrollbar.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<Scrollbar.notify\>]{role="ref"} readonly                    Sends a notification message,
                                                                       simulating the specified user
                                                                       interaction event.

  [removeEventListener\<Scrollbar.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                             particular type of event occuring in
                                                                       this element.

  [show\<Scrollbar.show\>]{role="ref"} readonly                        Shows this element.
  -------------------------------------------------------------------- ---------------------------------------

### Events

  -------------------------------------------------------- -------------------------------------------------
  [onActivate\<Scrollbar.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                 the element acquires the keyboard focus.

  [onChange\<Scrollbar.onChange\>]{role="ref"} readonly    An event-handler callback function, called when
                                                           the user has finished dragging the position
                                                           indicator, or has clicked the control.

  [onChanging\<Scrollbar.onChanging\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                 the content of the element is in the process of
                                                           changing

  [onDeactivate\<Scrollbar.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                                 the element loses the keyboard focus.

  [onDraw\<Scrollbar.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                           the window is about to be drawn.

  [onShortcutKey\<Scrollbar.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                                 the element\'s?shortcutKey?sequence is typed in
                                                           the active window.
  -------------------------------------------------------- -------------------------------------------------

::: {.container .hide}
::: {.toctree}
Scrollbar/stepdelta.rst Scrollbar/jumpdelta.rst Scrollbar/value.rst
Scrollbar/minvalue.rst Scrollbar/maxvalue.rst Scrollbar/active.rst
Scrollbar/shortcutKey.rst Scrollbar/graphics.rst Scrollbar/visible.rst
Scrollbar/bounds.rst Scrollbar/location.rst Scrollbar/maximumSize.rst
Scrollbar/minimumSize.rst Scrollbar/preferredSize.rst Scrollbar/size.rst
Scrollbar/windowBounds.rst Scrollbar/alignment.rst
Scrollbar/children.rst Scrollbar/properties.rst Scrollbar/enabled.rst
Scrollbar/helpTip.rst Scrollbar/indent.rst Scrollbar/parent.rst
Scrollbar/window.rst Scrollbar/type.rst

Scrollbar/notify.rst Scrollbar/show.rst Scrollbar/hide.rst
Scrollbar/addEventListener.rst Scrollbar/removeEventListener.rst
Scrollbar/dispatchEvent.rst

Scrollbar/onActivate.rst Scrollbar/onDeactivate.rst Scrollbar/onDraw.rst
Scrollbar/onChanging.rst Scrollbar/onChange.rst
Scrollbar/onShortcutKey.rst
:::
:::
