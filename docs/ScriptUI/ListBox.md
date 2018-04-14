ListBox {#ListBox}
=======

Description
-----------

Displays a list of choices, represented by?ListItem?objects.

When you create the object, you specify whether it allows the user to
select only one or multiple items. If a list contains more items than
can be displayed in the available area, a scrollbar may appear that
allows the user to scroll through all the list items.You can specify the
items on creation of the list object, or afterward using the list
object?s?add()?method. You can remove items programmatically with the
list object?s?remove()?and?removeAll()?methods. You can create a list
box with multiple columns; in this case, each row is a selectable
choice, and each?ListItem?represents one row.

### Properties

  ------------------------------------------------------ -------------------------------------------------
  [active\<ListBox.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<ListBox.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                         this value overrides the alignChildren setting
                                                         for the parent container.

  [bounds\<ListBox.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                         coordinates.

  [children\<ListBox.children\>]{role="ref"} readonly    An array of child?ListItem?elements.

  [columns\<ListBox.columns\>]{role="ref"} readonly      For a multi-column list box, the column
                                                         properties.

  [enabled\<ListBox.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<ListBox.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                         the element\'s appearance, in response to
                                                         the?onDraw()?event.

  [helpTip\<ListBox.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                         hovers over the element.

  [indent\<ListBox.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                         automatic layout.

  [itemSize\<ListBox.itemSize\>]{role="ref"} readonly    The width and height in pixels of each item in
                                                         the list.

  [items\<ListBox.items\>]{role="ref"} readonly          The array of choice items displayed in the list.

  [location\<ListBox.location\>]{role="ref"} readonly    The upper left corner of this element relative to
                                                         its parent.

  [maximumSize\<ListBox.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                               can be resized.

  [minimumSize\<ListBox.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                               can be resized.

  [parent\<ListBox.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<ListBox.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                               determine the best size for each element.

  [properties\<ListBox.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                               properties of the control (properties used only
                                                         when the element is created).

  [selection\<ListBox.selection\>]{role="ref"} readonly  The currently selected item for a
                                                         single-selection list, or an array of items for
                                                         current selection in a multi-selection list.

  [shortcutKey\<ListBox.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                               the?onShortcutKey()?callback for this element (in
                                                         Windows only).

  [size\<ListBox.size\>]{role="ref"} readonly            The current dimensions of this element.

  [type\<ListBox.type\>]{role="ref"} readonly            The element type; \"listbox\".

  [visible\<ListBox.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                         hidden.

  [window\<ListBox.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<ListBox.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                               top-level parent window.
  ------------------------------------------------------ -------------------------------------------------

### Methods

  ------------------------------------------------------------------ ----------------------------------------
  [add\<ListBox.add\>]{role="ref"} readonly                          Adds an item to the choices in this
                                                                     list.

  [addEventListener\<ListBox.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                           particular type of event occuring in
                                                                     this element.

  [dispatchEvent\<ListBox.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                     this target.

  [find\<ListBox.find\>]{role="ref"} readonly                        Retrieves an item object from the list
                                                                     that has a given text label.

  [hide\<ListBox.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<ListBox.notify\>]{role="ref"} readonly                    Sends a notification message, simulating
                                                                     the specified user interaction event.

  [remove\<ListBox.remove\>]{role="ref"} readonly                    Removes a child item from the list.

  [removeAll\<ListBox.removeAll\>]{role="ref"} readonly              Removes all child items from the list.

  [removeEventListener\<ListBox.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                           particular type of event occuring in
                                                                     this element.

  [show\<ListBox.show\>]{role="ref"} readonly                        Shows this element.
  ------------------------------------------------------------------ ----------------------------------------

### Events

  ------------------------------------------------------ ------------------------------------------------
  [onActivate\<ListBox.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                               the element acquires the keyboard focus.

  [onChange\<ListBox.onChange\>]{role="ref"} readonly    An event-handler callback function, called when
                                                         the content of the element has been changed

  [onDeactivate\<ListBox.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                               the element loses the keyboard focus.

  [onDoubleClick\<ListBox.onDoubleClick\>]{role="ref"}   An event-handler callback function, called when
  readonly                                               an item in the listbox is double-clicked

  [onDraw\<ListBox.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                         the window is about to be drawn.

  [onShortcutKey\<ListBox.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                               the element\'s?shortcutKey?sequence is typed in
                                                         the active window.
  ------------------------------------------------------ ------------------------------------------------

::: {.container .hide}
::: {.toctree}
ListBox/items.rst ListBox/itemSize.rst ListBox/selection.rst
ListBox/active.rst ListBox/shortcutKey.rst ListBox/graphics.rst
ListBox/visible.rst ListBox/bounds.rst ListBox/location.rst
ListBox/maximumSize.rst ListBox/minimumSize.rst
ListBox/preferredSize.rst ListBox/size.rst ListBox/windowBounds.rst
ListBox/alignment.rst ListBox/children.rst ListBox/columns.rst
ListBox/properties.rst ListBox/enabled.rst ListBox/helpTip.rst
ListBox/indent.rst ListBox/parent.rst ListBox/window.rst
ListBox/type.rst

ListBox/add.rst ListBox/find.rst ListBox/remove.rst
ListBox/removeAll.rst ListBox/notify.rst ListBox/show.rst
ListBox/hide.rst ListBox/addEventListener.rst
ListBox/removeEventListener.rst ListBox/dispatchEvent.rst

ListBox/onActivate.rst ListBox/onDeactivate.rst ListBox/onChange.rst
ListBox/onDoubleClick.rst ListBox/onShortcutKey.rst ListBox/onDraw.rst
:::
:::
