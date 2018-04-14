JavaScriptExecutionMode {#JavaScriptExecutionMode}
=======================

Description
-----------

When should a JavaScript debugger be shown.

### Static Properties

  ------------------------------------------------------------------------ ----------------------------------------
  [BEFORERUNNING\<JavaScriptExecutionMode.BEFORERUNNING\>]{role="ref"}     Show the JavaScript debugger when the
  readonly                                                                 first line of the JavaScript executes.

  [NEVER\<JavaScriptExecutionMode.NEVER\>]{role="ref"} readonly            Never show the JavaScript debugger.
                                                                           Treat runtime errors by throwing a
                                                                           JavaScript exceptions.

  [ONRUNTIMEERROR\<JavaScriptExecutionMode.ONRUNTIMEERROR\>]{role="ref"}   Show the JavaScript debugger if a
  readonly                                                                 runtime error occurs.
  ------------------------------------------------------------------------ ----------------------------------------

::: {.container .hide}
::: {.toctree}
JavaScriptExecutionMode/NEVER.rst
JavaScriptExecutionMode/ONRUNTIMEERROR.rst
JavaScriptExecutionMode/BEFORERUNNING.rst
:::
:::
