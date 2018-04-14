Object.watch {#Object.watch}
============

> void **watch** ([string]{role="ref"} **name**, [Function]{role="ref"}
> **func**)

Parameters
----------

  ---------- -------------------------------------------------------------
  **name**   The name of the property to watch.

  **func**   The function to be called when the value of this property
             changes.
  ---------- -------------------------------------------------------------

Description
-----------

Adds a watch function to a property, which is called when the value
changes.

This function can accept, modify, or reject a new value that the user,
application, or a script has attempted to place in a property.
