ScriptUIGraphics {#ScriptUIGraphics}
================

Description
-----------

An object used to draw custom graphics, found in the graphics property
of window, container, and control objects.

Allows a script to customize aspects of the element?s appearance, such
as the color and font. Use an onDraw callback function to set these
properties or call the functions.All measurements are in pixels.

### Properties

  ----------------------------------------------------------------------------------- ----------------------------------------
  [backgroundColor\<ScriptUIGraphics.backgroundColor\>]{role="ref"} readonly          The background color for containers; for
                                                                                      non-containers, the parent background
                                                                                      color.

  [currentPath\<ScriptUIGraphics.currentPath\>]{role="ref"} readonly                  The current drawing path, encapsulated
                                                                                      in a path object.

  [currentPoint\<ScriptUIGraphics.currentPoint\>]{role="ref"} readonly                The current position in the current
                                                                                      drawing path.

  [disabledBackgroundColor\<ScriptUIGraphics.disabledBackgroundColor\>]{role="ref"}   The background color for containers when
  readonly                                                                            disabled or inactive; for
                                                                                      non-containers, the parent background
                                                                                      color.

  [disabledForegroundColor\<ScriptUIGraphics.disabledForegroundColor\>]{role="ref"}   The text color when the element is
  readonly                                                                            disabled or inactive.

  [font\<ScriptUIGraphics.font\>]{role="ref"} readonly                                The default font to use for displaying
                                                                                      text.

  [foregroundColor\<ScriptUIGraphics.foregroundColor\>]{role="ref"} readonly          The text color.
  ----------------------------------------------------------------------------------- ----------------------------------------

### Static Properties

  ------------------------------------------------------- ----------------------------------------
  [BrushType\<ScriptUIGraphics.BrushType\>]{role="ref"}   Contains the enumerated constants for
  readonly                                                the type argument of?newBrush().

  [PenType\<ScriptUIGraphics.PenType\>]{role="ref"}       Contains the enumerated constants for
  readonly                                                the type argument of?newPen().
  ------------------------------------------------------- ----------------------------------------

### Methods

  --------------------------------------------------------------- --------------------------------------------------
  [closePath\<ScriptUIGraphics.closePath\>]{role="ref"} readonly  Closes the current path.

  [drawFocusRing\<ScriptUIGraphics.drawFocusRing\>]{role="ref"}   Draws a focus ring within a region of this
  readonly                                                        element.

  [drawImage\<ScriptUIGraphics.drawImage\>]{role="ref"} readonly  Draws an image within a given region of the
                                                                  element.

  [drawOSControl\<ScriptUIGraphics.drawOSControl\>]{role="ref"}   Draw the platform-specific control associated with
  readonly                                                        this element.

  [drawString\<ScriptUIGraphics.drawString\>]{role="ref"}         Draw a string of text starting at a given point in
  readonly                                                        this element, using a given drawing pen and font.

  [ellipsePath\<ScriptUIGraphics.ellipsePath\>]{role="ref"}       Defines an elliptical path within a given
  readonly                                                        rectangular area in the?currentPath?object, which
                                                                  can be filled using?fillPath()?or stroked
                                                                  using?strokePath().

  [fillPath\<ScriptUIGraphics.fillPath\>]{role="ref"} readonly    Fills a path using a given painting brush.

  [lineTo\<ScriptUIGraphics.lineTo\>]{role="ref"} readonly        Adds a path segment to the?currentPath.

  [measureString\<ScriptUIGraphics.measureString\>]{role="ref"}   Calculates the size needed to display a string
  readonly                                                        using the given font.

  [moveTo\<ScriptUIGraphics.moveTo\>]{role="ref"} readonly        Adds a given point to the?currentPath, and makes
                                                                  it the current drawing position.

  [newBrush\<ScriptUIGraphics.newBrush\>]{role="ref"} readonly    Creates a new painting brush object.

  [newPath\<ScriptUIGraphics.newPath\>]{role="ref"} readonly      Creates a new, empty path object.

  [newPen\<ScriptUIGraphics.newPen\>]{role="ref"} readonly        Creates a new drawing pen object.

  [rectPath\<ScriptUIGraphics.rectPath\>]{role="ref"} readonly    Defines a rectangular path in
                                                                  the?currentPath?object.

  [strokePath\<ScriptUIGraphics.strokePath\>]{role="ref"}         Strokes the path segments of a path with a given
  readonly                                                        drawing pen.
  --------------------------------------------------------------- --------------------------------------------------

::: {.container .hide}
::: {.toctree}
ScriptUIGraphics/backgroundColor.rst
ScriptUIGraphics/disabledBackgroundColor.rst
ScriptUIGraphics/disabledForegroundColor.rst ScriptUIGraphics/font.rst
ScriptUIGraphics/foregroundColor.rst ScriptUIGraphics/currentPath.rst
ScriptUIGraphics/currentPoint.rst

ScriptUIGraphics/BrushType.rst ScriptUIGraphics/PenType.rst

ScriptUIGraphics/newBrush.rst ScriptUIGraphics/newPen.rst
ScriptUIGraphics/newPath.rst ScriptUIGraphics/closePath.rst
ScriptUIGraphics/moveTo.rst ScriptUIGraphics/lineTo.rst
ScriptUIGraphics/rectPath.rst ScriptUIGraphics/ellipsePath.rst
ScriptUIGraphics/strokePath.rst ScriptUIGraphics/fillPath.rst
ScriptUIGraphics/drawFocusRing.rst ScriptUIGraphics/drawImage.rst
ScriptUIGraphics/drawOSControl.rst ScriptUIGraphics/drawString.rst
ScriptUIGraphics/measureString.rst
:::
:::
