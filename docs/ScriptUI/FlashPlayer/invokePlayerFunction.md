FlashPlayer.invokePlayerFunction {#FlashPlayer.invokePlayerFunction}
================================

> any **invokePlayerFunction** ([String]{role="ref"} **name**, any
> **argument**)

Parameters
----------

  -------------- ---------------------------------------------------------------
  **name**       The name of a Flash ActionScript function that has been
                 registered with the ExternalInterface object by the currently
                 loaded SWF file.

  **argument**   An argument to pass through to the function.
  -------------- ---------------------------------------------------------------

Description
-----------

Invokes an ActionScript function defined in the Flash application.

Returns the result of the invoked function, which must be one of the
allowed types. The ActionScript class and date objects are not supported
as return values.
