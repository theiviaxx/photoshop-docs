.. _DropDownList.size:

================================================
DropDownList.size
================================================

   :ref:`Dimension` **size**


Description
-----------

The current dimensions of this element.

Initially undefined, and unless explicitly set by a script, it is defined by a LayoutManager . A script can explicitly set size before the layout manager is invoked to establish an element size other than the preferredSize or the default size, but this is not recommended. Defined as [bounds.width, bounds.height]. Setting an element's size changes its bounds property, and vice-versa.