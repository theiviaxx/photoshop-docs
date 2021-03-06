.. _StaticText:

================================================
StaticText
================================================


Description
-----------

A text label that the user cannot change.




Properties
^^^^^^^^^^

+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<StaticText.active>`                      | Always false. This element cannot have input focus.                                                                          |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<StaticText.alignment>`                | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.   |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<StaticText.bounds>`                      | The boundaries of the element, in parent-relative coordinates.                                                               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`characters<StaticText.characters>`              | A number of characters for which to reserve space when calculating the preferred size of the element.                        |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<StaticText.children>` readonly         | An array of child elements.                                                                                                  |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<StaticText.enabled>`                    | True if this element is enabled.                                                                                             |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<StaticText.graphics>` readonly         | The graphics object that can be used to customize the element's appearance, in response to the onDraw() event.               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<StaticText.helpTip>`                    | The help text that is displayed when the mouse hovers over the element.                                                      |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<StaticText.indent>`                      | The number of pixels to indent the element during automatic layout.                                                          |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`justify<StaticText.justify>`                    | The text justification style.                                                                                                |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<StaticText.location>`                  | The upper left corner of this element relative to its parent.                                                                |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<StaticText.maximumSize>`            | The maximum height and width to which the element can be resized.                                                            |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<StaticText.minimumSize>`            | The minimum height and width to which the element can be resized.                                                            |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<StaticText.parent>` readonly             | The parent element.                                                                                                          |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<StaticText.preferredSize>`        | The preferred size, used by layout managers to determine the best size for each element.                                     |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<StaticText.properties>`              | An object that contains one or more creation properties of the container (properties used only when the element is created). |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<StaticText.shortcutKey>`            | The key sequence that invokes the onShortcutKey() callback for this element (in Windows only).                               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<StaticText.size>`                          | The current dimensions of this element.                                                                                      |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`text<StaticText.text>`                          | The text to display, a localizable string.                                                                                   |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<StaticText.type>` readonly                 | The element type, "statictext".                                                                                              |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<StaticText.visible>`                    | True if this element is shown, false if it is hidden.                                                                        |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<StaticText.window>` readonly             | The window that this element belongs to.                                                                                     |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<StaticText.windowBounds>` readonly | The bounds of this element relative to the top-level parent window.                                                          |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<StaticText.addEventListener>`       | Registers an event handler for a particular type of event occuring in this element.   |
+------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<StaticText.dispatchEvent>`             | Simulates the occurrence of an event in this target.                                  |
+------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<StaticText.hide>`                               | Hides this element.                                                                   |
+------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<StaticText.notify>`                           | Sends a notification message, simulating the specified user interaction event.        |
+------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<StaticText.removeEventListener>` | Unregisters an event handler for a particular type of event occuring in this element. |
+------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<StaticText.show>`                               | Shows this element.                                                                   |
+------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDraw<StaticText.onDraw>`               | An event-handler callback function, called when the window is about to be drawn.                                  |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<StaticText.onShortcutKey>` | An event-handler callback function, called when the element's shortcutKey sequence is typed in the active window. |
+------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      StaticText/characters.rst
      StaticText/justify.rst
      StaticText/text.rst
      StaticText/active.rst
      StaticText/shortcutKey.rst
      StaticText/graphics.rst
      StaticText/visible.rst
      StaticText/bounds.rst
      StaticText/location.rst
      StaticText/maximumSize.rst
      StaticText/minimumSize.rst
      StaticText/preferredSize.rst
      StaticText/size.rst
      StaticText/windowBounds.rst
      StaticText/alignment.rst
      StaticText/children.rst
      StaticText/properties.rst
      StaticText/enabled.rst
      StaticText/helpTip.rst
      StaticText/indent.rst
      StaticText/parent.rst
      StaticText/window.rst
      StaticText/type.rst
      
      

      StaticText/notify.rst
      StaticText/show.rst
      StaticText/hide.rst
      StaticText/addEventListener.rst
      StaticText/removeEventListener.rst
      StaticText/dispatchEvent.rst
      
      
      StaticText/onDraw.rst
      StaticText/onShortcutKey.rst
      
      