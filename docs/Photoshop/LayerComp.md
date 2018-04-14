LayerComp {#LayerComp}
=========

Description
-----------

A snapshot of a state of the layers in a document (can be used to view
different page layouts or compostions).

### Properties

  -------------------------------------------------- -------------------------------------
  [appearance\<LayerComp.appearance\>]{role="ref"}   If true, uses layer appearance (layer
  readonly                                           styles) settings.

  [comment\<LayerComp.comment\>]{role="ref"}         The description of the layer comp.
  readonly                                           

  [name\<LayerComp.name\>]{role="ref"} readonly      The name of the layer comp.

  [parent\<LayerComp.parent\>]{role="ref"} readonly  The object\'s container.

  [position\<LayerComp.position\>]{role="ref"}       If true, uses layer position.
  readonly                                           

  [selected\<LayerComp.selected\>]{role="ref"}       If true, the layer comp is currently
  readonly                                           selected.

  [typename\<LayerComp.typename\>]{role="ref"}       The class name of the object.
  readonly                                           

  [visibility\<LayerComp.visibility\>]{role="ref"}   If true, the layer comp is visible.
  readonly                                           
  -------------------------------------------------- -------------------------------------

### Methods

  -------------------------------------------------------- ------------------------------------
  [add\<LayerComp.add\>]{role="ref"} readonly              Adds an element.

  [apply\<LayerComp.apply\>]{role="ref"} readonly          Applies the layer comp to the
                                                           document.

  [recapture\<LayerComp.recapture\>]{role="ref"} readonly  Recaptures the current layer
                                                           state(s) for this layer comp.

  [remove\<LayerComp.remove\>]{role="ref"} readonly        Deletes this object.

  [removeAll\<LayerComp.removeAll\>]{role="ref"} readonly  Deletes all elements.

  [resetFromComp\<LayerComp.resetFromComp\>]{role="ref"}   Resets the layer comp state to the
  readonly                                                 document state.
  -------------------------------------------------------- ------------------------------------

::: {.container .hide}
::: {.toctree}
LayerComp/parent.rst LayerComp/typename.rst LayerComp/name.rst
LayerComp/comment.rst LayerComp/appearance.rst LayerComp/position.rst
LayerComp/visibility.rst LayerComp/selected.rst

LayerComp/add.rst LayerComp/remove.rst LayerComp/removeAll.rst
LayerComp/apply.rst LayerComp/recapture.rst LayerComp/resetFromComp.rst
:::
:::
