"""Pycpdflib: a python interface to cpdf.

Before using the library, you must load the libpycpdf and libcpdf DLLs. This is
achieved with the pycpdflib.loadDLL function, given the filename or full path
of the libpycpdf DLL.  On Windows, you may have to call os.add_dll_directory
first. On MacOS, you may need to give the full path, and you may need to
install libcpdf.so in a standard location /usr/local/lib/, or use the
install_name_tool command to tell libpycpdf.so where to find libcpdf.so.  """

"""
Loading the libpypcdf and libcpdf DLLs
--------------------------------------

Before using the library, you must load the ``libpycpdf`` and ``libcpdf`` DLLs.
This is achieved with the ``pycpdflib.loadDLL`` function, given the filename or
full path of the ``libpycpdf`` DLL.

On Windows, you may have to call ``os.add_dll_directory`` first. On MacOS, you
may need to give the full path, and you may need to install ``libcpdf.so`` in a
standard location ``/usr/local/lib/``, or use the ``install_name_tool`` command
to tell ``libpycpdf.so`` where to find ``libcpdf.so``.

Conventions
-----------

Any function may raise the exception ``CPDFError``, carrying a string
describing the error.

A 'range' is a list of integers specifying page numbers. Page numbers start at
1. Range arguments are called `r`.

Text arguments and results are in UTF8.

Units are in PDF points (1/72 inch).

Angles are in degrees.


Built-in values
---------------

Paper sizes:

a0portrait a1portrait a2portrait a3portrait a4portrait a5portrait a0landscape
a1landscape a2landscape a3landscape a4landscape a5landscape usletterportrait
usletterlandscape uslegalportrait uslegallandscape

Permissions:

noEdit noPrint noCopy noAnnot noForms noExtract noAssemble noHqPrint

Encryption methods:

pdf40bit pdf128bit aes128bitfalse aes128bittrue aes256bitfalse aes256bittrue
aes256bitisofalse aes256bitisotrue

Positions:

Positions with two numbers in a tuple e.g (posLeft, 10.0, 20.0)

posCentre posLeft posRight

Positions with one number in a tuple e.g (top, 5.0)

top topLeft topRight left bottomLeft bottomRight right

Positions with no numbers e.g diagonal

diagonal reverseDiagonal

Fonts:

timesRoman timesBold timesItalic timesBoldItalic helvetica helveticaBold
helveticaOblique helveticaBoldOblique courier courierBold courierOblique
courierBoldOblique

Justification:

leftJustify centreJustify rightJustify

Page layouts:

singlePage oneColumn twoColumnLeft twoColumnRight twoPageLeft twoPageRight

Page modes:

useNone useOutlines useThumbs useOC useAttachments

Page label styles:

decimalArabic uppercaseRoman lowercaseRoman uppercaseLetters lowercaseLetters

Line cap types:

capButt capRound capSquare

Line join types:

joinMiter joinRound joinBevel
"""


from ctypes import *
import sys
libc = None

# CHAPTER 0. Preliminaries


class Pdf:
    """The type of PDF documents."""
    pdf = -1

    def __init__(self, pdfnum):
        self.pdf = pdfnum

    def __del__(self):
        libc.pycpdf_deletePdf(self.pdf)


def loadDLL(f):
    """Load the libpycpdf DLL from a given file, and set up pycpdflib. Must be
    called prior to using any other function in the library."""
    global libc
    libc = CDLL(f)
    libc.pycpdf_tableOfContents.argtypes = [
        c_int, POINTER(c_char), c_double, POINTER(c_char), c_int]
    libc.pycpdf_version.restype = POINTER(c_char)
    libc.pycpdf_lastErrorString.restype = POINTER(c_char)
    libc.pycpdf_blankDocument.argtypes = [c_double, c_double, c_int]
    libc.pycpdf_textToPDF.argtypes = [
        c_double, c_double, POINTER(c_char), c_double, POINTER(c_char)]
    libc.pycpdf_textToPDFMemory.argtypes = [
        c_double, c_double, POINTER(c_char), c_double, POINTER(c_char), c_int]
    libc.pycpdf_textToPDFPaper.argtypes = [
        c_int, POINTER(c_char), c_double, POINTER(c_char)]
    libc.pycpdf_textToPDFPaperMemory.argtypes = [
        c_int, POINTER(c_char), c_double, POINTER(c_char), c_int]
    libc.pycpdf_ptOfCm.argtypes = [c_double]
    libc.pycpdf_ptOfCm.restype = c_double
    libc.pycpdf_ptOfMm.argtypes = [c_double]
    libc.pycpdf_ptOfMm.restype = c_double
    libc.pycpdf_ptOfIn.argtypes = [c_double]
    libc.pycpdf_ptOfIn.restype = c_double
    libc.pycpdf_cmOfPt.argtypes = [c_double]
    libc.pycpdf_cmOfPt.restype = c_double
    libc.pycpdf_mmOfPt.argtypes = [c_double]
    libc.pycpdf_mmOfPt.restype = c_double
    libc.pycpdf_inOfPt.argtypes = [c_double]
    libc.pycpdf_inOfPt.restype = c_double
    libc.pycpdf_stringOfPagespec.restype = POINTER(c_char)
    libc.pycpdf_toMemory.restype = POINTER(c_uint8)
    libc.pycpdf_outputJSONMemory.restype = POINTER(c_uint8)
    libc.pycpdf_annotationsJSON.restype = POINTER(c_uint8)
    libc.pycpdf_getBookmarksJSON.restype = POINTER(c_uint8)
    libc.pycpdf_compositionJSON.restype = POINTER(c_uint8)
    libc.pycpdf_scalePages.argtypes = [c_int, c_int, c_double, c_double]
    libc.pycpdf_scaleToFit.argtypes =\
        [c_int, c_int, c_double, c_double, c_double]
    libc.pycpdf_scaleToFitPaper.argtypes = [c_int, c_int, c_int, c_double]
    libc.pycpdf_scaleContents.argtypes =\
        [c_int, c_int, c_int, c_double, c_double, c_double]
    libc.pycpdf_shiftContents.argtypes = [c_int, c_int, c_double, c_double]
    libc.pycpdf_shiftBoxes.argtypes = [c_int, c_int, c_double, c_double]
    libc.pycpdf_rotateContents.argtypes = [c_int, c_int, c_double]
    libc.pycpdf_crop.argtypes =\
        [c_int, c_int, c_double, c_double, c_double, c_double]
    libc.pycpdf_thinLines.argtypes = [c_int, c_int, c_double]
    libc.pycpdf_stampAsXObject.restype = POINTER(c_char)
    libc.pycpdf_getTitle.restype = POINTER(c_char)
    libc.pycpdf_getAuthor.restype = POINTER(c_char)
    libc.pycpdf_getSubject.restype = POINTER(c_char)
    libc.pycpdf_getKeywords.restype = POINTER(c_char)
    libc.pycpdf_getCreator.restype = POINTER(c_char)
    libc.pycpdf_getProducer.restype = POINTER(c_char)
    libc.pycpdf_getCreationDate.restype = POINTER(c_char)
    libc.pycpdf_getModificationDate.restype = POINTER(c_char)
    libc.pycpdf_getTitleXMP.restype = POINTER(c_char)
    libc.pycpdf_getAuthorXMP.restype = POINTER(c_char)
    libc.pycpdf_getSubjectXMP.restype = POINTER(c_char)
    libc.pycpdf_getKeywordsXMP.restype = POINTER(c_char)
    libc.pycpdf_getCreatorXMP.restype = POINTER(c_char)
    libc.pycpdf_getProducerXMP.restype = POINTER(c_char)
    libc.pycpdf_getCreationDateXMP.restype = POINTER(c_char)
    libc.pycpdf_getModificationDateXMP.restype = POINTER(c_char)
    libc.pycpdf_setMediaBox.argtypes =\
        [c_int, c_int, c_double, c_double, c_double, c_double]
    libc.pycpdf_setCropBox.argtypes =\
        [c_int, c_int, c_double, c_double, c_double, c_double]
    libc.pycpdf_setTrimBox.argtypes =\
        [c_int, c_int, c_double, c_double, c_double, c_double]
    libc.pycpdf_setArtBox.argtypes =\
        [c_int, c_int, c_double, c_double, c_double, c_double]
    libc.pycpdf_setBleedBox.argtypes =\
        [c_int, c_int, c_double, c_double, c_double, c_double]
    libc.pycpdf_getBookmarkText.restype = POINTER(c_char)
    libc.pycpdf_addText.argtypes =\
        [c_int, c_int, c_int, POINTER(c_char), c_int, c_double, c_double,
         c_double, c_int, POINTER(
             c_char), c_double, c_double, c_double, c_double, c_int,
         c_int, c_int, c_double, c_int, c_int, c_int, POINTER(c_char),
         c_double, c_int]
    libc.pycpdf_addTextSimple.argtypes =\
        [c_int, c_int, POINTER(c_char), c_int, c_double,
         c_double, POINTER(c_char), c_double]
    libc.pycpdf_getMetadata.restype = POINTER(c_uint8)
    libc.pycpdf_getDictEntries.restype = POINTER(c_uint8)
    libc.pycpdf_getAttachmentData.restype = POINTER(c_uint8)
    libc.pycpdf_getAttachmentName.restype = POINTER(c_char)
    libc.pycpdf_startGetImageResolution.argtypes = [c_int, c_double]
    libc.pycpdf_getImageResolutionImageName.restype = POINTER(c_char)
    libc.pycpdf_getImagePages.restype = POINTER(c_char)
    libc.pycpdf_getImageName.restype = POINTER(c_char)
    libc.pycpdf_getImageColSpace.restype = POINTER(c_char)
    libc.pycpdf_getImageFilter.restype = POINTER(c_char)
    libc.pycpdf_getFontName.restype = POINTER(c_char)
    libc.pycpdf_getFontType.restype = POINTER(c_char)
    libc.pycpdf_getFontEncoding.restype = POINTER(c_char)
    libc.pycpdf_getPageLabelStringForPage.restype = POINTER(c_char)
    libc.pycpdf_getPageLabelPrefix.restype = POINTER(c_char)
    libc.pycpdf_dateStringOfComponents.restype = POINTER(c_char)
    libc.pycpdf_OCGListEntry.restype = POINTER(c_char)
    libc.pycpdf_stampExtended.argtypes = [
        c_int, c_int, c_int, c_int, c_int, c_int, c_double, c_double, c_int]
    libc.pycpdf_getImageResolutionXRes.restype = c_double
    libc.pycpdf_getImageResolutionYRes.restype = c_double
    libc.pycpdf_impose.argtypes = [c_int, c_double, c_double, c_int,
                                   c_int, c_int, c_int, c_int, c_double,
                                   c_double, c_double]
    libc.pycpdf_chopH.argtypes = [c_int, c_int, c_int, c_double]
    libc.pycpdf_chopV.argtypes = [c_int, c_int, c_int, c_double]
    libc.pycpdf_id1.restype = POINTER(c_char)
    libc.pycpdf_id2.restype = POINTER(c_char)
    libc.pycpdf_getSubformat.restype = POINTER(c_char)
    libc.pycpdf_pageInfoJSON.restype = POINTER(c_char)
    libc.pycpdf_fontsJSON.restype = POINTER(c_char)
    libc.pycpdf_imagesJSON.restype = POINTER(c_char)
    libc.pycpdf_imageResolutionJSON.restype = POINTER(c_char)
    libc.pycpdf_imageResolutionJSON.argtypes = [
        c_int, POINTER(c_int), c_double]
    libc.pycpdf_drawTo.argtypes = [c_double, c_double]
    libc.pycpdf_drawLine.argtypes = [c_double, c_double]
    libc.pycpdf_drawRect.argtypes = [c_double, c_double, c_double, c_double]
    libc.pycpdf_drawBez.argtypes = [
        c_double, c_double, c_double, c_double, c_double, c_double]
    libc.pycpdf_drawBez23.argtypes = [c_double, c_double, c_double, c_double]
    libc.pycpdf_drawBez13.argtypes = [c_double, c_double, c_double, c_double]
    libc.pycpdf_drawCircle.argtypes = [c_double, c_double, c_double]
    libc.pycpdf_drawStrokeColGrey.argtypes = [c_double]
    libc.pycpdf_drawStrokeColRGB.argtypes = [c_double, c_double, c_double]
    libc.pycpdf_drawStrokeColCYMK.argtypes = [
        c_double, c_double, c_double, c_double]
    libc.pycpdf_drawFillColGrey.argtypes = [c_double]
    libc.pycpdf_drawFillColRGB.argtypes = [c_double, c_double, c_double]
    libc.pycpdf_drawFillColCYMK.argtypes = [
        c_double, c_double, c_double, c_double]
    libc.pycpdf_drawThick.argtypes = [c_double]
    libc.pycpdf_drawMiter.argtypes = [c_double]
    libc.pycpdf_drawMTrans.argtypes = [c_double, c_double]
    libc.pycpdf_drawMRot.argtypes = [c_double, c_double, c_double]
    libc.pycpdf_drawMScale.argtypes = [c_double, c_double, c_double, c_double]
    libc.pycpdf_drawMShearX.argtypes = [c_double, c_double, c_double]
    libc.pycpdf_drawMShearY.argtypes = [c_double, c_double, c_double]
    libc.pycpdf_drawMatrix.argtypes = [
        c_double, c_double, c_double, c_double, c_double, c_double]
    libc.pycpdf_drawXObjBBox.argtypes = [
        c_double, c_double, c_double, c_double]
    libc.pycpdf_drawFillOpacity.argtypes = [c_double]
    libc.pycpdf_drawStrokeOpacity.argtypes = [c_double]
    libc.pycpdf_drawFontSize.argtypes = [c_double]
    libc.pycpdf_drawCharSpace.argtypes = [c_double]
    libc.pycpdf_drawWordSpace.argtypes = [c_double]
    libc.pycpdf_drawTextScale.argtypes = [c_double]
    libc.pycpdf_drawRise.argtypes = [c_double]
    libc.pycpdf_drawLeading.argtypes = [c_double]
    LP_c_char = POINTER(c_char)
    LP_LP_c_char = POINTER(LP_c_char)
    argc = len(sys.argv)
    argv = (LP_c_char * (argc + 1))()
    for i, arg in enumerate(sys.argv):
        enc_arg = arg.encode('utf-8')
        argv[i] = create_string_buffer(enc_arg)
    libc.pycpdf_startup.argtypes = [LP_LP_c_char]
    libc.pycpdf_startup(argv)
    checkerror()


class CPDFError(Exception):
    """Any function may raise an exception CPDFError, carrying a string
    describing what went wrong."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def lastError():
    """Return the last error. Not usually used directly, since pycpdflib
    functions raise exceptions."""
    return libc.pycpdf_lastError()


def lastErrorString():
    """Return the last error string. Not usually used directly, since pycpdflib
    functions raise exceptions."""
    return string_at(libc.pycpdf_lastErrorString()).decode()


def checkerror():
    """Raise an exception if the last function call resulted in an error. Not
    used directly, since pycpdflib functions will raise the exception
    directly."""
    if lastError() != 0:
        s = lastErrorString()
        clearError()
        raise CPDFError(s)


def version():
    """Return the version number of the pycpdflib library."""
    v = string_at(libc.pycpdf_version()).decode()
    checkerror()
    return v


def setFast():
    """Set fast mode. Some operations have a fast mode. The default is 'slow'
    mode, which works even on old-fashioned files. For more details, see
    section 1.13 of the CPDF manual. This function sets the mode globally."""
    libc.pycpdf_setFast()
    checkerror()


def setSlow():
    """Set slow mode. Some operations have a fast mode. The default is 'slow'
    mode, which works even on old-fashioned files. For more details, see
    section 1.13 of the CPDF manual. This function sets the mode globally."""
    libc.pycpdf_setSlow()
    checkerror()


def embedStd14(embed):
    """Calling this function with a true argument sets embedding for the
    Standard 14 fonts.  You must also set the directory to load them from with
    the embedStd14Dir function. Default value: False."""
    libc.pycpdf_embedStd14(embed)
    checkerror()


def embedStd14Dir(d):
    """Set the directory to load Standard 14 fonts for embedding."""
    libc.pycpdf_embedStd14Dir(str.encode(d))
    checkerror()


def clearError():
    """Clear the current error state."""
    libc.pycpdf_clearError()
    checkerror()


def onExit():
    """A debug function which prints some information about
    resource usage. This can be used to detect if PDFs or ranges are being
    deallocated properly."""
    libc.pycpdf_onExit()
    checkerror()

# CHAPTER 1. Basics


def fromFile(filename, userpw):
    """Load a PDF file from a given file.  Supply a user password (possibly
    blank) in case the file is encrypted. It won't be decrypted, but sometimes
    the password is needed just to load the file."""
    pdf = Pdf(libc.pycpdf_fromFile(str.encode(filename), str.encode(userpw)))
    checkerror()
    return pdf


def fromFileLazy(filename, userpw):
    """Load a PDF from a file, doing only minimal parsing. The objects will be
    read and parsed when they are actually needed.  Use this when the whole
    file won't be required. Also supply a user password (possibly blank) in
    case the file is encrypted. It won't be decrypted, but sometimes the
    password is needed just to load the file."""
    pdf = Pdf(libc.pycpdf_fromFileLazy(
        str.encode(filename), str.encode(userpw)))
    checkerror()
    return pdf


def fromMemory(data, userpw):
    """Load a file from a byte array and the user password (blank if none)."""
    pdf = Pdf(libc.pycpdf_fromMemory(data, len(data), str.encode(userpw)))
    checkerror()
    return pdf


def fromMemoryLazy(data, userpw):
    """Load a file from from a byte array and the user password (blank if
    none), but lazily like fromFileLazy."""
    pdf = Pdf(libc.pycpdf_fromMemoryLazy(data, len(data), str.encode(userpw)))
    checkerror()
    return pdf


def ptOfCm(i):
    """Convert a figure in centimetres to points (72 points to 1 inch)."""
    r = libc.pycpdf_ptOfCm(i)
    checkerror()
    return r


def ptOfMm(i):
    """Convert a figure in millimetres to points (72 points to 1 inch)."""
    r = libc.pycpdf_ptOfMm(i)
    checkerror()
    return r


def ptOfIn(i):
    """Convert a figure in inches to points (72 points to 1 inch)."""
    r = libc.pycpdf_ptOfIn(i)
    checkerror()
    return r


def cmOfPt(i):
    """Convert a figure in points to centimetres (72 points to 1 inch)."""
    r = libc.pycpdf_cmOfPt(i)
    checkerror()
    return r


def mmOfPt(i):
    """Convert a figure in points to millimetres (72 points to 1 inch)."""
    r = libc.pycpdf_mmOfPt(i)
    checkerror()
    return r


def inOfPt(i):
    """Convert a figure in points to inches (72 points to 1 inch)."""
    r = libc.pycpdf_inOfPt(i)
    checkerror()
    return r


def parsePagespec(pdf, pagespec):
    """Parse a page specification such as "1-3,8-end" to a range with reference
    to a given PDF (the PDF is supplied so that page ranges which reference
    pages which do not exist are rejected)."""
    rn = libc.pycpdf_parsePagespec(pdf.pdf, str.encode(pagespec))
    r = list_of_range(rn)
    deleteRange(rn)
    checkerror()
    return r


def validatePagespec(pagespec):
    """Validate a page specification, returning True or False, so far as is
    possible in the absence of the actual document."""
    r = libc.pycpdf_validatePagespec(str.encode(pagespec))
    checkerror()
    return r


def stringOfPagespec(pdf, r):
    """Build a page specification from a page range. For example, the range
    containing 1,2,3,6,7,8 in a document of 8 pages might yield "1-3,6-end"."""
    rn = range_of_list(r)
    r = string_at(libc.pycpdf_stringOfPagespec(pdf.pdf, rn)).decode()
    deleteRange(rn)
    checkerror()
    return r


def blankRange():
    """Create a range with no pages in."""
    r = libc.pycpdf_blankRange()
    checkerror()
    l = list_of_range(r)
    deleteRange(r)
    return l


def pageRange(f, t):
    """Build a range from one page to another inclusive. For example,
    pageRange(3,7) gives the range 3,4,5,6,7."""
    rn = libc.pycpdf_pageRange(f, t)
    r = list_of_range(rn)
    deleteRange(rn)
    checkerror()
    return r


def all(pdf):
    """The range containing all the pages in a given document."""
    rn = libc.pycpdf_all(pdf.pdf)
    r = list_of_range(rn)
    deleteRange(rn)
    checkerror()
    return r


def even(r):
    """A range which contains just the even pages of another range."""
    rn = range_of_list(r)
    reven = libc.pycpdf_even(rn)
    rout = list_of_range(reven)
    deleteRange(rn)
    deleteRange(reven)
    checkerror()
    return rout


def odd(r):
    """A range which contains just the odd pages of another range."""
    rn = range_of_list(r)
    rodd = libc.pycpdf_odd(rn)
    rout = list_of_range(rodd)
    deleteRange(rn)
    deleteRange(rodd)
    checkerror()
    return rout


def rangeUnion(a, b):
    """The union of two ranges giving a range containing
    the pages in range a and range b."""
    ra = range_of_list(a)
    rb = range_of_list(b)
    runion = libc.pycpdf_rangeUnion(ra, rb)
    rout = list_of_range(runion)
    deleteRange(ra)
    deleteRange(rb)
    deleteRange(runion)
    checkerror()
    return rout


def difference(a, b):
    """The difference of two ranges, giving a range
    containing all the pages in a except for those which are also in b."""
    ra = range_of_list(a)
    rb = range_of_list(b)
    rdiff = libc.pycpdf_difference(ra, rb)
    rout = list_of_range(rdiff)
    deleteRange(ra)
    deleteRange(rb)
    deleteRange(rdiff)
    checkerror()
    return rout


def removeDuplicates(r):
    """Deduplicates a range, returning a new one."""
    rn = range_of_list(r)
    rdup = libc.pycpdf_removeDuplicates(rn)
    rout = list_of_range(rdup)
    deleteRange(rn)
    deleteRange(rdup)
    checkerror()
    return rout


def rangeLength(r):
    """The number of pages in a range."""
    rn = range_of_list(r)
    l = libc.pycpdf_rangeLength(rn)
    deleteRange(rn)
    checkerror()
    return l


def rangeGet(r, n):
    """Get the page number at position n in a range, where
    n runs from 0 to rangeLength - 1."""
    rn = range_of_list(r)
    r2 = libc.pycpdf_rangeGet(rn, n)
    deleteRange(rn)
    checkerror()
    return r2


def rangeAdd(r, p):
    """Add the page to a range, if it is not already
    there."""
    rn = range_of_list(r)
    radd = libc.pycpdf_rangeAdd(rn, p)
    rout = list_of_range(radd)
    deleteRange(rn)
    deleteRange(radd)
    checkerror()
    return rout


def isInRange(r, p):
    """Returns True if the page p is in the range r, False otherwise."""
    rn = range_of_list(r)
    r2 = libc.pycpdf_isInRange(rn, p)
    deleteRange(rn)
    checkerror()
    return r2


def pages(pdf):
    """Return the number of pages in a PDF."""
    r = libc.pycpdf_pages(pdf.pdf)
    checkerror()
    return r


def pagesFast(userpw, filename):
    """Return the number of pages in a given PDF, with given user password. It
    tries to do this as fast as possible, without loading the whole file."""
    r = libc.pycpdf_pagesFast(str.encode(userpw), str.encode(filename))
    checkerror()
    return r


def toFile(pdf, filename, linearize, make_id):
    """Write the file to a given filename. If linearize is True, it will be
    linearized, if supported by libcpdf. If make_id is True, it will be given a
    new ID. NB: Unlike with the command line tool, cpdf, streams decompressed
    during processing will not automatically be compressed when writing. Call
    compress() first."""
    libc.pycpdf_toFile(pdf.pdf, str.encode(filename), False, False)
    checkerror()


def toFileExt(pdf, filename, linearize, make_id, preserve_objstm,
              generate_objstm, compress_objstm):
    """Write the file to a given filename. If linearize is True, it will be
    linearized, if supported by libcpdf. If make_id is True, it will be given a
    new ID.  If preserve_objstm is True, existing object streams will be
    preserved. If generate_objstm is True, object streams will be generated
    even if not originally present. If compress_objstm is True, object streams
    will be compressed (what we usually want). WARNING: the pdf argument will
    be invalid after this call and should not be used again."""
    libc.pycpdf_toFileExt(pdf.pdf, str.encode(filename), linearize, make_id,
                          preserve_objstm, generate_objstm, compress_objstm)
    checkerror()


def toMemory(pdf, linearize, make_id):
    """Write a file to memory, returning the buffer as a byte array of type
    bytes. NB: Unlike with the command line tool, cpdf, streams decompressed
    during processing will not automatically be compressed when writing. Call
    compress() first."""
    length = c_int32()
    data = libc.pycpdf_toMemory(pdf.pdf, linearize, make_id, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_toMemoryFree()
    checkerror()
    return out_data.raw


def isEncrypted(pdf):
    """Returns True if a documented is encrypted, False otherwise."""
    r = libc.pycpdf_isEncrypted(pdf.pdf)
    checkerror()
    return r


"""Permissions."""
noEdit = 0
noPrint = 1
noCopy = 2
noAnnot = 3
noForms = 4
noExtract = 5
noAssemble = 6
noHqPrint = 7

"""Encryption Methods."""
pdf40bit = 0
pdf128bit = 1
aes128bitfalse = 2
aes128bittrue = 3
aes256bitfalse = 4
aes256bittrue = 5
aes256bitisofalse = 6
aes256bitisotrue = 7


def toFileEncrypted(pdf, method, permissions, ownerpw, userpw, linearize,
                    makeid, filename):
    """Write the file to a given filename encrypted with the given encryption
    method, permissions list, and owener and user passwords. If linearize is
    True, it will be linearized, if supported by libcpdf. If make_id is True,
    it will be given a new ID."""
    c_perms = (c_uint8 * len(permissions))(*permissions)
    libc.pycpdf_toFileEncrypted(pdf.pdf, method, c_perms, len(permissions),
                                str.encode(ownerpw), str.encode(userpw),
                                linearize, makeid, str.encode(filename))
    checkerror()


def toFileEncryptedExt(pdf, method, permissions, ownerpw, userpw, linearize,
                       makeid, preserve_objstm, generate_objstm,
                       compress_objstm, filename):
    """Write the file to a given filename encrypted with the given encryption
    method, permissions list, and owener and user passwords. If linearize is
    True, it will be linearized, if supported by libcpdf. If make_id is True,
    it will be given a new ID. If preserve_objstm is True, existing object
    streams will be preserved. If generate_objstm is True, object streams will
    be generated even if not originally present. If compress_objstm is True,
    object streams will be compressed (what we usually want). WARNING: the pdf
    argument will be invalid after this call and should not be used again."""
    c_perms = (c_uint8 * len(permissions))(*permissions)
    libc.pycpdf_toFileEncryptedExt(pdf.pdf, method, c_perms, len(permissions),
                                   str.encode(ownerpw), str.encode(userpw),
                                   linearize, makeid, preserve_objstm,
                                   generate_objstm, compress_objstm,
                                   str.encode(filename))
    checkerror()


def decryptPdf(pdf, userpw):
    """Attempts to decrypt a PDF using the given user password. An exception is
    raised in the event of a bad password."""
    libc.pycpdf_decryptPdf(pdf.pdf, str.encode(userpw))
    checkerror()


def decryptPdfOwner(pdf, ownerpw):
    """Attempts to decrypt a PDF using the given owner password. An exception
    is raised in the event of a bad password."""
    libc.pycpdf_decryptPdfOwner(pdf.pdf, str.encode(ownerpw))
    checkerror()


def hasPermission(pdf, perm):
    """Returns True if the given permission (restriction) is present."""
    r = libc.pycpdf_hasPermission(pdf.pdf, perm)
    checkerror()
    return r


def encryptionKind(pdf):
    """Return the encryption method currently in use on a document."""
    r = libc.pycpdf_encryptionKind(pdf.pdf)
    checkerror()
    return r


def loadFont(name, filename):
    """Loads a TrueType font from the given file name, and names it. It may
    then be used when adding text or drawing, using the name in place of a
    standard font name. """
    libc.pycpdf_loadFont(str.encode(name), str.encode(filename))
    checkerror()
    return

# CHAPTER 2. Merging and Splitting


def mergeSimple(pdfs):
    """Given a list of PDFs, merges the documents into a new PDF, which is
    returned."""
    raw_pdfs = list(map(lambda p: p.pdf, pdfs))
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    r = Pdf(libc.pycpdf_mergeSimple(c_pdfs, len(pdfs)))
    checkerror()
    return r


def merge(pdfs, retain_numbering, remove_duplicate_fonts):
    """Merges the list of PDFs. If retain_numbering is True page labels are not
    rewritten. If remove_duplicate_fonts is True, duplicate fonts are merged.
    This is useful when the source documents for merging originate from the
    same source."""
    raw_pdfs = map(lambda p: p.pdf, pdfs)
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    r = Pdf(libc.pycpdf_merge(c_pdfs, len(pdfs),
            retain_numbering, remove_duplicate_fonts))
    checkerror()
    return r


def mergeSame(pdfs, retain_numbering, remove_duplicate_fonts, ranges):
    """The same as merge, except that it has an additional argument (a list of
    page ranges). This is used to select the pages to pick from each PDF. This
    avoids duplication of information when multiple discrete parts of a single
    source PDF are included."""
    ranges = list(map(range_of_list, ranges))
    raw_pdfs = map(lambda p: p.pdf, pdfs)
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    c_ranges = (c_int * len(ranges))(*ranges)
    r = Pdf(libc.pycpdf_mergeSame(c_pdfs, len(pdfs),
            retain_numbering, remove_duplicate_fonts, c_ranges))
    for x in ranges:
        deleteRange(x)
    checkerror()
    return r


def selectPages(pdf, r):
    """Returns a new document which just those pages in the page range."""
    rn = range_of_list(r)
    r = Pdf(libc.pycpdf_selectPages(pdf.pdf, rn))
    deleteRange(rn)
    checkerror()
    return r

# CHAPTER 3. Pages


def scalePages(pdf, r, sx, sy):
    """Scale the page dimensions and content of the given range of pages by
    the given scale (sx, sy), about (0, 0). Other boxes (crop etc. are altered
    as appropriate)."""
    r = range_of_list(r)
    libc.pycpdf_scalePages(pdf.pdf, r, sx, sy)
    deleteRange(r)
    checkerror()


def scaleToFit(pdf, r, w, h, scale_to_fit_scale):
    """Scales the pages in the range to fit new page dimensions (w and h)
    multiplied by scale_to_fit_scale (typically 1.0).  Other boxes (crop etc.)
    are altered as appropriate."""
    r = range_of_list(r)
    libc.pycpdf_scaleToFit(pdf.pdf, r, w, h, scale_to_fit_scale)
    deleteRange(r)
    checkerror()


"""Paper sizes."""
a0portrait = 0
a1portrait = 1
a2portrait = 2
a3portrait = 3
a4portrait = 4
a5portrait = 5
a0landscape = 6
a1landscape = 7
a2landscape = 8
a3landscape = 9
a4landscape = 10
a5landscape = 11
usletterportrait = 12
usletterlandscape = 13
uslegalportrait = 14
uslegallandscape = 15


def scaleToFitPaper(pdf, r, papersize, scale_to_fit_scale):
    """Scales the given pages to fit the given page size, possibly multiplied
    by scale_to_fit_scale (typically 1.0)."""
    r = range_of_list(r)
    libc.pycpdf_scaleToFitPaper(pdf.pdf, r, papersize, scale_to_fit_scale)
    deleteRange(r)
    checkerror()


"""Positions with two numbers in a tuple e.g (posLeft, 10.0, 20.0):"""
posCentre = 0
posLeft = 1
posRight = 2
"""Positions with one number in a tuple e.g (top, 5.0):"""
top = 3
topLeft = 4
topRight = 5
left = 6
bottomLeft = 7
bottomRight = 8
right = 9
"""Positions with no numbers e.g diagonal:"""
diagonal = 10
reverseDiagonal = 11


def tripleOfPosition(p):
    if p == diagonal:
        return (p, 0.0, 0.0)
    if p == reverseDiagonal:
        return (p, 0.0, 0.0)
    if p[0] == top:
        return (p[0], p[1], 0.0)
    if p[0] == topLeft:
        return (p[0], p[1], 0.0)
    if p[0] == topRight:
        return (p[0], p[1], 0.0)
    if p[0] == left:
        return (p[0], p[1], 0.0)
    if p[0] == bottomLeft:
        return (p[0], p[1], 0.0)
    if p[0] == bottomRight:
        return (p[0], p[1], 0.0)
    if p[0] == right:
        return (p[0], p[1], 0.0)
    if p[0] == posCentre:
        return (p[0], p[1], p[2])
    if p[0] == posLeft:
        return (p[0], p[1], p[2])
    if p[0] == posRight:
        return (p[0], p[1], p[2])


def scaleContents(pdf, r, pos, scale):
    """Scales the contents of the pages in the range about the point given by
    the position, by the scale given."""
    r = range_of_list(r)
    a, b, c = tripleOfPosition(pos)
    libc.pycpdf_scaleContents(pdf.pdf, r, a, b, c, scale)
    deleteRange(r)
    checkerror()


def shiftContents(pdf, r, dx, dy):
    """Shift the content of the pages in the range by (dx, dy)."""
    r = range_of_list(r)
    libc.pycpdf_shiftContents(pdf.pdf, r, dx, dy)
    deleteRange(r)
    checkerror()


def shiftBoxes(pdf, r, dx, dy):
    """Shift the pages boxes in the range by (dx, dy)."""
    r = range_of_list(r)
    libc.pycpdf_shiftBoxes(pdf.pdf, r, dx, dy)
    deleteRange(r)
    checkerror()


def rotate(pdf, r, rotation):
    """Change the viewing rotation of the pages in the range to an absolute
    value. Appropriate rotations are 0, 90, 180, 270."""
    r = range_of_list(r)
    libc.pycpdf_rotate(pdf.pdf, r, rotation)
    deleteRange(r)
    checkerror()


def rotateBy(pdf, r, rotation):
    """Change the viewing rotation of the pages in the range by a given number
    of degrees. Appropriate values are 90, 180, 270."""
    r = range_of_list(r)
    libc.pycpdf_rotateBy(pdf.pdf, r, rotation)
    deleteRange(r)
    checkerror()


def rotateContents(pdf, r, rotation):
    """Rotate the content about the centre of the page by the given number of
    degrees, in a clockwise direction."""
    r = range_of_list(r)
    libc.pycpdf_rotateContents(pdf.pdf, r, rotation)
    deleteRange(r)
    checkerror()


def upright(pdf, r):
    """Change the viewing rotation of the pages in the range, counter-rotating
    the dimensions and content such that there is no visual change."""
    r = range_of_list(r)
    libc.pycpdf_upright(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def hFlip(pdf, r):
    """Flip horizontally the pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_hFlip(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def vFlip(pdf, r):
    """Flip vertically the pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_vFlip(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def crop(pdf, r, x, y, w, h):
    """Crop a page to the box defined by (x, y, w, h), replacing any existing
    crop box."""
    r = range_of_list(r)
    libc.pycpdf_crop(pdf.pdf, r, x, y, w, h)
    deleteRange(r)
    checkerror()


def removeCrop(pdf, r):
    """Remove any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeCrop(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def removeTrim(pdf, r):
    """Remove any trim box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeTrim(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def removeArt(pdf, r):
    """Remove any art box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeArt(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def removeBleed(pdf, r):
    """Remove any bleed box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeBleed(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def trimMarks(pdf, r):
    """Add trim marks to the given pages, if the trimbox exists."""
    r = range_of_list(r)
    libc.pycpdf_trimMarks(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def showBoxes(pdf, r):
    """Show the boxes on the given pages, for debug."""
    r = range_of_list(r)
    libc.pycpdf_showBoxes(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def hardBox(pdf, r, boxname):
    """Make a given box a 'hard box' i.e clip it explicitly. Boxname could be,
    for example "/TrimBox"."""
    r = range_of_list(r)
    libc.pycpdf_hardBox(pdf.pdf, r, str.encode(boxname))
    deleteRange(r)
    checkerror()

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in pycpdflib

# CHAPTER 5. Compression


def compress(pdf):
    """Compress any uncompressed streams in the given PDF using the Flate
    algorithm."""
    libc.pycpdf_compress(pdf.pdf)
    checkerror()


def decompress(pdf):
    """Decompress any streams in the given PDF, so long as the compression
    method is supported."""
    libc.pycpdf_decompress(pdf.pdf)
    checkerror()


def squeezeInMemory(pdf):
    """squeezeToMemory(pdf) squeezes a pdf in memory. Squeezing is a lossless
    compression method which works by rearrangement of a PDFs internal
    structure."""
    libc.pycpdf_squeezeInMemory(pdf.pdf)
    checkerror()

# CHAPTER 6. Bookmarks


def getBookmarks(pdf):
    """Get the bookmarks for a PDF as a list of tuples of the form:
    (level : int, page : int, text : string, openstatus : bool)"""
    l = []
    libc.pycpdf_startGetBookmarkInfo(pdf.pdf)
    n = libc.pycpdf_numberBookmarks()
    for x in range(n):
        level = libc.pycpdf_getBookmarkLevel(x)
        page = libc.pycpdf_getBookmarkPage(pdf.pdf, x)
        text = string_at(libc.pycpdf_getBookmarkText(x)).decode()
        openStatus = libc.pycpdf_getBookmarkOpenStatus(x)
        l.append((level, page, text, openStatus))
    libc.pycpdf_endGetBookmarkInfo(pdf.pdf)
    checkerror()
    return l


def setBookmarks(pdf, marks):
    """Set the bookmarks for a PDF as a list of tuples of the form:
    (level : int, page : int, text : string, openstatus : bool)"""
    libc.pycpdf_startSetBookmarkInfo(len(marks))
    for n, m in enumerate(marks):
        level, page, text, openStatus = m
        libc.pycpdf_setBookmarkLevel(n, level)
        libc.pycpdf_setBookmarkPage(pdf.pdf, n, page)
        libc.pycpdf_setBookmarkOpenStatus(n, openStatus)
        libc.pycpdf_setBookmarkText(n, str.encode(text))
    libc.pycpdf_endSetBookmarkInfo(pdf.pdf)
    checkerror()


def getBookmarksJSON(pdf):
    """Get the bookmarks in JSON format."""
    length = c_int32()
    data = libc.pycpdf_getBookmarksJSON(pdf.pdf, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_getBookmarksJSONFree()
    checkerror()
    return out_data.raw


def setBookmarksJSON(pdf, data):
    """Sets the bookmarks from JSON bookmark data."""
    libc.pycpdf_setBookmarksJSON(pdf.pdf, data, len(data))
    checkerror()
    return


def tableOfContents(pdf, font, fontsize, title, bookmark):
    """Typesets a table of contents from existing bookmarks and prepends it to
    the document. If bookmark is set, the table of contents gets its own
    bookmark."""
    pdf = libc.pycpdf_tableOfContents(
        pdf.pdf, str.encode(font), fontsize, str.encode(title), bookmark)
    checkerror()
    return pdf

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps


def stampOn(pdf, pdf2, r):
    """Stamps pdf on top of all the pages in pdf2 which are in the range. The
    stamp is placed with its origin at the origin of the target document."""
    r = range_of_list(r)
    libc.pycpdf_stampOn(pdf.pdf, pdf2.pdf, r)
    deleteRange(r)
    checkerror()


def stampUnder(pdf, pdf2, r):
    """Stamps pdf under under all the pages in pdf2 which are in the range. The
    stamp is placed with its origin at the origin of the target document."""
    r = range_of_list(r)
    libc.pycpdf_stampUnder(pdf.pdf, pdf2.pdf, r)
    deleteRange(r)
    checkerror()


def stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, pos,
                  relative_to_cropbox):
    """A stamping function with extra features:

     - isover True, pdf goes over pdf2, isover False, pdf goes under pdf2
     - scale_stamp_to_fit scales the stamp to fit the page
     - pos gives the position to put the stamp
     - relative_to_cropbox: if True, pos is relative to crop box not media box
    """
    r = range_of_list(r)
    a, b, c = tripleOfPosition(pos)
    libc.pycpdf_stampExtended(pdf.pdf, pdf2.pdf, r, isover, scale_stamp_to_fit,
                              a, b, c, relative_to_cropbox)
    deleteRange(r)
    checkerror()


def combinePages(pdf, pdf2):
    """Combines the PDFs page-by-page, putting each page of pdf2 over each page
    of pdf."""
    output = libc.pycpdf_combinePages(pdf.pdf, pdf2.pdf)
    checkerror()
    return Pdf(output)


"""Fonts."""
timesRoman = "Times-Roman"
timesBold = "Times-Bold"
timesItalic = "Times-Italic"
timesBoldItalic = "Times-BoldItalic"
helvetica = "Helvetica"
helveticaBold = "Helvetica-Bold"
helveticaOblique = "Helvetica-Oblique"
helveticaBoldOblique = "Helvetica-BoldOblique"
courier = "Courier"
courierBold = "Courier-Bold"
courierOblique = "Courier-Oblique"
courierBoldOblique = "Courier-BoldOblique"


"""Justifications."""
leftJustify = 0
centreJustify = 1
rightJustify = 2


def addText(metrics, pdf, r, text, p, line_spacing, bates, font, size, red,
            green, blue, underneath, relative_to_cropbox, outline, opacity,
            justification, midline, topline, filename, line_width,
            embed_fonts):
    """Adding text. Adds text to a PDF, if the characters exist in the font.

         * metrics: If True, don't actually add text but collect metrics.
         * pdf:	Document
         * r: Page Range
         * text: The text to add
         * p: Position to add text at
         * line_spacing: Linespacing, 1.0 = normal
         * bates: Starting Bates number
         * font: Font
         * size: Font size in points
         * red: Red component of colour, 0.0 - 1.0
         * green: Green component of colour, 0.0 - 1.0
         * blue: Blue component of colour, 0.0 - 1.0
         * underneath: If True, text is added underneath rather than on top
         * relative_to_cropbox: If True, position is relative to crop box not
           media box
         * outline: If True, text is outline rather than filled
         * opacity: Opacity, 1.0 = opaque, 0.0 = wholly transparent
         * justification: Justification
         * midline: If True, position is relative to midline of text, not
           baseline
         * topline: If True, position is relative to topline of text, not
           baseline
         * filename: filename that this document was read from (optional)
         * line_width: line width
         * embed_fonts: embed fonts

    Special codes

      * %Page     Page number in arabic notation (1, 2, 3...)
      * %roman    Page number in lower-case roman notation (i, ii, iii...)
      * %Roman    Page number in upper-case roman notation (I, II, III...)
      * %EndPage  Last page of document in arabic notation
      * %Label    The page label of the page
      * %EndLabel The page label of the last page
      * %filename The full file name of the input document
      * %a        Abbreviated weekday name (Sun, Mon etc.)
      * %A        Full weekday name (Sunday, Monday etc.)
      * %b        Abbreviated month name (Jan, Feb etc.)
      * %B        Full month name (January, February etc.)
      * %d        Day of the month (01-31)
      * %e        Day of the month (1-31)
      * %H        Hour in 24-hour clock (00-23)
      * %I        Hour in 12-hour clock (01-12)
      * %j        Day of the year (001-366)
      * %m        Month of the year (01-12)
      * %M        Minute of the hour (00-59)
      * %p        "a.m" or "p.m"
      * %S        Second of the minute (00-61)
      * %T        Same as %H:%M:%S
      * %u        Weekday (1-7, 1 = Monday)
      * %w        Weekday (0-6, 0 = Monday)
      * %Y        Year (0000-9999)
      * %%        The % character"""
    a, b, c = tripleOfPosition(p)
    r = range_of_list(r)
    libc.pycpdf_addText(metrics, pdf.pdf, r, str.encode(text), a, b, c,
                        line_spacing, bates, str.encode(
                            font), size, red, green, blue,
                        underneath, relative_to_cropbox, outline, opacity,
                        justification, midline, topline, str.encode(filename),
                        line_width, embed_fonts)
    deleteRange(r)
    checkerror()


def addTextSimple(pdf, r, text, p, font, size):
    """Like addText, but with most parameters default

         * pdf = the document
         * r = the range
         * text = the text
         * p = the position
         * font = the font
         * size = the font size
    NB: %filename cannot be used here. """

    a, b, c = tripleOfPosition(p)
    r = range_of_list(r)
    libc.pycpdf_addTextSimple(
        pdf.pdf, r, str.encode(text), a, b, c, str.encode(font), size)
    deleteRange(r)
    checkerror()


def removeText(pdf, r):
    """Remove any text added by libcpdf from the given pages."""
    r = range_of_list(r)
    libc.pycpdf_removeText(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def textWidth(font, string):
    """Return the width of a given string in the given font in thousandths of a
    point."""
    r = libc.pycpdf_textWidth(str.encode(font), str.encode(string))
    checkerror()
    return r


def addContent(content, before, pdf, r):
    """Add page content before (if True) or after (if False) the existing
    content to pages in the given range in the given PDF. Warning: this a low
    level function requiring understanding of the PDF format."""
    r = range_of_list(r)
    libc.pycpdf_addContent(str.encode(content), before, pdf.pdf, r)
    deleteRange(r)
    checkerror()


def stampAsXObject(pdf, r, stamp_pdf):
    """Stamps stamp_pdf onto the pages in the given range in pdf as a shared
    Form XObject. The name of the newly-created XObject is returned, for use
    with addContent. """
    r = range_of_list(r)
    r2 = string_at(libc.pycpdf_stampAsXObject(
        pdf.pdf, r, stamp_pdf.pdf)).decode()
    deleteRange(r)
    checkerror()
    return r2


# CHAPTER 9. Multipage facilities

def twoUp(pdf):
    """Impose a document two up by retaining the existing page size, scaling
    pages down."""
    libc.pycpdf_twoUp(pdf.pdf)
    checkerror()


def twoUpStack(pdf):
    """Impose a document two up by doubling the page size, to fit two pages on
    one."""
    libc.pycpdf_twoUpStack(pdf.pdf)
    checkerror()


def impose(pdf, x, y, fit, columns, rtl, btt, center, margin, spacing, linewidth):
    """Impose a PDF. There are two modes: imposing x * y, or imposing to fit a
    page of size x * y. This is controlled by fit. Columns imposes by columns
    rather than rows. rtl is right-to-left, btt bottom-to-top. Center is unused
    for now. Margin is the margin around the output, spacing the spacing
    between imposed inputs."""
    libc.pycpdf_impose(pdf.pdf, x, y, fit, columns, rtl,
                       btt, center, margin, spacing, linewidth)
    checkerror()


def chop(pdf, r, x, y, columns, rtl, btt):
    """Chop each page in the range into x * y pieces. If columns is set, the
    pieces go by columns instead of rows. If rtl is set, the pieces are taken
    right-to-left. If btt is set, the pieces are taken from bottom to top. """
    r = range_of_list(r)
    libc.pycpdf_chop(pdf.pdf, r, x, y, columns, rtl, btt)
    deleteRange(r)
    checkerror()


def chopH(pdf, r, columns, y):
    """Chop each page in the range horizontally at position y. If columns is
    set, the pieces are arranged in reverse order. """
    r = range_of_list(r)
    libc.pycpdf_chopH(pdf.pdf, r, columns, y)
    deleteRange(r)
    checkerror()


def chopV(pdf, r, columns, x):
    """Chop each page in the range vertically at position x. If columns is
    set, the pieces are arranged in reverse order. """
    r = range_of_list(r)
    libc.pycpdf_chopV(pdf.pdf, r, columns, x)
    deleteRange(r)
    checkerror()


def padBefore(pdf, r):
    """Adds a blank page before each page in the given range."""
    r = range_of_list(r)
    libc.pycpdf_padBefore(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def padAfter(pdf, r):
    """Adds a blank page after each page in the given range."""
    r = range_of_list(r)
    libc.pycpdf_padAfter(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def padEvery(pdf, n):
    """Adds a blank page after every n pages."""
    libc.pycpdf_padEvery(pdf.pdf, n)
    checkerror()


def padMultiple(pdf, n):
    """Adds pages at the end to pad the file to a multiple of n pages in
    length."""
    libc.pycpdf_padMultiple(pdf.pdf, n)
    checkerror()


def padMultipleBefore(pdf, n):
    """Adds pages at the beginning to pad the file to a multiple of n pages in
    length."""
    libc.pycpdf_padMultipleBefore(pdf.pdf, n)
    checkerror()

# CHAPTER 10. Annotations


def annotationsJSON(pdf):
    """Gets the annotations in JSON format."""
    length = c_int32()
    data = libc.pycpdf_annotationsJSON(pdf.pdf, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_annotationsJSONFree()
    checkerror()
    return out_data.raw


def removeAnnotations(pdf, r):
    """Removes all annotations from pages in the given range."""
    rn = range_of_list(r)
    libc.pycpdf_removeAnnotations(pdf.pdf, rn)
    deleteRange(rn)
    checkerror()
    return


def setAnnotationsJSON(pdf, data):
    """Adds the annotations given in JSON format to the PDF, on top of any
    existing annotations."""
    libc.pycpdf_setAnnotationsJSON(pdf.pdf, data, len(data))
    checkerror()
    return

# CHAPTER 11. Document Information and Metadata


def isLinearized(filename):
    """Finds out if a document is linearized as quickly as possible without
    loading it."""
    r = libc.pycpdf_isLinearized(str.encode(filename))
    checkerror()
    return r


def hasAcroForm(pdf):
    """Returns True if the document has an AcroForm."""
    r = libc.pycpdf_hasAcroForm(pdf.pdf)
    checkerror()
    return r


def getSubformats(pdf):
    """Returns a list of the subformats of the PDF, if any."""
    n = libc.pycpdf_startGetSubformats(pdf.pdf)
    l = []
    for x in range(n):
        l.append(string_at(libc.pycpdf_getSubformat(serial)).decode())
    libc.pycpdf_endGetSubformats()
    checkerror()
    return l


def hasObjectStreams(pdf):
    """Returns True if a document was written using object streams."""
    r = libc.pycpdf_hasObjectStreams(pdf.pdf)
    checkerror()
    return r


def id1(pdf):
    """Return the first ID string of the PDF, if any, in hexadecimal string
    format."""
    r = string_at(libc.pycpdf_id1(pdf.pdf)).decode()
    checkerror()
    return r


def id2(pdf):
    """Return the second ID string of the PDF, if any, in hexadecimal string
    format."""
    r = string_at(libc.pycpdf_id2(pdf.pdf)).decode()
    checkerror()
    return r


def getVersion(pdf):
    """Return the minor version number of a document."""
    r = libc.pycpdf_getVersion(pdf.pdf)
    checkerror()
    return r


def getMajorVersion(pdf):
    """Return the minor version number of a document."""
    r = libc.pycpdf_getMajorVersion(pdf.pdf)
    checkerror()
    return r


def getTitle(pdf):
    """Return the title of a document."""
    r = string_at(libc.pycpdf_getTitle(pdf.pdf)).decode()
    checkerror()
    return r


def getAuthor(pdf):
    """Return the subject of a document."""
    r = string_at(libc.pycpdf_getAuthor(pdf.pdf)).decode()
    checkerror()
    return r


def getSubject(pdf):
    """Return the subject of a document."""
    r = string_at(libc.pycpdf_getSubject(pdf.pdf)).decode()
    checkerror()
    return r


def getKeywords(pdf):
    """Return the keywords of a document."""
    r = string_at(libc.pycpdf_getKeywords(pdf.pdf)).decode()
    checkerror()
    return r


def getCreator(pdf):
    """Return the creator of a document."""
    r = string_at(libc.pycpdf_getCreator(pdf.pdf)).decode()
    checkerror()
    return r


def getProducer(pdf):
    """Return the producer of a document."""
    r = string_at(libc.pycpdf_getProducer(pdf.pdf)).decode()
    checkerror()
    return r


def getCreationDate(pdf):
    """Return the creation date of a document."""
    r = string_at(libc.pycpdf_getCreationDate(pdf.pdf)).decode()
    checkerror()
    return r


def getModificationDate(pdf):
    """Return the modification date of a document."""
    r = string_at(libc.pycpdf_getModificationDate(pdf.pdf)).decode()
    checkerror()
    return r


def getTitleXMP(pdf):
    """Return the XMP title of a document."""
    r = string_at(libc.pycpdf_getTitleXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getAuthorXMP(pdf):
    """Return the XMP author of a document."""
    r = string_at(libc.pycpdf_getAuthorXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getSubjectXMP(pdf):
    """Return the XMP subject of a document."""
    r = string_at(libc.pycpdf_getSubjectXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getKeywordsXMP(pdf):
    """Return the XMP keywords of a document."""
    r = string_at(libc.pycpdf_getKeywordsXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getCreatorXMP(pdf):
    """Return the XMP creator of a document."""
    r = string_at(libc.pycpdf_getCreatorXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getProducerXMP(pdf):
    """Return the XMP producer of a document."""
    r = string_at(libc.pycpdf_getProducerXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getCreationDateXMP(pdf):
    """Return the XMP creation date of a document."""
    r = string_at(libc.pycpdf_getCreationDateXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getModificationDateXMP(pdf):
    """Return the XMP modification date of a document."""
    r = string_at(libc.pycpdf_getModificationDateXMP(pdf.pdf)).decode()
    checkerror()
    return r


def setTitle(pdf, s):
    """Set the title of a document."""
    libc.pycpdf_setTitle(pdf.pdf, str.encode(s))
    checkerror()
    return


def setAuthor(pdf, s):
    """Set the author of a document."""
    libc.pycpdf_setAuthor(pdf.pdf, str.encode(s))
    checkerror()
    return


def setSubject(pdf, s):
    """Set the subject of a document."""
    libc.pycpdf_setSubject(pdf.pdf, str.encode(s))
    checkerror()
    return


def setKeywords(pdf, s):
    """Set the keywords of a document."""
    libc.pycpdf_setKeywords(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreator(pdf, s):
    """Set the creator of a document."""
    libc.pycpdf_setCreator(pdf.pdf, str.encode(s))
    checkerror()
    return


def setProducer(pdf, s):
    """Set the producer of a document."""
    libc.pycpdf_setProducer(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreationDate(pdf, s):
    """Set the creation date of a document."""
    libc.pycpdf_setCreationDate(pdf.pdf, str.encode(s))
    checkerror()
    return


def setModificationDate(pdf, s):
    """Set the modifcation date of a document."""
    libc.pycpdf_setModificationDate(pdf.pdf, str.encode(s))
    checkerror()
    return


def setTitleXMP(pdf, s):
    """Set the XMP title of a document."""
    libc.pycpdf_setTitleXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setAuthorXMP(pdf, s):
    """Set the XMP author of a document."""
    libc.pycpdf_setAuthorXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setSubjectXMP(pdf, s):
    """Set the XMP subject of a document."""
    libc.pycpdf_setSubjectXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setKeywordsXMP(pdf, s):
    """Set the XMP keywords of a document."""
    libc.pycpdf_setKeywordsXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreatorXMP(pdf, s):
    """Set the XMP creator of a document."""
    libc.pycpdf_setCreatorXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setProducerXMP(pdf, s):
    """Set the XMP producer of a document."""
    libc.pycpdf_setProducerXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreationDateXMP(pdf, s):
    """Set the XMP creation date of a document."""
    libc.pycpdf_setCreationDateXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setModificationDateXMP(pdf, s):
    """Set the XMP modification date of a document."""
    libc.pycpdf_setModificationDateXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def getDateComponents(string):
    """Return the components (year, month, day, hour, minute, second,
    hour_offset, minute_offset) from a PDF date string.

    Month 1-31, day 1-31, hours (0-23), minutes (0-59), seconds (0-59),
    hour_offset is the offset from UT in hours (-23 to 23); minute_offset is
    the offset from UT in minutes (-59 to 59)."""

    year = c_int(0)
    month = c_int(0)
    day = c_int(0)
    hour = c_int(0)
    minute = c_int(0)
    second = c_int(0)
    hour_offset = c_int(0)
    minute_offset = c_int(0)
    libc.pycpdf_getDateComponents(str.encode(string), byref(year),
                                  byref(month), byref(day), byref(hour),
                                  byref(minute), byref(second),
                                  byref(hour_offset), byref(minute_offset))
    checkerror()
    return (year.value, month.value, day.value, hour.value, minute.value,
            second.value, hour_offset.value, minute_offset.value)


def dateStringOfComponents(cs):
    """Build a PDF date string a (year, month, day, hour, minute, second,
    hour_offset, minute_offset) tuple.

    Dates: Month 1-31, day 1-31, hours (0-23), minutes (0-59), seconds (0-59),
    hour_offset is the offset from UT in hours (-23 to 23); minute_offset is
    the offset from UT in minutes (-59 to 59)."""
    year, month, day, hour, minute, second, hour_offset, minute_offset = cs
    r = string_at(libc.pycpdf_dateStringOfComponents(year, month, day, hour,
                                                     minute, second,
                                                     hour_offset,
                                                     minute_offset)).decode()
    checkerror()
    return r


def getPageRotation(pdf, pagenumber):
    """Get the viewing rotation for a given page."""
    r = libc.pycpdf_getPageRotation(pdf.pdf, pagenumber)
    checkerror()
    return r


def hasBox(pdf, pagenumber, boxname):
    """Returns True, if the page has the given box. E.g "/CropBox"."""
    r = libc.pycpdf_hasBox(pdf.pdf, pagenumber, str.encode(boxname))
    checkerror()
    return r


def numAnnots(pdf, pagenumber):
    """Return the number of annotations on the given page in the given PDF."""
    r = libc.pycpdf_numAnnots(pdf.pdf, pagenumber)
    checkerror()
    return r


def getMediaBox(pdf, pagenumber):
    """Get a mediabox box given the document, page range, min x, max x, min y,
    max y in points. Only suceeds if such a box exists, as checked by
    hasBox."""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getMediaBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getCropBox(pdf, pagenumber):
    """Get a crop box given the document, page range, min x, max x, min y, max
    y in points. Only suceeds if such a box exists, as checked by hasBox."""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getCropBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getTrimBox(pdf, pagenumber):
    """Get a trim box given the document, page range, min x, max x, min y, max
    y in points. Only suceeds if such a box exists, as checked by hasBox."""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getTrimBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getArtBox(pdf, pagenumber):
    """Get an art box given the document, page range, min x, max x, min y, max
    y in points. Only suceeds if such a box exists, as checked by hasBox."""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getArtBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getBleedBox(pdf, pagenumber):
    """Get a bleed box given the document, page range, min x, max x, min y, max
    y in points. Only suceeds if such a box exists, as checked by hasBox."""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getBleedBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def setMediaBox(pdf, r, minx, maxx, miny, maxy):
    """Set the media box given the document, page range, min x, max x, min y,
    max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setMediaBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def setCropBox(pdf, r, minx, maxx, miny, maxy):
    """Set the crop box given the document, page range, min x, max x, min y,
    max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setCropBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def setTrimBox(pdf, r, minx, maxx, miny, maxy):
    """Set the trim box given the document, page range, min x, max x, min y,
    max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setTrimBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def setArtBox(pdf, r, minx, maxx, miny, maxy):
    """Set the art box given the document, page range, min x, max x, min y, max
    y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setArtBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def pageInfoJSON(pdf):
    """Returns JSON data for the page information."""
    length = c_int32()
    data = libc.pycpdf_pageInfoJSON(pdf.pdf, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_pageInfoJSONFree()
    checkerror()
    return out_data.raw


def setBleedBox(pdf, r, minx, maxx, miny, maxy):
    """Set the bleed box given the document, page range, min x, max x,
    min y, max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setBleedBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def markTrapped(pdf):
    """Mark a document as trapped."""
    libc.pycpdf_markTrapped(pdf.pdf)
    checkerror()
    return


def markUntrapped(pdf):
    """Mark a document as untrapped."""
    libc.pycpdf_markUntrapped(pdf.pdf)
    checkerror()
    return


def markTrappedXMP(pdf):
    """Mark a document as trapped in XMP metadata."""
    libc.pycpdf_markTrappedXMP(pdf.pdf)
    checkerror()
    return


def markUntrappedXMP(pdf):
    """Mark a document as untrapped in XMP metadata."""
    libc.pycpdf_markUntrappedXMP(pdf.pdf)
    checkerror()
    return


"""Page layouts."""
singlePage = 0
oneColumn = 1
twoColumnLeft = 2
twoColumnRight = 3
twoPageLeft = 4
twoPageRight = 5


def setPageLayout(pdf, layout):
    """Set the page layout for a document."""
    libc.pycpdf_setPageLayout(pdf.pdf, layout)
    checkerror()
    return


def getPageLayout(pdf):
    """Get the page layout for a document."""
    r = libc.pycpdf_getPageLayout(pdf.pdf)
    checkerror()
    return r


"""Page modes."""
useNone = 0
useOutlines = 1
useThumbs = 2
useOC = 3
useAttachments = 4


def setPageMode(pdf, mode):
    """Set the page mode for a document."""
    libc.pycpdf_setPageMode(pdf.pdf, mode)
    checkerror()
    return


def getPageMode(pdf):
    """Get the page mode for a document"""
    r = libc.pycpdf_getPageMode(pdf.pdf)
    checkerror()
    return r


def hideToolbar(pdf, flag):
    """Sets the hide toolbar flag."""
    libc.pycpdf_hideToolbar(pdf.pdf, flag)
    checkerror()
    return


def getHideToolbar(pdf):
    """Get the hide toolbar flag."""
    r = libc.pycpdf_getHideToolbar(pdf.pdf)
    checkerror()
    return r


def hideMenubar(pdf, flag):
    """Set the hide menu bar flag."""
    libc.pycpdf_hideMenubar(pdf.pdf, flag)
    checkerror()
    return


def getHideMenubar(pdf):
    """Get the hide menubar flag."""
    r = libc.pycpdf_getHideMenubar(pdf.pdf)
    checkerror()
    return r


def hideWindowUi(pdf, flag):
    """Set the hide window UI flag."""
    libc.pycpdf_hideWindowUi(pdf.pdf, flag)
    checkerror()
    return


def getHideWindowUi(pdf):
    """Get the hide window UI flag."""
    r = libc.pycpdf_getHideWindowUi(pdf.pdf)
    checkerror()
    return r


def fitWindow(pdf, flag):
    """Set the fit window flag."""
    libc.pycpdf_fitWindow(pdf.pdf, flag)
    checkerror()
    return


def getFitWindow(pdf):
    """Get the fit window flag."""
    r = libc.pycpdf_getFitWindow(pdf.pdf)
    checkerror()
    return r


def centerWindow(pdf, flag):
    """Set the center window flag."""
    libc.pycpdf_centerWindow(pdf.pdf, flag)
    checkerror()
    return


def getCenterWindow(pdf):
    """Get the center window flag."""
    r = libc.pycpdf_getCenterWindow(pdf.pdf)
    checkerror()
    return r


def displayDocTitle(pdf, flag):
    """Set the display document title flag."""
    libc.pycpdf_displayDocTitle(pdf.pdf, flag)
    checkerror()
    return


def getDisplayDocTitle(pdf):
    """Get the display document title flag."""
    r = libc.pycpdf_getDisplayDocTitle(pdf.pdf)
    checkerror()
    return r


def nonFullScreenPageMode(pdf, flag):
    """set the non full screen page mode flag."""
    libc.pycpdf_nonFullScreenPageMode(pdf.pdf, flag)
    checkerror()
    return


def getNonFullScreenPageMode(pdf):
    """get the non full screen page mode flag."""
    r = libc.pycpdf_getNonFullScreenPageMode(pdf.pdf)
    checkerror()
    return r


def openAtPage(pdf, fitflag, pagenumber):
    """Set the PDF to open, possibly with zoom-to-fit, at the given page number.
    """
    libc.pycpdf_openAtPage(pdf.pdf, fitflag, pagenumber)
    checkerror()
    return


def openAtPageCustom(pdf, custom):
    """Set a custom openAtPage description."""
    libc.pycpdf_openAtPageCustom(pdf.pdf, str.encode(custom))
    checkerror()
    return


def setMetadataFromFile(pdf, filename):
    """Set the XMP metadata of a document, given a file name."""
    libc.pycpdf_setMetadataFromFile(pdf.pdf, str.encode(filename))
    checkerror()
    return


def setMetadataFromByteArray(pdf, data):
    """Set the XMP metadata from an array of bytes."""
    libc.pycpdf_setMetadataFromByteArray(pdf.pdf, data, len(data))
    checkerror()
    return


def getMetadata(pdf):
    """Return the XMP metadata as a byte array of type bytes"""
    length = c_int32()
    data = libc.pycpdf_getMetadata(pdf.pdf, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_getMetadataFree()
    checkerror()
    return out_data.raw


def removeMetadata(pdf):
    """Remove the XMP metadata from a document."""
    libc.pycpdf_removeMetadata(pdf.pdf)
    checkerror()
    return


def createMetadata(pdf):
    """Builds fresh XMP metadata as good as possible from existing
    metadata in the document."""
    libc.pycpdf_createMetadata(pdf.pdf)
    checkerror()
    return


def setMetadataDate(pdf, date):
    """Set the metadata date for a PDF. The date is given in PDF date format --
    cpdf will convert it to XMP format. The date 'now' means now."""
    libc.pycpdf_setMetadataDate(pdf.pdf, str.encode(date))
    checkerror()
    return


"""Label styles."""
decimalArabic = 0
uppercaseRoman = 1
lowercaseRoman = 2
uppercaseLetters = 3
lowercaseLetters = 4


def getPageLabels(pdf):
    """Get page labels as a list of tuples (style, prefix, offset, startvalue)

    For example, a document might have five pages of introduction with roman
    numerals, followed by the rest of the pages in decimal arabic, numbered
    from one. First label:

    * labelstyle = LowercaseRoman
    * labelprefix = ""
    * startpage = 1
    * startvalue = 1

    Second label:

    * labelstyle = DecimalArabic
    * labelprefix = ""
    * startpage = 6
    * startvalue = 1"""
    n = libc.pycpdf_startGetPageLabels(pdf.pdf)
    l = []
    for x in range(n):
        style = libc.pycpdf_getPageLabelStyle(x)
        prefix = string_at(libc.pycpdf_getPageLabelPrefix(x)).decode()
        offset = libc.pycpdf_getPageLabelOffset(x)
        startvalue = libc.pycpdf_getPageLabelRange(x)
        l.append((style, prefix, offset, startvalue))
    libc.pycpdf_endGetPageLabels()
    checkerror()
    return l


def addPageLabels(pdf, label, progress):
    """Add one group of page labels from a tuple (style, prefix, offset, range).

    The prefix is prefix text for each label. The range is the page range the
    labels apply to. Offset can be used to shift the numbering up or down."""
    style, prefix, offset, plrange = label
    rn = range_of_list(plrange)
    libc.pycpdf_addPageLabels(pdf.pdf, style, str.encode(
        prefix), offset, rn, progress)
    deleteRange(rn)
    checkerror()
    return


def removePageLabels(pdf):
    """Removes all page labels from the document."""
    libc.pycpdf_removePageLabels(pdf.pdf)
    checkerror()
    return


def getPageLabelStringForPage(pdf, pagenumber):
    """Calculate the full label string for a given page, and return it."""
    r = string_at(libc.pycpdf_getPageLabelStringForPage(
        pdf.pdf, pagenumber)).decode()
    checkerror()
    return r


def compositionJSON(filesize, pdf):
    """Get the composition in JSON format."""
    length = c_int32()
    data = libc.pycpdf_compositionJSON(filesize, pdf.pdf, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_compositionJSONFree()
    checkerror()
    return out_data.raw

# CHAPTER 12. File Attachments


def attachFile(filename, pdf):
    """Attach a file to the pdf. It is attached at document level."""
    libc.pycpdf_attachFile(str.encode(filename), pdf.pdf)
    checkerror()


def attachFileToPage(filename, pdf, pagenumber):
    """Attach a file, given its file name, pdf, and the page number to which
    it should be attached."""
    libc.pycpdf_attachFileToPage(str.encode(filename), pdf.pdf, pagenumber)
    checkerror()


def attachFileFromMemory(data, filename, pdf):
    """Attach a file from a byte array. It is attached at document level."""
    libc.pycpdf_attachFileFromMemory(
        data, len(data), str.encode(filename), pdf.pdf)
    checkerror()


def attachFileToPageFromMemory(data, filename, pdf, pagenumber):
    """Attach a file to a given pag from a byte array. It is attached at
    document level."""
    libc.pycpdf_attachFileToPageFromMemory(
        data, len(data), str.encode(filename), pdf.pdf, pagenumber)
    checkerror()


def removeAttachedFiles(pdf):
    """Remove all page- and document-level attachments from a document."""
    libc.pycpdf_removeAttachedFiles(pdf.pdf)
    checkerror()


def getAttachments(pdf):
    """List information about attachements. Returns a list of tuples (name,
    page number, byte array of data). Page 0 = document-level attachment."""
    libc.pycpdf_startGetAttachments(pdf.pdf)
    n = libc.pycpdf_numberGetAttachments()
    l = []
    for i in range(n):
        name = string_at(libc.pycpdf_getAttachmentName(i)).decode()
        page = libc.pycpdf_getAttachmentPage(i)
        length = c_int32()
        data = libc.pycpdf_getAttachmentData(i, byref(length))
        out_data = create_string_buffer(length.value)
        memmove(out_data, data, length.value)
        libc.pycpdf_getAttachmentFree()
        l.append((name, page, out_data.raw))
    libc.pycpdf_endGetAttachments()
    checkerror()
    return l

# CHAPTER 13. Images


def getImageResolution(pdf, resolution):
    """Return a list of all uses of images in the PDF which do not meet the
    minimum required resolution in dpi as tuples of:
    (pagenumber, name, x pixels, y pixels, x resolution, y resolution, objnum).
    """
    n = libc.pycpdf_startGetImageResolution(pdf.pdf, resolution)
    l = []
    for x in range(n):
        pagenumber = libc.pycpdf_getImageResolutionPageNumber(x)
        imagename = string_at(
            libc.pycpdf_getImageResolutionImageName(x)).decode()
        xp = libc.pycpdf_getImageResolutionXPixels(x)
        yp = libc.pycpdf_getImageResolutionYPixels(x)
        xr = libc.pycpdf_getImageResolutionXRes(x)
        yr = libc.pycpdf_getImageResolutionYRes(x)
        on = libc.pycpdf_getImageResolutionObjNum(x)
        l.append((pagenumber, imagename, xp, yp, xr, yr, on))
    libc.pycpdf_endGetImageResolution()
    checkerror()
    return l


def imageResolutionJSON(pdf, resolution):
    """Return the image resolution data in JSON format."""
    length = c_int32()
    data = libc.pycpdf_imageResolutionJSON(pdf.pdf, byref(length), resolution)
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_imageResolutionJSONFree()
    checkerror()
    return out_data.raw


def getImages(pdf):
    """Return a list of images in the PDF as tuples of:
    (object number, pages occurring, image name, width, height, size,
     bitspercomponent, color space, filter)
    """
    n = libc.pycpdf_startGetImages(pdf.pdf)
    l = []
    for x in range(n):
        on = libc.pycpdf_getImageObjNum(x)
        pages = string_at(libc.pycpdf_getImagePages(x)).decode()
        imagename = string_at(libc.pycpdf_getImageName(x)).decode()
        w = libc.pycpdf_getImageWidth(x)
        h = libc.pycpdf_getImageHeight(x)
        size = libc.pycpdf_getImageSize(x)
        bpc = libc.pycpdf_getImageBPC(x)
        colspace = string_at(libc.pycpdf_getImageColSpace(x)).decode()
        filt = string_at(libc.pycpdf_getImageFilter(x)).decode()
        l.append((on, pages, imagename, w, h, size, bpc, colspace, filt))
    libc.pycpdf_endGetImages()
    checkerror()
    return l


def imagesJSON(pdf):
    """Return the list of images in the PDF in JSON format."""
    length = c_int32()
    data = libc.pycpdf_imagesJSON(pdf.pdf, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_imagesJSONFree()
    checkerror()
    return out_data.raw


# CHAPTER 14. Fonts


def getFontInfo(pdf):
    """Get a list of (pagenumber, fontname, fonttype, fontencoding) tuples,
    showing each font used on each page."""
    libc.pycpdf_startGetFontInfo(pdf.pdf)
    n = libc.pycpdf_numberFonts()
    l = []
    for x in range(n):
        pagenumber = libc.pycpdf_getFontPage(x)
        fontname = string_at(libc.pycpdf_getFontName(x)).decode()
        fonttype = string_at(libc.pycpdf_getFontType(x)).decode()
        fontencoding = string_at(libc.pycpdf_getFontEncoding(x)).decode()
        l.append((pagenumber, fontname, fonttype, fontencoding))
    libc.pycpdf_endGetFontInfo(pdf.pdf)
    checkerror()
    return l


def fontsJSON(pdf):
    """Return font information in JSON format."""
    length = c_int32()
    data = libc.pycpdf_fontsJSON(pdf.pdf, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_fontsJSONFree()
    checkerror()
    return out_data.raw


def removeFonts(pdf):
    """Remove all font data from a file."""
    libc.pycpdf_removeFonts(pdf.pdf)
    checkerror()


def copyFont(pdf, pdf2, r, pagenumber, fontname):
    """Copy the given font from the given page in the pdf PDF to every page in
    the pdf2 PDF. The new font is stored under its font name."""
    r = range_of_list(r)
    libc.pycpdf_copyFont(pdf.pdf, pdf2.pdf, r,
                         pagenumber, str.encode(fontname))
    deleteRange(r)
    checkerror()

# CHAPTER 15. PDF and JSON


def JSONUTF8(utf8):
    """Set the JSON output format. If true, the newer UTF8 format is used.
    Default: False."""
    libc.pycpdf_JSONUTF8(utf8)
    checkerror()


def outputJSON(filename, parse_content, no_stream_data, decompress_streams, pdf):
    """Output a PDF in JSON format to the given filename. If parse_content is
    True, page content is parsed. If decompress_streams is True, streams are
    decompressed. If no_stream_data is True, all stream data is suppressed
    entirely."""
    libc.pycpdf_outputJSON(str.encode(filename),
                           parse_content, no_stream_data, decompress_streams, pdf.pdf)
    checkerror()


def outputJSONMemory(pdf, parse_content, no_stream_data, decompress_streams):
    """outputJSONMemory(pdf, parse_content, no_stream_data, decompress_stream)
    is like outputJSON, but it write to a buffer in memory)."""
    length = c_int32()
    data = libc.pycpdf_outputJSONMemory(
        pdf.pdf, parse_content, no_stream_data, decompress_streams, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_outputJSONMemoryFree()
    checkerror()
    return out_data.raw


def fromJSON(filename):
    """Load a PDF from a JSON file given its filename."""
    pdf = Pdf(libc.pycpdf_fromJSON(str.encode(filename)))
    checkerror()
    return pdf


def fromJSONMemory(data):
    """ Load a PDF from JSON data in memory."""
    pdf = Pdf(libc.pycpdf_fromJSONMemory(data, len(data)))
    checkerror()
    return pdf


# CHAPTER 16. Optional Content Groups


def getOCGList(pdf):
    """Return a list of Optional Content Groups in the given pdf as strings."""
    l = []
    n = libc.pycpdf_startGetOCGList(pdf.pdf)
    for x in range(n):
        l.append(string_at(libc.pycpdf_OCGListEntry(x)).decode())
    libc.pycpdf_endGetOCGList()
    checkerror()
    return l


def OCGRename(pdf, n_from, n_to):
    """Rename an optional content group."""
    libc.pycpdf_OCGRename(pdf.pdf, str.encode(n_from), str.encode(n_to))
    checkerror()


def OCGOrderAll(pdf):
    """Ensure that every optional content group appears in the OCG order list.
    """
    libc.pycpdf_OCGOrderAll(pdf.pdf)
    checkerror()


def OCGCoalesce(pdf):
    """Coalesce optional content groups. For example, if we merge or stamp two
    files both with an OCG called "Layer 1", we will have two different
    optional content groups. This function will merge the two into a single
    optional content group."""
    libc.pycpdf_OCGCoalesce(pdf.pdf)
    checkerror()

# CHAPTER 17. Making New PDFs


def blankDocument(w, h, pages):
    """Create a blank document with pages of the given width (in points),
    height (in points), and number of pages."""
    pdf = Pdf(libc.pycpdf_blankDocument(w, h, pages))
    checkerror()
    return pdf


def blankDocumentPaper(papersize, pages):
    """Create a blank document with pages of the given paper size, and number
    of pages."""
    r = Pdf(libc.pycpdf_blankDocumentPaper(papersize, pages))
    checkerror()
    return r


def textToPDF(w, h, font, fontsize, filename):
    """Typesets a UTF8 text file ragged right on a page of size w * h in points
    in the given font and font size."""
    pdf = Pdf(libc.pycpdf_textToPDF(
        w, h, str.encode(font), fontsize, str.encode(filename)))
    checkerror()
    return pdf


def textToPDFMemory(w, h, font, fontsize, data):
    """Typesets a UTF8 text file ragged right on a page of size w * h in points
    in the given font and font size."""
    pdf = Pdf(libc.pycpdf_textToPDFMemory(
        w, h, str.encode(font), fontsize, data, len(data)))
    checkerror()
    return pdf


def textToPDFPaper(papersize, font, fontsize, filename):
    """Typesets a UTF8 text file ragged right on a page of the given size in
    the given font and font size."""
    pdf = Pdf(libc.pycpdf_textToPDFPaper(
        papersize, str.encode(font), fontsize, str.encode(filename)))
    checkerror()
    return pdf


def textToPDFPaperMemory(papersize, font, fontsize, data):
    """Typesets a UTF8 text file ragged right on a page of the given size in
    the given font and font size."""
    pdf = Pdf(libc.pycpdf_textToPDFPaperMemory(
        papersize, str.encode(font), fontsize, data, len(data)))
    checkerror()
    return pdf


def fromPNG(filename):
    """Builds a PDF from a non-interlaced non-transparent PNG file."""
    pdf = Pdf(libc.pycpdf_fromPNG(str.encode(filename)))
    checkerror()
    return pdf


def fromPNGMemory(data):
    """Builds a PDF from a non-interlaced non-transparent PNG file bytearray."""
    pdf = Pdf(libc.pycpdf_fromPNGMemory(data, len(data)))
    checkerror()
    return pdf


def fromJPEG(filename):
    """Builds a PDF from a JPEG file."""
    pdf = Pdf(libc.pycpdf_fromJPEG(str.encode(filename)))
    checkerror()
    return pdf


def fromJPEGMemory(data):
    """Builds a PDF from a JPEG file bytearray."""
    pdf = Pdf(libc.pycpdf_fromJPEGMemory(data, len(data)))
    checkerror()
    return pdf

# CHAPTER 18. Drawing on PDFs


def drawBegin():
    """Sets up the drawing process. It must be called before any other draw*
    function."""
    libc.pycpdf_drawBegin()
    checkerror()
    return


def drawEnd(pdf, r):
    """Commits the drawing to the given PDF on pages in the given range."""
    libc.pycpdf_drawEnd()
    checkerror()
    return


def drawEndExtended(pdf, r, underneath, bates, filename):
    """The same as drawEnd, but provides the special parameters which may be
    required when using drawSText."""
    rn = range_of_list(r)
    libc.pycpdf_drawEndExtended(
        pdf.pdf, rn, underneath, bates, filename, str.encode(filename))
    deleteRange(rn)
    checkerror()
    return


def drawRect(x, y, w, h):
    """Add a rectangle to the current path."""
    libc.pycpdf_drawRect(x, y, w, h)
    checkerror()
    return


def drawTo(x, y):
    """Move the current point to (x, y)."""
    libc.pycpdf_drawTo(x, y)
    checkerror()
    return


def drawLine(x, y):
    """Adds a line from the current point to (x, y) to the current path."""
    libc.pycpdf_drawLine(x, y)
    checkerror()
    return


def drawBez(x1, y1, x2, y2, x3, y3):
    """Adds a Bezier curve to the current path."""
    libc.pycpdf_drawBez(x1, y1, x2, y2, x3, y3)
    checkerror()
    return


def drawBez23(x2, y2, x3, y3):
    """Adds a Bezier curve twith (x1, y1) = current point."""
    libc.pycpdf_drawBez23(x2, y2, x3, y3)
    checkerror()
    return


def drawBez13(x1, y1, x3, y3):
    """Adds a Bezier curve with (x3, y3) = new current point."""
    libc.pycpdf_drawBez13(x1, y1, x3, y3)
    checkerror()
    return


def drawCircle(x, y, r):
    """Adds a circle to the current path."""
    libc.pycpdf_drawCircle(x, y, r)
    checkerror()
    return


def drawStroke():
    """Stroke the current path and clear it."""
    libc.pycpdf_drawStroke()
    checkerror()
    return


def drawFill():
    """Fills the current path with a non-zero winding rule, and clears it. """
    libc.pycpdf_drawFill()
    checkerror()
    return


def drawFillEo():
    """Fills the current path with an even-odd winding rule, and clears it. """
    libc.pycpdf_drawFillEo()
    checkerror()
    return


def drawStrokeFill():
    """Fills and then strokes the current path with a non-zero winding rule,
    and clears it. """
    libc.pycpdf_drawStrokeFill()
    checkerror()
    return


def drawStrokeFillEo():
    """Fills and then strokes the current path with an even-odd winding rule,
    and clears it. """
    libc.pycpdf_drawStrokeFillEo()
    checkerror()
    return


def drawClose():
    """Closes the current path by appending a straight line segment from the
    current point to the starting point of the subpath. """
    libc.pycpdf_drawClose()
    checkerror()
    return


def drawClip():
    """Uses the current path as a clipping region, using the non-zero winding
    rule. """
    libc.pycpdf_drawClip()
    checkerror()
    return


def drawClipEo():
    """Uses the current path as a clipping region, using the even-odd winding
    rule. """
    libc.pycpdf_drawClipEo()
    checkerror()
    return


def drawStrokeColGrey(g):
    """Changes to a greyscale stroke colourspace and sets the stroke colour.
    """
    libc.pycpdf_drawStrokeColGrey(g)
    checkerror()
    return


def drawStrokeColRGB(r, g, b):
    """Changes to an RGB stroke colourspace and sets the stroke colour. """
    libc.pycpdf_drawStrokeColRGB(r, g, b)
    checkerror()
    return


def drawStrokeColCYMK(c, y, m, k):
    """Changes to a CYMK stroke colourspace and sets the stroke colour. """
    libc.pycpdf_drawStrokeColCYMK(c, y, m, k)
    checkerror()
    return


def drawFillColGrey(g):
    """Changes to a greyscale fill colourspace and sets the fill colour. """
    libc.pycpdf_drawFillColGrey(g)
    checkerror()
    return


def drawFillColRGB(r, g, b):
    """Changes to an RGB fill colourspace and sets the fill colour. """
    libc.pycpdf_drawFillColRGB(r, g, b)
    checkerror()
    return


def drawFillColCYMK(c, y, m, k):
    """Changes to a CYMK fill colourspace and sets the fill colour. """
    libc.pycpdf_drawFillColCYMK(c, y, m, k)
    checkerror()
    return


def drawThick(thickness):
    """Sets the line thickness."""
    libc.pycpdf_drawThick(thickness)
    checkerror()
    return


"""Cap types."""
capButt = 0
capRound = 1
capSquare = 2


def drawCap(captype):
    """Sets the line cap."""
    libc.pycpdf_drawCap(captype)
    checkerror()
    return


"""Join types."""
joinMiter = 0
joinRound = 1
joinBevel = 2


def drawJoin(jointype):
    """Sets the line join type"""
    libc.pycpdf_drawJoin(jointype)
    checkerror()
    return


def drawMiter(miter):
    """Sets the miter limit."""
    libc.pycpdf_drawMiter(miter)
    checkerror()
    return


def drawDash(description):
    """Sets the line dash style"""
    libc.pycpdf_drawDash(str.encode(description))
    checkerror()
    return


def drawPush():
    """Saves the current graphics state on the stack. """
    libc.pycpdf_drawPush()
    checkerror()
    return


def drawPop():
    """Restores the graphics state from the stack. """
    libc.pycpdf_drawPop()
    checkerror()
    return


def drawMatrix(a, b, c, d, e, f):
    """Appends the given matrix to the Current Transformation Matrix. """
    libc.pycpdf_drawMatrix(a, b, c, d, e, f)
    checkerror()
    return


def drawMTrans(tx, ty):
    """Appends a translation by (tx, ty) to the Current Transformation Matrix.
    """
    libc.pycpdf_drawMTrans(tx, ty)
    checkerror()
    return


def drawMRot(x, y, a):
    """Appends a rotation by a around (a, y) to the Current Transformation
    Matrix. """
    libc.pycpdf_drawMRot(x, y, a)
    checkerror()
    return


def drawMScale(x, y, sx, sy):
    """Appends a scaling by (sx, sy) around (x, y) to the Current
    Transformation Matrix. """
    libc.pycpdf_drawMScale(x, y, sx, sy)
    checkerror()
    return


def drawMShearX(x, y, a):
    """Appends an X shearing of angle a around (x, y) to the Current
    Transformation Matrix. """
    libc.pycpdf_drawMShearX(x, y, a)
    checkerror()
    return


def drawMShearY(x, y, a):
    """Appends an X shearing of angle a around (x, y) to the Current
    Transformation Matrix. """
    libc.pycpdf_drawMShearY(x, y, a)
    checkerror()
    return


def drawXObjBBox(x, y, w, h):
    """Sets the XObject bounding box. """
    libc.pycpdf_drawXObjBBox(x, y, w, h)
    checkerror()
    return


def drawXObj(name):
    """Begins the storing of an XObject. """
    libc.pycpdf_drawXObj(str.encode(name))
    checkerror()
    return


def drawEndXObj():
    """Ends the storing of an XObject."""
    libc.pycpdf_drawEndXObj()
    checkerror()
    return


def drawUse(name):
    """Uses the named XObject. """
    libc.pycpdf_drawUse(str.encode(name))
    checkerror()
    return


def drawJPEG(name, filename):
    """Loads a JPEG from the given file, storing it under the given name. """
    libc.pycpdf_drawJPEG(str.encode(name), str.encode(filename))
    checkerror()
    return


def drawJPEGMemory(name, data):
    """Loads a JPEG from the given bytearray, storing it under the given name.
    """
    libc.pycpdf_drawJPEGMemory(str.encode(name), data, len(data))
    checkerror()
    return


def drawPNG(name, filename):
    """Loads a non-interlaced non-transparent PNG from the given file, storing
    it under the given name. """
    libc.pycpdf_drawPNG(str.encode(name), str.encode(filename))
    checkerror()
    return


def drawPNGMemory(name, data):
    """Loads a non-interlaced non-transparent PNG from the given bytearray,
    storing it under the given name. """
    libc.pycpdf_drawPNGMemory(str.encode(name), data, len(data))
    checkerror()
    return


def drawImage(name):
    """Draws a stored image. To draw at the expected size, it is required to
    scale the Current Transformation Matrix by the width and height of the
    image. """
    libc.pycpdf_drawImage(str.encode(name))
    checkerror()
    return


def drawFillOpacity(n):
    """Sets the fill opacity."""
    libc.pycpdf_drawFillOpacity(n)
    checkerror()
    return


def drawStrokeOpacity(n):
    """Sets the stroke opacity."""
    libc.pycpdf_drawStrokeOpacity(n)
    checkerror()
    return


def drawBT():
    """Begins a text section."""
    libc.pycpdf_drawBT()
    checkerror()
    return


def drawET():
    """Ends a text section."""
    libc.pycpdf_drawET()
    checkerror()
    return


def drawFont(name):
    """Sets the font."""
    libc.pycpdf_drawFont(str.encode(name))
    checkerror()
    return


def drawFontSize(n):
    """Sets the font size."""
    libc.pycpdf_drawFontSize(n)
    checkerror()
    return


def drawText(text):
    """Draws text."""
    libc.pycpdf_drawText(str.encode(text))
    checkerror()
    return


def drawSText(text):
    """draws text with %Specials. You may need to use cpdf_drawEndExtended
    instead of cpdf_drawEnd later, to provide the extra information required.
    """
    libc.pycpdf_drawSText(str.encode(text))
    checkerror()
    return


def drawLeading(n):
    """Sets the leading."""
    libc.pycpdf_drawLeading(n)
    checkerror()
    return


def drawCharSpace(n):
    """Sets the character spacing."""
    libc.pycpdf_drawCharSpace(n)
    checkerror()
    return


def drawWordSpace(n):
    """Sets the word spacing."""
    libc.pycpdf_drawWordSpace(n)
    checkerror()
    return


def drawTextScale(n):
    """Sets the text scaling."""
    libc.pycpdf_drawTextScale(n)
    checkerror()
    return


def drawRenderMode(n):
    """Sets the text rendering mode."""
    libc.pycpdf_drawRenderMode(n)
    checkerror()
    return


def drawRise(n):
    """Sets the text rise."""
    libc.pycpdf_drawRise(n)
    checkerror()
    return


def drawNL():
    """Moves to the next line. """
    libc.pycpdf_drawNL()
    checkerror()
    return


def drawNewPage():
    """Moves to the next page, creating it if necessary, and setting the range
    to just that new page. """
    libc.pycpdf_drawNewPage()
    checkerror()
    return

# CHAPTER 19. Miscellaneous


def draft(pdf, r, boxes):
    """Remove images on the given pages, replacing them with crossed boxes if
    'boxes' is True."""
    r = range_of_list(r)
    libc.pycpdf_draft(pdf.pdf, r, boxes)
    deleteRange(r)
    checkerror()


def removeAllText(pdf, r):
    """Remove all text from the given pages in a document."""
    r = range_of_list(r)
    libc.pycpdf_removeAllText(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def blackText(pdf, r):
    """Blacken all text on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackText(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def blackLines(pdf, r):
    """Blacken all lines on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackLines(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def blackFills(pdf, r):
    """Blacken all fills on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackFills(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def thinLines(pdf, r, linewidth):
    """Thicken every line less than linewidth to linewidth. Thickness given in
    points."""
    r = range_of_list(r)
    libc.pycpdf_thinLines(pdf.pdf, r, linewidth)
    deleteRange(r)
    checkerror()


def copyId(pdf, pdf2):
    """Copy the /ID from one pdf to pdf2."""
    libc.pycpdf_copyId(pdf.pdf, pdf2.pdf)
    checkerror()


def removeId(pdf):
    """Remove a document's /ID"""
    libc.pycpdf_removeId(pdf.pdf)
    checkerror()


def setVersion(pdf, version):
    """Set the minor version number of a document."""
    libc.pycpdf_setVersion(pdf.pdf, version)
    checkerror()


def setFullVersion(pdf, major, minor):
    """Set the major and minor version number of a document."""
    libc.pycpdf_setFullVersion(pdf.pdf, major, minor)
    checkerror()


def removeDictEntry(pdf, key):
    """Remove any dictionary entry with the given key anywhere in the
    document."""
    libc.pycpdf_removeDictEntry(pdf.pdf, str.encode(key))
    checkerror()


def removeDictEntrySearch(pdf, key, searchterm):
    """Remove any dictionary entry with the given key anywhere in the document,
    if its value matches the given search term."""
    libc.pycpdf_removeDictEntrySearch(
        pdf.pdf, str.encode(key), str.encode(searchterm))
    checkerror()


def replaceDictEntry(pdf, key, newvalue):
    """Replace any dictionary entry with the given key anywhere in the document
    using the new value given."""
    libc.pycpdf_replaceDictEntry(
        pdf.pdf, str.encode(key), str.encode(newvalue))
    checkerror()


def replaceDictEntrySearch(pdf, key, newvalue, searchterm):
    """Replace any dictionary entry with the given key anywhere in the
    document, if its value matches the given search term, with the new value
    given."""
    libc.pycpdf_replaceDictEntrySearch(
        pdf.pdf, str.encode(key), str.encode(newvalue), str.encode(searchterm))
    checkerror()


def getDictEntries(pdf, key):
    """Return JSON of any dict entries with the given key."""
    length = c_int32()
    data = libc.pycpdf_getDictEntries(pdf.pdf, str.encode(key), byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_getDictEntriesFree()
    checkerror()
    return out_data.raw


def removeClipping(pdf, r):
    """Remove all clipping from pages in the given range"""
    r = range_of_list(r)
    libc.pycpdf_removeClipping(pdf.pdf, r)
    deleteRange(r)
    checkerror()

# CHAPTER X. Undocumented or Internal


def list_of_range(r):
    """Internal."""
    l = []
    for x in range(libc.pycpdf_rangeLength(r)):
        l.append(libc.pycpdf_rangeGet(r, x))
    checkerror()
    return l


def range_of_list(l):
    """Internal."""
    r = libc.pycpdf_blankRange()
    for x in l:
        rn = libc.pycpdf_rangeAdd(r, x)
        deleteRange(r)
        r = rn
    checkerror()
    return r


def deleteRange(r):
    """Internal."""
    r = libc.pycpdf_deleteRange(r)
    checkerror()
    return r
