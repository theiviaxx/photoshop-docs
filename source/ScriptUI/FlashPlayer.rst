.. _FlashPlayer:

================================================
FlashPlayer
================================================


Description
-----------

A control that contains a Flash Player, which can load and play Flash movies stored in SWF files.

The ScriptUI FlashPlayer element runs the Flash application within an Adobe application. The Flash application runs ActionScript, a different implementation of JavaScript from the ExtendScript version of JavaScript that Adobe applications run. A control object of this type contains functions that allow your script to load SWF files, control movie playback, and communicate with the ActionScript environment.


Properties
^^^^^^^^^^

+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`active<FlashPlayer.active>` readonly               | True if this element is active.                                                                                              |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`alignment<FlashPlayer.alignment>` readonly         | The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.   |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bounds<FlashPlayer.bounds>` readonly               | The boundaries of the element, in parent-relative coordinates.                                                               |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`enabled<FlashPlayer.enabled>` readonly             | True if this element is enabled.                                                                                             |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`helpTip<FlashPlayer.helpTip>` readonly             | The help text that is displayed when the mouse hovers over the element.                                                      |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`indent<FlashPlayer.indent>` readonly               | The number of pixels to indent the element during automatic layout.                                                          |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`location<FlashPlayer.location>` readonly           | The upper left corner of this element relative to its parent.                                                                |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`maximumSize<FlashPlayer.maximumSize>` readonly     | The maximum height and width to which the element can be resized.                                                            |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`minimumSize<FlashPlayer.minimumSize>` readonly     | The minimum height and width to which the element can be resized.                                                            |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<FlashPlayer.parent>` readonly               | The parent element.                                                                                                          |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preferredSize<FlashPlayer.preferredSize>` readonly | The preferred size, used by layout managers to determine the best size for each element.                                     |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`properties<FlashPlayer.properties>` readonly       | An object that contains one or more creation properties of the container (properties used only when the element is created). |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`size<FlashPlayer.size>` readonly                   | The current dimensions of this element.                                                                                      |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`type<FlashPlayer.type>` readonly                   | The element type, "flashplayer".                                                                                             |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<FlashPlayer.visible>` readonly             | True if this element is shown, false if it is hidden.                                                                        |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`window<FlashPlayer.window>` readonly               | The window that this element belongs to.                                                                                     |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`windowBounds<FlashPlayer.windowBounds>` readonly   | The bounds of this element relative to the top-level parent window.                                                          |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`addEventListener<FlashPlayer.addEventListener>` readonly         | Registers an event handler for a particular type of event occuring in this element.   |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`dispatchEvent<FlashPlayer.dispatchEvent>` readonly               | Simulates the occurrence of an event in this target.                                  |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`hide<FlashPlayer.hide>` readonly                                 | Hides this element.                                                                   |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`invokePlayerFunction<FlashPlayer.invokePlayerFunction>` readonly | Invokes an ActionScript function defined in the Flash application.                    |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`loadMovie<FlashPlayer.loadMovie>` readonly                       | Loads a movie into the Flash Player, and begins playing it.                           |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`notify<FlashPlayer.notify>` readonly                             | Sends a notification message, simulating the specified user interaction event.        |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`playMovie<FlashPlayer.playMovie>` readonly                       | Restarts a movie that has been stopped.                                               |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`removeEventListener<FlashPlayer.removeEventListener>` readonly   | Unregisters an event handler for a particular type of event occuring in this element. |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`show<FlashPlayer.show>` readonly                                 | Shows this element.                                                                   |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| :ref:`stopMovie<FlashPlayer.stopMovie>` readonly                       | Halts playback of the current movie.                                                  |
+------------------------------------------------------------------------+---------------------------------------------------------------------------------------+



Events
^^^^^^

+------------------------------------------------+-------------------------------------------------------------------------------+
| :ref:`callback<FlashPlayer.callback>` readonly | A function definition for a callback from the Flash ActionScript environment. |
+------------------------------------------------+-------------------------------------------------------------------------------+


.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      FlashPlayer/active.rst
      FlashPlayer/visible.rst
      FlashPlayer/bounds.rst
      FlashPlayer/location.rst
      FlashPlayer/maximumSize.rst
      FlashPlayer/minimumSize.rst
      FlashPlayer/preferredSize.rst
      FlashPlayer/size.rst
      FlashPlayer/windowBounds.rst
      FlashPlayer/alignment.rst
      FlashPlayer/properties.rst
      FlashPlayer/enabled.rst
      FlashPlayer/helpTip.rst
      FlashPlayer/indent.rst
      FlashPlayer/parent.rst
      FlashPlayer/window.rst
      FlashPlayer/type.rst
      
      

      FlashPlayer/invokePlayerFunction.rst
      FlashPlayer/loadMovie.rst
      FlashPlayer/playMovie.rst
      FlashPlayer/stopMovie.rst
      FlashPlayer/notify.rst
      FlashPlayer/show.rst
      FlashPlayer/hide.rst
      FlashPlayer/addEventListener.rst
      FlashPlayer/removeEventListener.rst
      FlashPlayer/dispatchEvent.rst
      
      
      FlashPlayer/callback.rst
      
      