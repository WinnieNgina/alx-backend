 jinja2.ext.autoescape and jinja2.ext.with_ extensions are deprecated in Jinja2 version 3.0.0 and later. These extensions have been added to the compiler in these versions 1.

You should remove these extensions from your babel.cfg file. Your babel.cfg file should look like this:

[python: **.py]
[jinja2: **/templates/**.html]
;extensions=jinja2.ext.autoescape,jinja2.ext.with_

