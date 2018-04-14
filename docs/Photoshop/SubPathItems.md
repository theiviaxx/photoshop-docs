SubPathItems {#SubPathItems}
============

Description
-----------

An array of path point info objects that describes a straight or curved
segment of a path. You do not use the sub path item object to create a
sub path. Rather, you use the sub path item object to retrieve
information about a sub path. To create sub paths, see sub path info.

### Properties

  ------------------------------------------------- -------------------------------
  [length\<SubPathItems.length\>]{role="ref"}       Number of elements in the
  readonly                                          collection.

  [parent\<SubPathItems.parent\>]{role="ref"}       The object\'s container.
  readonly                                          

  [typename\<SubPathItems.typename\>]{role="ref"}   The class name of the object.
  readonly                                          
  ------------------------------------------------- -------------------------------

### Methods

  --------------------------------------------------- ---------------------------------------
  [\[\]\<SubPathItems.\[\]\>]{role="ref"} readonly    Get an element in the collection with
                                                      the provided index.

  [getByName\<SubPathItems.getByName\>]{role="ref"}   Get the first element in the collection
  readonly                                            with the provided name.
  --------------------------------------------------- ---------------------------------------

::: {.container .hide}
::: {.toctree}
SubPathItems/parent.rst SubPathItems/typename.rst
SubPathItems/length.rst

SubPathItems/getByName.rst SubPathItems/\[\].rst
:::
:::
