.. _Progressbar:

================================================
Progressbar
================================================


Description
-----------

A horizontal bar with an indicator that shows the progress of an operation.

All progressbar controls have a horizontal orientation. The value property contains the current position of the progress indicator; the default is 0. There is a minvalue property, but it is always 0; attempts to set it to a different value are silently ignored.


Properties
^^^^^^^^^^

+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<Progressbar.alignment>`                | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.   |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<Progressbar.bounds>`                      | The boundaries of the element, in parent-relative coordinates.                                                               |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<Progressbar.children>` readonly         | An array of child elements.                                                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<Progressbar.enabled>`                    | True if this element is enabled.                                                                                             |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<Progressbar.graphics>` readonly         | The graphics object that can be used to customize the element's appearance, in response to the onDraw() event.               |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<Progressbar.helpTip>`                    | The help text that is displayed when the mouse hovers over the element.                                                      |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<Progressbar.indent>`                      | The number of pixels to indent the element during automatic layout.                                                          |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<Progressbar.location>`                  | The upper left corner of this element relative to its parent.                                                                |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<Progressbar.maximumSize>`            | The maximum height and width to which the element can be resized.                                                            |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maxvalue<Progressbar.maxvalue>`                  | The maximum value in the range. Default is 100.                                                                              |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<Progressbar.minimumSize>`            | The minimum height and width to which the element can be resized.                                                            |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minvalue<Progressbar.minvalue>`                  | The minimum value in the range; always 0. If set to a different value, it is ignored.                                        |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Progressbar.parent>` readonly             | The parent element.                                                                                                          |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<Progressbar.preferredSize>`        | The preferred size, used by layout managers to determine the best size for each element.                                     |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<Progressbar.properties>`              | An object that contains one or more creation properties of the container (properties used only when the element is created). |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<Progressbar.size>`                          | The current dimensions of this element.                                                                                      |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<Progressbar.type>` readonly                 | The element type, "progessbar".                                                                                              |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`value<Progressbar.value>`                        | The current position of the indicator.                                                                                       |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<Progressbar.visible>`                    | True if this element is shown, false if it is hidden.                                                                        |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<Progressbar.window>` readonly             | The window that this element belongs to.                                                                                     |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<Progressbar.windowBounds>` readonly | The bounds of this element relative to the top-level parent window.                                                          |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+-------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<Progressbar.addEventListener>`       | Registers an event handler for a particular type of event occuring in this element.   |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<Progressbar.dispatchEvent>`             | Simulates the occurrence of an event in this target.                                  |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<Progressbar.hide>`                               | Hides this element.                                                                   |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<Progressbar.removeEventListener>` | Unregisters an event handler for a particular type of event occuring in this element. |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<Progressbar.show>`                               | Shows this element.                                                                   |
+-------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+-----------------------------------+----------------------------------------------------------------------------------+
| :ref:`onDraw<Progressbar.onDraw>` | An event-handler callback function, called when the window is about to be drawn. |
+-----------------------------------+----------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Progressbar/value.rst
      Progressbar/minvalue.rst
      Progressbar/maxvalue.rst
      Progressbar/graphics.rst
      Progressbar/visible.rst
      Progressbar/bounds.rst
      Progressbar/location.rst
      Progressbar/maximumSize.rst
      Progressbar/minimumSize.rst
      Progressbar/preferredSize.rst
      Progressbar/size.rst
      Progressbar/windowBounds.rst
      Progressbar/alignment.rst
      Progressbar/children.rst
      Progressbar/properties.rst
      Progressbar/enabled.rst
      Progressbar/helpTip.rst
      Progressbar/indent.rst
      Progressbar/parent.rst
      Progressbar/window.rst
      Progressbar/type.rst
      
      

      Progressbar/show.rst
      Progressbar/hide.rst
      Progressbar/addEventListener.rst
      Progressbar/removeEventListener.rst
      Progressbar/dispatchEvent.rst
      
      
      Progressbar/onDraw.rst
      
      