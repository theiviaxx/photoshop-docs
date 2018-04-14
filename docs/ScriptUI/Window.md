Window {#Window}
======

Description
-----------

The instance represents a top-level window or dialog box, which contains
user-interface elements.

The globally available?Window?object provides access to predefined and
script-defined windows.

### Properties

  ------------------------------------------------------- --------------------------------------------------
  [active\<Window.active\>]{role="ref"} readonly          Set to true to make this window active.

  [alignChildren\<Window.alignChildren\>]{role="ref"}     Tells the layout manager how unlike-sized children
  readonly                                                of this container should be aligned within a
                                                          column or row.

  [alignment\<Window.alignment\>]{role="ref"} readonly    The alignment style for child elements of a
                                                          container. If defined, this value overrides the
                                                          alignChildren setting for the parent container.

  [bounds\<Window.bounds\>]{role="ref"} readonly          The bounds of the window\'s drawable area,
                                                          excluding the frame, in screen coordinates.

  [cancelElement\<Window.cancelElement\>]{role="ref"}     For windows of type dialog, the UI element to
  readonly                                                notify when the user presses a cancellation key
                                                          combination.

  [characters\<Window.characters\>]{role="ref"} readonly  A number of characters for which to reserve space
                                                          when calculating the preferred size of the window.

  [children\<Window.children\>]{role="ref"} readonly      The collection of UI elements that have been added
                                                          to this container.

  [defaultElement\<Window.defaultElement\>]{role="ref"}   For windows of type dialog, the UI element to
  readonly                                                notify when the user presses a Enter key.

  [enabled\<Window.enabled\>]{role="ref"} readonly        True if this element is enabled.

  [frameBounds\<Window.frameBounds\>]{role="ref"}         The bounds of the window frame in screen
  readonly                                                coordinates.

  [frameLocation\<Window.frameLocation\>]{role="ref"}     The top left corner of the window frame in screen
  readonly                                                coordinates.

  [frameSize\<Window.frameSize\>]{role="ref"} readonly    The size and location of the window\'s frame in
                                                          screen coordinates.

  [graphics\<Window.graphics\>]{role="ref"} readonly      The graphics object that can be used to customize
                                                          the window?s appearance, in response to the onDraw
                                                          event.

  [helpTip\<Window.helpTip\>]{role="ref"} readonly        The help text that is displayed when the mouse
                                                          hovers over the element.

  [indent\<Window.indent\>]{role="ref"} readonly          The number of pixels to indent the element.

  [justify\<Window.justify\>]{role="ref"} readonly        The default text justification style for child
                                                          text elements.

  [layout\<Window.layout\>]{role="ref"} readonly          The layout manager for this container.

  [location\<Window.location\>]{role="ref"} readonly      The upper left corner of the window\'s drawable
                                                          area.

  [margins\<Window.margins\>]{role="ref"} readonly        The number of pixels between the edges of a
                                                          container and the outermost child elements.

  [maximized\<Window.maximized\>]{role="ref"} readonly    True if the window is expanded.

  [maximumSize\<Window.maximumSize\>]{role="ref"}         The largest rectangle to which the window can be
  readonly                                                resized.

  [minimized\<Window.minimized\>]{role="ref"} readonly    True if the window is minimized or iconified.

  [minimumSize\<Window.minimumSize\>]{role="ref"}         The smallest rectangle to which the window can be
  readonly                                                resized.

  [opacity\<Window.opacity\>]{role="ref"} readonly        The opacity of the window, in the range \[0..1\].

  [orientation\<Window.orientation\>]{role="ref"}         The layout orientation of children in a container.
  readonly                                                

  [parent\<Window.parent\>]{role="ref"} readonly          The immediate parent element.

  [preferredSize\<Window.preferredSize\>]{role="ref"}     The preferred size of the window.
  readonly                                                

  [properties\<Window.properties\>]{role="ref"} readonly  An object that contains one or more creation
                                                          properties of the container (properties used only
                                                          when the element is created).

  [shortcutKey\<Window.shortcutKey\>]{role="ref"}         The keypress combination that invokes this
  readonly                                                element\'s?onShortcutKey()?callback.

  [size\<Window.size\>]{role="ref"} readonly              The current size and location of the content area
                                                          of the window in screen coordinates.

  [spacing\<Window.spacing\>]{role="ref"} readonly        The number of pixels separating one child element
                                                          from its adjacent sibling element.

  [text\<Window.text\>]{role="ref"} readonly              The title, label, or displayed text, a
                                                          localizeable string.

  [type\<Window.type\>]{role="ref"} readonly              The element type; \"dialog\", \"palette\", or
                                                          \"window\".

  [visible\<Window.visible\>]{role="ref"} readonly        When true, the element is shown, when false it is
                                                          hidden.

  [window\<Window.window\>]{role="ref"} readonly          The window that this element belongs to.

  [windowBounds\<Window.windowBounds\>]{role="ref"}       The bounds of this window relative to the
  readonly                                                top-level parent window.
  ------------------------------------------------------- --------------------------------------------------

### Static Properties

  ----------------------------------------------------- -------------------------------------
  [frameworkName\<Window.frameworkName\>]{role="ref"}   Deprecated.
  readonly                                              Use?ScriptUI.frameworkName?instead.

  [version\<Window.version\>]{role="ref"} readonly      Deprecated.
                                                        Use?ScriptUI.version?instead.
  ----------------------------------------------------- -------------------------------------

### Constructors

  --------------------------------------- -----------------------
  [Window\<Window.Window\>]{role="ref"}   Creates a new window.
  readonly                                
  --------------------------------------- -----------------------

### Methods

  ----------------------------------------------------------------- ------------------------------------------
  [add\<Window.add\>]{role="ref"} readonly                          Creates and returns a new control or
                                                                    container object and adds it to the
                                                                    children of this window.

  [addEventListener\<Window.addEventListener\>]{role="ref"}         Registers an event handler for a
  readonly                                                          particular type of event occuring in this
                                                                    window.

  [center\<Window.center\>]{role="ref"} readonly                    Centers this window on screen or with
                                                                    repect to another window.

  [close\<Window.close\>]{role="ref"} readonly                      Closes this window.

  [dispatchEvent\<Window.dispatchEvent\>]{role="ref"} readonly      Simulates the occurrence of an event in
                                                                    this target.

  [hide\<Window.hide\>]{role="ref"} readonly                        Hides this windows.

  [notify\<Window.notify\>]{role="ref"} readonly                    Sends a notification message to all
                                                                    listeners, simulating the specified user
                                                                    interaction event.

  [remove\<Window.remove\>]{role="ref"} readonly                    Removes the specified child control from
                                                                    this window?s children array.

  [removeEventListener\<Window.removeEventListener\>]{role="ref"}   Unregisters an event handler for a
  readonly                                                          particular type of event occuring in this
                                                                    window.

  [show\<Window.show\>]{role="ref"} readonly                        Makes this window visible.
  ----------------------------------------------------------------- ------------------------------------------

### Static Methods

  ----------------------------------------- --------------------------------------------------
  [alert\<Window.alert\>]{role="ref"}       Displays a platform-standard dialog containing a
  readonly                                  short message and an OK button.

  [confirm\<Window.confirm\>]{role="ref"}   Displays a platform-standard dialog containing a
  readonly                                  short message and two buttons labeled Yes and No.

  [find\<Window.find\>]{role="ref"}         Use this method to find an existing window.
  readonly                                  

  [prompt\<Window.prompt\>]{role="ref"}     Displays a modal dialog that returns the user?s
  readonly                                  text input.
  ----------------------------------------- --------------------------------------------------

### Events

  ----------------------------------------------------- ---------------------------------------------------
  [onActivate\<Window.onActivate\>]{role="ref"}         An event-handler callback function, called when the
  readonly                                              window acquires the keyboard focus.

  [onClose\<Window.onClose\>]{role="ref"} readonly      An event-handler callback function, called when the
                                                        window is about to be closed.

  [onDeactivate\<Window.onDeactivate\>]{role="ref"}     An event-handler callback function, called when the
  readonly                                              window loses the keyboard focus.

  [onMove\<Window.onMove\>]{role="ref"} readonly        An event-handler callback function, called when the
                                                        window has been moved

  [onMoving\<Window.onMoving\>]{role="ref"} readonly    An event-handler callback function, called when the
                                                        window is being moved

  [onResize\<Window.onResize\>]{role="ref"} readonly    An event-handler callback function, called after
                                                        the window has been resized

  [onResizing\<Window.onResizing\>]{role="ref"}         An event-handler callback function, called while a
  readonly                                              window is being resized

  [onShortcutKey\<Window.onShortcutKey\>]{role="ref"}   In Windows only, an event-handler callback
  readonly                                              function, called a shortcut-key sequence is typed
                                                        that matches the?shortcutKey?value for this window.

  [onShow\<Window.onShow\>]{role="ref"} readonly        An event-handler callback function, called just
                                                        before the window is displayed
  ----------------------------------------------------- ---------------------------------------------------

::: {.container .hide}
::: {.toctree}
Window/graphics.rst Window/visible.rst Window/bounds.rst
Window/frameBounds.rst Window/frameLocation.rst Window/frameSize.rst
Window/location.rst Window/maximumSize.rst Window/minimumSize.rst
Window/preferredSize.rst Window/size.rst Window/windowBounds.rst
Window/characters.rst Window/justify.rst Window/text.rst
Window/active.rst Window/shortcutKey.rst Window/cancelElement.rst
Window/defaultElement.rst Window/maximized.rst Window/minimized.rst
Window/alignChildren.rst Window/children.rst Window/layout.rst
Window/margins.rst Window/orientation.rst Window/spacing.rst
Window/alignment.rst Window/properties.rst Window/enabled.rst
Window/helpTip.rst Window/indent.rst Window/parent.rst Window/window.rst
Window/type.rst Window/opacity.rst

Window/frameworkName.rst Window/version.rst

Window/show.rst Window/hide.rst Window/notify.rst Window/center.rst
Window/close.rst Window/add.rst Window/remove.rst
Window/addEventListener.rst Window/removeEventListener.rst
Window/dispatchEvent.rst

Window/find.rst Window/alert.rst Window/confirm.rst Window/prompt.rst

Window/onActivate.rst Window/onDeactivate.rst Window/onClose.rst
Window/onMove.rst Window/onMoving.rst Window/onResize.rst
Window/onResizing.rst Window/onShortcutKey.rst Window/onShow.rst

Window/Window.rst
:::
:::
