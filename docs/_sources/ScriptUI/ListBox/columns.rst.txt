.. _ListBox.columns:

================================================
ListBox.columns
================================================

   :ref:`Object` **columns**


Description
-----------

For a multi-column list box, the column properties.

A JavaScript object with two read-only properties whose values are set by the creation parameters:                            titles: An array of column title strings, whose length matches the number of columns specified at creation.                                         preferredWidths: An array of column widths, whose length matches the number of columns specified at creation.                                         visible: An array of boolean visible attributes, whose length matches the number of columns specified at creation.This property can be used to show/hide a column. Avaiblable in ScriptUI Version 6.0 or later provided ScriptUI.frameworkName == 'Flex'.