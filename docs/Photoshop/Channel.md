Channel {#Channel}
=======

Description
-----------

Object that stores information about a color element in the image,
analogous to a plate in the printing process that applies a single
color. The document\'s color mode determines the number of default
channels. For example, an RGB document has four default channels: A
composite channel: RGB; and three component channels: red, green, and
blue. A channel can also be an alpha channel, which stores selections as
masks; or a spot channel, which stores spot colors.

### Properties

  ---------------------------------------------- -----------------------------------------------------
  [color\<Channel.color\>]{role="ref"} readonly  The color of the channel. Not valid for component
                                                 channels.

  [histogram\<Channel.histogram\>]{role="ref"}   A histogram of the color of the channel.
  readonly                                       

  [kind\<Channel.kind\>]{role="ref"} readonly    The type of channel.

  [name\<Channel.name\>]{role="ref"} readonly    The channel name.

  [opacity\<Channel.opacity\>]{role="ref"}       The opacity of alpha channels (called solidity for
  readonly                                       spot channels). Range: 0 to 100. Valid only when
                                                 \'type\' = masked area or selected area.

  [parent\<Channel.parent\>]{role="ref"}         The object\'s container.
  readonly                                       

  [typename\<Channel.typename\>]{role="ref"}     The class name of the object.
  readonly                                       

  [visible\<Channel.visible\>]{role="ref"}       If true, the channel is visible.
  readonly                                       
  ---------------------------------------------- -----------------------------------------------------

### Methods

  ---------------------------------------------- -------------------------------------
  [add\<Channel.add\>]{role="ref"} readonly      Adds an element.

  [duplicate\<Channel.duplicate\>]{role="ref"}   Duplicate this object.
  readonly                                       

  [duplicate\<Channel.duplicate\>]{role="ref"}   Duplicates the channel.
  readonly                                       

  [merge\<Channel.merge\>]{role="ref"} readonly  Merges a spot channel into the
                                                 component channels.

  [remove\<Channel.remove\>]{role="ref"}         Deletes this object.
  readonly                                       

  [removeAll\<Channel.removeAll\>]{role="ref"}   Deletes all elements.
  readonly                                       
  ---------------------------------------------- -------------------------------------

::: {.container .hide}
::: {.toctree}
Channel/parent.rst Channel/typename.rst Channel/histogram.rst
Channel/name.rst Channel/kind.rst Channel/opacity.rst
Channel/visible.rst Channel/color.rst

Channel/add.rst Channel/duplicate.rst Channel/remove.rst
Channel/removeAll.rst Channel/merge.rst Channel/duplicate.rst
:::
:::
