MeasurementLog.exportMeasurements {#MeasurementLog.exportMeasurements}
=================================

> void **exportMeasurements** ([File]{role="ref"} **file**,
> [MeasurementRange]{role="ref"} **range**, [string]{role="ref"}
> **dataPoints**)

Parameters
----------

  ---------------- ----------------------------------------------------------------
  **file**         The file to export to. If not specified, a \'file save\' dialog
                   is displayed.

  **range**        The measurements to export. Default: selected.

  **dataPoints**   An array of identifiers of data points to export. The order of
                   the data points is respected in the exported file. Defaults to
                   data points visible in Measurement Log palette.
  ---------------- ----------------------------------------------------------------

Description
-----------

Exports the specified measurements.
