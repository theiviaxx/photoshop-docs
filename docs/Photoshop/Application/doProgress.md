Application.doProgress {#Application.doProgress}
======================

> void **doProgress** ([string]{role="ref"} **progressString**,
> [string]{role="ref"} **javaScriptString**)

Parameters
----------

  ---------------------- ----------------------------------------
  **progressString**     String to show in the progress window.

  **javaScriptString**   JavaScriptString to execute.
  ---------------------- ----------------------------------------

Description
-----------

Performs a task with a progress bar. Other progress APIs must be called
periodically to update the progress bar and allow cancelling.
