.. _DropDownList.selection:

================================================
DropDownList.selection
================================================

   :ref:`ListItem` **selection**


Description
-----------

The currently selected  list item.

Setting this value causes the selected item to be highlighted and to be scrolled into view if necessary. If no items are selected, the value is null. Set to null to deselect all items.You can set the value using the index of an item, rather than an object reference. If set to an index value that is out of range, the operation is ignored. When set with an index value, the property still returns an object reference.