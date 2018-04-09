.. _TreeView:

================================================
TreeView
================================================


Description
-----------

A hierarchical list whose items can contain child items.

The?ListItem?children of this control (in the?items?array) can be of type node, which means that they can contain child items. An item with child items can expanded, so that the child items are displayed, or collapsed, so that the child items are hidden Individual items can be selected at any level of the tree.


Properties
^^^^^^^^^^

+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<TreeView.active>` readonly               | True if this element is active.                                                                                            |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<TreeView.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container. |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<TreeView.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                             |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<TreeView.children>` readonly           | An array of child elements.                                                                                                |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<TreeView.enabled>` readonly             | True if this element is enabled.                                                                                           |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<TreeView.graphics>` readonly           | The graphics object that can be used to customize the element's appearance, in response to the?onDraw()?event.             |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<TreeView.helpTip>` readonly             | The help text that is displayed when the mouse hovers over the element.                                                    |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<TreeView.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                        |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`itemSize<TreeView.itemSize>` readonly           | The width and height in pixels of each item in the list.                                                                   |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`items<TreeView.items>` readonly                 | The array of top-level items displayed in the list.                                                                        |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<TreeView.location>` readonly           | The upper left corner of this element relative to its parent.                                                              |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<TreeView.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                          |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<TreeView.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                          |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<TreeView.parent>` readonly               | The parent element.                                                                                                        |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<TreeView.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                   |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<TreeView.properties>` readonly       | An object that contains one or more creation properties of the control (properties used only when the element is created). |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`selection<TreeView.selection>` readonly         | The currently selected  list item.                                                                                         |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<TreeView.shortcutKey>` readonly     | The key sequence that invokes the?onShortcutKey()?callback for this element (in Windows only).                             |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<TreeView.size>` readonly                   | The current dimensions of this element.                                                                                    |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<TreeView.type>` readonly                   | The element type, "treeview".                                                                                              |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<TreeView.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                      |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<TreeView.window>` readonly               | The window that this element belongs to.                                                                                   |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<TreeView.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                        |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`add<TreeView.add>` readonly                                 | Adds an item to the top-level choices in this list.                                   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<TreeView.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this element.   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<TreeView.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                  |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`find<TreeView.find>` readonly                               | Retrieves an item object from the list that has a given text label.                   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<TreeView.hide>` readonly                               | Hides this element.                                                                   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<TreeView.notify>` readonly                           | Sends a notification message, simulating the specified user interaction event.        |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`remove<TreeView.remove>` readonly                           | Removes a child item from the list.                                                   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeAll<TreeView.removeAll>` readonly                     | Removes all child items from the list.                                                |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<TreeView.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this element. |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<TreeView.show>` readonly                               | Shows this element.                                                                   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onActivate<TreeView.onActivate>` readonly       | An event-handler callback function, called when the element acquires the keyboard focus.                          |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onChange<TreeView.onChange>` readonly           | An event-handler callback function, called when the content of the element has been changed                       |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onCollapse<TreeView.onCollapse>` readonly       | An event-handler callback function, called when the user collapses (closes) an expanded node in the treeview.     |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDeactivate<TreeView.onDeactivate>` readonly   | An event-handler callback function, called when the element loses the keyboard focus.                             |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDraw<TreeView.onDraw>` readonly               | An event-handler callback function, called when the window is about to be drawn.                                  |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onExpand<TreeView.onExpand>` readonly           | An event-handler callback function, called when the user expands (opens) a collapsed node in the treeview.        |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<TreeView.onShortcutKey>` readonly | An event-handler callback function, called when the element's?shortcutKey?sequence is typed in the active window. |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      TreeView/items.rst
      TreeView/itemSize.rst
      TreeView/selection.rst
      TreeView/active.rst
      TreeView/shortcutKey.rst
      TreeView/graphics.rst
      TreeView/visible.rst
      TreeView/bounds.rst
      TreeView/location.rst
      TreeView/maximumSize.rst
      TreeView/minimumSize.rst
      TreeView/preferredSize.rst
      TreeView/size.rst
      TreeView/windowBounds.rst
      TreeView/alignment.rst
      TreeView/children.rst
      TreeView/properties.rst
      TreeView/enabled.rst
      TreeView/helpTip.rst
      TreeView/indent.rst
      TreeView/parent.rst
      TreeView/window.rst
      TreeView/type.rst
      
      

      TreeView/add.rst
      TreeView/find.rst
      TreeView/remove.rst
      TreeView/removeAll.rst
      TreeView/notify.rst
      TreeView/show.rst
      TreeView/hide.rst
      TreeView/addEventListener.rst
      TreeView/removeEventListener.rst
      TreeView/dispatchEvent.rst
      
      
      TreeView/onActivate.rst
      TreeView/onDeactivate.rst
      TreeView/onCollapse.rst
      TreeView/onDraw.rst
      TreeView/onExpand.rst
      TreeView/onChange.rst
      TreeView/onShortcutKey.rst
      
      