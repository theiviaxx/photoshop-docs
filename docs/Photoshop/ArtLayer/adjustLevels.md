ArtLayer.adjustLevels {#ArtLayer.adjustLevels}
=====================

> void **adjustLevels** (int **inputRangeStart**, int **inputRangeEnd**,
> [number]{role="ref"} **inputRangeGamma**, int **outputRangeStart**,
> int **outputRangeEnd**)

Parameters
----------

  ---------------------- -----------------------------------------------------
  **inputRangeStart**    The input levels minimum. Range: 0 to 253.

  **inputRangeEnd**      The input levels maximum. Range: (input range start +
                         2) to 253.

  **inputRangeGamma**    The input levels gamma. Range: 0.10 to 9.99.

  **outputRangeStart**   The output levels minimum. Range: 0 to 253.

  **outputRangeEnd**     The output levels maximum. Range: (output range start
                         + 2) to 253.
  ---------------------- -----------------------------------------------------

Description
-----------

Adjusts levels of the selected channels.
