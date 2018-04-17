.. _ListBox.selection:

================================================
ListBox.selection
================================================

   :ref:`ListItem` **selection**


Description
-----------

The currently selected item for a single-selection list, or an array of items for current selection in a multi-selection list.

Setting this value causes the selected item to be highlighted and to be scrolled into view if necessary. If no items are selected, the value is null. Set to null to deselect all items. You can set the value using the index of an item or an array of indices, rather than object references. If set to an index value that is out of range, the operation is ignored. When set with index values, the property still returns object references.             If you set the value to an array for a single-selection list, only the first item in the array is selected.             If you set the value to a single item for a multi-selection list, that item is added to the current selection.