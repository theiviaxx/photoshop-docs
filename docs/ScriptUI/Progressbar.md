Progressbar {#Progressbar}
===========

Description
-----------

A horizontal bar with an indicator that shows the progress of an
operation.

All progressbar controls have a horizontal orientation.
The?value?property contains the current position of the progress
indicator; the default is 0. There is a?minvalue?property, but it is
always 0; attempts to set it to a different value are silently ignored.

### Properties

  ---------------------------------------------------------- ------------------------------------------------
  [alignment\<Progressbar.alignment\>]{role="ref"} readonly  The alignment style for this element. If
                                                             defined, this value overrides the alignChildren
                                                             setting for the parent container.

  [bounds\<Progressbar.bounds\>]{role="ref"} readonly        The boundaries of the element, in
                                                             parent-relative coordinates.

  [children\<Progressbar.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<Progressbar.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<Progressbar.graphics\>]{role="ref"} readonly    The graphics object that can be used to
                                                             customize the element\'s appearance, in response
                                                             to the?onDraw()?event.

  [helpTip\<Progressbar.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                             hovers over the element.

  [indent\<Progressbar.indent\>]{role="ref"} readonly        The number of pixels to indent the element
                                                             during automatic layout.

  [location\<Progressbar.location\>]{role="ref"} readonly    The upper left corner of this element relative
                                                             to its parent.

  [maximumSize\<Progressbar.maximumSize\>]{role="ref"}       The maximum height and width to which the
  readonly                                                   element can be resized.

  [maxvalue\<Progressbar.maxvalue\>]{role="ref"} readonly    The maximum value in the range. Default is 100.

  [minimumSize\<Progressbar.minimumSize\>]{role="ref"}       The minimum height and width to which the
  readonly                                                   element can be resized.

  [minvalue\<Progressbar.minvalue\>]{role="ref"} readonly    The minimum value in the range; always 0. If set
                                                             to a different value, it is ignored.

  [parent\<Progressbar.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<Progressbar.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                   determine the best size for each element.

  [properties\<Progressbar.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                   properties of the container (properties used
                                                             only when the element is created).

  [size\<Progressbar.size\>]{role="ref"} readonly            The current dimensions of this element.

  [type\<Progressbar.type\>]{role="ref"} readonly            The element type, \"progessbar\".

  [value\<Progressbar.value\>]{role="ref"} readonly          The current position of the indicator.

  [visible\<Progressbar.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                             hidden.

  [window\<Progressbar.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<Progressbar.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                   top-level parent window.
  ---------------------------------------------------------- ------------------------------------------------

### Methods

  ---------------------------------------------------------------------- ---------------------------------------
  [addEventListener\<Progressbar.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                               particular type of event occuring in
                                                                         this element.

  [dispatchEvent\<Progressbar.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                         this target.

  [hide\<Progressbar.hide\>]{role="ref"} readonly                        Hides this element.

  [removeEventListener\<Progressbar.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                               particular type of event occuring in
                                                                         this element.

  [show\<Progressbar.show\>]{role="ref"} readonly                        Shows this element.
  ---------------------------------------------------------------------- ---------------------------------------

### Events

  -------------------------------------------- ----------------------------------------------
  [onDraw\<Progressbar.onDraw\>]{role="ref"}   An event-handler callback function, called
  readonly                                     when the window is about to be drawn.
  -------------------------------------------- ----------------------------------------------

::: {.container .hide}
::: {.toctree}
Progressbar/value.rst Progressbar/minvalue.rst Progressbar/maxvalue.rst
Progressbar/graphics.rst Progressbar/visible.rst Progressbar/bounds.rst
Progressbar/location.rst Progressbar/maximumSize.rst
Progressbar/minimumSize.rst Progressbar/preferredSize.rst
Progressbar/size.rst Progressbar/windowBounds.rst
Progressbar/alignment.rst Progressbar/children.rst
Progressbar/properties.rst Progressbar/enabled.rst
Progressbar/helpTip.rst Progressbar/indent.rst Progressbar/parent.rst
Progressbar/window.rst Progressbar/type.rst

Progressbar/show.rst Progressbar/hide.rst
Progressbar/addEventListener.rst Progressbar/removeEventListener.rst
Progressbar/dispatchEvent.rst

Progressbar/onDraw.rst
:::
:::
