.. _DropDownList.items:

================================================
DropDownList.items
================================================

   :ref:`ListItem` **items**


Description
-----------

The array of choice items displayed in the drop-down or pop-up list.

Access this array with a 0-based index. To obtain the number of items in the list, use items.length.The objects are created when items are specified on creation of the parent list object, or afterward using the list control?s?add()?method. Items in a drop-down list can be of type separator, in which case they cannot be selected, and are shown as a horizontal line. Each item has a?selected?property that is true when it is in the selected state.