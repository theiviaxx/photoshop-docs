.. _Application.doForcedProgress:

================================================
Application.doForcedProgress
================================================

   void **doForcedProgress** (:ref:`string` **progressString**, :ref:`string` **javaScriptString**)


Parameters
----------

+----------------------+----------------------------------------+
| **progressString**   | String to show in the progress window. |
+----------------------+----------------------------------------+
| **javaScriptString** | JavaScriptString to execute.           |
+----------------------+----------------------------------------+



Description
-----------

Performs a task with a progress bar. Forces progress bar to display, ignoring the normal heuristics that keep it from showing unnecessarily (e.g. during very short tasks). Other progress APIs must be called periodically to update the progress bar and allow cancelling.




