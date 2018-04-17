.. _Window:

================================================
Window
================================================


Description
-----------

The instance represents a top-level window or dialog box, which contains user-interface elements.

The globally available?Window?object provides access to predefined and script-defined windows.


Properties
^^^^^^^^^^

+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<Window.active>` readonly                 | Set to true to make this window active.                                                                                                     |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignChildren<Window.alignChildren>` readonly   | Tells the layout manager how unlike-sized children of this container should be aligned within a column or row.                              |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<Window.alignment>` readonly           | The alignment style for child elements of a container. If defined, this value overrides the alignChildren setting for the parent container. |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<Window.bounds>` readonly                 | The bounds of the window's drawable area, excluding the frame, in screen coordinates.                                                       |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`cancelElement<Window.cancelElement>` readonly   | For windows of type dialog, the UI element to notify when the user presses a cancellation key combination.                                  |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`characters<Window.characters>` readonly         | A number of characters for which to reserve space when calculating the preferred size of the window.                                        |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<Window.children>` readonly             | The collection of UI elements that have been added to this container.                                                                       |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`defaultElement<Window.defaultElement>` readonly | For windows of type dialog, the UI element to notify when the user presses a Enter key.                                                     |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<Window.enabled>` readonly               | True if this element is enabled.                                                                                                            |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`frameBounds<Window.frameBounds>` readonly       | The bounds of the window frame in screen coordinates.                                                                                       |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`frameLocation<Window.frameLocation>` readonly   | The top left corner of the window frame in screen coordinates.                                                                              |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`frameSize<Window.frameSize>` readonly           | The size and location of the window's frame in screen coordinates.                                                                          |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<Window.graphics>` readonly             | The graphics object that can be used to customize the window?s appearance, in response to the onDraw event.                                 |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<Window.helpTip>` readonly               | The help text that is displayed when the mouse hovers over the element.                                                                     |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<Window.indent>` readonly                 | The number of pixels to indent the element.                                                                                                 |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`justify<Window.justify>` readonly               | The default text justification style for child text elements.                                                                               |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`layout<Window.layout>` readonly                 | The layout manager for this container.                                                                                                      |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<Window.location>` readonly             | The upper left corner of the window's drawable area.                                                                                        |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`margins<Window.margins>` readonly               | The number of pixels between the edges of a container and the outermost child elements.                                                     |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximized<Window.maximized>` readonly           | True if the window is expanded.                                                                                                             |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<Window.maximumSize>` readonly       | The largest rectangle to which the window can be resized.                                                                                   |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimized<Window.minimized>` readonly           | True if the window is minimized or iconified.                                                                                               |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<Window.minimumSize>` readonly       | The smallest rectangle to which the window can be resized.                                                                                  |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`opacity<Window.opacity>` readonly               | The opacity of the window, in the range [0..1].                                                                                             |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`orientation<Window.orientation>` readonly       | The layout orientation of children in a container.                                                                                          |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Window.parent>` readonly                 | The immediate parent element.                                                                                                               |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<Window.preferredSize>` readonly   | The preferred size of the window.                                                                                                           |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<Window.properties>` readonly         | An object that contains one or more creation properties of the container (properties used only when the element is created).                |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<Window.shortcutKey>` readonly       | The keypress combination that invokes this element's?onShortcutKey()?callback.                                                              |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<Window.size>` readonly                     | The current size and location of the content area of the window in screen coordinates.                                                      |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`spacing<Window.spacing>` readonly               | The number of pixels separating one child element from its adjacent sibling element.                                                        |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`text<Window.text>` readonly                     | The title, label, or displayed text, a localizeable string.                                                                                 |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<Window.type>` readonly                     | The element type; "dialog", "palette", or "window".                                                                                         |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<Window.visible>` readonly               | When true, the element is shown, when false it is hidden.                                                                                   |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<Window.window>` readonly                 | The window that this element belongs to.                                                                                                    |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<Window.windowBounds>` readonly     | The bounds of this window relative to the top-level parent window.                                                                          |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Static Properties
^^^^^^^^^^^^^^^^^

+-----------------------------------------------------+-------------------------------------------------+
| :ref:`frameworkName<Window.frameworkName>` readonly | Deprecated. Use?ScriptUI.frameworkName?instead. |
+-----------------------------------------------------+-------------------------------------------------+
| :ref:`version<Window.version>` readonly             | Deprecated. Use?ScriptUI.version?instead.       |
+-----------------------------------------------------+-------------------------------------------------+


Constructors
^^^^^^^^^^^^

+---------------------------------------+-----------------------+
| :ref:`Window<Window.Window>` readonly | Creates a new window. |
+---------------------------------------+-----------------------+


Methods
^^^^^^^

+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`add<Window.add>` readonly                                 | Creates and returns a new control or container object and adds it to the children of this window. |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`addEventListener<Window.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this window.                |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`center<Window.center>` readonly                           | Centers this window on screen or with repect to another window.                                   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`close<Window.close>` readonly                             | Closes this window.                                                                               |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<Window.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                              |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`hide<Window.hide>` readonly                               | Hides this windows.                                                                               |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`notify<Window.notify>` readonly                           | Sends a notification message to all listeners, simulating the specified user interaction event.   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`remove<Window.remove>` readonly                           | Removes the specified child control from this window?s children array.                            |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`removeEventListener<Window.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this window.              |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`show<Window.show>` readonly                               | Makes this window visible.                                                                        |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

Static Methods
^^^^^^^^^^^^^^

+-----------------------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`alert<Window.alert>` readonly     | Displays a platform-standard dialog containing a short message and an OK button.                   |
+-----------------------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`confirm<Window.confirm>` readonly | Displays a platform-standard dialog containing a short message and two buttons labeled Yes and No. |
+-----------------------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`find<Window.find>` readonly       | Use this method to find an existing window.                                                        |
+-----------------------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`prompt<Window.prompt>` readonly   | Displays a modal dialog that returns the user?s text input.                                        |
+-----------------------------------------+----------------------------------------------------------------------------------------------------+

Events
^^^^^^

+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onActivate<Window.onActivate>` readonly       | An event-handler callback function, called when the window acquires the keyboard focus.                                                          |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onClose<Window.onClose>` readonly             | An event-handler callback function, called  when the window is about to be closed.                                                               |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onDeactivate<Window.onDeactivate>` readonly   | An event-handler callback function, called when the window loses the keyboard focus.                                                             |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onMove<Window.onMove>` readonly               | An event-handler callback function, called  when the window  has been moved                                                                      |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onMoving<Window.onMoving>` readonly           | An event-handler callback function, called  when the window is being moved                                                                       |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onResize<Window.onResize>` readonly           | An event-handler callback function, called after the window has been resized                                                                     |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onResizing<Window.onResizing>` readonly       | An event-handler callback function, called while a window is being resized                                                                       |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<Window.onShortcutKey>` readonly | In Windows only, an event-handler callback function, called a shortcut-key sequence is typed that matches the?shortcutKey?value for this window. |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`onShow<Window.onShow>` readonly               | An event-handler callback function, called just before the window is displayed                                                                   |
+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Window/graphics.rst
      Window/visible.rst
      Window/bounds.rst
      Window/frameBounds.rst
      Window/frameLocation.rst
      Window/frameSize.rst
      Window/location.rst
      Window/maximumSize.rst
      Window/minimumSize.rst
      Window/preferredSize.rst
      Window/size.rst
      Window/windowBounds.rst
      Window/characters.rst
      Window/justify.rst
      Window/text.rst
      Window/active.rst
      Window/shortcutKey.rst
      Window/cancelElement.rst
      Window/defaultElement.rst
      Window/maximized.rst
      Window/minimized.rst
      Window/alignChildren.rst
      Window/children.rst
      Window/layout.rst
      Window/margins.rst
      Window/orientation.rst
      Window/spacing.rst
      Window/alignment.rst
      Window/properties.rst
      Window/enabled.rst
      Window/helpTip.rst
      Window/indent.rst
      Window/parent.rst
      Window/window.rst
      Window/type.rst
      Window/opacity.rst
      
      Window/frameworkName.rst
      Window/version.rst
      

      Window/show.rst
      Window/hide.rst
      Window/notify.rst
      Window/center.rst
      Window/close.rst
      Window/add.rst
      Window/remove.rst
      Window/addEventListener.rst
      Window/removeEventListener.rst
      Window/dispatchEvent.rst
      
      Window/find.rst
      Window/alert.rst
      Window/confirm.rst
      Window/prompt.rst
      
      Window/onActivate.rst
      Window/onDeactivate.rst
      Window/onClose.rst
      Window/onMove.rst
      Window/onMoving.rst
      Window/onResize.rst
      Window/onResizing.rst
      Window/onShortcutKey.rst
      Window/onShow.rst
      
      Window/Window.rst
      