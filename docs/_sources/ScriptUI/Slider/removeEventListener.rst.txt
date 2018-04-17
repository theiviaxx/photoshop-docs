.. _Slider.removeEventListener:

================================================
Slider.removeEventListener
================================================

   :ref:`Boolean` **removeEventListener** (:ref:`String` **eventName**, :ref:`Function` **handler**, :ref:`Boolean` **capturePhase**)


Parameters
----------

+------------------+-----------------------------------------------------------------------------------+
| **eventName**    | The name of the event.                                                            |
+------------------+-----------------------------------------------------------------------------------+
| **handler**      | The function that handles the event.                                              |
+------------------+-----------------------------------------------------------------------------------+
| **capturePhase** | Whether to call the handler only in the capturing phase of the event propagation. |
+------------------+-----------------------------------------------------------------------------------+



Description
-----------

Unregisters an event handler for a particular type of event occuring in this element.

All arguments must be identical to those that were used to register the event handler.


