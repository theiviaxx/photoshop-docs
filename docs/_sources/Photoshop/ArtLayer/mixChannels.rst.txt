.. _ArtLayer.mixChannels:

================================================
ArtLayer.mixChannels
================================================

   void **mixChannels** (any **outputChannels**, bool **monochrome**)


Parameters
----------

+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **outputChannels** | A list of channel specifications. For each component channel that the document has, you must specify a list of adjustment values followed by a 'constant' value. |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **monochrome**     | If true, uses monochrome mixing. Note: If this is true, you can only specify one channel value.                                                                  |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+



Description
-----------

Modifies a targeted (output) color channel using a mix of the existing color channels in the image. (output channels = An array of channel specifications. For each component channel, specify a list of adjustment values (-200 to 200) followed by a 'constant' value (-200 to 200).) When monochrome = true, the maximum number of channel value specifications is 1. Valid only when 'document mode' = RGB or CMYK. RGB arrays must include four doubles. CMYK arrays must include five doubles.




