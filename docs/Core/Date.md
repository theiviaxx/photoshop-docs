Date {#Date}
====

Description
-----------

A date/time object.

### Constructors

  --------------------------------- ----------------------------------------------
  [Date\<Date.Date\>]{role="ref"}   Returns a new Date object holding the current
  readonly                          date and time.
  --------------------------------- ----------------------------------------------

### Methods

  ------------------------------------------------------------- ------------------------------------------------
  [getDate\<Date.getDate\>]{role="ref"} readonly                Returns the day of the month of the specified
                                                                Date object in local time.

  [getDay\<Date.getDay\>]{role="ref"} readonly                  Returns the day of the week for the specified
                                                                Date object in local time.

  [getFullYear\<Date.getFullYear\>]{role="ref"} readonly        Returns the four digit year of the specified
                                                                Date object in local time.

  [getHours\<Date.getHours\>]{role="ref"} readonly              Returns the hour of the specified Date object in
                                                                local time.

  [getMilliseconds\<Date.getMilliseconds\>]{role="ref"}         Returns the milliseconds of the specified Date
  readonly                                                      object in local time.

  [getMinutes\<Date.getMinutes\>]{role="ref"} readonly          Returns the minutes of the specified Date object
                                                                in local time.

  [getMonth\<Date.getMonth\>]{role="ref"} readonly              Returns the month of the specified Date object
                                                                in local time.

  [getSeconds\<Date.getSeconds\>]{role="ref"} readonly          Returns the seconds of the specified Date object
                                                                in local time.

  [getTime\<Date.getTime\>]{role="ref"} readonly                Returns the number of milliseconds since
                                                                midnight January 1,1970 UTC for the specified
                                                                Date object.

  [getTimezoneOffset\<Date.getTimezoneOffset\>]{role="ref"}     Returns the difference in minutes between the
  readonly                                                      computer\'s local time and UTC.

  [getUTCDate\<Date.getUTCDate\>]{role="ref"} readonly          Returns the day of the month of the specified
                                                                Date object according to UTC.

  [getUTCDay\<Date.getUTCDay\>]{role="ref"} readonly            Returns the day of the week for the specified
                                                                Date object according to UTC.

  [getUTCFullYear\<Date.getUTCFullYear\>]{role="ref"} readonly  Returns the four digit year of the specified
                                                                Date object according to UTC.

  [getUTCHours\<Date.getUTCHours\>]{role="ref"} readonly        Returns the hour of the specified Date object
                                                                according to UTC.

  [getUTCMilliseconds\<Date.getUTCMilliseconds\>]{role="ref"}   Returns the milliseconds of the specified Date
  readonly                                                      object according to UTC.

  [getUTCMinutes\<Date.getUTCMinutes\>]{role="ref"} readonly    Returns the minutes of the specified Date object
                                                                according to UTC.

  [getUTCMonth\<Date.getUTCMonth\>]{role="ref"} readonly        Returns the month of the specified Date object
                                                                according to UTC.

  [getUTCSeconds\<Date.getUTCSeconds\>]{role="ref"} readonly    Returns the seconds of the specified Date object
                                                                according to UTC.

  [getYear\<Date.getYear\>]{role="ref"} readonly                Returns the year of the specified Date object,
                                                                as a difference from 1900, in local time.

  [setDate\<Date.setDate\>]{role="ref"} readonly                Sets the day of the month of a specified Date
                                                                object according to local time.

  [setFullYear\<Date.setFullYear\>]{role="ref"} readonly        Sets the year of a specified Date object
                                                                according to local time.

  [setHours\<Date.setHours\>]{role="ref"} readonly              Sets the hours of a specified Date object
                                                                according to local time.

  [setMilliseconds\<Date.setMilliseconds\>]{role="ref"}         Sets the milliseconds of a specified Date object
  readonly                                                      according to local time.

  [setMinutes\<Date.setMinutes\>]{role="ref"} readonly          Sets the minutes of a specified Date object
                                                                according to local time.

  [setMonth\<Date.setMonth\>]{role="ref"} readonly              Sets the month of a specified Date object
                                                                according to local time.

  [setSeconds\<Date.setSeconds\>]{role="ref"} readonly          Sets the seconds of a specified Date object
                                                                according to local time.

  [setTime\<Date.setTime\>]{role="ref"} readonly                Sets the date of a specified Date object in
                                                                milliseconds since midnight, January 1, 1970.

  [setUTCDate\<Date.setUTCDate\>]{role="ref"} readonly          Sets the date of a specified Date object
                                                                according to universal time.

  [setUTCFullYear\<Date.setUTCFullYear\>]{role="ref"} readonly  Sets the year of a specified Date object
                                                                according to UTC, can also set the month and
                                                                date.

  [setUTCHours\<Date.setUTCHours\>]{role="ref"} readonly        Sets the hours of a specified Date object
                                                                according to UTC.

  [setUTCMilliseconds\<Date.setUTCMilliseconds\>]{role="ref"}   Sets the milliseconds of a specified Date object
  readonly                                                      according to UTC.

  [setUTCMinutes\<Date.setUTCMinutes\>]{role="ref"} readonly    Sets the minutes of a specified Date object
                                                                according to UTC.

  [setUTCMonth\<Date.setUTCMonth\>]{role="ref"} readonly        Sets the month of a specified Date object
                                                                according to UTC.

  [setUTCSeconds\<Date.setUTCSeconds\>]{role="ref"} readonly    Sets the seconds of a specified Date object
                                                                according to UTC.

  [setYear\<Date.setYear\>]{role="ref"} readonly                Sets the year of a specified Date object
                                                                according to local time, as a difference between
                                                                the current year and 1900.

  [toDateString\<Date.toDateString\>]{role="ref"} readonly      

  [toGMTString\<Date.toGMTString\>]{role="ref"} readonly        

  [toLocaleDateString\<Date.toLocaleDateString\>]{role="ref"}   
  readonly                                                      

  [toLocaleString\<Date.toLocaleString\>]{role="ref"} readonly  

  [toLocaleTimeString\<Date.toLocaleTimeString\>]{role="ref"}   
  readonly                                                      

  [toSource\<Date.toSource\>]{role="ref"} readonly              Creates a string representation of this object
                                                                that can be fed back to?eval()?to re-create an
                                                                object. Works only with built-in classes.

  [toString\<Date.toString\>]{role="ref"} readonly              Returns a string value representing the date and
                                                                time stored in the Date object in human readable
                                                                format.

  [toTimeString\<Date.toTimeString\>]{role="ref"} readonly      

  [toUTCString\<Date.toUTCString\>]{role="ref"} readonly        

  [valueOf\<Date.valueOf\>]{role="ref"} readonly                The valueOf() method returns the number of
                                                                milliseconds that have passed since midnight,
                                                                Returns an integer.
  ------------------------------------------------------------- ------------------------------------------------

### Static Methods

  ----------------------------------- ------------------------------------------------------
  [UTC\<Date.UTC\>]{role="ref"}       Returns the number of milliseconds between midnight
  readonly                            January 1, 1970, UTC, and the specified time.

  [parse\<Date.parse\>]{role="ref"}   Parses a string, returning a new Date object. The
  readonly                            string should be similar to the string returned bt
                                      toString().
  ----------------------------------- ------------------------------------------------------

::: {.container .hide}
::: {.toctree}
Date/getDate.rst Date/getDay.rst Date/getYear.rst Date/getFullYear.rst
Date/getHours.rst Date/getMilliseconds.rst Date/getMinutes.rst
Date/getMonth.rst Date/getSeconds.rst Date/getTime.rst
Date/getTimezoneOffset.rst Date/getUTCDate.rst Date/getUTCDay.rst
Date/getUTCFullYear.rst Date/getUTCHours.rst Date/getUTCMilliseconds.rst
Date/getUTCMinutes.rst Date/getUTCMonth.rst Date/getUTCSeconds.rst
Date/setDate.rst Date/setFullYear.rst Date/setHours.rst
Date/setMilliseconds.rst Date/setMinutes.rst Date/setSeconds.rst
Date/setMonth.rst Date/setUTCDate.rst Date/setUTCFullYear.rst
Date/setUTCHours.rst Date/setUTCMilliseconds.rst Date/setUTCMinutes.rst
Date/setUTCSeconds.rst Date/setUTCMonth.rst Date/setTime.rst
Date/setYear.rst Date/toDateString.rst Date/toTimeString.rst
Date/toLocaleString.rst Date/toLocaleDateString.rst
Date/toLocaleTimeString.rst Date/toGMTString.rst Date/toUTCString.rst
Date/toString.rst Date/valueOf.rst Date/toSource.rst

Date/parse.rst Date/UTC.rst

Date/Date.rst
:::
:::
