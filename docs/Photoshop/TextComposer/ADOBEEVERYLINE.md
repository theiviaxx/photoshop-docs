TextComposer.ADOBEEVERYLINE {#TextComposer.ADOBEEVERYLINE}
===========================

> int **ADOBEEVERYLINE**

Description
-----------

Considers a network of break points for a range of lines and thus
optimizes earlier lines in the paragraph to eliminate especially
unattractive breaks later on. Results in more even spacing and fewer
hyphens.

The Adobe Every-line composer approaches composition by identifying
possible breakpoints, evaluating them, and assigning a weighted penalty
based on these principles: Highest importance is given to evenness of
letter and word spacing; Possible breakpoints are evaluated and
penalized according to how much they deviate from optimal spacing;
Hyphenation is avoided when possible; Breakpoints that require
hyphenation are penalized more than those that create uneven spacing;
Good breakpoints are preferred over bad breakpoints.
