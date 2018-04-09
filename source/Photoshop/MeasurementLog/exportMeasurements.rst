.. _MeasurementLog.exportMeasurements:

================================================
MeasurementLog.exportMeasurements
================================================

   void **exportMeasurements** (:ref:`File` **file**, :ref:`MeasurementRange` **range**, :ref:`string` **dataPoints**)


Parameters
----------

+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **file**       | The file to export to. If not specified, a 'file save' dialog is displayed.                                                                                                   |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **range**      | The measurements to export. Default: selected.                                                                                                                                |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **dataPoints** | An array of identifiers of data points to export. The order of the data points is respected in the exported file. Defaults to data points visible in Measurement Log palette. |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



Description
-----------

Exports the specified measurements.




