.. _FlashPlayer.alignment:

================================================
FlashPlayer.alignment
================================================

   :ref:`String` **alignment**


Description
-----------

The alignment style for this element. If defined, this value overrides the alignChildren setting for the parent container.

This can be a single string, which indicates the alignment for the orientation specified in the parent container, or an array of two strings, indicating both the horizontal and vertical alignment (in that order). Allowed values depend on the orientation value of the parent container. They are not case sensitive.                            For orientation=row:top, bottom, fill                                         For orientation=column: left, right, fill                                         For orientation=stack:top, bottom, left, right, fill