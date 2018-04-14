SubPathItem {#SubPathItem}
===========

Description
-----------

Information about a path. You do not use the sub path item object to
create a path. Rather, you create path segments using the sub path info
object. Use the sub path item object to retrieve information about a
path. All properties are read-only.

### Properties

  ---------------------------------------------------- --------------------------------
  [closed\<SubPathItem.closed\>]{role="ref"} readonly  If true, the path is closed.

  [operation\<SubPathItem.operation\>]{role="ref"}     The sub path operation on other
  readonly                                             sub paths.

  [parent\<SubPathItem.parent\>]{role="ref"} readonly  The object\'s container.

  [pathPoints\<SubPathItem.pathPoints\>]{role="ref"}   The path points collection in
  readonly                                             the sub path.

  [typename\<SubPathItem.typename\>]{role="ref"}       The class name of the object.
  readonly                                             
  ---------------------------------------------------- --------------------------------

::: {.container .hide}
::: {.toctree}
SubPathItem/parent.rst SubPathItem/typename.rst SubPathItem/closed.rst
SubPathItem/operation.rst SubPathItem/pathPoints.rst
:::
:::
