.. _Button:

================================================
Button
================================================


Description
-----------

A pushbutton element containing a mouse-sensitive text string.

Calls the?onClick()?callback if the control is clicked or if its?notify()?method is called.


Properties
^^^^^^^^^^

+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<Button.active>` readonly               | True if this element is active.                                                                                              |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<Button.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.   |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<Button.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`characters<Button.characters>` readonly       | A number of characters for which to reserve space when calculating the preferred size of the element.                        |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<Button.children>` readonly           | An array of child elements.                                                                                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<Button.enabled>` readonly             | True if this element is enabled.                                                                                             |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<Button.graphics>` readonly           | The graphics object that can be used to customize the element's appearance, in response to the?onDraw()?event.               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<Button.helpTip>` readonly             | The help string that is displayed when the mouse hovers over the element.                                                    |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<Button.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                          |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`justify<Button.justify>` readonly             | The text justification style.                                                                                                |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<Button.location>` readonly           | The upper left corner of this element relative to its parent.                                                                |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<Button.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                            |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<Button.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                            |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Button.parent>` readonly               | The parent element.                                                                                                          |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<Button.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                     |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<Button.properties>` readonly       | An object that contains one or more creation properties of the container (properties used only when the element is created). |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<Button.shortcutKey>` readonly     | The key sequence that invokes the?onShortcutKey()?callback for this element (in Windows only).                               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<Button.size>` readonly                   | The current dimensions of this element.                                                                                      |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`text<Button.text>` readonly                   | The text to display, a localizable string.                                                                                   |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<Button.type>` readonly                   | The element type; "button".                                                                                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<Button.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<Button.window>` readonly               | The window that this element belongs to.                                                                                     |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<Button.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                          |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<Button.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this element.   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<Button.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                  |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<Button.hide>` readonly                               | Hides this element.                                                                   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<Button.notify>` readonly                           | Sends a notification message, simulating the specified user interaction event.        |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<Button.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this element. |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<Button.show>` readonly                               | Shows this element.                                                                   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onActivate<Button.onActivate>` readonly       | An event-handler callback function, called when the element acquires the keyboard focus.                          |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onClick<Button.onClick>` readonly             | An event-handler callback function, called when the element has been clicked                                      |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDeactivate<Button.onDeactivate>` readonly   | An event-handler callback function, called when the element loses the keyboard focus.                             |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDraw<Button.onDraw>` readonly               | An event-handler callback function, called when the window is about to be drawn.                                  |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<Button.onShortcutKey>` readonly | An event-handler callback function, called when the element's shortcutKey sequence is typed in the active window. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Button/characters.rst
      Button/justify.rst
      Button/text.rst
      Button/active.rst
      Button/shortcutKey.rst
      Button/graphics.rst
      Button/visible.rst
      Button/bounds.rst
      Button/location.rst
      Button/maximumSize.rst
      Button/minimumSize.rst
      Button/preferredSize.rst
      Button/size.rst
      Button/windowBounds.rst
      Button/alignment.rst
      Button/children.rst
      Button/properties.rst
      Button/enabled.rst
      Button/helpTip.rst
      Button/indent.rst
      Button/parent.rst
      Button/window.rst
      Button/type.rst
      
      

      Button/notify.rst
      Button/show.rst
      Button/hide.rst
      Button/addEventListener.rst
      Button/removeEventListener.rst
      Button/dispatchEvent.rst
      
      
      Button/onActivate.rst
      Button/onDeactivate.rst
      Button/onDraw.rst
      Button/onClick.rst
      Button/onShortcutKey.rst
      
      