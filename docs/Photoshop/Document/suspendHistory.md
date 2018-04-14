Document.suspendHistory {#Document.suspendHistory}
=======================

> void **suspendHistory** ([string]{role="ref"} **historyString**,
> [string]{role="ref"} **javaScriptString**)

Parameters
----------

  ---------------------- ------------------------------------------------------
  **historyString**      The string to use for the history state.

  **javaScriptString**   A string of JavaScript code to execute during the
                         suspension of history.
  ---------------------- ------------------------------------------------------

Description
-----------

Provides a single history state for the entire script. Allows a single
undo for all actions taken in the script.
