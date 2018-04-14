ListBox.add {#ListBox.add}
===========

> [ListItem]{role="ref"} **add** ([String]{role="ref"} **type**,
> [String]{role="ref"} **text**)

Parameters
----------

  ---------- ---------------------------------------------------
  **type**   The type of the child element, the string \"item\".

  **text**   The localizable text label for the item.
  ---------- ---------------------------------------------------

Description
-----------

Adds an item to the choices in this list.

Returns the item control object. If this is a multi-column list box,
each added?ListItem?represents one selectable row.
Its?text?and?image?values specify the label in the first column, and
the?subitems?property specifies the labels in the additional columns.
