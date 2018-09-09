.. _FlashPlayer.stopMovie:

================================================
FlashPlayer.stopMovie
================================================

   void **stopMovie** ()




Description
-----------

Halts playback of the current movie.

The stopMovie()-playMovie() sequence does not work for SWF files produced by Flex, or for some files produced by Flash Authoring (depending on how they were implemented).Using stopMovie() from the player's hosting environment has no effect on an SWF file playing in a ScriptUI Flash Player element. It is, however, possible to produce an SWF using Flash Authoring that can stop itself in response to user interaction.


