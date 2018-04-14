Date.Date {#Date.Date}
=========

> [Date]{role="ref"} **Date** ([number]{role="ref"} **year**,
> [number]{role="ref"} **month**, [number]{role="ref"} **day**,
> [number]{role="ref"} **hours**, [number]{role="ref"} **min**,
> [number]{role="ref"} **sec**, [number]{role="ref"} **ms**)

Parameters
----------

  ----------- ---------------------------------------------------------------
  **year**    The year expressed in four digits.

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

Returns a new Date object holding the current date and time.

If parameters are supplied, returns a new Date object holding the
supplied date and time.
