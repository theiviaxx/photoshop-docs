.. _ListBox.preferredSize:

================================================
ListBox.preferredSize
================================================

   :ref:`Dimension` **preferredSize**


Description
-----------

The preferred size, used by layout managers to determine the best size for each element.

If not explicitly set by a script, value is established by the UI framework in which ScriptUI is employed, and is based on such attributes of the element as its text, font, font size, icon size, and other UI framework-specific attributes.A script can explicitly set this value before the layout manager is invoked in order to establish an element size other than the default.