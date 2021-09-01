Pycpdf: PDF document manipulator
================================

Pycpdf is a library providing a huge range of tools for manipulating PDF files.
It is based on ``cpdf``, the command line tool for PDF manipulation. It
requires Python 3.8 or above.

License
-------

Pycpdf itself is licensed under the BSD 3-clause license. See the file LICENSE
in the distribution.

However, using pycpdf requires the DLLs ``libpycpdf`` and
``libcpdf`` which are free for non-commercial use only. See the
`license file <https://github.com/coherentgraphics/cpdflib-binary/blob/master/LICENSE>`_.

Commercial licenses may be purchased from `Coherent Graphics Ltd
<https://www.coherentpdf.com/>`_.

Enquires to contact@coherentgraphics.co.uk

Documentation
-------------

This documentation should be read alongside the PDF manual `pycpdflibmanual.pdf
<https://coherentpdf.com/pycpdflibmanual.pdf>`_ which describes the command line
tools upon which ``pycpdf`` is based, together with the Python interface.

There are `some examples
<https://github.com/coherentgraphics/python-libcpdf/tree/master/examples>`_ in
the project's GitHub repository.

Obtaining the libpycpdf and libcpdf DLLs
----------------------------------------

The DLLs required are available to download in binary form for most major
platforms `from here <https:://github.com/coherentgraphics/cpdflib-binary/>`_.
For other platforms, please write to contact@coherentgraphics.co.uk. 

Loading the libpypcdf and libcpdf DLLs
--------------------------------------

Before using the library, you must load the ``libpycpdf`` and ``libcpdf`` DLLs.
This is achieved with the ``pycpdf.loadDLL`` function, given the filename or
full path of the ``libpycpdf`` DLL.

On Windows, you may have to call ``os.add_dll_directory`` first. On MacOS, you
may need to give the full path, and you may need to install ``libcpdf.so`` in a
standard location ``/usr/local/lib/``, or use the ``install_name_tool`` command
to tell ``libpycpdf.so`` where to find ``libcpdf.so``.

Conventions
-----------

Any function may raise the exception ``CPDFError``, carrying a string describing
the error.

A 'range' is a list of integers specifying page numbers. Page numbers start at
1. Range arguments are called `r`.

Text arguments and results are in UTF8.

Units are in PDF points (1/72 inch).

Angles are in degrees.


Built-in values
---------------

**Paper sizes**

``a0portrait`` ``a1portrait`` ``a2portrait`` ``a3portrait`` ``a4portrait`` ``a5portrait`` ``a0landscape``
``a1landscape`` ``a2landscape`` ``a3landscape`` ``a4landscape`` ``a5landscape`` ``usletterportrait``
``usletterlandscape`` ``uslegalportrait`` ``uslegallandscape``

**Permissions**

``noEdit`` ``noPrint`` ``noCopy`` ``noAnnot`` ``noForms`` ``noExtract`` ``noAssemble`` ``noHqPrint``

**Encryption methods**

``pdf40bit`` ``pdf128bit`` ``aes128bitfalse`` ``aes128bittrue`` ``aes256bitfalse`` ``aes256bittrue``
``aes256bitisofalse`` ``aes256bitisotrue``

**Positions**

*Positions with two numbers in a tuple e.g (posLeft, 10.0, 20.0)*

``posCentre`` ``posLeft`` ``posRight``

*Positions with one number in a tuple e.g (top, 5.0)*

``top`` ``topLeft`` ``topRight`` ``left`` ``bottomLeft`` ``bottomRight`` ``right``

*Positions with no numbers e.g diagonal*

``diagonal`` ``reverseDiagonal``

**Fonts**

``timesRoman`` ``timesBold`` ``timesItalic`` ``timesBoldItalic`` ``helvetica`` ``helveticaBold``
``helveticaOblique`` ``helveticaBoldOblique`` ``courier`` ``courierBold`` ``courierOblique``
``courierBoldOblique``

**Justification**

``leftJustify`` ``centreJustify`` ``rightJustify``

**Page layouts**

``singlePage`` ``oneColumn`` ``twoColumnLeft`` ``twoColumnRight`` ``twoPageLeft`` ``twoPageRight``

**Page modes**

``useNone`` ``useOutlines`` ``useThumbs`` ``useOC`` ``useAttachments``

**Page label styles**

``decimalArabic`` ``uppercaseRoman`` ``lowercaseRoman`` ``uppercaseLetters`` ``lowercaseLetters``

Chapter 0. Preliminaries
------------------------

.. currentmodule:: pycpdf
.. autoclass:: Pdf
.. autofunction:: loadDLL
.. autoexception:: CPDFError
.. autofunction:: lastError
.. autofunction:: lastErrorString
.. autofunction:: checkerror
.. autofunction:: version
.. autofunction:: setFast
.. autofunction:: setSlow
.. autofunction:: clearError
.. autofunction:: onExit

Chapter 1. Basics
-----------------

.. autofunction:: fromFile
.. autofunction:: fromFileLazy
.. autofunction:: fromMemory
.. autofunction:: fromMemoryLazy
.. autofunction:: blankDocument
.. autofunction:: blankDocumentPaper
.. autofunction:: ptOfCm
.. autofunction:: ptOfMm 
.. autofunction:: ptOfIn
.. autofunction:: cmOfPt
.. autofunction:: mmOfPt
.. autofunction:: inOfPt
.. autofunction:: parsePagespec
.. autofunction:: validatePagespec
.. autofunction:: stringOfPagespec
.. autofunction:: blankRange
.. autofunction:: pageRange
.. autofunction:: all
.. autofunction:: even
.. autofunction:: odd
.. autofunction:: rangeUnion
.. autofunction:: difference
.. autofunction:: removeDuplicates
.. autofunction:: rangeLength
.. autofunction:: rangeGet
.. autofunction:: rangeAdd
.. autofunction:: isInRange
.. autofunction:: pages
.. autofunction:: pagesFast
.. autofunction:: toFile
.. autofunction:: toFileExt
.. autofunction:: toMemory
.. autofunction:: isEncrypted
.. autofunction:: toFileEncrypted
.. autofunction:: toFileEncryptedExt
.. autofunction:: decryptPdf
.. autofunction:: decryptPdfOwner
.. autofunction:: hasPermission
.. autofunction:: encryptionKind

Chapter 2. Merging and Splitting
--------------------------------

.. autofunction:: mergeSimple
.. autofunction:: merge
.. autofunction:: mergeSame
.. autofunction:: selectPages

Chapter 3. Pages
----------------

.. autofunction:: scalePages
.. autofunction:: scaleToFit
.. autofunction:: scaleToFitPaper
.. autofunction:: scaleContents
.. autofunction:: shiftContents
.. autofunction:: rotate
.. autofunction:: rotateBy
.. autofunction:: rotateContents
.. autofunction:: upright
.. autofunction:: hFlip
.. autofunction:: vFlip
.. autofunction:: crop
.. autofunction:: removeCrop
.. autofunction:: removeTrim
.. autofunction:: removeArt
.. autofunction:: removeBleed
.. autofunction:: trimMarks 
.. autofunction:: showBoxes
.. autofunction:: hardBox

Chapter 4. Encryption
---------------------

Encryption covered under Chapter 1 in pycpdflib.

Chapter 5. Compression
----------------------

.. autofunction:: compress
.. autofunction:: decompress
.. autofunction:: squeezeInMemory

Chapter 6. Bookmarks
--------------------

.. autofunction:: getBookmarks
.. autofunction:: setBookmarks

Chapter 7. Presentations
------------------------

Not included in the library version.

Chapter 8. Logos, Watermarks and Stamps
---------------------------------------

.. autofunction:: stampOn
.. autofunction:: stampUnder
.. autofunction:: stampExtended 
.. autofunction:: combinePages
.. autofunction:: addText
.. autofunction:: addTextSimple
.. autofunction:: removeText
.. autofunction:: textWidth
.. autofunction:: addContent
.. autofunction:: stampAsXObject

Chapter 9. Multipage facilities
-------------------------------

.. autofunction:: twoUp
.. autofunction:: twoUpStack
.. autofunction:: padBefore
.. autofunction:: padAfter
.. autofunction:: padEvery
.. autofunction:: padMultiple
.. autofunction:: padMultipleBefore

Chapter 10. Annotations
-----------------------

Not in the library version.

Chapter 11. Document Information and Metadata
---------------------------------------------

.. autofunction:: isLinearized
.. autofunction:: getVersion
.. autofunction:: getMajorVersion
.. autofunction:: getTitle
.. autofunction:: getAuthor
.. autofunction:: getSubject
.. autofunction:: getKeywords
.. autofunction:: getCreator
.. autofunction:: getCreationDate
.. autofunction:: getModificationDate
.. autofunction:: getTitleXMP
.. autofunction:: getAuthorXMP
.. autofunction:: getSubjectXMP
.. autofunction:: getKeywordsXMP
.. autofunction:: getCreatorXMP
.. autofunction:: getCreationDateXMP
.. autofunction:: getModificationDateXMP
.. autofunction:: setTitle
.. autofunction:: setAuthor
.. autofunction:: setSubject
.. autofunction:: setKeywords
.. autofunction:: setCreator
.. autofunction:: setProducer
.. autofunction:: setCreationDate
.. autofunction:: setModificationDate
.. autofunction:: setTitleXMP
.. autofunction:: setAuthorXMP
.. autofunction:: setSubjectXMP
.. autofunction:: setKeywordsXMP
.. autofunction:: setCreatorXMP
.. autofunction:: setProducerXMP
.. autofunction:: setCreationDateXMP
.. autofunction:: setModificationDateXMP
.. autofunction:: getDateComponents
.. autofunction:: dateStringOfComponents
.. autofunction:: getPageRotation
.. autofunction:: hasBox
.. autofunction:: getMediaBox
.. autofunction:: getCropBox
.. autofunction:: getTrimBox
.. autofunction:: getArtBox
.. autofunction:: getBleedBox
.. autofunction:: setMediaBox
.. autofunction:: setCropBox
.. autofunction:: setTrimBox
.. autofunction:: setArtBox
.. autofunction:: setBleedBox
.. autofunction:: markTrapped
.. autofunction:: markUntrapped
.. autofunction:: markTrappedXMP
.. autofunction:: markUntrappedXMP
.. autofunction:: setPageLayout
.. autofunction:: setPageMode
.. autofunction:: hideToolbar
.. autofunction:: hideMenubar
.. autofunction:: hideWindowUi
.. autofunction:: fitWindow
.. autofunction:: centerWindow
.. autofunction:: displayDocTitle
.. autofunction:: openAtPage
.. autofunction:: setMetadataFromFile
.. autofunction:: setMetadataFromByteArray
.. autofunction:: getMetadata
.. autofunction:: removeMetadata
.. autofunction:: createMetadata
.. autofunction:: setMetadataDate
.. autofunction:: getPageLabels
.. autofunction:: addPageLabels
.. autofunction:: getPageLabelStringForPage

Chapter 12. File Attachments
----------------------------

.. autofunction:: attachFile
.. autofunction:: attachFileToPage
.. autofunction:: attachFileFromMemory
.. autofunction:: attachFileToPageFromMemory
.. autofunction:: getAttachments

Chapter 13. Images
------------------

.. autofunction:: getImageResolution


Chapter 14. Fonts
-----------------

.. autofunction:: getFontInfo
.. autofunction:: removeFonts
.. autofunction:: copyFont

Chapter 15. PDF and JSON
------------------------

.. autofunction:: outputJSON

Chapter 16. Optional Content Groups
-----------------------------------

.. autofunction:: getOCGList
.. autofunction:: OCGRename
.. autofunction:: OCGOrderAll
.. autofunction:: OCGCoalesce

Chapter 17. Miscellaneous
-------------------------

.. autofunction:: draft
.. autofunction:: removeAllText
.. autofunction:: blackText
.. autofunction:: blackLines
.. autofunction:: blackFills
.. autofunction:: thinLines
.. autofunction:: copyId
.. autofunction:: removeId
.. autofunction:: setVersion
.. autofunction:: setFullVersion
.. autofunction:: removeDictEntry
.. autofunction:: removeClipping
