.. _BitmapConversionOptions:

================================================
BitmapConversionOptions
================================================


Description
-----------

Options for changing the document mode to Bitmap.






Static Properties
^^^^^^^^^^^^^^^^^

+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`angle<BitmapConversionOptions.angle>` readonly             | The angle (in degrees) at which to orient individual dots. Valid only when 'method' = halftone screen. Range: -180 to 180. |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`frequency<BitmapConversionOptions.frequency>` readonly     | The number of printer dots per inch. Valid only when 'method' = halftone screen. Range: 1.0 to 999.99.                     |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`method<BitmapConversionOptions.method>` readonly           | The conversion method.                                                                                                     |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`patternName<BitmapConversionOptions.patternName>` readonly | The name of the pattern to use. Valid only when 'method' = custom.                                                         |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`resolution<BitmapConversionOptions.resolution>` readonly   | The output resolution (in pixels per inch)                                                                                 |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`shape<BitmapConversionOptions.shape>` readonly             | The dot shape. Valid only when 'method' = halftone screen.                                                                 |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      BitmapConversionOptions/resolution.rst
      BitmapConversionOptions/method.rst
      BitmapConversionOptions/patternName.rst
      BitmapConversionOptions/frequency.rst
      BitmapConversionOptions/angle.rst
      BitmapConversionOptions/shape.rst
      

      
      
      
      