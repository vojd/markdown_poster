Markdown Poster
===============

Allow parsing and posting of markdown files through a simple admin interface

Meta data
---------

Document meta data is written at the top of the markdown document.
Meta data lines starts with two colons, ::

``:: some meta text ``
``:: slug : the_first_document``
``:: type : blog``
``:: created : now``


Slug
----
`` slug `` must be written as a single word consisting of letters, numbers and underscores
`` type `` defines what to do with the text, render as blog or page?
`` created `` date formattable string (YYYY-mm-dd) or now
