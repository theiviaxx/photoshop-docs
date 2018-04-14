Application.putCustomOptions {#Application.putCustomOptions}
============================

> void **putCustomOptions** ([string]{role="ref"} **key**,
> [ActionDescriptor]{role="ref"} **customObject**, bool **persistent**)

Parameters
----------

  ------------------ ------------------------------------------------------
  **key**            The unique string ID for the user object.

  **customObject**   The user-defined custom object to save in the
                     registry.

  **persistent**     If true, the object persists after the script has
                     finished.
  ------------------ ------------------------------------------------------

Description
-----------

Save user objects in the Photoshop registry.
