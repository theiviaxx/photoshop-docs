global.parseFloat {#global.parseFloat}
=================

> [number]{role="ref"} **parseFloat** ([string]{role="ref"} **text**)

Parameters
----------

  ---------- -----------------------------------------------------------
  **text**   The string from which to extract a floating point number.
  ---------- -----------------------------------------------------------

Description
-----------

Extracts a floating-point number from a string.

Parses a string to find the first set of characters that can be
converted to a floating point number, and returns that number, or NaN if
it does not encounter characters that it can converted to a number. The
function supports exponential notation.
