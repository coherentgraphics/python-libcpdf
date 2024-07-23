# pycpdflib

pycpdflib is a Python interface to the cpdf pdf tools.

pycpdflib is distributed under the AGPL - see LICENSE.md. If you are unable to
abide by the terms of the AGPL, you will need a commercial license.

For commercial licenses, email
[contact@coherentgraphics.co.uk](mailto:contact@coherentgraphics.co.uk) or
visit [https://www.coherentpdf.com/](https://www.coherentpdf.com/)

The python package may be installed with

pip install pycpdflib

and imported into your program with

import pycpdflib


Functionality
-------------

* Quality Split and Merge, keeping bookmarks. Extract pages. Split on Bookmarks.
* Encrypt and Decrypt (including AES 128 and AES 256 encryption)
* Scale, rotate, crop and flip pages. Scale pages to fit
* Copy, Remove and Add bookmarks
* Stamp logos, watermarks, page numbers and multiline text. Transparency.
* Supports Unicode UTF8 text input and output
* Put multiple pages on a single page
* List, copy, or remove annotations
* Read and set document information and metadata
* Add and remove file attachments to document or page.
* Thicken hairlines, blacken text, make draft documents
* Reconstruct malformed files
* Detect missing fonts, low resolution images


Obtaining the DLLs
------------------

The DLLs `pycpdflib` and `cpdflib` are required. They may be obtained here:

<https://github.com/coherentgraphics/cpdflib-binary>


Documentation
-------------

Full manual (required reading): <https://coherentpdf.com/pycpdflibmanual.pdf>

Follow the instructions at the end of Chapter 1 to load the DLLs and write your
first pycpdflib program.

Quick reference API docs: <https://python-libcpdf.readthedocs.io/en/latest/>


Contact
-------

For commercial licenses, or queries: <mailto:contact@coherentgraphics.co.uk>

Bug report: <https://github.com/coherentgraphics/python-libcpdf>
