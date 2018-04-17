.. _ListBox:

================================================
ListBox
================================================


Description
-----------

Displays a list of choices, represented by?ListItem?objects.

When you create the object, you specify whether it allows the user to select only one or multiple items. If a list contains more items than can be displayed in the available area, a scrollbar may appear that allows the user to scroll through all the list items.You can specify the items on creation of the list object, or afterward using the list object?s?add()?method. You can remove items programmatically with the list object?s?remove()?and?removeAll()?methods. You can create a list box with multiple columns; in this case, each row is a selectable choice, and each?ListItem?represents one row.


Properties
^^^^^^^^^^

+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<ListBox.active>` readonly               | True if this element is active.                                                                                                |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<ListBox.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.     |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<ListBox.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                                 |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<ListBox.children>` readonly           | An array of child?ListItem?elements.                                                                                           |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`columns<ListBox.columns>` readonly             | For a multi-column list box, the column properties.                                                                            |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<ListBox.enabled>` readonly             | True if this element is enabled.                                                                                               |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<ListBox.graphics>` readonly           | The graphics object that can be used to customize the element's appearance, in response to the?onDraw()?event.                 |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<ListBox.helpTip>` readonly             | The help text that is displayed when the mouse hovers over the element.                                                        |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<ListBox.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                            |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`itemSize<ListBox.itemSize>` readonly           | The width and height in pixels of each item in the list.                                                                       |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`items<ListBox.items>` readonly                 | The array of choice items displayed in the list.                                                                               |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<ListBox.location>` readonly           | The upper left corner of this element relative to its parent.                                                                  |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<ListBox.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                              |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<ListBox.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                              |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<ListBox.parent>` readonly               | The parent element.                                                                                                            |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<ListBox.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                       |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<ListBox.properties>` readonly       | An object that contains one or more creation properties of the control (properties used only when the element is created).     |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`selection<ListBox.selection>` readonly         | The currently selected item for a single-selection list, or an array of items for current selection in a multi-selection list. |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<ListBox.shortcutKey>` readonly     | The key sequence that invokes the?onShortcutKey()?callback for this element (in Windows only).                                 |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<ListBox.size>` readonly                   | The current dimensions of this element.                                                                                        |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<ListBox.type>` readonly                   | The element type; "listbox".                                                                                                   |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<ListBox.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                          |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<ListBox.window>` readonly               | The window that this element belongs to.                                                                                       |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<ListBox.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                            |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`add<ListBox.add>` readonly                                 | Adds an item to the choices in this list.                                             |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<ListBox.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this element.   |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<ListBox.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                  |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`find<ListBox.find>` readonly                               | Retrieves an item object from the list that has a given text label.                   |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<ListBox.hide>` readonly                               | Hides this element.                                                                   |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<ListBox.notify>` readonly                           | Sends a notification message, simulating the specified user interaction event.        |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`remove<ListBox.remove>` readonly                           | Removes a child item from the list.                                                   |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeAll<ListBox.removeAll>` readonly                     | Removes all child items from the list.                                                |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<ListBox.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this element. |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<ListBox.show>` readonly                               | Shows this element.                                                                   |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onActivate<ListBox.onActivate>` readonly       | An event-handler callback function, called when the element acquires the keyboard focus.                          |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onChange<ListBox.onChange>` readonly           | An event-handler callback function, called when the content of the element has been changed                       |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDeactivate<ListBox.onDeactivate>` readonly   | An event-handler callback function, called when the element loses the keyboard focus.                             |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDoubleClick<ListBox.onDoubleClick>` readonly | An event-handler callback function, called when an item in the listbox is double-clicked                          |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDraw<ListBox.onDraw>` readonly               | An event-handler callback function, called when the window is about to be drawn.                                  |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<ListBox.onShortcutKey>` readonly | An event-handler callback function, called when the element's?shortcutKey?sequence is typed in the active window. |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      ListBox/items.rst
      ListBox/itemSize.rst
      ListBox/selection.rst
      ListBox/active.rst
      ListBox/shortcutKey.rst
      ListBox/graphics.rst
      ListBox/visible.rst
      ListBox/bounds.rst
      ListBox/location.rst
      ListBox/maximumSize.rst
      ListBox/minimumSize.rst
      ListBox/preferredSize.rst
      ListBox/size.rst
      ListBox/windowBounds.rst
      ListBox/alignment.rst
      ListBox/children.rst
      ListBox/columns.rst
      ListBox/properties.rst
      ListBox/enabled.rst
      ListBox/helpTip.rst
      ListBox/indent.rst
      ListBox/parent.rst
      ListBox/window.rst
      ListBox/type.rst
      
      

      ListBox/add.rst
      ListBox/find.rst
      ListBox/remove.rst
      ListBox/removeAll.rst
      ListBox/notify.rst
      ListBox/show.rst
      ListBox/hide.rst
      ListBox/addEventListener.rst
      ListBox/removeEventListener.rst
      ListBox/dispatchEvent.rst
      
      
      ListBox/onActivate.rst
      ListBox/onDeactivate.rst
      ListBox/onChange.rst
      ListBox/onDoubleClick.rst
      ListBox/onShortcutKey.rst
      ListBox/onDraw.rst
      
      