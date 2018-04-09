.. _Application.doProgressSegmentTask:

================================================
Application.doProgressSegmentTask
================================================

   bool **doProgressSegmentTask** (int **segmentLength**, int **done**, int **total**, :ref:`string` **javaScriptString**)


Parameters
----------

+----------------------+------------------------------------------+
| **segmentLength**    | The length of the current task.          |
+----------------------+------------------------------------------+
| **done**             | The total length of all completed tasks. |
+----------------------+------------------------------------------+
| **total**            | The total length of all tasks.           |
+----------------------+------------------------------------------+
| **javaScriptString** | JavaScriptString to execute.             |
+----------------------+------------------------------------------+



Description
-----------

Sections off a portion of the unused progress bar for execution of a subtask. Returns false on cancel. Use when iterating a list of tasks with unequal run times.




