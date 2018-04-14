\$.sleep {#$.sleep}
========

> void **sleep** ([number]{role="ref"} **msecs**)

Parameters
----------

  ----------- ----------------------------------
  **msecs**   Number of milliseconds to sleep.
  ----------- ----------------------------------

Description
-----------

Suspends the calling thread for a number of milliseconds.

During a sleep period, checks at 100 millisecond intervals to see
whether the sleep should be terminated. This can happen if there is a
break request, or if the script timeout has expired.
