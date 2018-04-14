Notifiers.add {#Notifiers.add}
=============

> [Notifier]{role="ref"} **add** ([string]{role="ref"} **event**,
> [File]{role="ref"} **eventFile**, [string]{role="ref"} **eventClass**)

Parameters
----------

  ---------------- -------------------------------------------------------------------
  **event**        The class id of the event, four characters or a unique string.

  **eventFile**    The script file to execute when the event occurs.

  **eventClass**   The class of the object the event is applied to, four characters or
                   a unique string. When an event applies to multiple types of
                   objects, you use the event class parameter to distinguish which
                   object this Notifier applies to. For example, the Make event (?Mk?)
                   applies to documents (?Dcmn?), channels (?Chnl?) and other objects.
  ---------------- -------------------------------------------------------------------

Description
-----------

Creates a notifier.
