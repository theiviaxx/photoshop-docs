.. _ListItem:

================================================
ListItem
================================================


Description
-----------

An item in a list box, drop-down list, or tree view.

You can specify initial items in the creation parameters when creating the parent list. Create new items using the add() method (ListBox.add(), DropDownList.add(), TreeView.add()) in the parent list with control type="item", or, for?DropDownList?controls, type="separator".For a multi-column list box, the object represents one selectable row. Its?text?and?image?values specify the label in the first column, and the?subitems?property specifies the labels in the additional columns.


Properties
^^^^^^^^^^

+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`checked<ListItem.checked>` readonly       | The checked state of an item in a list.                                                                                 |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`expanded<ListItem.expanded>` readonly     | The expansion state of an item of type node that is a child of a?TreeView?list control.                                 |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`image<ListItem.image>` readonly           | An image object for an icon to display in the item.                                                                     |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`index<ListItem.index>` readonly           | The 0-based index of this item in the items collection of its parent list control.                                      |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<ListItem.parent>` readonly         | The parent element, a list control.                                                                                     |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<ListItem.properties>` readonly | An object that contains one or more creation properties of the item (properties used only when the element is created). |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`selected<ListItem.selected>` readonly     | The selection state of this item.                                                                                       |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`subItems<ListItem.subItems>` readonly     | When the parent is a multi-column?ListBox, this describes the labels for this selectable row in additional columns.     |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`text<ListItem.text>` readonly             | The label text to display for the item, a localizable string.                                                           |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<ListItem.type>` readonly             | The element type.                                                                                                       |
+-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+














.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      ListItem/checked.rst
      ListItem/expanded.rst
      ListItem/index.rst
      ListItem/selected.rst
      ListItem/image.rst
      ListItem/text.rst
      ListItem/subItems.rst
      ListItem/properties.rst
      ListItem/parent.rst
      ListItem/type.rst
      
      

      
      
      
      