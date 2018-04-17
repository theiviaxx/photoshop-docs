.. _Slider:

================================================
Slider
================================================


Description
-----------

A slider bar that indicates a numeric value with a moveable position indicator.

All slider controls have a horizontal orientation. Calls the?onChange()?callback after the position of the indicator is changed or if its?notify()?method is called. Calls the?onChanging()?callback repeatedly while the user is moving the indicator. The?value?property contains the current position of the indicator within the range of?minvalue?to?maxvalue.


Properties
^^^^^^^^^^

+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<Slider.active>` readonly               | True if this element is active.                                                                                              |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<Slider.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.   |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<Slider.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<Slider.children>` readonly           | An array of child elements.                                                                                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<Slider.enabled>` readonly             | True if this element is enabled.                                                                                             |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<Slider.graphics>` readonly           | The graphics object that can be used to customize the element's appearance, in response to the?onDraw()?event.               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<Slider.helpTip>` readonly             | The help text that is displayed when the mouse hovers over the element.                                                      |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<Slider.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                          |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<Slider.location>` readonly           | The upper left corner of this element relative to its parent.                                                                |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<Slider.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                            |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maxvalue<Slider.maxvalue>` readonly           | The maximum value allowed in the?value?property.                                                                             |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<Slider.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                            |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minvalue<Slider.minvalue>` readonly           | The minimum value allowed in the?value?property.                                                                             |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Slider.parent>` readonly               | The parent element.                                                                                                          |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<Slider.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                     |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<Slider.properties>` readonly       | An object that contains one or more creation properties of the container (properties used only when the element is created). |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<Slider.shortcutKey>` readonly     | The key sequence that invokes the?onShortcutKey()?callback for this element (in Windows only).                               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<Slider.size>` readonly                   | The current dimensions of this element.                                                                                      |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<Slider.type>` readonly                   | The element type, "slider".                                                                                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`value<Slider.value>` readonly                 | The current position of the indicator.                                                                                       |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<Slider.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<Slider.window>` readonly               | The window that this element belongs to.                                                                                     |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<Slider.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                          |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<Slider.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this element.   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<Slider.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                  |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<Slider.hide>` readonly                               | Hides this element.                                                                   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<Slider.notify>` readonly                           | Sends a notification message, simulating the specified user interaction event.        |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<Slider.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this element. |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<Slider.show>` readonly                               | Shows this element.                                                                   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onActivate<Slider.onActivate>` readonly       | An event-handler callback function, called when the element acquires the keyboard focus.                                           |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onChange<Slider.onChange>` readonly           | An event-handler callback function, called when the user has finished dragging the position indicator, or has clicked the control. |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onChanging<Slider.onChanging>` readonly       | An event-handler callback function, called when the content of the element is in the process of changing                           |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onDeactivate<Slider.onDeactivate>` readonly   | An event-handler callback function, called when the element loses the keyboard focus.                                              |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onDraw<Slider.onDraw>` readonly               | An event-handler callback function, called when the window is about to be drawn.                                                   |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<Slider.onShortcutKey>` readonly | An event-handler callback function, called when the element's?shortcutKey?sequence is typed in the active window.                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Slider/value.rst
      Slider/minvalue.rst
      Slider/maxvalue.rst
      Slider/active.rst
      Slider/shortcutKey.rst
      Slider/graphics.rst
      Slider/visible.rst
      Slider/bounds.rst
      Slider/location.rst
      Slider/maximumSize.rst
      Slider/minimumSize.rst
      Slider/preferredSize.rst
      Slider/size.rst
      Slider/windowBounds.rst
      Slider/alignment.rst
      Slider/children.rst
      Slider/properties.rst
      Slider/enabled.rst
      Slider/helpTip.rst
      Slider/indent.rst
      Slider/parent.rst
      Slider/window.rst
      Slider/type.rst
      
      

      Slider/notify.rst
      Slider/show.rst
      Slider/hide.rst
      Slider/addEventListener.rst
      Slider/removeEventListener.rst
      Slider/dispatchEvent.rst
      
      
      Slider/onActivate.rst
      Slider/onDeactivate.rst
      Slider/onDraw.rst
      Slider/onChanging.rst
      Slider/onChange.rst
      Slider/onShortcutKey.rst
      
      