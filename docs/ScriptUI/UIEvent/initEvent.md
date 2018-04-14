UIEvent.initEvent {#UIEvent.initEvent}
=================

> void **initEvent** ([String]{role="ref"} **type**,
> [Boolean]{role="ref"} **captures**, [Boolean]{role="ref"} **bubbles**,
> [Boolean]{role="ref"} **cancelable**)

Parameters
----------

  ---------------- --------------------------------------------------
  **type**         The event type.

  **captures**     Set to true if this event can be captured.

  **bubbles**      Set to true if the event bubbles.

  **cancelable**   Set to true if the default action is cancelable.
  ---------------- --------------------------------------------------

Description
-----------

Initializes a UI event as a core W3C event.
