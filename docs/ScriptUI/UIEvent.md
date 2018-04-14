UIEvent {#UIEvent}
=======

Description
-----------

Encapsulates input event information for an event that propagates
through a container and control hierarchy.

Implements W3C standard event handling. This object is passed to a
function that you register to respond to events of a certain type that
occur in a window or control. Use windowObj.addEventListener()?or
controlObj.addEventListener() to register a handler function.

### Properties

  ------------------------------------------------------ --------------------------------------------------
  [bubbles\<UIEvent.bubbles\>]{role="ref"} readonly      True if the event is of a type that bubbles.

  [cancelable\<UIEvent.cancelable\>]{role="ref"}         True if the default action associated with the
  readonly                                               event can be canceled with preventDefault().

  [captures\<UIEvent.captures\>]{role="ref"} readonly    True if this event can be captured.

  [currentTarget\<UIEvent.currentTarget\>]{role="ref"}   The event target object which is currently
  readonly                                               handling the event. During capturing and bubbling,
                                                         this is different from the property target.

  [detail\<UIEvent.detail\>]{role="ref"} readonly        The click count for a mouse-click event.

  [eventPhase\<UIEvent.eventPhase\>]{role="ref"}         The current phase of event propagation; one of
  readonly                                               none, target, capture, bubble.

  [target\<UIEvent.target\>]{role="ref"} readonly        The event target object for this event.

  [timeStamp\<UIEvent.timeStamp\>]{role="ref"} readonly  The date and time at which the event occurred.

  [type\<UIEvent.type\>]{role="ref"} readonly            The name of the event that this object represents.

  [view\<UIEvent.view\>]{role="ref"} readonly            The ScriptUI element that this event relates to.
  ------------------------------------------------------ --------------------------------------------------

### Constructors

  ------------------------------------------ -------------------
  [UIEvent\<UIEvent.UIEvent\>]{role="ref"}   Creates an event.
  readonly                                   
  ------------------------------------------ -------------------

### Methods

  ---------------------------------------------------------- ---------------------------------------
  [initEvent\<UIEvent.initEvent\>]{role="ref"} readonly      Initializes a UI event as a core W3C
                                                             event.

  [initUIEvent\<UIEvent.initUIEvent\>]{role="ref"} readonly  Initializes an event.

  [preventDefault\<UIEvent.preventDefault\>]{role="ref"}     Prevents the default action associated
  readonly                                                   with this event from being called.

  [stopPropagation\<UIEvent.stopPropagation\>]{role="ref"}   Stops the propagation of this event.
  readonly                                                   
  ---------------------------------------------------------- ---------------------------------------

::: {.container .hide}
::: {.toctree}
UIEvent/captures.rst UIEvent/bubbles.rst UIEvent/cancelable.rst
UIEvent/currentTarget.rst UIEvent/eventPhase.rst UIEvent/target.rst
UIEvent/timeStamp.rst UIEvent/type.rst UIEvent/view.rst
UIEvent/detail.rst

UIEvent/preventDefault.rst UIEvent/stopPropagation.rst
UIEvent/initEvent.rst UIEvent/initUIEvent.rst

UIEvent/UIEvent.rst
:::
:::
