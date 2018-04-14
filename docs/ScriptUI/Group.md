Group {#Group}
=====

Description
-----------

A container for other controls within a window.

A group can specify layout options for its child elements. Hiding a
group hides all its children. Making it visible makes visible those
children that are not individually hidden.

### Properties

  ---------------------------------------------------- -------------------------------------------------
  [alignChildren\<Group.alignChildren\>]{role="ref"}   Tells the layout manager how unlike-sized
  readonly                                             children of this container should be aligned
                                                       within a column or row.

  [alignment\<Group.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                       this value overrides the alignChildren setting
                                                       for the parent container.

  [bounds\<Group.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                       coordinates.

  [children\<Group.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<Group.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<Group.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                       the element\'s appearance, in response to
                                                       the?onDraw()?event.

  [helpTip\<Group.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                       hovers over the element.

  [indent\<Group.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                       automatic layout.

  [layout\<Group.layout\>]{role="ref"} readonly        The layout manager for this container.

  [location\<Group.location\>]{role="ref"} readonly    The upper left corner of this element relative to
                                                       its parent.

  [margins\<Group.margins\>]{role="ref"} readonly      The number of pixels between the edges of a
                                                       container and the outermost child elements.

  [maximumSize\<Group.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                             can be resized.

  [minimumSize\<Group.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                             can be resized.

  [orientation\<Group.orientation\>]{role="ref"}       The layout orientation of children in a
  readonly                                             container.

  [parent\<Group.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<Group.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                             determine the best size for each element.

  [properties\<Group.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                             properties of the control (properties used only
                                                       when the element is created).

  [size\<Group.size\>]{role="ref"} readonly            The current dimensions of this element.

  [spacing\<Group.spacing\>]{role="ref"} readonly      The number of pixels separating one child element
                                                       from its adjacent sibling element.

  [type\<Group.type\>]{role="ref"} readonly            The element type; \"group\".

  [visible\<Group.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                       hidden.

  [window\<Group.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<Group.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                             top-level parent window.
  ---------------------------------------------------- -------------------------------------------------

### Methods

  ---------------------------------------------------------------- ----------------------------------------
  [add\<Group.add\>]{role="ref"} readonly                          Adds a child element to this container.

  [addEventListener\<Group.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                         particular type of event occuring in
                                                                   this element.

  [dispatchEvent\<Group.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                   this target.

  [hide\<Group.hide\>]{role="ref"} readonly                        Hides this element.

  [remove\<Group.remove\>]{role="ref"} readonly                    Removes the specified child control from
                                                                   this group\'s?children?array.

  [removeEventListener\<Group.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                         particular type of event occuring in
                                                                   this element.

  [show\<Group.show\>]{role="ref"} readonly                        Shows this element.
  ---------------------------------------------------------------- ----------------------------------------

### Events

  -------------------------------------- ------------------------------------------------
  [onDraw\<Group.onDraw\>]{role="ref"}   An event-handler callback function, called when
  readonly                               the group is about to be drawn.
  -------------------------------------- ------------------------------------------------

::: {.container .hide}
::: {.toctree}
Group/graphics.rst Group/visible.rst Group/bounds.rst Group/location.rst
Group/maximumSize.rst Group/minimumSize.rst Group/preferredSize.rst
Group/size.rst Group/windowBounds.rst Group/alignChildren.rst
Group/children.rst Group/layout.rst Group/margins.rst
Group/orientation.rst Group/spacing.rst Group/alignment.rst
Group/properties.rst Group/enabled.rst Group/helpTip.rst
Group/indent.rst Group/parent.rst Group/window.rst Group/type.rst

Group/show.rst Group/hide.rst Group/add.rst Group/remove.rst
Group/addEventListener.rst Group/removeEventListener.rst
Group/dispatchEvent.rst

Group/onDraw.rst
:::
:::
