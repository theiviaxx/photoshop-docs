.. _Scrollbar:

================================================
Scrollbar
================================================


Description
-----------

A scrollbar with a draggable scroll indicator and stepper buttons to move the indicator.

The scrollbar control has a horizontal orientation if the width is greater than the height at creation time, or vertical if its height is greater than its width.         Calls the?onChange()?callback after the position of the indicator is changed or if its?notify()?method is called. Calls the?onChanging()?callback repeatedly while the user is moving the indicator. Scrollbars are often created with an associated?EditText?field to display the current value of the scrollbar, and to allow setting the scrollbar's position to a specific value.


Properties
^^^^^^^^^^

+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<Scrollbar.active>` readonly               | True if this element is active.                                                                                                  |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<Scrollbar.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.       |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<Scrollbar.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                                   |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<Scrollbar.children>` readonly           | An array of child elements.                                                                                                      |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<Scrollbar.enabled>` readonly             | True if this element is enabled.                                                                                                 |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<Scrollbar.graphics>` readonly           | The graphics object that can be used to customize the element's appearance, in response to the?onDraw()?event.                   |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<Scrollbar.helpTip>` readonly             | The help text that is displayed when the mouse hovers over the element.                                                          |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<Scrollbar.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                              |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`jumpdelta<Scrollbar.jumpdelta>` readonly         | The amount to increment or decrement a scrollbar indicator's position when the user clicks ahead or behind the moveable element. |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<Scrollbar.location>` readonly           | The upper left corner of this element relative to its parent.                                                                    |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<Scrollbar.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                                |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maxvalue<Scrollbar.maxvalue>` readonly           | The maximum value allowed in the value property.                                                                                 |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<Scrollbar.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                                |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minvalue<Scrollbar.minvalue>` readonly           | The minimum value allowed in the value property.                                                                                 |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Scrollbar.parent>` readonly               | The parent element.                                                                                                              |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<Scrollbar.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                         |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<Scrollbar.properties>` readonly       | An object that contains one or more creation properties of the container (properties used only when the element is created).     |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<Scrollbar.shortcutKey>` readonly     | The key sequence that invokes the ?onShortcutKey()?callback for this element (in Windows only).                                  |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<Scrollbar.size>` readonly                   | The current dimensions of this element.                                                                                          |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`stepdelta<Scrollbar.stepdelta>` readonly         | The amount by which to increment or decrement a scrollbar element's position when the user clicks a stepper button.              |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<Scrollbar.type>` readonly                   | The element type, "scrollbar".                                                                                                   |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`value<Scrollbar.value>` readonly                 | The current position of the indicator.                                                                                           |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<Scrollbar.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                            |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<Scrollbar.window>` readonly               | The window that this element belongs to.                                                                                         |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<Scrollbar.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                              |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<Scrollbar.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this element.   |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<Scrollbar.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                  |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<Scrollbar.hide>` readonly                               | Hides this element.                                                                   |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<Scrollbar.notify>` readonly                           | Sends a notification message, simulating the specified user interaction event.        |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<Scrollbar.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this element. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<Scrollbar.show>` readonly                               | Shows this element.                                                                   |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onActivate<Scrollbar.onActivate>` readonly       | An event-handler callback function, called when the element acquires the keyboard focus.                                           |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onChange<Scrollbar.onChange>` readonly           | An event-handler callback function, called when the user has finished dragging the position indicator, or has clicked the control. |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onChanging<Scrollbar.onChanging>` readonly       | An event-handler callback function, called when the content of the element is in the process of changing                           |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onDeactivate<Scrollbar.onDeactivate>` readonly   | An event-handler callback function, called when the element loses the keyboard focus.                                              |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onDraw<Scrollbar.onDraw>` readonly               | An event-handler callback function, called when the window is about to be drawn.                                                   |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<Scrollbar.onShortcutKey>` readonly | An event-handler callback function, called when the element's?shortcutKey?sequence is typed in the active window.                  |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Scrollbar/stepdelta.rst
      Scrollbar/jumpdelta.rst
      Scrollbar/value.rst
      Scrollbar/minvalue.rst
      Scrollbar/maxvalue.rst
      Scrollbar/active.rst
      Scrollbar/shortcutKey.rst
      Scrollbar/graphics.rst
      Scrollbar/visible.rst
      Scrollbar/bounds.rst
      Scrollbar/location.rst
      Scrollbar/maximumSize.rst
      Scrollbar/minimumSize.rst
      Scrollbar/preferredSize.rst
      Scrollbar/size.rst
      Scrollbar/windowBounds.rst
      Scrollbar/alignment.rst
      Scrollbar/children.rst
      Scrollbar/properties.rst
      Scrollbar/enabled.rst
      Scrollbar/helpTip.rst
      Scrollbar/indent.rst
      Scrollbar/parent.rst
      Scrollbar/window.rst
      Scrollbar/type.rst
      
      

      Scrollbar/notify.rst
      Scrollbar/show.rst
      Scrollbar/hide.rst
      Scrollbar/addEventListener.rst
      Scrollbar/removeEventListener.rst
      Scrollbar/dispatchEvent.rst
      
      
      Scrollbar/onActivate.rst
      Scrollbar/onDeactivate.rst
      Scrollbar/onDraw.rst
      Scrollbar/onChanging.rst
      Scrollbar/onChange.rst
      Scrollbar/onShortcutKey.rst
      
      