Date.UTC {#Date.UTC}
========

> [Date]{role="ref"} **UTC** ([number]{role="ref"} **year**,
> [number]{role="ref"} **month**, [number]{role="ref"} **day**,
> [number]{role="ref"} **hours**, [number]{role="ref"} **min**,
> [number]{role="ref"} **sec**, [number]{role="ref"} **ms**)

Parameters
----------

  ----------- ---------------------------------------------------------------
  **year**    The year expressed in four digits, for example, 2001.

  **month**   An integer value from 0 (Jan) to 11 (Dec).

  **day**     An integer value from 1 to 31, If this argument is not
              supplied, its value is set to 0.

  **hours**   An integer value from 0 (midnight) to 23 (11 PM). If this
              argument is not supplied, its value is set to 0.

  **min**     An integer value from 0 to 59. If this argument is not
              supplied, its value is set to 0.

  **sec**     An Integer value from 0 to 59. If this argument is not
              supplied, its value is set to 0.

  **ms**      An integer value from 0 to 999. If this argument is not
              supplied, its value is set to 0.
  ----------- ---------------------------------------------------------------

Description
-----------

Returns the number of milliseconds between midnight January 1, 1970,
UTC, and the specified time.
