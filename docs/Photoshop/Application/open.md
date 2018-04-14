Application.open {#Application.open}
================

> [Document]{role="ref"} **open** ([File]{role="ref"} **document**, any
> **as**, bool **asSmartObject**)

Parameters
----------

  ------------------- -------------------------------------------------------
  **document**        The document(s) to opend.

  **as**              The document type (The default is to let Photoshop
                      deduce the format).

  **asSmartObject**   Creates a smart object around the document.
  ------------------- -------------------------------------------------------

Description
-----------

Opens the specified document file(s).

``` {.sourceCode .javascript}
var doc_a = app.open(new File('path/to/file_a.psd'));
var doc_b = app.open(new File('path/to/file_b.psd'));

if (app.activeDocument === doc_b) {
    app.activeDocument = doc_a;
}
```
