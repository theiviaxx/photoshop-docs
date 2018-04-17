.. _Channel:

================================================
Channel
================================================


Description
-----------

Object that stores information about a color element in the image, analogous to a plate in the printing process that applies a single color. The document's color mode determines the number of default channels. For example, an RGB document has four default channels: A composite channel: RGB; and three component channels: red, green, and blue. A channel can also be an alpha channel, which stores selections as masks; or a spot channel, which stores spot colors.




Properties
^^^^^^^^^^

+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`color<Channel.color>` readonly         | The color of the channel. Not valid for component channels.                                                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`histogram<Channel.histogram>` readonly | A histogram of the color of the channel.                                                                                                   |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`kind<Channel.kind>` readonly           | The type of channel.                                                                                                                       |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`name<Channel.name>` readonly           | The channel name.                                                                                                                          |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`opacity<Channel.opacity>` readonly     | The opacity of alpha channels (called solidity for spot channels). Range: 0 to 100. Valid only when 'type' = masked area or selected area. |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Channel.parent>` readonly       | The object's container.                                                                                                                    |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`typename<Channel.typename>` readonly   | The class name of the object.                                                                                                              |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`visible<Channel.visible>` readonly     | If true, the channel is visible.                                                                                                           |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+----------------------------------------------+----------------------------------------------------+
| :ref:`add<Channel.add>` readonly             | Adds an element.                                   |
+----------------------------------------------+----------------------------------------------------+
| :ref:`duplicate<Channel.duplicate>` readonly | Duplicate this object.                             |
+----------------------------------------------+----------------------------------------------------+
| :ref:`duplicate<Channel.duplicate>` readonly | Duplicates the channel.                            |
+----------------------------------------------+----------------------------------------------------+
| :ref:`merge<Channel.merge>` readonly         | Merges a spot channel into the component channels. |
+----------------------------------------------+----------------------------------------------------+
| :ref:`remove<Channel.remove>` readonly       | Deletes this object.                               |
+----------------------------------------------+----------------------------------------------------+
| :ref:`removeAll<Channel.removeAll>` readonly | Deletes all elements.                              |
+----------------------------------------------+----------------------------------------------------+






.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Channel/parent.rst
      Channel/typename.rst
      Channel/histogram.rst
      Channel/name.rst
      Channel/kind.rst
      Channel/opacity.rst
      Channel/visible.rst
      Channel/color.rst
      
      

      Channel/add.rst
      Channel/duplicate.rst
      Channel/remove.rst
      Channel/removeAll.rst
      Channel/merge.rst
      Channel/duplicate.rst
      
      
      
      