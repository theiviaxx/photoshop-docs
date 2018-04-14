Document.convertProfile {#Document.convertProfile}
=======================

> void **convertProfile** ([string]{role="ref"} **destinationProfile**,
> [Intent]{role="ref"} **intent**, bool **blackPointCompensation**, bool
> **dither**)

Parameters
----------

  ---------------------------- ---------------------------------------------------------
  **destinationProfile**       The color profile to convert to. Either a string
                               specifying a color profile, one of the working color
                               spaces, or Lab color.

  **intent**                   The conversion intent.

  **blackPointCompensation**   If true, black point compensation is used.

  **dither**                   If true, dither is used.
  ---------------------------- ---------------------------------------------------------

Description
-----------

Converts the document from using one color profile to using another.
