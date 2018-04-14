EditText {#EditText}
========

Description
-----------

An editable text field that the user can select and change.

Calls the?onChange()?callback if the text is changed and the user types
Enter or the control loses focus, or if its?notify()?method is called.
Calls the?onChanging()?callback when any change is made to the text.
The?textselection?property contains currently selected text.

### Properties

  ------------------------------------------------------- -------------------------------------------------
  [active\<EditText.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<EditText.alignment\>]{role="ref"} readonly  The alignment style for this element. If defined,
                                                          this value overrides the alignChildren setting
                                                          for the parent container.

  [bounds\<EditText.bounds\>]{role="ref"} readonly        The boundaries of the element, in parent-relative
                                                          coordinates.

  [characters\<EditText.characters\>]{role="ref"}         A number of characters for which to reserve space
  readonly                                                when calculating the preferred size of the
                                                          element.

  [children\<EditText.children\>]{role="ref"} readonly    An array of child elements.

  [enabled\<EditText.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [graphics\<EditText.graphics\>]{role="ref"} readonly    The graphics object that can be used to customize
                                                          the element\'s appearance, in response to
                                                          the?onDraw()?event.

  [helpTip\<EditText.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                          hovers over the element.

  [indent\<EditText.indent\>]{role="ref"} readonly        The number of pixels to indent the element during
                                                          automatic layout.

  [justify\<EditText.justify\>]{role="ref"} readonly      The text justification style.

  [location\<EditText.location\>]{role="ref"} readonly    The upper left corner of this element relative to
                                                          its parent.

  [maximumSize\<EditText.maximumSize\>]{role="ref"}       The maximum height and width to which the element
  readonly                                                can be resized.

  [minimumSize\<EditText.minimumSize\>]{role="ref"}       The minimum height and width to which the element
  readonly                                                can be resized.

  [parent\<EditText.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<EditText.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                determine the best size for each element.

  [properties\<EditText.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                properties of the container (properties used only
                                                          when the element is created).

  [shortcutKey\<EditText.shortcutKey\>]{role="ref"}       The key sequence that invokes
  readonly                                                the?onShortcutKey()?callback for this element (in
                                                          Windows only).

  [size\<EditText.size\>]{role="ref"} readonly            The current dimensions of this element.

  [text\<EditText.text\>]{role="ref"} readonly            The current text displayed in the field, a
                                                          localizable string.

  [textselection\<EditText.textselection\>]{role="ref"}   The currently selected text, or the empty string
  readonly                                                if there is no text selected.

  [type\<EditText.type\>]{role="ref"} readonly            The element type; \"edittext\".

  [visible\<EditText.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                          hidden.

  [window\<EditText.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<EditText.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                top-level parent window.
  ------------------------------------------------------- -------------------------------------------------

### Methods

  ------------------------------------------------------------------- ----------------------------------------
  [addEventListener\<EditText.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                            particular type of event occuring in
                                                                      this element.

  [dispatchEvent\<EditText.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                      this target.

  [hide\<EditText.hide\>]{role="ref"} readonly                        Hides this element.

  [notify\<EditText.notify\>]{role="ref"} readonly                    Sends a notification message, simulating
                                                                      the specified user interaction event.

  [removeEventListener\<EditText.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                            particular type of event occuring in
                                                                      this element.

  [show\<EditText.show\>]{role="ref"} readonly                        Shows this element.
  ------------------------------------------------------------------- ----------------------------------------

### Events

  ------------------------------------------------------- -----------------------------------------------
  [onActivate\<EditText.onActivate\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                the element acquires the keyboard focus.

  [onChange\<EditText.onChange\>]{role="ref"} readonly    An event-handler callback function, called when
                                                          the content of the element has been changed

  [onChanging\<EditText.onChanging\>]{role="ref"}         An event-handler callback function, called when
  readonly                                                the content of the element is in the process of
                                                          changing

  [onDeactivate\<EditText.onDeactivate\>]{role="ref"}     An event-handler callback function, called when
  readonly                                                the element loses the keyboard focus.

  [onDraw\<EditText.onDraw\>]{role="ref"} readonly        An event-handler callback function, called when
                                                          the window is about to be drawn.

  [onShortcutKey\<EditText.onShortcutKey\>]{role="ref"}   An event-handler callback function, called when
  readonly                                                the element\'s?shortcutKey?sequence is typed in
                                                          the active window.
  ------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
EditText/textselection.rst EditText/characters.rst EditText/justify.rst
EditText/text.rst EditText/graphics.rst EditText/visible.rst
EditText/bounds.rst EditText/location.rst EditText/maximumSize.rst
EditText/minimumSize.rst EditText/preferredSize.rst EditText/size.rst
EditText/windowBounds.rst EditText/active.rst EditText/shortcutKey.rst
EditText/alignment.rst EditText/children.rst EditText/properties.rst
EditText/enabled.rst EditText/helpTip.rst EditText/indent.rst
EditText/parent.rst EditText/window.rst EditText/type.rst

EditText/show.rst EditText/hide.rst EditText/notify.rst
EditText/addEventListener.rst EditText/removeEventListener.rst
EditText/dispatchEvent.rst

EditText/onActivate.rst EditText/onDeactivate.rst EditText/onDraw.rst
EditText/onChanging.rst EditText/onChange.rst EditText/onShortcutKey.rst
:::
:::
