.. _Panel:

================================================
Panel
================================================


Description
-----------

A container for other types of controls, with an optional frame.

A panel can specify layout options for its child elements. Hiding a panel hides all its children. Making it visible makes visible those children that are not individually hidden.


Properties
^^^^^^^^^^

+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignChildren<Panel.alignChildren>`        | Specifies how to align the child elements.                                                                                 |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<Panel.alignment>`                | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container. |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<Panel.bounds>`                      | The boundaries of the element, in parent-relative coordinates.                                                             |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`characters<Panel.characters>`              | Reserve space for the specified number of characters; affects calculation of preferredSize .                               |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<Panel.children>` readonly         | An array of child elements.                                                                                                |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<Panel.enabled>`                    | True if this element is enabled.                                                                                           |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<Panel.graphics>` readonly         | The graphics object that can be used to customize the element's appearance, in response to the onDraw() event.             |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<Panel.helpTip>`                    | The help text that is displayed when the mouse hovers over the element.                                                    |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<Panel.indent>`                      | The number of pixels to indent the element during automatic layout.                                                        |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`justify<Panel.justify>`                    | The default text justification style for child text elements.                                                              |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`layout<Panel.layout>`                      | The layout manager for this container.                                                                                     |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<Panel.location>`                  | The upper left corner of this element's frame relative to its parent.                                                      |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`margins<Panel.margins>`                    | The number of pixels between the edges of a container and the outermost child elements.                                    |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<Panel.maximumSize>`            | The maximum height and width to which the element can be resized.                                                          |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<Panel.minimumSize>`            | The minimum height and width to which the element can be resized.                                                          |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`orientation<Panel.orientation>`            | The layout orientation of children in a container.                                                                         |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Panel.parent>` readonly             | The parent element.                                                                                                        |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<Panel.preferredSize>`        | The preferred size, used by layout managers to determine the best size for each element.                                   |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<Panel.properties>`              | An object that contains one or more creation properties of the control (properties used only when the element is created). |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<Panel.size>`                          | The current dimensions of this element.                                                                                    |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`spacing<Panel.spacing>`                    | The number of pixels separating one child element from its adjacent sibling element.                                       |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`text<Panel.text>`                          | The title or label text, a localizable string.                                                                             |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<Panel.type>` readonly                 | The element type; "panel".                                                                                                 |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<Panel.visible>`                    | True if this element is shown, false if it is hidden.                                                                      |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<Panel.window>` readonly             | The window that this element belongs to.                                                                                   |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<Panel.windowBounds>` readonly | The bounds of this element relative to the top-level parent window.                                                        |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`add<Panel.add>`                                 | Adds a child element to this container.                                               |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<Panel.addEventListener>`       | Registers an event handler for a particular type of event occuring in this element.   |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<Panel.dispatchEvent>`             | Simulates the occurrence of an event in this target.                                  |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<Panel.hide>`                               | Hides this element.                                                                   |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`remove<Panel.remove>`                           | Removes the specified child control from this group's children array.                 |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<Panel.removeEventListener>` | Unregisters an event handler for a particular type of event occuring in this element. |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<Panel.show>`                               | Shows this element.                                                                   |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+-----------------------------+---------------------------------------------------------------------------------+
| :ref:`onDraw<Panel.onDraw>` | An event-handler callback function, called when the panel is about to be drawn. |
+-----------------------------+---------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Panel/characters.rst
      Panel/justify.rst
      Panel/text.rst
      Panel/graphics.rst
      Panel/visible.rst
      Panel/bounds.rst
      Panel/location.rst
      Panel/maximumSize.rst
      Panel/minimumSize.rst
      Panel/preferredSize.rst
      Panel/size.rst
      Panel/windowBounds.rst
      Panel/alignChildren.rst
      Panel/children.rst
      Panel/layout.rst
      Panel/margins.rst
      Panel/orientation.rst
      Panel/spacing.rst
      Panel/alignment.rst
      Panel/properties.rst
      Panel/enabled.rst
      Panel/helpTip.rst
      Panel/indent.rst
      Panel/parent.rst
      Panel/window.rst
      Panel/type.rst
      
      

      Panel/show.rst
      Panel/hide.rst
      Panel/add.rst
      Panel/remove.rst
      Panel/addEventListener.rst
      Panel/removeEventListener.rst
      Panel/dispatchEvent.rst
      
      
      Panel/onDraw.rst
      
      