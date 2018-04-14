ListItem {#ListItem}
========

Description
-----------

An item in a list box, drop-down list, or tree view.

You can specify initial items in the creation parameters when creating
the parent list. Create new items using the add() method (ListBox.add(),
DropDownList.add(), TreeView.add()) in the parent list with control
type=\"item\", or, for?DropDownList?controls, type=\"separator\".For a
multi-column list box, the object represents one selectable row.
Its?text?and?image?values specify the label in the first column, and
the?subitems?property specifies the labels in the additional columns.

### Properties

  ------------------------------------------------- --------------------------------------------------
  [checked\<ListItem.checked\>]{role="ref"}         The checked state of an item in a list.
  readonly                                          

  [expanded\<ListItem.expanded\>]{role="ref"}       The expansion state of an item of type node that
  readonly                                          is a child of a?TreeView?list control.

  [image\<ListItem.image\>]{role="ref"} readonly    An image object for an icon to display in the
                                                    item.

  [index\<ListItem.index\>]{role="ref"} readonly    The 0-based index of this item in the items
                                                    collection of its parent list control.

  [parent\<ListItem.parent\>]{role="ref"} readonly  The parent element, a list control.

  [properties\<ListItem.properties\>]{role="ref"}   An object that contains one or more creation
  readonly                                          properties of the item (properties used only when
                                                    the element is created).

  [selected\<ListItem.selected\>]{role="ref"}       The selection state of this item.
  readonly                                          

  [subItems\<ListItem.subItems\>]{role="ref"}       When the parent is a multi-column?ListBox, this
  readonly                                          describes the labels for this selectable row in
                                                    additional columns.

  [text\<ListItem.text\>]{role="ref"} readonly      The label text to display for the item, a
                                                    localizable string.

  [type\<ListItem.type\>]{role="ref"} readonly      The element type.
  ------------------------------------------------- --------------------------------------------------

::: {.container .hide}
::: {.toctree}
ListItem/checked.rst ListItem/expanded.rst ListItem/index.rst
ListItem/selected.rst ListItem/image.rst ListItem/text.rst
ListItem/subItems.rst ListItem/properties.rst ListItem/parent.rst
ListItem/type.rst
:::
:::
