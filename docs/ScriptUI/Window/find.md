Window.find {#Window.find}
===========

> [Window]{role="ref"} **find** ([String]{role="ref"} **type**,
> [String]{role="ref"} **title**)

Parameters
----------

  ----------- ---------------------------------------------------------------
  **type**    The name of a predefined resource available to JavaScript in
              the current application; or the window type.

  **title**   The window title.
  ----------- ---------------------------------------------------------------

Description
-----------

Use this method to find an existing window.

This includes windows defined by ScriptUI resource strings, windows
already created by a script, and windows created by the application (if
the application supports this case). This function is not supported by
all applications. Returns a?Window?object found or generated from the
resource, or null if no such window or resource exists.
