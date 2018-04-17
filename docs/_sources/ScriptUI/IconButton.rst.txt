.. _IconButton:

================================================
IconButton
================================================


Description
-----------

A  mouse-sensitive pushbutton that displays an image instead of text.

Calls the?onClick()?callback if the control is clicked or if its?notify()?method is called.


Properties
^^^^^^^^^^

+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<IconButton.active>` readonly               | True if this element is active.                                                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<IconButton.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.   |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<IconButton.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                               |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<IconButton.children>` readonly           | An array of child elements.                                                                                                  |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<IconButton.enabled>` readonly             | True if this element is enabled.                                                                                             |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<IconButton.graphics>` readonly           | The graphics object that can be used to customize the element's appearance, in response to the?onDraw()?event.               |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<IconButton.helpTip>` readonly             | The help text that is displayed when the mouse hovers over the element.                                                      |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`image<IconButton.image>` readonly                 | The image object that defines the image to be drawn.                                                                         |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<IconButton.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<IconButton.location>` readonly           | The upper left corner of this element relative to its parent.                                                                |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<IconButton.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                            |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<IconButton.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                            |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<IconButton.parent>` readonly               | The parent element.                                                                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<IconButton.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                     |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<IconButton.properties>` readonly       | An object that contains one or more creation properties of the container (properties used only when the element is created). |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<IconButton.shortcutKey>` readonly     | The key sequence that invokes the?onShortcutKey()?callback for this element (in Windows only).                               |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<IconButton.size>` readonly                   | The current dimensions of this element.                                                                                      |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<IconButton.type>` readonly                   | The element type; "iconbutton".                                                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<IconButton.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<IconButton.window>` readonly               | The window that this element belongs to.                                                                                     |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<IconButton.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+---------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<IconButton.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this element.   |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<IconButton.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                  |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<IconButton.hide>` readonly                               | Hides this element.                                                                   |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<IconButton.notify>` readonly                           | Sends a notification message, simulating the specified user interaction event.        |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<IconButton.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this element. |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<IconButton.show>` readonly                               | Shows this element.                                                                   |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onActivate<IconButton.onActivate>` readonly       | An event-handler callback function, called when the element acquires the keyboard focus.                          |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onClick<IconButton.onClick>` readonly             | An event-handler callback function, called when the element has been clicked.                                     |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDeactivate<IconButton.onDeactivate>` readonly   | An event-handler callback function, called when the element loses the keyboard focus.                             |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDraw<IconButton.onDraw>` readonly               | An event-handler callback function, called when the window is about to be drawn.                                  |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<IconButton.onShortcutKey>` readonly | An event-handler callback function, called when the element's shortcutKey sequence is typed in the active window. |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      IconButton/image.rst
      IconButton/active.rst
      IconButton/shortcutKey.rst
      IconButton/graphics.rst
      IconButton/visible.rst
      IconButton/bounds.rst
      IconButton/location.rst
      IconButton/maximumSize.rst
      IconButton/minimumSize.rst
      IconButton/preferredSize.rst
      IconButton/size.rst
      IconButton/windowBounds.rst
      IconButton/alignment.rst
      IconButton/children.rst
      IconButton/properties.rst
      IconButton/enabled.rst
      IconButton/helpTip.rst
      IconButton/indent.rst
      IconButton/parent.rst
      IconButton/window.rst
      IconButton/type.rst
      
      

      IconButton/notify.rst
      IconButton/show.rst
      IconButton/hide.rst
      IconButton/addEventListener.rst
      IconButton/removeEventListener.rst
      IconButton/dispatchEvent.rst
      
      
      IconButton/onActivate.rst
      IconButton/onDeactivate.rst
      IconButton/onDraw.rst
      IconButton/onClick.rst
      IconButton/onShortcutKey.rst
      
      