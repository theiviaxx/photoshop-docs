Application.doProgressTask {#Application.doProgressTask}
==========================

> bool **doProgressTask** ([number]{role="ref"} **taskLength**,
> [string]{role="ref"} **javaScriptString**)

Parameters
----------

  ---------------------- -----------------------------------------------------
  **taskLength**         Amount of the unused progress bar to section off,
                         between 0.0 and 1.0.

  **javaScriptString**   JavaScriptString to execute.
  ---------------------- -----------------------------------------------------

Description
-----------

Sections off a portion of the unused progress bar for execution of a
subtask. Returns false on cancel.
