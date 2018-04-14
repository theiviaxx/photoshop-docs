PathPointInfo {#PathPointInfo}
=============

Description
-----------

A point on a path, expressed as an array of three coordinate arrays: the
anchor point, left direction point, and right direction point. For paths
that are straight segments (not curved), the coordinates of all three
points are the same. For curved segements, the coordinates are
different. The difference between the anchor point and the left or right
direction points determines the arc of the curve. You use the left
direction point to bend the curve \"outward\" or make it convex; you use
the right direction point to bend the curve \"inward\" or make it
concave.

### Properties

  -------------------------------------------------------------- -----------------------------------
  [anchor\<PathPointInfo.anchor\>]{role="ref"} readonly          The x and y coordinates of one end
                                                                 point of the path segment.

  [kind\<PathPointInfo.kind\>]{role="ref"} readonly              The point type.

  [leftDirection\<PathPointInfo.leftDirection\>]{role="ref"}     The location of the left direction
  readonly                                                       point (\"in\" position).

  [rightDirection\<PathPointInfo.rightDirection\>]{role="ref"}   The location of the right direction
  readonly                                                       point (\"out\" position).
  -------------------------------------------------------------- -----------------------------------

### Static Properties

  -------------------------------------------------------------- -----------------------------------
  [anchor\<PathPointInfo.anchor\>]{role="ref"} readonly          The x and y coordinates of one end
                                                                 point of the path segment.

  [kind\<PathPointInfo.kind\>]{role="ref"} readonly              The point type.

  [leftDirection\<PathPointInfo.leftDirection\>]{role="ref"}     The location of the left direction
  readonly                                                       point (\"in\" position).

  [rightDirection\<PathPointInfo.rightDirection\>]{role="ref"}   The location of the right direction
  readonly                                                       point (\"out\" position).
  -------------------------------------------------------------- -----------------------------------

::: {.container .hide}
::: {.toctree}
PathPointInfo/anchor.rst PathPointInfo/leftDirection.rst
PathPointInfo/rightDirection.rst PathPointInfo/kind.rst

PathPointInfo/anchor.rst PathPointInfo/leftDirection.rst
PathPointInfo/rightDirection.rst PathPointInfo/kind.rst
:::
:::
