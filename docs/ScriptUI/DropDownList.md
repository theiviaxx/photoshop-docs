DropDownList {#DropDownList}
============

Description
-----------

Displays a single visible item. When you click the control, a list drops
down or pops up, and allows you to select one of the other items in the
list.

Drop-down lists can have nonselectable separator items for visually
separating groups of related items, as in a menu. You can specify the
items on creation of the list object, or afterward using the list
object?s?add()?method. You can remove items programmatically with the
list object?s remove() and removeAll() methods. Calls
the?onChange()?callback if the item selection is changed or if
its?notify()?method is called.

### Properties

  ----------------------------------------------------------- ------------------------------------------------
  [active\<DropDownList.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<DropDownList.alignment\>]{role="ref"} readonly  The alignment style for this element. If
                                                              defined, this value overrides the alignChildren
                                                              setting for the parent container.

  [bounds\<DropDownList.bounds\>]{role="ref"} readonly        The boundaries of the element, in
                                                              parent-relative coordinates.

  [children\<DropDownList.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<DropDownList.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<DropDownList.graphics\>]{role="ref"} readonly    The graphics object that can be used to
                                                              customize the element\'s appearance, in response
                                                              to the?onDraw()?event.

  [helpTip\<DropDownList.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                              hovers over the element.

  [indent\<DropDownList.indent\>]{role="ref"} readonly        The number of pixels to indent the element
                                                              during automatic layout.

  [itemSize\<DropDownList.itemSize\>]{role="ref"} readonly    The width and height in pixels of each item in
                                                              the list.

  [items\<DropDownList.items\>]{role="ref"} readonly          The array of choice items displayed in the
                                                              drop-down or pop-up list.

  [location\<DropDownList.location\>]{role="ref"} readonly    The upper left corner of this element relative
                                                              to its parent.

  [maximumSize\<DropDownList.maximumSize\>]{role="ref"}       The maximum height and width to which the
  readonly                                                    element can be resized.

  [minimumSize\<DropDownList.minimumSize\>]{role="ref"}       The minimum height and width to which the
  readonly                                                    element can be resized.

  [parent\<DropDownList.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<DropDownList.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                    determine the best size for each element.

  [properties\<DropDownList.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                    properties of the container (properties used
                                                              only when the element is created).

  [selection\<DropDownList.selection\>]{role="ref"} readonly  The currently selected list item.

  [shortcutKey\<DropDownList.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                                    the?onShortcutKey()?callback for this element
                                                              (in Windows only).

  [size\<DropDownList.size\>]{role="ref"} readonly            The current dimensions of this element.

  [type\<DropDownList.type\>]{role="ref"} readonly            The element type; \"dropdownlist\".

  [visible\<DropDownList.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                              hidden.

  [window\<DropDownList.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<DropDownList.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                    top-level parent window.
  ----------------------------------------------------------- ------------------------------------------------

### Methods

  ----------------------------------------------------------------------- ---------------------------------------
  [add\<DropDownList.add\>]{role="ref"} readonly                          Adds an item or separator to the
                                                                          choices in this list.

  [addEventListener\<DropDownList.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                                particular type of event occuring in
                                                                          this element.

  [dispatchEvent\<DropDownList.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                          this target.

  [find\<DropDownList.find\>]{role="ref"} readonly                        Retrieves an item object from the list
                                                                          that has a given text label.

  [hide\<DropDownList.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<DropDownList.notify\>]{role="ref"} readonly                    Sends a notification message,
                                                                          simulating the specified user
                                                                          interaction event.

  [remove\<DropDownList.remove\>]{role="ref"} readonly                    Removes a child item from the list.

  [removeAll\<DropDownList.removeAll\>]{role="ref"} readonly              Removes all child items from the list.

  [removeEventListener\<DropDownList.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                                particular type of event occuring in
                                                                          this element.

  [show\<DropDownList.show\>]{role="ref"} readonly                        Shows this element.
  ----------------------------------------------------------------------- ---------------------------------------

### Events

  ----------------------------------------------------------- ----------------------------------------------
  [onActivate\<DropDownList.onActivate\>]{role="ref"}         An event-handler callback function, called
  readonly                                                    when the element acquires the keyboard focus.

  [onChange\<DropDownList.onChange\>]{role="ref"} readonly    An event-handler callback function, called
                                                              when the content of the element has been
                                                              changed

  [onDeactivate\<DropDownList.onDeactivate\>]{role="ref"}     An event-handler callback function, called
  readonly                                                    when the element loses the keyboard focus.

  [onDraw\<DropDownList.onDraw\>]{role="ref"} readonly        An event-handler callback function, called
                                                              when the window is about to be drawn.

  [onShortcutKey\<DropDownList.onShortcutKey\>]{role="ref"}   An event-handler callback function, called
  readonly                                                    when the element\'s?shortcutKey?sequence is
                                                              typed in the active window.
  ----------------------------------------------------------- ----------------------------------------------

::: {.container .hide}
::: {.toctree}
DropDownList/items.rst DropDownList/itemSize.rst
DropDownList/selection.rst DropDownList/active.rst
DropDownList/shortcutKey.rst DropDownList/graphics.rst
DropDownList/visible.rst DropDownList/bounds.rst
DropDownList/location.rst DropDownList/maximumSize.rst
DropDownList/minimumSize.rst DropDownList/preferredSize.rst
DropDownList/size.rst DropDownList/windowBounds.rst
DropDownList/alignment.rst DropDownList/children.rst
DropDownList/properties.rst DropDownList/enabled.rst
DropDownList/helpTip.rst DropDownList/indent.rst DropDownList/parent.rst
DropDownList/window.rst DropDownList/type.rst

DropDownList/add.rst DropDownList/find.rst DropDownList/remove.rst
DropDownList/removeAll.rst DropDownList/notify.rst DropDownList/show.rst
DropDownList/hide.rst DropDownList/addEventListener.rst
DropDownList/removeEventListener.rst DropDownList/dispatchEvent.rst

DropDownList/onActivate.rst DropDownList/onDeactivate.rst
DropDownList/onChange.rst DropDownList/onShortcutKey.rst
DropDownList/onDraw.rst
:::
:::
