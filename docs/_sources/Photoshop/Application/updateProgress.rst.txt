.. _Application.updateProgress:

================================================
Application.updateProgress
================================================

   bool **updateProgress** (int **done**, int **total**)


Parameters
----------

+-----------+--------------------------------+
| **done**  | The number of tasks completed. |
+-----------+--------------------------------+
| **total** | The total number of tasks.     |
+-----------+--------------------------------+



Description
-----------

Updates the progress bar started by doProgress. Use for manual non-task based progress updating. Returns false on cancel.




