``` {.sourceCode .javascript}
var doc_a = app.open(new File('path/to/file_a.psd'));
var doc_b = app.open(new File('path/to/file_b.psd'));

if (app.activeDocument === doc_b) {
    app.activeDocument = doc_a;
}
```
