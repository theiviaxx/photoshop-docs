.. _Group:

================================================
Group
================================================


Description
-----------

A container for other controls within a window.

A group can specify layout options for its child elements. Hiding a group hides all its children. Making it visible makes visible those children that are not individually hidden.


Properties
^^^^^^^^^^

+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignChildren<Group.alignChildren>` readonly | Tells the layout manager how unlike-sized children of this container should be aligned within a column or row.             |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<Group.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container. |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<Group.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                             |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<Group.children>` readonly           | An array of child elements.                                                                                                |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<Group.enabled>` readonly             | True if this element is enabled.                                                                                           |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<Group.graphics>` readonly           | The graphics object that can be used to customize the element's appearance, in response to the?onDraw()?event.             |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<Group.helpTip>` readonly             | The help text that is displayed when the mouse hovers over the element.                                                    |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<Group.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                        |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`layout<Group.layout>` readonly               | The layout manager for this container.                                                                                     |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<Group.location>` readonly           | The upper left corner of this element relative to its parent.                                                              |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`margins<Group.margins>` readonly             | The number of pixels between the edges of a container and the outermost child elements.                                    |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<Group.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                          |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<Group.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                          |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`orientation<Group.orientation>` readonly     | The layout orientation of children in a container.                                                                         |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Group.parent>` readonly               | The parent element.                                                                                                        |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<Group.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                   |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<Group.properties>` readonly       | An object that contains one or more creation properties of the control (properties used only when the element is created). |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<Group.size>` readonly                   | The current dimensions of this element.                                                                                    |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`spacing<Group.spacing>` readonly             | The number of pixels separating one child element from its adjacent sibling element.                                       |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<Group.type>` readonly                   | The element type; "group".                                                                                                 |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<Group.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                      |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<Group.window>` readonly               | The window that this element belongs to.                                                                                   |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<Group.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                        |
+----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`add<Group.add>` readonly                                 | Adds a child element to this container.                                               |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<Group.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this element.   |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<Group.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                  |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<Group.hide>` readonly                               | Hides this element.                                                                   |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`remove<Group.remove>` readonly                           | Removes the specified child control from this group's?children?array.                 |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<Group.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this element. |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<Group.show>` readonly                               | Shows this element.                                                                   |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+--------------------------------------+---------------------------------------------------------------------------------+
| :ref:`onDraw<Group.onDraw>` readonly | An event-handler callback function, called when the group is about to be drawn. |
+--------------------------------------+---------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Group/graphics.rst
      Group/visible.rst
      Group/bounds.rst
      Group/location.rst
      Group/maximumSize.rst
      Group/minimumSize.rst
      Group/preferredSize.rst
      Group/size.rst
      Group/windowBounds.rst
      Group/alignChildren.rst
      Group/children.rst
      Group/layout.rst
      Group/margins.rst
      Group/orientation.rst
      Group/spacing.rst
      Group/alignment.rst
      Group/properties.rst
      Group/enabled.rst
      Group/helpTip.rst
      Group/indent.rst
      Group/parent.rst
      Group/window.rst
      Group/type.rst
      
      

      Group/show.rst
      Group/hide.rst
      Group/add.rst
      Group/remove.rst
      Group/addEventListener.rst
      Group/removeEventListener.rst
      Group/dispatchEvent.rst
      
      
      Group/onDraw.rst
      
      