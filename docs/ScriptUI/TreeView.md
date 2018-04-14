TreeView {#TreeView}
========

Description
-----------

A hierarchical list whose items can contain child items.

The?ListItem?children of this control (in the?items?array) can be of
type node, which means that they can contain child items. An item with
child items can expanded, so that the child items are displayed, or
collapsed, so that the child items are hidden Individual items can be
selected at any level of the tree.

### Properties

  ------------------------------------------------------- -------------------------------------------------
  [active\<TreeView.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<TreeView.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                          this value overrides the alignChildren setting
                                                          for the parent container.

  [bounds\<TreeView.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                          coordinates.

  [children\<TreeView.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<TreeView.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<TreeView.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                          the element\'s appearance, in response to
                                                          the?onDraw()?event.

  [helpTip\<TreeView.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                          hovers over the element.

  [indent\<TreeView.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                          automatic layout.

  [itemSize\<TreeView.itemSize\>]{role="ref"} readonly    The width and height in pixels of each item in
                                                          the list.

  [items\<TreeView.items\>]{role="ref"} readonly          The array of top-level items displayed in the
                                                          list.

  [location\<TreeView.location\>]{role="ref"} readonly    The upper left corner of this element relative to
                                                          its parent.

  [maximumSize\<TreeView.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                                can be resized.

  [minimumSize\<TreeView.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                                can be resized.

  [parent\<TreeView.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<TreeView.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                determine the best size for each element.

  [properties\<TreeView.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                properties of the control (properties used only
                                                          when the element is created).

  [selection\<TreeView.selection\>]{role="ref"} readonly  The currently selected list item.

  [shortcutKey\<TreeView.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                                the?onShortcutKey()?callback for this element (in
                                                          Windows only).

  [size\<TreeView.size\>]{role="ref"} readonly            The current dimensions of this element.

  [type\<TreeView.type\>]{role="ref"} readonly            The element type, \"treeview\".

  [visible\<TreeView.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                          hidden.

  [window\<TreeView.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<TreeView.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                top-level parent window.
  ------------------------------------------------------- -------------------------------------------------

### Methods

  ------------------------------------------------------------------- ----------------------------------------
  [add\<TreeView.add\>]{role="ref"} readonly                          Adds an item to the top-level choices in
                                                                      this list.

  [addEventListener\<TreeView.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                            particular type of event occuring in
                                                                      this element.

  [dispatchEvent\<TreeView.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                      this target.

  [find\<TreeView.find\>]{role="ref"} readonly                        Retrieves an item object from the list
                                                                      that has a given text label.

  [hide\<TreeView.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<TreeView.notify\>]{role="ref"} readonly                    Sends a notification message, simulating
                                                                      the specified user interaction event.

  [remove\<TreeView.remove\>]{role="ref"} readonly                    Removes a child item from the list.

  [removeAll\<TreeView.removeAll\>]{role="ref"} readonly              Removes all child items from the list.

  [removeEventListener\<TreeView.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                            particular type of event occuring in
                                                                      this element.

  [show\<TreeView.show\>]{role="ref"} readonly                        Shows this element.
  ------------------------------------------------------------------- ----------------------------------------

### Events

  ------------------------------------------------------- -----------------------------------------------
  [onActivate\<TreeView.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                the element acquires the keyboard focus.

  [onChange\<TreeView.onChange\>]{role="ref"} readonly    An event-handler callback function, called when
                                                          the content of the element has been changed

  [onCollapse\<TreeView.onCollapse\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                the user collapses (closes) an expanded node in
                                                          the treeview.

  [onDeactivate\<TreeView.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                                the element loses the keyboard focus.

  [onDraw\<TreeView.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                          the window is about to be drawn.

  [onExpand\<TreeView.onExpand\>]{role="ref"} readonly    An event-handler callback function, called when
                                                          the user expands (opens) a collapsed node in
                                                          the treeview.

  [onShortcutKey\<TreeView.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                                the element\'s?shortcutKey?sequence is typed in
                                                          the active window.
  ------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
TreeView/items.rst TreeView/itemSize.rst TreeView/selection.rst
TreeView/active.rst TreeView/shortcutKey.rst TreeView/graphics.rst
TreeView/visible.rst TreeView/bounds.rst TreeView/location.rst
TreeView/maximumSize.rst TreeView/minimumSize.rst
TreeView/preferredSize.rst TreeView/size.rst TreeView/windowBounds.rst
TreeView/alignment.rst TreeView/children.rst TreeView/properties.rst
TreeView/enabled.rst TreeView/helpTip.rst TreeView/indent.rst
TreeView/parent.rst TreeView/window.rst TreeView/type.rst

TreeView/add.rst TreeView/find.rst TreeView/remove.rst
TreeView/removeAll.rst TreeView/notify.rst TreeView/show.rst
TreeView/hide.rst TreeView/addEventListener.rst
TreeView/removeEventListener.rst TreeView/dispatchEvent.rst

TreeView/onActivate.rst TreeView/onDeactivate.rst
TreeView/onCollapse.rst TreeView/onDraw.rst TreeView/onExpand.rst
TreeView/onChange.rst TreeView/onShortcutKey.rst
:::
:::
