.. _ArtLayer.applyWave:

================================================
ArtLayer.applyWave
================================================

   void **applyWave** (int **generatorNumber**, int **minimumWavelength**, int **maximumWavelength**, int **minimumAmplitude**, int **maximumAmplitude**, int **horizontalScale**, int **verticalScale**, :ref:`WaveType` **waveType**, :ref:`UndefinedAreas` **undefinedAreas**, int **randomSeed**)


Parameters
----------

+-----------------------+--------------------------------------------------------------------+
| **generatorNumber**   | The number of generators. Range: 1 to 999.                         |
+-----------------------+--------------------------------------------------------------------+
| **minimumWavelength** | The minimum wave length. Range: 1 to 998.                          |
+-----------------------+--------------------------------------------------------------------+
| **maximumWavelength** | The maximum wave length. Range: 2 to (minimum wavelength + 1)      |
+-----------------------+--------------------------------------------------------------------+
| **minimumAmplitude**  | The minimum amplitude. Range: 1 to 998.                            |
+-----------------------+--------------------------------------------------------------------+
| **maximumAmplitude**  | The maximum amplitude. Range: 2 to (minimum amplitude + 1)         |
+-----------------------+--------------------------------------------------------------------+
| **horizontalScale**   | The amount of horizontal scale (as a percentage). Range: 1 to 100. |
+-----------------------+--------------------------------------------------------------------+
| **verticalScale**     | The amount of vertical scale (as a percentage). Range: 1 to 100.   |
+-----------------------+--------------------------------------------------------------------+
| **waveType**          | The wave type.                                                     |
+-----------------------+--------------------------------------------------------------------+
| **undefinedAreas**    | The treatment of areas left blank by the distortion.               |
+-----------------------+--------------------------------------------------------------------+
| **randomSeed**        | The random seed.                                                   |
+-----------------------+--------------------------------------------------------------------+



Description
-----------

Applies the wave filter.




