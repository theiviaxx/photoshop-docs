Panel {#Panel}
=====

Description
-----------

A container for other types of controls, with an optional frame.

A panel can specify layout options for its child elements. Hiding a
panel hides all its children. Making it visible makes visible those
children that are not individually hidden.

### Properties

  ---------------------------------------------------- -------------------------------------------------
  [alignChildren\<Panel.alignChildren\>]{role="ref"}   Specifies how to align the child elements.
  readonly                                             

  [alignment\<Panel.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                       this value overrides the alignChildren setting
                                                       for the parent container.

  [bounds\<Panel.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                       coordinates.

  [characters\<Panel.characters\>]{role="ref"}         Reserve space for the specified number of
  readonly                                             characters; affects calculation
                                                       of?preferredSize?.

  [children\<Panel.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<Panel.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<Panel.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                       the element\'s appearance, in response to
                                                       the?onDraw()?event.

  [helpTip\<Panel.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                       hovers over the element.

  [indent\<Panel.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                       automatic layout.

  [justify\<Panel.justify\>]{role="ref"} readonly      The default text justification style for child
                                                       text elements.

  [layout\<Panel.layout\>]{role="ref"} readonly        The layout manager for this container.

  [location\<Panel.location\>]{role="ref"} readonly    The upper left corner of this element\'s frame
                                                       relative to its parent.

  [margins\<Panel.margins\>]{role="ref"} readonly      The number of pixels between the edges of a
                                                       container and the outermost child elements.

  [maximumSize\<Panel.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                             can be resized.

  [minimumSize\<Panel.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                             can be resized.

  [orientation\<Panel.orientation\>]{role="ref"}       The layout orientation of children in a
  readonly                                             container.

  [parent\<Panel.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<Panel.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                             determine the best size for each element.

  [properties\<Panel.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                             properties of the control (properties used only
                                                       when the element is created).

  [size\<Panel.size\>]{role="ref"} readonly            The current dimensions of this element.

  [spacing\<Panel.spacing\>]{role="ref"} readonly      The number of pixels separating one child element
                                                       from its adjacent sibling element.

  [text\<Panel.text\>]{role="ref"} readonly            The title or label text, a localizable string.

  [type\<Panel.type\>]{role="ref"} readonly            The element type; \"panel\".

  [visible\<Panel.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                       hidden.

  [window\<Panel.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<Panel.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                             top-level parent window.
  ---------------------------------------------------- -------------------------------------------------

### Methods

  ---------------------------------------------------------------- ----------------------------------------
  [add\<Panel.add\>]{role="ref"} readonly                          Adds a child element to this container.

  [addEventListener\<Panel.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                         particular type of event occuring in
                                                                   this element.

  [dispatchEvent\<Panel.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                   this target.

  [hide\<Panel.hide\>]{role="ref"} readonly                        Hides this element.

  [remove\<Panel.remove\>]{role="ref"} readonly                    Removes the specified child control from
                                                                   this group\'s?children?array.

  [removeEventListener\<Panel.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                         particular type of event occuring in
                                                                   this element.

  [show\<Panel.show\>]{role="ref"} readonly                        Shows this element.
  ---------------------------------------------------------------- ----------------------------------------

### Events

  -------------------------------------- ------------------------------------------------
  [onDraw\<Panel.onDraw\>]{role="ref"}   An event-handler callback function, called when
  readonly                               the panel is about to be drawn.
  -------------------------------------- ------------------------------------------------

::: {.container .hide}
::: {.toctree}
Panel/characters.rst Panel/justify.rst Panel/text.rst Panel/graphics.rst
Panel/visible.rst Panel/bounds.rst Panel/location.rst
Panel/maximumSize.rst Panel/minimumSize.rst Panel/preferredSize.rst
Panel/size.rst Panel/windowBounds.rst Panel/alignChildren.rst
Panel/children.rst Panel/layout.rst Panel/margins.rst
Panel/orientation.rst Panel/spacing.rst Panel/alignment.rst
Panel/properties.rst Panel/enabled.rst Panel/helpTip.rst
Panel/indent.rst Panel/parent.rst Panel/window.rst Panel/type.rst

Panel/show.rst Panel/hide.rst Panel/add.rst Panel/remove.rst
Panel/addEventListener.rst Panel/removeEventListener.rst
Panel/dispatchEvent.rst

Panel/onDraw.rst
:::
:::
