.. _EditText.textselection:

================================================
EditText.textselection
================================================

   :ref:`String` **textselection**


Description
-----------

The currently selected text, or the empty string if there is no text selected.

Setting the value replaces the current text selection and modifies the value of the?text?property. If there is no current selection, inserts the new value into the text string at the current insertion point. The textselection value is reset to an empty string after it modifies the text value. Note that setting the textselection property before the element?s parent Window exists is an undefined operation.