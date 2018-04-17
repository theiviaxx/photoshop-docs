.. _ListBox.properties:

================================================
ListBox.properties
================================================

   :ref:`Object` **properties**


Description
-----------

An object that contains one or more creation properties of the control (properties used only when the element is created).

Creation properties of a ListBox object can include:                            multiselect: When false (the default), only one item can be selected. When true, multiple items can be selected.                                         items: An array of strings for the text of each list item. An item object is created for each item. An item with the text string "-" creates a separator item. Supply this property, or the items argument to the?add()?method, not both. This form is most useful for elements defined using Resource Specifications.                                         numberOfColumns: A number of columns in which to display the items; default is 1. When there are multiple columns, each?ListItem?object represents a selectable row. Its?text?and?image?values specify the label in the first column, and the?subitems?property specifies the labels in the additional columns.                                         showHeaders: True to display column titles.                                         columnWidths: An array of numbers for the preferred width in pixels of each column.                                         columnTitles: A corresponding array of strings for the title of each column, to be shown if showHeaders is true.