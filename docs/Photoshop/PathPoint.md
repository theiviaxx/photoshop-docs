PathPoint {#PathPoint}
=========

Description
-----------

Information about an array of path point info objects. You do not use
the path point object to create points that make up a path. Rather, you
use the path point object to retrieve information about the points that
describe path segments. To create path points, use the path point info
object.

### Properties

  ---------------------------------------------------------- -------------------------------------
  [anchor\<PathPoint.anchor\>]{role="ref"} readonly          The position (coordinates) of the
                                                             anchor point.

  [kind\<PathPoint.kind\>]{role="ref"} readonly              The type of point.

  [leftDirection\<PathPoint.leftDirection\>]{role="ref"}     The location of the left direction
  readonly                                                   point (the \"in\" position).

  [parent\<PathPoint.parent\>]{role="ref"} readonly          The object\'s container.

  [rightDirection\<PathPoint.rightDirection\>]{role="ref"}   The location of the right direction
  readonly                                                   point (the \"out\" position).

  [typename\<PathPoint.typename\>]{role="ref"} readonly      The class name of the object.
  ---------------------------------------------------------- -------------------------------------

::: {.container .hide}
::: {.toctree}
PathPoint/parent.rst PathPoint/typename.rst PathPoint/anchor.rst
PathPoint/leftDirection.rst PathPoint/rightDirection.rst
PathPoint/kind.rst
:::
:::
