.. _$.flags:

================================================
$.flags
================================================

   :ref:`number` **flags**


Description
-----------

Gets or sets low-level debug output flags.

A logical AND of bit flag values: 0x0002 (2): Displays each line with its line number as it is executed. 0x0040 (64): Enables excessive garbage collection. Usually, garbage collection starts when the number of objects has increased by a certain amount since the last garbage collection. This flag causes ExtendScript to garbage collect after almost every statement. This impairs performance severely, but is useful when you suspect that an object gets released too soon. 0x0080 (128): Displays all calls with their arguments and the return value.  0x0100 (256): Enables extended error handling (see?strict).  0x0200 (512): Enables the localization feature of the toString method. Equivalent to the localize property.