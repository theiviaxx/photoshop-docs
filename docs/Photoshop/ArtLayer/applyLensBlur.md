ArtLayer.applyLensBlur {#ArtLayer.applyLensBlur}
======================

> void **applyLensBlur** ([DepthMapSource]{role="ref"} **source**, int
> **focalDistance**, bool **invertDepthMap**, [Geometry]{role="ref"}
> **shape**, int **radius**, int **bladeCurvature**, int **rotation**,
> int **brightness**, int **threshold**, int **amount**,
> [NoiseDistribution]{role="ref"} **distribution**, bool
> **monochromatic**)

Parameters
----------

  -------------------- -------------------------------------------------------------
  **source**           The source for the depth map.

  **focalDistance**    The blur focal distance (in pixels) for the depth map. RangeL
                       0 to 255. Valid only when \'source\' is transparency or layer
                       mask.

  **invertDepthMap**   If true, inverts the depth map.

  **shape**            The shape of the iris.

  **radius**           The radius of the iris. Range: 0 to 100.

  **bladeCurvature**   The blade curvature of the iris. Range: 0 to 100.

  **rotation**         The rotation of the iris (in degrees). Range: 0 to 360.

  **brightness**       The brightness for the specular highlights. Range: 0 to 100.

  **threshold**        The threshold for the specular highlights. Range: 0 to 255.

  **amount**           The amount of noise. Range: 0 to 100.

  **distribution**     The distribution value for the noise.

  **monochromatic**    If true, the noise is monochromatic.
  -------------------- -------------------------------------------------------------

Description
-----------

Apply the lens blur filter.