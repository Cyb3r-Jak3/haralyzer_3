Overview
--------

The haralyzer_3 module contains three classes for analyzing web pages based
on a HAR file. ``HarParser()`` represents a full file (which might have
multiple pages). ``HarPage()`` represents a single page from said file.
``HarEntry()`` represents an entry in a ``HarPage()``, and there are are multiple entries per page.
Each ``HarEntry`` has a request and response that contains items such as the headers, status code, timings, etc

``HarParser`` has a couple of helpful methods for analyzing single entries
from a HAR file, but most of the pertinent functions are inside of the page
object.

``haralyzer_3`` was designed to be easy to use, but you can also access more
powerful functions directly.