.. _ScriptUIGraphics:

================================================
ScriptUIGraphics
================================================


Description
-----------

An object used to draw custom graphics, found in the graphics property of window, container, and control objects.

Allows a script to customize aspects of the element?s appearance, such as the color and font. Use an onDraw callback function to set these properties or call the functions.All measurements are in pixels.


Properties
^^^^^^^^^^

+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`backgroundColor<ScriptUIGraphics.backgroundColor>` readonly                 | The background color for containers; for non-containers, the parent background color.                           |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`currentPath<ScriptUIGraphics.currentPath>` readonly                         | The current drawing path, encapsulated in a path object.                                                        |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`currentPoint<ScriptUIGraphics.currentPoint>` readonly                       | The current position in the current drawing path.                                                               |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`disabledBackgroundColor<ScriptUIGraphics.disabledBackgroundColor>` readonly | The background color for containers when disabled or inactive; for non-containers, the parent background color. |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`disabledForegroundColor<ScriptUIGraphics.disabledForegroundColor>` readonly | The text color when the element is disabled or inactive.                                                        |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`font<ScriptUIGraphics.font>` readonly                                       | The default font to use for displaying text.                                                                    |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`foregroundColor<ScriptUIGraphics.foregroundColor>` readonly                 | The text color.                                                                                                 |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

Static Properties
^^^^^^^^^^^^^^^^^

+-------------------------------------------------------+------------------------------------------------------------------------+
| :ref:`BrushType<ScriptUIGraphics.BrushType>` readonly | Contains the enumerated constants for the type argument of?newBrush(). |
+-------------------------------------------------------+------------------------------------------------------------------------+
| :ref:`PenType<ScriptUIGraphics.PenType>` readonly     | Contains the enumerated constants for the type argument of?newPen().   |
+-------------------------------------------------------+------------------------------------------------------------------------+





Methods
^^^^^^^

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`closePath<ScriptUIGraphics.closePath>` readonly         | Closes the current path.                                                                                                                                  |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`drawFocusRing<ScriptUIGraphics.drawFocusRing>` readonly | Draws a focus ring within a region of this element.                                                                                                       |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`drawImage<ScriptUIGraphics.drawImage>` readonly         | Draws an image within a given region of the element.                                                                                                      |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`drawOSControl<ScriptUIGraphics.drawOSControl>` readonly | Draw the platform-specific control associated with this element.                                                                                          |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`drawString<ScriptUIGraphics.drawString>` readonly       | Draw a string of text starting at a given point in this element, using a given drawing pen and font.                                                      |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`ellipsePath<ScriptUIGraphics.ellipsePath>` readonly     | Defines an elliptical path within a given rectangular area in the?currentPath?object, which can be filled using?fillPath()?or stroked using?strokePath(). |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`fillPath<ScriptUIGraphics.fillPath>` readonly           | Fills a path using a given painting brush.                                                                                                                |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`lineTo<ScriptUIGraphics.lineTo>` readonly               | Adds a path segment to the?currentPath.                                                                                                                   |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`measureString<ScriptUIGraphics.measureString>` readonly | Calculates the size needed to display a string using the given font.                                                                                      |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`moveTo<ScriptUIGraphics.moveTo>` readonly               | Adds a given point to the?currentPath, and makes it the current drawing position.                                                                         |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`newBrush<ScriptUIGraphics.newBrush>` readonly           | Creates a new painting brush object.                                                                                                                      |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`newPath<ScriptUIGraphics.newPath>` readonly             | Creates a new, empty path object.                                                                                                                         |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`newPen<ScriptUIGraphics.newPen>` readonly               | Creates a new drawing pen object.                                                                                                                         |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`rectPath<ScriptUIGraphics.rectPath>` readonly           | Defines a rectangular path in the?currentPath?object.                                                                                                     |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`strokePath<ScriptUIGraphics.strokePath>` readonly       | Strokes the path segments of a path with a given drawing pen.                                                                                             |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+






.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      ScriptUIGraphics/backgroundColor.rst
      ScriptUIGraphics/disabledBackgroundColor.rst
      ScriptUIGraphics/disabledForegroundColor.rst
      ScriptUIGraphics/font.rst
      ScriptUIGraphics/foregroundColor.rst
      ScriptUIGraphics/currentPath.rst
      ScriptUIGraphics/currentPoint.rst
      
      ScriptUIGraphics/BrushType.rst
      ScriptUIGraphics/PenType.rst
      

      ScriptUIGraphics/newBrush.rst
      ScriptUIGraphics/newPen.rst
      ScriptUIGraphics/newPath.rst
      ScriptUIGraphics/closePath.rst
      ScriptUIGraphics/moveTo.rst
      ScriptUIGraphics/lineTo.rst
      ScriptUIGraphics/rectPath.rst
      ScriptUIGraphics/ellipsePath.rst
      ScriptUIGraphics/strokePath.rst
      ScriptUIGraphics/fillPath.rst
      ScriptUIGraphics/drawFocusRing.rst
      ScriptUIGraphics/drawImage.rst
      ScriptUIGraphics/drawOSControl.rst
      ScriptUIGraphics/drawString.rst
      ScriptUIGraphics/measureString.rst
      
      
      
      