ArtLayer.applyDisplace {#ArtLayer.applyDisplace}
======================

> void **applyDisplace** (int **horizontalScale**, int
> **verticalScale**, [DisplacementMapType]{role="ref"}
> **displacementType**, [UndefinedAreas]{role="ref"} **undefinedAreas**,
> [File]{role="ref"} **displacementMapFile**)

Parameters
----------

  ------------------------- -------------------------------------------------
  **horizontalScale**       The amount of horizontal distortion. Range: -999
                            to 999.

  **verticalScale**         The amount of vertical distortion. Range: -999 to
                            999.

  **displacementType**      The displacement type.

  **undefinedAreas**        The treatment of undistorted areas.

  **displacementMapFile**   The distortion image map.
  ------------------------- -------------------------------------------------

Description
-----------

Applies the displace filter.
