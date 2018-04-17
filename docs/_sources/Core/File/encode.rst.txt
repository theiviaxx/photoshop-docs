.. _File.encode:

================================================
File.encode
================================================

   :ref:`string` **encode** (:ref:`string` **name**)


Parameters
----------

+----------+-----------------------+
| **name** | The string to encode. |
+----------+-----------------------+



Description
-----------

Encodes a string as required by RFC 2396, and returns the encoded string.

All special characters are encoded in UTF-8 and stored as escaped characters starting with the percent sign followed by two hexadecimal digits. For example, the string "my file" is encoded as "my%20file". Special characters are those with a numeric value greater than 127, except the following: / - _ . ! ~ * ' ( ) See also?encodeURI().


