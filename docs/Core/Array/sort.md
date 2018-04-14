Array.sort {#Array.sort}
==========

> void **sort** ([Function]{role="ref"} **userFunction**)

Parameters
----------

  ------------------ ----------------------------------------------------------------
  **userFunction**   A user-supplied function of the form userFunction(a, b) which
                     returns less than 0 if a is greater than b, 0 if a and b are
                     equal, and greater than 0 if b is greater than a.
  ------------------ ----------------------------------------------------------------

Description
-----------

Sorts the elements of the array in place, using the given function to
compare to elements.

If no function is provided, the elements are sorted alphabetically.
Returns no return value.
