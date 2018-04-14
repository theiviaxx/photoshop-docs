.. _UnitValue:

================================================
UnitValue
================================================


Description
-----------

Represents a measurement as a combination of values and unit.

Note that this object is not available in all applications.


Properties
^^^^^^^^^^

+----------------------------------------------+--------------------+
| :ref:`baseUnit<UnitValue.baseUnit>` readonly | The base unit.     |
+----------------------------------------------+--------------------+
| :ref:`type<UnitValue.type>` readonly         | The unit name.     |
+----------------------------------------------+--------------------+
| :ref:`value<UnitValue.value>` readonly       | The numeric value. |
+----------------------------------------------+--------------------+

Static Properties
^^^^^^^^^^^^^^^^^

+----------------------------------------------+------------------------------------+
| :ref:`baseUnit<UnitValue.baseUnit>` readonly | The base unit for all conversions. |
+----------------------------------------------+------------------------------------+





Methods
^^^^^^^

+--------------------------------------------+---------------------------------------------+
| :ref:`as<UnitValue.as>` readonly           | Returns this instance as a different unit.  |
+--------------------------------------------+---------------------------------------------+
| :ref:`convert<UnitValue.convert>` readonly | Converts this instance to a different unit. |
+--------------------------------------------+---------------------------------------------+






.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      UnitValue/type.rst
      UnitValue/value.rst
      UnitValue/baseUnit.rst
      
      UnitValue/baseUnit.rst
      

      UnitValue/convert.rst
      UnitValue/as.rst
      
      
      
      