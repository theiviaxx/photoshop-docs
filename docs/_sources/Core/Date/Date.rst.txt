.. _Date.Date:

================================================
Date.Date
================================================

   :ref:`Date` **Date** (:ref:`number` **year**, :ref:`number` **month**, :ref:`number` **day**, :ref:`number` **hours**, :ref:`number` **min**, :ref:`number` **sec**, :ref:`number` **ms**)


Parameters
----------

+-----------+------------------------------------------------------------------------------------------------------------+
| **year**  | The year expressed in four digits.                                                                         |
+-----------+------------------------------------------------------------------------------------------------------------+
| **month** | An integer value from 0 (Jan) to 11 (Dec).                                                                 |
+-----------+------------------------------------------------------------------------------------------------------------+
| **day**   | An integer value from 1 to 31, If this argument is not supplied, its value is set to 0.                    |
+-----------+------------------------------------------------------------------------------------------------------------+
| **hours** | An integer value from 0 (midnight) to 23 (11 PM). If this argument is not supplied, its value is set to 0. |
+-----------+------------------------------------------------------------------------------------------------------------+
| **min**   | An integer value from 0 to 59. If this argument is not supplied, its value is set to 0.                    |
+-----------+------------------------------------------------------------------------------------------------------------+
| **sec**   | An Integer value from 0 to 59. If this argument is not supplied, its value is set to 0.                    |
+-----------+------------------------------------------------------------------------------------------------------------+
| **ms**    | An integer value from 0 to 999. If this argument is not supplied, its value is set to 0.                   |
+-----------+------------------------------------------------------------------------------------------------------------+



Description
-----------

Returns a new Date object holding the current date and time.

If parameters are supplied, returns a new Date object holding the supplied date and time.


