.. _EditText:

================================================
EditText
================================================


Description
-----------

An editable text field that the user can select and change.

Calls the?onChange()?callback if the text is changed and the user types Enter or the control loses focus, or if its?notify()?method is called. Calls the?onChanging()?callback when any change is made to the text. The?textselection?property contains currently selected text.


Properties
^^^^^^^^^^

+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<EditText.active>` readonly               | True if this element is active.                                                                                              |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<EditText.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.   |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<EditText.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`characters<EditText.characters>` readonly       | A number of characters for which to reserve space when calculating the preferred size of the element.                        |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`children<EditText.children>` readonly           | An array of child elements.                                                                                                  |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<EditText.enabled>` readonly             | True if this element is enabled.                                                                                             |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`graphics<EditText.graphics>` readonly           | The graphics object that can be used to customize the element's appearance, in response to the?onDraw()?event.               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<EditText.helpTip>` readonly             | The help text that is displayed when the mouse hovers over the element.                                                      |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<EditText.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                          |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`justify<EditText.justify>` readonly             | The text justification style.                                                                                                |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<EditText.location>` readonly           | The upper left corner of this element relative to its parent.                                                                |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<EditText.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                            |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<EditText.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                            |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<EditText.parent>` readonly               | The parent element.                                                                                                          |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<EditText.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                     |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<EditText.properties>` readonly       | An object that contains one or more creation properties of the container (properties used only when the element is created). |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`shortcutKey<EditText.shortcutKey>` readonly     | The key sequence that invokes the?onShortcutKey()?callback for this element (in Windows only).                               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<EditText.size>` readonly                   | The current dimensions of this element.                                                                                      |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`text<EditText.text>` readonly                   | The current text displayed in the field, a localizable string.                                                               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`textselection<EditText.textselection>` readonly | The currently selected text, or the empty string if there is no text selected.                                               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<EditText.type>` readonly                   | The element type; "edittext".                                                                                                |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<EditText.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                        |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<EditText.window>` readonly               | The window that this element belongs to.                                                                                     |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<EditText.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                          |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<EditText.addEventListener>` readonly       | Registers an event handler for a particular type of event occuring in this element.   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<EditText.dispatchEvent>` readonly             | Simulates the occurrence of an event in this target.                                  |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<EditText.hide>` readonly                               | Hides this element.                                                                   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<EditText.notify>` readonly                           | Sends a notification message, simulating the specified user interaction event.        |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<EditText.removeEventListener>` readonly | Unregisters an event handler for a particular type of event occuring in this element. |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<EditText.show>` readonly                               | Shows this element.                                                                   |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onActivate<EditText.onActivate>` readonly       | An event-handler callback function, called when the element acquires the keyboard focus.                          |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onChange<EditText.onChange>` readonly           | An event-handler callback function, called when the content of the element has been changed                       |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onChanging<EditText.onChanging>` readonly       | An event-handler callback function, called when the content of the element is in the process of changing          |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDeactivate<EditText.onDeactivate>` readonly   | An event-handler callback function, called when the element loses the keyboard focus.                             |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onDraw<EditText.onDraw>` readonly               | An event-handler callback function, called when the window is about to be drawn.                                  |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`onShortcutKey<EditText.onShortcutKey>` readonly | An event-handler callback function, called when the element's?shortcutKey?sequence is typed in the active window. |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      EditText/textselection.rst
      EditText/characters.rst
      EditText/justify.rst
      EditText/text.rst
      EditText/graphics.rst
      EditText/visible.rst
      EditText/bounds.rst
      EditText/location.rst
      EditText/maximumSize.rst
      EditText/minimumSize.rst
      EditText/preferredSize.rst
      EditText/size.rst
      EditText/windowBounds.rst
      EditText/active.rst
      EditText/shortcutKey.rst
      EditText/alignment.rst
      EditText/children.rst
      EditText/properties.rst
      EditText/enabled.rst
      EditText/helpTip.rst
      EditText/indent.rst
      EditText/parent.rst
      EditText/window.rst
      EditText/type.rst
      
      

      EditText/show.rst
      EditText/hide.rst
      EditText/notify.rst
      EditText/addEventListener.rst
      EditText/removeEventListener.rst
      EditText/dispatchEvent.rst
      
      
      EditText/onActivate.rst
      EditText/onDeactivate.rst
      EditText/onDraw.rst
      EditText/onChanging.rst
      EditText/onChange.rst
      EditText/onShortcutKey.rst
      
      