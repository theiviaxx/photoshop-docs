FlashPlayer {#FlashPlayer}
===========

Description
-----------

A control that contains a Flash Player, which can load and play Flash
movies stored in SWF files.

The ScriptUI FlashPlayer element runs the Flash application within an
Adobe application. The Flash application runs ActionScript, a different
implementation of JavaScript from the ExtendScript version of JavaScript
that Adobe applications run. A control object of this type contains
functions that allow your script to load SWF files, control movie
playback, and communicate with the ActionScript environment.

### Properties

  ---------------------------------------------------------- ------------------------------------------------
  [active\<FlashPlayer.active\>]{role="ref"} readonly        True if this element is active.

  [alignment\<FlashPlayer.alignment\>]{role="ref"} readonly  The alignment style for this element. If
                                                             defined, this value overrides the alignChildren
                                                             setting for the parent container.

  [bounds\<FlashPlayer.bounds\>]{role="ref"} readonly        The boundaries of the element, in
                                                             parent-relative coordinates.

  [enabled\<FlashPlayer.enabled\>]{role="ref"} readonly      True if this element is enabled.

  [helpTip\<FlashPlayer.helpTip\>]{role="ref"} readonly      The help text that is displayed when the mouse
                                                             hovers over the element.

  [indent\<FlashPlayer.indent\>]{role="ref"} readonly        The number of pixels to indent the element
                                                             during automatic layout.

  [location\<FlashPlayer.location\>]{role="ref"} readonly    The upper left corner of this element relative
                                                             to its parent.

  [maximumSize\<FlashPlayer.maximumSize\>]{role="ref"}       The maximum height and width to which the
  readonly                                                   element can be resized.

  [minimumSize\<FlashPlayer.minimumSize\>]{role="ref"}       The minimum height and width to which the
  readonly                                                   element can be resized.

  [parent\<FlashPlayer.parent\>]{role="ref"} readonly        The parent element.

  [preferredSize\<FlashPlayer.preferredSize\>]{role="ref"}   The preferred size, used by layout managers to
  readonly                                                   determine the best size for each element.

  [properties\<FlashPlayer.properties\>]{role="ref"}         An object that contains one or more creation
  readonly                                                   properties of the container (properties used
                                                             only when the element is created).

  [size\<FlashPlayer.size\>]{role="ref"} readonly            The current dimensions of this element.

  [type\<FlashPlayer.type\>]{role="ref"} readonly            The element type, \"flashplayer\".

  [visible\<FlashPlayer.visible\>]{role="ref"} readonly      True if this element is shown, false if it is
                                                             hidden.

  [window\<FlashPlayer.window\>]{role="ref"} readonly        The window that this element belongs to.

  [windowBounds\<FlashPlayer.windowBounds\>]{role="ref"}     The bounds of this element relative to the
  readonly                                                   top-level parent window.
  ---------------------------------------------------------- ------------------------------------------------

### Methods

  ------------------------------------------------------------------------ --------------------------------------
  [addEventListener\<FlashPlayer.addEventListener\>]{role="ref"} readonly  Registers an event handler for a
                                                                           particular type of event occuring in
                                                                           this element.

  [dispatchEvent\<FlashPlayer.dispatchEvent\>]{role="ref"} readonly        Simulates the occurrence of an event
                                                                           in this target.

  [hide\<FlashPlayer.hide\>]{role="ref"} readonly                          Hides this element.

  [invokePlayerFunction\<FlashPlayer.invokePlayerFunction\>]{role="ref"}   Invokes an ActionScript function
  readonly                                                                 defined in the Flash application.

  [loadMovie\<FlashPlayer.loadMovie\>]{role="ref"} readonly                Loads a movie into the Flash Player,
                                                                           and begins playing it.

  [notify\<FlashPlayer.notify\>]{role="ref"} readonly                      Sends a notification message,
                                                                           simulating the specified user
                                                                           interaction event.

  [playMovie\<FlashPlayer.playMovie\>]{role="ref"} readonly                Restarts a movie that has been
                                                                           stopped.

  [removeEventListener\<FlashPlayer.removeEventListener\>]{role="ref"}     Unregisters an event handler for a
  readonly                                                                 particular type of event occuring in
                                                                           this element.

  [show\<FlashPlayer.show\>]{role="ref"} readonly                          Shows this element.

  [stopMovie\<FlashPlayer.stopMovie\>]{role="ref"} readonly                Halts playback of the current movie.
  ------------------------------------------------------------------------ --------------------------------------

### Events

  ------------------------------------------------ --------------------------------------------
  [callback\<FlashPlayer.callback\>]{role="ref"}   A function definition for a callback from
  readonly                                         the Flash ActionScript environment.
  ------------------------------------------------ --------------------------------------------

::: {.container .hide}
::: {.toctree}
FlashPlayer/active.rst FlashPlayer/visible.rst FlashPlayer/bounds.rst
FlashPlayer/location.rst FlashPlayer/maximumSize.rst
FlashPlayer/minimumSize.rst FlashPlayer/preferredSize.rst
FlashPlayer/size.rst FlashPlayer/windowBounds.rst
FlashPlayer/alignment.rst FlashPlayer/properties.rst
FlashPlayer/enabled.rst FlashPlayer/helpTip.rst FlashPlayer/indent.rst
FlashPlayer/parent.rst FlashPlayer/window.rst FlashPlayer/type.rst

FlashPlayer/invokePlayerFunction.rst FlashPlayer/loadMovie.rst
FlashPlayer/playMovie.rst FlashPlayer/stopMovie.rst
FlashPlayer/notify.rst FlashPlayer/show.rst FlashPlayer/hide.rst
FlashPlayer/addEventListener.rst FlashPlayer/removeEventListener.rst
FlashPlayer/dispatchEvent.rst

FlashPlayer/callback.rst
:::
:::
