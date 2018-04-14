RadioButton.addEventListener {#RadioButton.addEventListener}
============================

> [Boolean]{role="ref"} **addEventListener** ([String]{role="ref"}
> **eventName**, [Function]{role="ref"} **handler**,
> [Boolean]{role="ref"} **capturePhase**)

Parameters
----------

  ------------------ ----------------------------------------------------------
  **eventName**      The name of the event.

  **handler**        The function that handles the event.

  **capturePhase**   When true, the handler is called only in the capturing
                     phase of the event propagation.
  ------------------ ----------------------------------------------------------

Description
-----------

Registers an event handler for a particular type of event occuring in
this element.
