Slider {#Slider}
======

Description
-----------

A slider bar that indicates a numeric value with a moveable position
indicator.

All slider controls have a horizontal orientation. Calls
the?onChange()?callback after the position of the indicator is changed
or if its?notify()?method is called. Calls the?onChanging()?callback
repeatedly while the user is moving the indicator. The?value?property
contains the current position of the indicator within the range
of?minvalue?to?maxvalue.

### Properties

  ----------------------------------------------------- -------------------------------------------------
  [active\<Slider.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<Slider.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                        this value overrides the alignChildren setting
                                                        for the parent container.

  [bounds\<Slider.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                        coordinates.

  [children\<Slider.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<Slider.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<Slider.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                        the element\'s appearance, in response to
                                                        the?onDraw()?event.

  [helpTip\<Slider.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                        hovers over the element.

  [indent\<Slider.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                        automatic layout.

  [location\<Slider.location\>]{role="ref"} readonly    The upper left corner of this element relative to
                                                        its parent.

  [maximumSize\<Slider.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                              can be resized.

  [maxvalue\<Slider.maxvalue\>]{role="ref"} readonly    The maximum value allowed in the?value?property.

  [minimumSize\<Slider.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                              can be resized.

  [minvalue\<Slider.minvalue\>]{role="ref"} readonly    The minimum value allowed in the?value?property.

  [parent\<Slider.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<Slider.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                              determine the best size for each element.

  [properties\<Slider.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                              properties of the container (properties used only
                                                        when the element is created).

  [shortcutKey\<Slider.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                              the?onShortcutKey()?callback for this element (in
                                                        Windows only).

  [size\<Slider.size\>]{role="ref"} readonly            The current dimensions of this element.

  [type\<Slider.type\>]{role="ref"} readonly            The element type, \"slider\".

  [value\<Slider.value\>]{role="ref"} readonly          The current position of the indicator.

  [visible\<Slider.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                        hidden.

  [window\<Slider.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<Slider.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                              top-level parent window.
  ----------------------------------------------------- -------------------------------------------------

### Methods

  ----------------------------------------------------------------- ----------------------------------------
  [addEventListener\<Slider.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                          particular type of event occuring in
                                                                    this element.

  [dispatchEvent\<Slider.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                    this target.

  [hide\<Slider.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<Slider.notify\>]{role="ref"} readonly                    Sends a notification message, simulating
                                                                    the specified user interaction event.

  [removeEventListener\<Slider.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                          particular type of event occuring in
                                                                    this element.

  [show\<Slider.show\>]{role="ref"} readonly                        Shows this element.
  ----------------------------------------------------------------- ----------------------------------------

### Events

  ----------------------------------------------------- --------------------------------------------------
  [onActivate\<Slider.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                              the element acquires the keyboard focus.

  [onChange\<Slider.onChange\>]{role="ref"} readonly    An event-handler callback function, called when
                                                        the user has finished dragging the position
                                                        indicator, or has clicked the control.

  [onChanging\<Slider.onChanging\>]{role="ref"}         An event-handler callback function, called when
  readonly                                              the content of the element is in the process of
                                                        changing

  [onDeactivate\<Slider.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                              the element loses the keyboard focus.

  [onDraw\<Slider.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                        the window is about to be drawn.

  [onShortcutKey\<Slider.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                              the element\'s?shortcutKey?sequence is typed in
                                                        the active window.
  ----------------------------------------------------- --------------------------------------------------

::: {.container .hide}
::: {.toctree}
Slider/value.rst Slider/minvalue.rst Slider/maxvalue.rst
Slider/active.rst Slider/shortcutKey.rst Slider/graphics.rst
Slider/visible.rst Slider/bounds.rst Slider/location.rst
Slider/maximumSize.rst Slider/minimumSize.rst Slider/preferredSize.rst
Slider/size.rst Slider/windowBounds.rst Slider/alignment.rst
Slider/children.rst Slider/properties.rst Slider/enabled.rst
Slider/helpTip.rst Slider/indent.rst Slider/parent.rst Slider/window.rst
Slider/type.rst

Slider/notify.rst Slider/show.rst Slider/hide.rst
Slider/addEventListener.rst Slider/removeEventListener.rst
Slider/dispatchEvent.rst

Slider/onActivate.rst Slider/onDeactivate.rst Slider/onDraw.rst
Slider/onChanging.rst Slider/onChange.rst Slider/onShortcutKey.rst
:::
:::
