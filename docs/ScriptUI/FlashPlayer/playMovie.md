FlashPlayer.playMovie {#FlashPlayer.playMovie}
=====================

> void **playMovie** ([Boolean]{role="ref"} **rewind**)

Parameters
----------

  ------------ ---------------------------------------------------------------
  **rewind**   When true, restarts the movie from the beginning; otherwise,
               starts playing from thepoint where it was stopped.
  ------------ ---------------------------------------------------------------

Description
-----------

Restarts a movie that has been stopped.

Do not use on a movie that is currently playing.The
stopMovie()-playMovie() sequence does not work for SWF files produced by
Flex, or for some files produced by Flash Authoring (depending on how
they were implemented).
