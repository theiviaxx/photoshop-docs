ArtLayer.applyAddNoise {#ArtLayer.applyAddNoise}
======================

> void **applyAddNoise** ([number]{role="ref"} **amount**,
> [NoiseDistribution]{role="ref"} **distribution**, bool
> **monochromatic**)

Parameters
----------

  ------------------- -----------------------------------------------------------
  **amount**          The amount of noise (as a percentage). Range: 0.1 to 400.0.

  **distribution**    The noise distribution type.

  **monochromatic**   If true, applies the filter only to the tonal elements in
                      the image without changing the colors.
  ------------------- -----------------------------------------------------------

Description
-----------

Applies the add noise filter.
