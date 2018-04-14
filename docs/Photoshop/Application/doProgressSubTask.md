Application.doProgressSubTask {#Application.doProgressSubTask}
=============================

> bool **doProgressSubTask** (int **index**, int **limit**,
> [string]{role="ref"} **javaScriptString**)

Parameters
----------

  ---------------------- ----------------------------------------
  **index**              The 0-based index of the current task.

  **limit**              The total number of tasks.

  **javaScriptString**   JavaScriptString to execute.
  ---------------------- ----------------------------------------

Description
-----------

Sections off a portion of the unused progress bar for execution of a
subtask. Returns false on cancel. Use when iterating a simple list of
tasks with equal run times.
