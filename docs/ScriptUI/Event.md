Event {#Event}
=====

Description
-----------

Base class for UIEvent.

Encapsulates input event information for an event that propagates
through a container and control hierarchy. Implements W3C standard event
handling.

### Properties

  ---------------------------------------------------- ---------------------------------------------------
  [bubbles\<Event.bubbles\>]{role="ref"} readonly      True if the event is of a type that bubbles.

  [cancelable\<Event.cancelable\>]{role="ref"}         True if the default action associated with the
  readonly                                             event can be canceled with preventDefault().

  [captures\<Event.captures\>]{role="ref"} readonly    True if this event can be captured.

  [currentTarget\<Event.currentTarget\>]{role="ref"}   The event target object which is currently handling
  readonly                                             the event. During capturing and bubbling, this is
                                                       different from the property target.

  [eventPhase\<Event.eventPhase\>]{role="ref"}         The current phase of event propagation; one of
  readonly                                             none, target, capture, bubble.

  [target\<Event.target\>]{role="ref"} readonly        The event target object for this event.

  [timeStamp\<Event.timeStamp\>]{role="ref"} readonly  The date and time at which the event occurred.

  [type\<Event.type\>]{role="ref"} readonly            The name of the event that this object represents.
  ---------------------------------------------------- ---------------------------------------------------

### Static Properties

  ---------------------------------------------------------- --
  [AT\_TARGET\<Event.AT\_TARGET\>]{role="ref"} readonly      

  [BUBBLING\_PHASE\<Event.BUBBLING\_PHASE\>]{role="ref"}     
  readonly                                                   

  [CAPTURING\_PHASE\<Event.CAPTURING\_PHASE\>]{role="ref"}   
  readonly                                                   

  [NOT\_DISPATCHING\<Event.NOT\_DISPATCHING\>]{role="ref"}   
  readonly                                                   
  ---------------------------------------------------------- --

### Methods

  -------------------------------------------------------- ----------------------------------------
  [preventDefault\<Event.preventDefault\>]{role="ref"}     Prevents the default action associated
  readonly                                                 with this event from being called.

  [stopPropagation\<Event.stopPropagation\>]{role="ref"}   Stops the propagation of this event.
  readonly                                                 
  -------------------------------------------------------- ----------------------------------------

::: {.container .hide}
::: {.toctree}
Event/captures.rst Event/bubbles.rst Event/cancelable.rst
Event/currentTarget.rst Event/eventPhase.rst Event/target.rst
Event/timeStamp.rst Event/type.rst

Event/NOT\_DISPATCHING.rst Event/CAPTURING\_PHASE.rst
Event/AT\_TARGET.rst Event/BUBBLING\_PHASE.rst

Event/preventDefault.rst Event/stopPropagation.rst
:::
:::
