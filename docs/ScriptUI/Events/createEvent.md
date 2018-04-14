Events.createEvent {#Events.createEvent}
==================

> [Event]{role="ref"} **createEvent** ([String]{role="ref"}
> **eventType**)

Parameters
----------

  --------------- -----------------------------------------------------------
  **eventType**   The name of an event type: one of \"UIEvent\",
                  \"KeyboardEvent\", or \"MouseEvent\".
  --------------- -----------------------------------------------------------

Description
-----------

Creates an instance of the specified?Event?subclass.

The?Event?returned is a?UIEvent, KeyboardEvent?or?MouseEvent?object,
depending on the requested type. This object can be passed as a
parameter to an element\'s dispatchEvent function in order to simulate a
user-interaction event.
