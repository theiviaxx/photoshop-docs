.. _ArtLayer.shadowHighlight:

================================================
ArtLayer.shadowHighlight
================================================

   void **shadowHighlight** (int **shadowAmount**, int **shadowWidth**, int **shadowRaduis**, int **highlightAmount**, int **highlightWidth**, int **highlightRaduis**, int **colorCorrection**, int **midtoneContrast**, :ref:`number` **blackClip**, :ref:`number` **whiteClip**)


Parameters
----------

+---------------------+-------------------------------------------------------------------------------------------------+
| **shadowAmount**    | The shadow amount, as a percentage. Range: 0 to 100.                                            |
+---------------------+-------------------------------------------------------------------------------------------------+
| **shadowWidth**     | The shadow width, as a percentage. Range: 0 to 100 for tonal width (0 = narrow), (100 = broad). |
+---------------------+-------------------------------------------------------------------------------------------------+
| **shadowRaduis**    | The shadow radius (in pixels). Range: 0 to 2500.                                                |
+---------------------+-------------------------------------------------------------------------------------------------+
| **highlightAmount** | The highlight amount, as a percentage. Range: 0 to 100.                                         |
+---------------------+-------------------------------------------------------------------------------------------------+
| **highlightWidth**  | The highlight width. Range: 0 to 100 for tonal width (0 = narrow), (100 = broad).               |
+---------------------+-------------------------------------------------------------------------------------------------+
| **highlightRaduis** | The highlight radius (in pixels). Range: 0 to 2500.                                             |
+---------------------+-------------------------------------------------------------------------------------------------+
| **colorCorrection** | The amount to adjust the colors in the changed portion of the image. Range: -100 to 100.        |
+---------------------+-------------------------------------------------------------------------------------------------+
| **midtoneContrast** | The amount of midtone contrast. Range: -100 to 100.                                             |
+---------------------+-------------------------------------------------------------------------------------------------+
| **blackClip**       | Fractions of whites to be clipped. Range: 0.000 to 50.000.                                      |
+---------------------+-------------------------------------------------------------------------------------------------+
| **whiteClip**       | Fractions of blacks to be clipped. Range: 0.000 to 50.000.                                      |
+---------------------+-------------------------------------------------------------------------------------------------+



Description
-----------

Adjusts the range of tones in the shadows and highlights.




