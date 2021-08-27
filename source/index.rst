Welcome to pycpdflib's documentation!
=====================================

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

Paper sizes:

* a0portrait
* a1portrait
* a2portrait
* a3portrait
* a4portrait
* a5portrait
* a0landscape
* a1landscape
* a2landscape
* a3landscape
* a4landscape
* a5landscape
* usletterportrait
* usletterlandscape
* uslegalportrait
* uslegallandscape

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

Permissions:

* noEdit
* noPrint
* noCopy
* noAnnot
* noForms
* noExtract
* noAssemble
* noHqPrint

Encryption Methods.

* pdf40bit
* pdf128bit
* aes128bitfalse
* aes128bittrue
* aes256bitfalse
* aes256bittrue
* aes256bitisofalse
* aes256bitisotrue

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


Positions with two numbers in a tuple e.g (posLeft, 10.0, 20.0):

* posCentre
* posLeft
* posRight

Positions with one number in a tuple e.g (top, 5.0):

* top
* topLeft
* topRight
* left
* bottomLeft
* bottomRight
* right

Positions with no numbers e.g diagonal:

* diagonal
* reverseDiagonal

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

Fonts:

* timesRoman
* timesBold
* timesItalic
* timesBoldItalic
* helvetica
* helveticaBold
* helveticaOblique
* helveticaBoldOblique
* courier
* courierBold
* courierOblique
* courierBoldOblique


Jusitifications:

* leftJustify
* centreJustify
* rightJustify


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


Page layouts:

* singlePage
* oneColumn
* twoColumnLeft
* twoColumnRight
* twoPageLeft
* twoPageRight

.. autofunction:: setPageLayout

Page modes:

* useNone
* useOutlines
* useThumbs
* useOC
* useAttachments

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

Label styles:

* decimalArabic
* uppercaseRoman
* lowercaseRoman
* uppercaseLetters
* lowercaseLetters

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
