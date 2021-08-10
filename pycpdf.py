"""Pycpdf: a python interface to cpdf.

Before using the library, you must load the libpycpdf and libcpdf DLLs. This is
achieved with the pycpdf.loadDLL function, given the filename or full path of
the libpycpdf DLL.  On Windows, you may have to call os.add_dll_directory
first. On MacOS, you may need to give the full path, and you may need to
install libcpdf.so in a standard location /usr/local/lib/, or use the
install_name_tool command to tell libpycpdf.so where to find libcpdf.so.

FIXME: EXCEPTIONS



A 'range' is a list of integers specifying page numbers.

Text arguments and results are in UTF8.
"""

from ctypes import *
import sys

libc = None


class Pdf:
    """The type of PDF documents."""
    pdf = -1

    def __init__(self, pdfnum):
        self.pdf = pdfnum

    def __del__(self):
        libc.pycpdf_deletePdf(self.pdf)


def loadDLL(f):
    """Load the libpycpdf DLL from a given file, and set up pycpdflib."""
    global libc
    libc = CDLL(f)
    libc.pycpdf_version.restype = POINTER(c_char)
    libc.pycpdf_lastErrorString.restype = POINTER(c_char)
    libc.pycpdf_blankDocument.argtypes = [c_double, c_double, c_int]
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
    libc.pycpdf_scalePages.argtypes = [c_int, c_int, c_double, c_double]
    libc.pycpdf_scaleToFit.argtypes =\
        [c_int, c_int, c_double, c_double, c_double]
    libc.pycpdf_scaleToFitPaper.argtypes = [c_int, c_int, c_int, c_double]
    libc.pycpdf_scaleContents.argtypes =\
        [c_int, c_int, c_int, c_double, c_double, c_double]
    libc.pycpdf_shiftContents.argtypes = [c_int, c_int, c_double, c_double]
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
         c_double, c_int, c_int, c_double, c_double, c_double, c_double, c_int,
         c_int, c_int, c_double, c_int, c_int, c_int, POINTER(c_char),
         c_double, c_int]
    libc.pycpdf_addTextSimple.argtypes =\
        [c_int, c_int, POINTER(c_char), c_int, c_double,
         c_double, c_int, c_double]
    libc.pycpdf_getMetadata.restype = POINTER(c_uint8)
    libc.pycpdf_getAttachmentData.restype = POINTER(c_uint8)
    libc.pycpdf_getAttachmentName.restype = POINTER(c_uint8)
    libc.pycpdf_startGetImageResolution.argtypes = [c_int, c_double]
    libc.pycpdf_getImageResolutionImageName.restype = POINTER(c_char)
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
    describing what went wrong"""

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

# CHAPTER 0. Preliminaries


def version():
    """Returns the version number of the pycpdflib library."""
    v = string_at(libc.pycpdf_version()).decode()
    checkerror()
    return v


def setFast():
    """ Some operations have a fast mode. The default is 'slow' mode, which
    works even on old-fashioned files. For more details, see section 1.13 of
    the CPDF manual. These functions set the mode globally. """
    libc.pycpdf_setFast()
    checkerror()


def setSlow():
    """ Some operations have a fast mode. The default is 'slow' mode, which
    works even on old-fashioned files. For more details, see section 1.13 of
    the CPDF manual. These functions set the mode globally. """
    libc.pycpdf_setSlow()
    checkerror()


def clearError():
    """ clearError clears the current error state. """
    libc.pycpdf_clearError()
    checkerror()


def onExit():
    """ onExit is a debug function which prints some information about
    resource usage. This can be used to detect if PDFs or ranges are being
    deallocated properly."""
    libc.pycpdf_onExit()
    checkerror()

# CHAPTER 1. Basics


def fromFile(filename, userpw):
    """ fromFile(filename, userpw) loads a PDF file from a given file.
    Supply a user password (possibly blank) in case the file is encypted. It
    won't be decrypted, but sometimes the password is needed just to load the
    file."""
    pdf = Pdf(libc.pycpdf_fromFile(str.encode(filename), str.encode(userpw)))
    checkerror()
    return pdf


def fromFileLazy(filename, userpw):
    """ fromFileLazy(pdf, userpw) loads a PDF from a file, doing only
    minimal parsing. The objects will be read and parsed when they are actually
    needed.  Use this when the whole file won't be required. Also supply a user
    password (possibly blank) in case the file is encypted. It won't be
    decrypted, but sometimes the password is needed just to load the file."""
    pdf = Pdf(libc.pycpdf_fromFileLazy(
        str.encode(filename), str.encode(userpw)))
    checkerror()
    return pdf


def fromMemory(data, userpw):
    """ fromMemory(data, length, userpw) loads a file from memory, given a
    pointer and a length, and the user password."""
    pdf = Pdf(libc.pycpdf_fromMemory(data, len(data), str.encode(userpw)))
    checkerror()
    return pdf


def fromMemoryLazy(data, userpw):
    """ fromMemoryLazy(data, length, userpw) loads a file from memory, given a
    pointer and a length, and the user password, but lazily like
    fromFileLazy."""
    pdf = Pdf(libc.pycpdf_fromMemoryLazy(data, len(data), str.encode(userpw)))
    checkerror()
    return pdf


def blankDocument(w, h, pages):
    """ blankDocument(width, height, num_pages) creates a blank document
    with pages of the given width (in points), height (in points), and number
    of pages."""
    pdf = Pdf(libc.pycpdf_blankDocument(w, h, pages))
    checkerror()
    return pdf


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


def blankDocumentPaper(papersize, pages):
    """blankDocument(width, height, num_pages) creates a blank document
    with pages of the given width (in points), height (in points), and number
    of pages. """
    r = Pdf(libc.pycpdf_blankDocumentPaper(papersize, pages))
    checkerror()
    return r


def ptOfCm(i):
    """Convert a figure in centimetres to points (72 points to 1 inch)"""
    r = libc.pycpdf_ptOfCm(i)
    checkerror()
    return r


def ptOfMm(i):
    """Convert a figure in millimetres to points (72 points to 1 inch)"""
    r = libc.pycpdf_ptOfMm(i)
    checkerror()
    return r


def ptOfIn(i):
    """Convert a figure in inches to points (72 points to 1 inch)"""
    r = libc.pycpdf_ptOfIn(i)
    checkerror()
    return r


def cmOfPt(i):
    """Convert a figure in points to centimetres (72 points to 1 inch)"""
    r = libc.pycpdf_cmOfPt(i)
    checkerror()
    return r


def mmOfPt(i):
    """Convert a figure in points to millimetres (72 points to 1 inch)"""
    r = libc.pycpdf_mmOfPt(i)
    checkerror()
    return r


def inOfPt(i):
    """Convert a figure in points to inches (72 points to 1 inch)"""
    r = libc.pycpdf_inOfPt(i)
    checkerror()
    return r


def parsePagespec(pdf, pagespec):
    """parsePagespec(pdf, pagespec) parses a page specification with reference to
    a given PDF (the PDF is supplied so that page ranges which reference pages
    which do not exist are rejected)."""

    rn = libc.pycpdf_parsePagespec(pdf.pdf, str.encode(pagespec))
    r = list_of_range(rn)
    deleteRange(rn)
    checkerror()
    return r


def validatePagespec(pagespec):
    """validatePagespec(range) validates a page specification so far as is
    possible in the absence of the actual document."""
    r = libc.pycpdf_validatePagespec(str.encode(pagespec))
    checkerror()
    return r


def stringOfPagespec(pdf, r):
    """stringOfPagespec(pdf, range) builds a page specification from a page
    range. For example, the range containing 1,2,3,6,7,8 in a document of 8
    pages might yield "1-3,6-end" """
    rn = range_of_list(r)
    r = string_at(libc.pycpdf_stringOfPagespec(pdf.pdf, rn)).decode()
    deleteRange(rn)
    checkerror()
    return r


def blankRange():
    """blankRange() creates a range with no pages in."""
    r = libc.pycpdf_blankRange()
    checkerror()
    l = list_of_range(r)
    deleteRange(r)
    return l


def pageRange(f, t):
    """ pageRange(from, to) build a range from one page to another inclusive.
    For example, pageRange(3,7) gives the range 3,4,5,6,7 """
    rn = libc.pycpdf_pageRange(f, t)
    r = list_of_range(rn)
    deleteRange(rn)
    checkerror()
    return r


def all(pdf):
    """all(pdf) is the range containing all the pages in a given document."""
    rn = libc.pycpdf_all(pdf.pdf)
    r = list_of_range(rn)
    deleteRange(rn)
    checkerror()
    return r


def even(r):
    """even(range) makes a range which contains just the even pages of another
    range"""
    rn = range_of_list(r)
    reven = libc.pycpdf_even(rn)
    rout = list_of_range(reven)
    deleteRange(rn)
    deleteRange(reven)
    checkerror()
    return rout


def odd(r):
    """odd(range) makes a range which contains just the odd pages of another
    range"""
    rn = range_of_list(r)
    rodd = libc.pycpdf_odd(rn)
    rout = list_of_range(rodd)
    deleteRange(rn)
    deleteRange(rodd)
    checkerror()
    return rout


def rangeUnion(a, b):
    """rangeUnion(a, b) makes the union of two ranges giving a range containing
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
    """difference(a, b) makes the difference of two ranges, giving a range
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
    """removeDuplicates(range) deduplicates a range, making a new one."""
    rn = range_of_list(r)
    rdup = libc.pycpdf_removeDuplicates(rn)
    rout = list_of_range(rdup)
    deleteRange(rn)
    deleteRange(rdup)
    checkerror()
    return rout


def rangeLength(r):
    """rangeLength gives the number of pages in a range."""
    rn = range_of_list(r)
    l = libc.pycpdf_rangeLength(rn)
    deleteRange(rn)
    checkerror()
    return l


def rangeGet(r, n):
    """rangeGet(range, n) gets the page number at position n in a range, where
    n runs from 0 to rangeLength - 1."""
    rn = range_of_list(r)
    r2 = libc.pycpdf_rangeGet(rn, n)
    deleteRange(rn)
    checkerror()
    return r2


def rangeAdd(r, p):
    """rangeAdd(range, page) adds the page to a range, if it is not already
    there."""
    rn = range_of_list(r)
    radd = libc.pycpdf_rangeAdd(rn, p)
    rout = list_of_range(radd)
    deleteRange(rn)
    deleteRange(radd)
    checkerror()
    return rout


def isInRange(r, p):
    """isInRange(range, page) returns True if the page is in the range, False
    otherwise."""
    rn = range_of_list(r)
    r2 = libc.pycpdf_isInRange(rn, p)
    deleteRange(rn)
    checkerror()
    return r2


def pages(pdf):
    """pages(pdf) returns the number of pages in a PDF."""
    r = libc.pycpdf_pages(pdf.pdf)
    checkerror()
    return r


def pagesFast(userpw, filename):
    """pagesFast(password, filename) returns the number of pages in a given
    PDF, with given user encryption password. It tries to do this as fast as
    possible, without loading the whole file."""
    r = libc.pycpdf_pagesFast(str.encode(userpw), str.encode(filename))
    checkerror()
    return r


def toFile(pdf, filename, linearize, make_id):
    """toFile (pdf, filename, linearize, make_id) writes the file to a given
    filename. If linearize is True, it will be linearized. If make_id is True,
    it will be given a new ID."""
    libc.pycpdf_toFile(pdf.pdf, str.encode(filename), False, False)
    checkerror()


def toFileExt(pdf, filename, linearize, make_id, preserve_objstm,
              generate_objstm, compress_objstm):
    """toFileExt (pdf, filename, linearize, make_id, preserve_objstm,
    generate_objstm, compress_objstm) writes the file to a given filename. If
    make_id is True, it will be given a new ID.  If preserve_objstm is True,
    existing object streams will be preserved. If generate_objstm is True,
    object streams will be generated even if not originally present. If
    compress_objstm is True, object streams will be compressed (what we usually
    want). WARNING: the pdf argument will be invalid after this call and should
    not be used again."""
    libc.pycpdf_toFileExt(pdf.pdf, str.encode(filename), linearize, make_id,
                          preserve_objstm, generate_objstm, compress_objstm)
    checkerror()


def toMemory(pdf, linearize, make_id):
    """Given a buffer of the correct size, toMemory (pdf, linearize,
    make_id) writes it and returns the buffer as a byte array of type bytes."""
    length = c_int32()
    data = libc.pycpdf_toMemory(pdf.pdf, linearize, make_id, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_toMemoryFree()
    checkerror()
    return out_data.raw


def isEncrypted(pdf):
    """isEncrypted(pdf) returns True if a documented is encrypted, False
    otherwise."""
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
    """toFileEncrypted(pdf, encryption_method, permissions, permission_length,
    owner_password, user password, linearize, makeid, filename) writes a file
    as encrypted."""
    c_perms = (c_uint8 * len(permissions))(*permissions)
    libc.pycpdf_toFileEncrypted(pdf.pdf, method, c_perms, len(permissions),
                                str.encode(ownerpw), str.encode(userpw),
                                linearize, makeid, str.encode(filename))
    checkerror()


def toFileEncryptedExt(pdf, method, permissions, ownerpw, userpw, linearize,
                       makeid, preserve_objstm, generate_objstm,
                       compress_objstm, filename):
    """toFileEncryptedExt(pdf, encryption_method, permissions,
    permission_length, owner_password, user_password, linearize, makeid,
    preserve_objstm, generate_objstm, compress_objstm, filename) WARNING: the
    pdf argument will be invalid after this call, and should be discarded."""
    c_perms = (c_uint8 * len(permissions))(*permissions)
    libc.pycpdf_toFileEncryptedExt(pdf.pdf, method, c_perms, len(permissions),
                                   str.encode(ownerpw), str.encode(userpw),
                                   linearize, makeid, preserve_objstm,
                                   generate_objstm, compress_objstm,
                                   str.encode(filename))
    checkerror()


def decryptPdf(pdf, userpw):
    """decryptPdf(pdf, userpw) attempts to decrypt a PDF using the given user
    password."""
    libc.pycpdf_decryptPdf(pdf.pdf, str.encode(userpw))
    checkerror()


def decryptPdfOwner(pdf, ownerpw):
    """decryptPdfOwner(pdf, ownerpw) attempts to decrypt a PDF using the given
    owner password."""
    libc.pycpdf_decryptPdfOwner(pdf.pdf, str.encode(ownerpw))
    checkerror()


def hasPermission(pdf, perm):
    """hasPermission(pdf, permission) returns True if the given permission
    (restriction) is present."""
    r = libc.pycpdf_hasPermission(pdf.pdf, perm)
    checkerror()
    return r


def encryptionKind(pdf):
    """encryptionMethod(pdf) return the encryption method currently in use on
    a document."""
    r = libc.pycpdf_encryptionKind(pdf.pdf)
    checkerror()
    return r

# CHAPTER 2. Merging and Splitting


def mergeSimple(pdfs):
    """mergeSimple(pdfs), given a list of PDFs,
    merges the files into a new one, which is returned."""
    raw_pdfs = list(map(lambda p: p.pdf, pdfs))
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    r = Pdf(libc.pycpdf_mergeSimple(c_pdfs, len(pdfs)))
    checkerror()
    return r


def merge(pdfs, retain_numbering, remove_duplicate_fonts):
    """merge(pdfs, retain_numbering, remove_duplicate_fonts) merges
    the list of PDFs. If retain_numbering is True page labels are not
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
    """mergeSame(pdfs, retain_numbering, remove_duplicate_fonts, ranges)
    is the same as merge, except that it has an additional argument
    - an array of page ranges. This is used to select the pages to pick from
    each PDF. This avoids duplication of information when multiple discrete
    parts of a source PDF are included."""
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
    """ selectPages(pdf, range) returns a new document which just those pages
    in the page range."""
    rn = range_of_list(r)
    r = Pdf(libc.pycpdf_selectPages(pdf.pdf, rn))
    deleteRange(rn)
    checkerror()
    return r

# CHAPTER 3. Pages


def scalePages(pdf, r, sx, sy):
    """scalePages(pdf, range, x scale, y scale) scales the page dimensions
    and content by the given scale, about (0, 0). Other boxes (crop etc. are
    altered as appropriate)"""
    r = range_of_list(r)
    libc.pycpdf_scalePages(pdf.pdf, r, sx, sy)
    deleteRange(r)
    checkerror()


def scaleToFit(pdf, r, sx, sy, scale_to_fit_scale):
    """scaleToFit(pdf, range, width height, scale) scales the content to fit
    new page dimensions (width x height) multiplied by scale (typically 1.0).
    Other boxed (crop etc. are altered as appropriate)"""
    r = range_of_list(r)
    libc.pycpdf_scaleToFit(pdf.pdf, r, sx, sy, scale_to_fit_scale)
    deleteRange(r)
    checkerror()


def scaleToFitPaper(pdf, r, papersize, scale_to_fit_scale):
    """scaleToFitPaper(pdf, range, papersize, scale) scales the page content
    to fit the given page size, possibly multiplied by scale (typically 1.0)"""
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
    """scaleContents(pdf, range, position, scale) scales the contents of the
    pages in the range about the point given by the position, by the
    scale given."""
    r = range_of_list(r)
    a, b, c = tripleOfPosition(pos)
    libc.pycpdf_scaleContents(pdf.pdf, r, a, b, c, scale)
    deleteRange(r)
    checkerror()


def shiftContents(pdf, r, dx, dy):
    """shiftContents(pdf, range, dx, dy) shifts the content of the pages in
    the range."""
    r = range_of_list(r)
    libc.pycpdf_shiftContents(pdf.pdf, r, dx, dy)
    deleteRange(r)
    checkerror()


def rotate(pdf, r, rotation):
    """rotate(pdf, range, rotation) changes the viewing rotation to an
    absolute value. Appropriate rotations are 0, 90, 180, 270."""
    r = range_of_list(r)
    libc.pycpdf_rotate(pdf.pdf, r, rotation)
    deleteRange(r)
    checkerror()


def rotateBy(pdf, r, rotation):
    """rotateBy(pdf, range, rotation) changes the viewing rotation by a
    given number of degrees. Appropriate values are 90, 180, 270."""
    r = range_of_list(r)
    libc.pycpdf_rotateBy(pdf.pdf, r, rotation)
    deleteRange(r)
    checkerror()


def rotateContents(pdf, r, rotation):
    """rotateContents(pdf, range, angle) rotates the content about the centre
    of the page by the given number of degrees, in a clockwise direction."""
    r = range_of_list(r)
    libc.pycpdf_rotateContents(pdf.pdf, r, rotation)
    deleteRange(r)
    checkerror()


def upright(pdf, r):
    """upright(pdf, range) changes the viewing rotation of the pages in the
    range, counter-rotating the dimensions and content such that there is no
    visual change."""
    r = range_of_list(r)
    libc.pycpdf_upright(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def hFlip(pdf, r):
    """hFlip(pdf, range) flips horizontally the pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_hFlip(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def vFlip(pdf, r):
    """vFlip(pdf, range) flips vertically the pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_vFlip(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def crop(pdf, r, x, y, w, h):
    """crop(pdf, range, x, y, w, h) crops a page, replacing any existing
    crop box. The dimensions are in points."""
    r = range_of_list(r)
    libc.pycpdf_crop(pdf.pdf, r, x, y, w, h)
    deleteRange(r)
    checkerror()


def removeCrop(pdf, r):
    """removeCrop(pdf, range) removes any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeCrop(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def removeTrim(pdf, r):
    """removeTrim(pdf, range) removes any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeTrim(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def removeArt(pdf, r):
    """removeArt(pdf, range) removes any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeArt(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def removeBleed(pdf, r):
    """removeBleed(pdf, range) removes any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeBleed(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def trimMarks(pdf, r):
    """trimMarks(pdf, range) adds trim marks to the given pages, if the trimbox
    exists."""
    r = range_of_list(r)
    libc.pycpdf_trimMarks(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def showBoxes(pdf, r):
    """showBoxes(pdf, range) shows the boxes on the given pages, for debug."""
    r = range_of_list(r)
    libc.pycpdf_showBoxes(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def hardBox(pdf, r, boxname):
    """hardBox make a given box a 'hard box' i.e clips it explicitly."""
    r = range_of_list(r)
    libc.pycpdf_hardBox(pdf.pdf, r, str.encode(boxname))
    deleteRange(r)
    checkerror()

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression


def compress(pdf):
    """compress(pdf) compresses any uncompressed streams in the given PDF
    using the Flate algorithm."""
    libc.pycpdf_compress(pdf.pdf)
    checkerror()


def decompress(pdf):
    """uncompress(pdf) uncompresses any streams in the given PDF, so long as
    the compression method is supported."""
    libc.pycpdf_decompress(pdf.pdf)
    checkerror()


def squeezeInMemory(pdf):
    """squeezeToMemory(pdf) squeezes a pdf in memory."""
    libc.pycpdf_squeezeInMemory(pdf.pdf)
    checkerror()

# CHAPTER 6. Bookmarks


def getBookmarks(pdf):
    """Get the bookmarks for a PDF as a list of tuples.
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
    """Set the bookmarks for a PDF as a list of tuples.
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

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps


def stampOn(pdf, pdf2, r):
    """stampOn(stamp_pdf, pdf, range) stamps stamp_pdf on top of all the
    pages in the document which are in the range. The stamp is placed with its
    origin at the origin of the target document."""
    r = range_of_list(r)
    libc.pycpdf_stampOn(pdf.pdf, pdf2.pdf, r)
    deleteRange(r)
    checkerror()


def stampUnder(pdf, pdf2, r):
    """stampUnder(stamp_pdf, pdf, range) stamps stamp_pdf under all the pages
    in the document which are in the range. The stamp is placed with its origin
    at the origin of the target document."""
    r = range_of_list(r)
    libc.pycpdf_stampUnder(pdf.pdf, pdf2.pdf, r)
    deleteRange(r)
    checkerror()


def stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, pos,
                  relative_to_cropbox):
    """stampExtended(pdf, pdf2, range, isover, scale_stamp_to_fit, pos,
    relative_to_cropbox) is a stamping function with extra features.
     - isover True, pdf goes over pdf2, isover False, pdf goes under pdf2
     - scale_stamp_to_fit scales the stamp to fit the page
     - pos gives the position to put the stamp
     - relative_to_cropbox: if True, pos is relative to cropbox not mediabox"""
    r = range_of_list(r)
    a, b, c = tripleOfPosition(pos)
    libc.pycpdf_stampExtended(pdf.pdf, pdf2.pdf, r, isover, scale_stamp_to_fit,
                              a, b, c, relative_to_cropbox)
    deleteRange(r)
    checkerror()


def combinePages(pdf, pdf2):
    """combinePages(under, over) combines the PDFs page-by-page, putting
    each page of 'over' over each page of 'under'"""
    output = libc.pycpdf_combinePages(pdf.pdf, pdf2.pdf)
    checkerror()
    return Pdf(output)

"""Fonts."""
timesRoman = 0
timesBold = 1
timesItalic = 2
timesBoldItalic = 3
helvetica = 4
helveticaBold = 5
helveticaOblique = 6
helveticaBoldOblique = 7
courier = 8
courierBold = 9
courierOblique = 10
courierBoldOblique = 11


"""Jusitifications."""
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
                        line_spacing, bates, font, size, red, green, blue,
                        underneath, relative_to_cropbox, outline, opacity,
                        justification, midline, topline, str.encode(filename),
                        line_width, embed_fonts)
    deleteRange(r)
    checkerror()


def addTextSimple(pdf, r, text, p, font, size):
    """like addText, but with most parameters default
         * pdf = the document
         * r = the range
         * p = the position
         * font = the font
         * size = the font size"""
    a, b, c = tripleOfPosition(p)
    r = range_of_list(r)
    libc.pycpdf_addTextSimple(
        pdf.pdf, r, str.encode(text), a, b, c, font, size)
    deleteRange(r)
    checkerror()


def removeText(pdf, r):
    """removeText(pdf, range) will remove any text added by libcpdf from the
    given pages."""
    r = range_of_list(r)
    libc.pycpdf_removeText(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def textWidth(font, string):
    """Return the width of a given string in the given font in thousandths of a
    point."""
    r = libc.pycpdf_textWidth(font, str.encode(string))
    checkerror()
    return r


def addContent(content, before, pdf, r):
    """addContent(content, before, range, pdf) adds page content before (if
    True) or after (if False) the existing content to pages in the given range
    in the given PDF."""
    r = range_of_list(r)
    libc.pycpdf_addContent(str.encode(content), before, pdf.pdf, r)
    deleteRange(r)
    checkerror()


def stampAsXObject(pdf, r, stamp_pdf):
    """stampAsXObject(pdf, range, stamp_pdf) stamps stamp_pdf onto the pages
    in the given range in pdf as a shared Form XObject. The name of the
    newly-created XObject is returned."""
    r = range_of_list(r)
    r2 = string_at(libc.pycpdf_stampAsXObject(
        pdf.pdf, r, stamp_pdf.pdf)).decode()
    deleteRange(r)
    checkerror()
    return r2


# CHAPTER 9. Mulitpage facilities
def twoUp(pdf):
    """Impose a document two up. twoUp does so by retaining the existing page
    size, scaling pages down. twoUpStack does so by doubling the page size,
    to fit two pages on one."""
    libc.pycpdf_twoUp(pdf.pdf)
    checkerror()


def twoUpStack(pdf):
    """Impose a document two up. twoUp does so by retaining the existing page
    size, scaling pages down. twoUpStack does so by doubling the page size,
    to fit two pages on one."""
    libc.pycpdf_twoUpStack(pdf.pdf)
    checkerror()


def padBefore(pdf, r):
    """padBefore(pdf, range) adds a blank page before each page in the given
    range"""
    r = range_of_list(r)
    libc.pycpdf_padBefore(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def padAfter(pdf, r):
    """padAfter(pdf, range) adds a blank page after each page in the given
    range"""
    r = range_of_list(r)
    libc.pycpdf_padAfter(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def padEvery(pdf, n):
    """pageEvery(pdf, n) adds a blank page after every n pages"""
    libc.pycpdf_padEvery(pdf.pdf, n)
    checkerror()


def padMultiple(pdf, n):
    """padMultiple(pdf, n) adds pages at the end to pad the file to a multiple
    of n pages in length."""
    libc.pycpdf_padMultiple(pdf.pdf, n)
    checkerror()


def padMultipleBefore(pdf, n):
    """padMultiple(pdf, n) adds pages at the beginning to pad the file to a
    multiple of n pages in length."""
    libc.pycpdf_padMultipleBefore(pdf.pdf, n)
    checkerror()

# CHAPTER 10. Annotations

# Not in the library version.

# CHAPTER 11. Document Information and Metadata


def isLinearized(filename):
    """isLinearized(filename) finds out if a document is linearized as quickly
    as possible without loading it."""
    r = libc.pycpdf_isLinearized(str.encode(filename))
    checkerror()
    return r


def getVersion(pdf):
    """vetVersion(pdf) returns the minor version number of a document."""
    r = libc.pycpdf_getVersion(pdf.pdf)
    checkerror()
    return r


def getMajorVersion(pdf):
    """getMajorVersion(pdf) returns the minor version number of a document."""
    r = libc.pycpdf_getMajorVersion(pdf.pdf)
    checkerror()
    return r


def getTitle(pdf):
    """getTitle(pdf) returns the title of a document."""
    r = string_at(libc.pycpdf_getTitle(pdf.pdf)).decode()
    checkerror()
    return r


def getAuthor(pdf):
    """getSubject(pdf) returns the subject of a document."""
    r = string_at(libc.pycpdf_getAuthor(pdf.pdf)).decode()
    checkerror()
    return r


def getSubject(pdf):
    """getSubject(pdf) returns the subject of a document."""
    r = string_at(libc.pycpdf_getSubject(pdf.pdf)).decode()
    checkerror()
    return r


def getKeywords(pdf):
    """getKeywords(pdf) returns the keywords of a document."""
    r = string_at(libc.pycpdf_getKeywords(pdf.pdf)).decode()
    checkerror()
    return r


def getCreator(pdf):
    """getCreator(pdf) returns the creator of a document."""
    r = string_at(libc.pycpdf_getCreator(pdf.pdf)).decode()
    checkerror()
    return r


def getProducer(pdf):
    """getProducer(pdf) returns the producer of a document."""
    r = string_at(libc.pycpdf_getProducer(pdf.pdf)).decode()
    checkerror()
    return r


def getCreationDate(pdf):
    """getCreationDate(pdf) returns the creation date of a document."""
    r = string_at(libc.pycpdf_getCreationDate(pdf.pdf)).decode()
    checkerror()
    return r


def getModificationDate(pdf):
    """getModificationDate(pdf) returns the modification date of a document."""
    r = string_at(libc.pycpdf_getModificationDate(pdf.pdf)).decode()
    checkerror()
    return r


def getTitleXMP(pdf):
    """getTitleXMP(pdf) returns the XMP title of a document."""
    r = string_at(libc.pycpdf_getTitleXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getAuthorXMP(pdf):
    """getAuthorXMP(pdf) returns the XMP author of a document."""
    r = string_at(libc.pycpdf_getAuthorXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getSubjectXMP(pdf):
    """getSubjectXMP(pdf) returns the XMP subject of a document."""
    r = string_at(libc.pycpdf_getSubjectXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getKeywordsXMP(pdf):
    """getKeywordsXMP(pdf) returns the XMP keywords of a document."""
    r = string_at(libc.pycpdf_getKeywordsXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getCreatorXMP(pdf):
    """getCreatorXMP(pdf) returns the XMP creator of a document."""
    r = string_at(libc.pycpdf_getCreatorXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getProducerXMP(pdf):
    """getProducerXMP(pdf) returns the XMP producer of a document."""
    r = string_at(libc.pycpdf_getProducerXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getCreationDateXMP(pdf):
    """getCreationDateXMP(pdf) returns the XMP creation date of a document."""
    r = string_at(libc.pycpdf_getCreationDateXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getModificationDateXMP(pdf):
    """getModificationDateXMP(pdf) returns the XMP modification date of a
    document."""
    r = string_at(libc.pycpdf_getModificationDateXMP(pdf.pdf)).decode()
    checkerror()
    return r


def setTitle(pdf, s):
    """setTitle(pdf) sets the title of a document."""
    libc.pycpdf_setTitle(pdf.pdf, str.encode(s))
    checkerror()
    return


def setAuthor(pdf, s):
    """setAuthor(pdf) sets the author of a document."""
    libc.pycpdf_setAuthor(pdf.pdf, str.encode(s))
    checkerror()
    return


def setSubject(pdf, s):
    """setSubject(pdf) sets the subject of a document."""
    libc.pycpdf_setSubject(pdf.pdf, str.encode(s))
    checkerror()
    return


def setKeywords(pdf, s):
    """setKeywords(pdf) sets the keywords of a document."""
    libc.pycpdf_setKeywords(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreator(pdf, s):
    """setCreator(pdf) sets the creator of a document."""
    libc.pycpdf_setCreator(pdf.pdf, str.encode(s))
    checkerror()
    return


def setProducer(pdf, s):
    """setProducer(pdf) sets the producer of a document."""
    libc.pycpdf_setProducer(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreationDate(pdf, s):
    """setCreationDate(pdf) sets the creation date of a document."""
    libc.pycpdf_setCreationDate(pdf.pdf, str.encode(s))
    checkerror()
    return


def setModificationDate(pdf, s):
    """setModificationDate(pdf) sets the modifcation date of a document."""
    libc.pycpdf_setModificationDate(pdf.pdf, str.encode(s))
    checkerror()
    return


def setTitleXMP(pdf, s):
    """setTitleXMP(pdf) set the XMP title of a document."""
    libc.pycpdf_setTitleXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setAuthorXMP(pdf, s):
    """setAuthorXMP(pdf) set the XMP author of a document."""
    libc.pycpdf_setAuthorXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setSubjectXMP(pdf, s):
    """setSubjectXMP(pdf) set the XMP subject of a document."""
    libc.pycpdf_setSubjectXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setKeywordsXMP(pdf, s):
    """setKeywordsXMP(pdf) set the XMP keywords of a document."""
    libc.pycpdf_setKeywordsXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreatorXMP(pdf, s):
    """setCreatorXMP(pdf) set the XMP creator of a document."""
    libc.pycpdf_setCreatorXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setProducerXMP(pdf, s):
    """setProducerXMP(pdf) set the XMP producer of a document."""
    libc.pycpdf_setProducerXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreationDateXMP(pdf, s):
    """setCreationDateXMP(pdf) set the XMP creation date of a document."""
    libc.pycpdf_setCreationDateXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setModificationDateXMP(pdf, s):
    """setModificationDateXMP(pdf) set the XMP modification date of a
    document."""
    libc.pycpdf_setModificationDateXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def getDateComponents(string):
    """Dates: Month 1-31, day 1-31, hours (0-23), minutes (0-59), seconds
    (0-59), hour_offset is the offset from UT in hours (-23 to 23);
    minute_offset is the offset from UT in minutes (-59 to 59).

    getDateComponents(datestring, year, month, day, hour, minute, second,
    hour_offset, minute_offset) returns the components from a PDF date
    string."""
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
    """Dates: Month 1-31, day 1-31, hours (0-23), minutes (0-59), seconds
    (0-59), hour_offset is the offset from UT in hours (-23 to 23);
    minute_offset is the offset from UT in minutes (-59 to 59).

    dateStringOfComponents(year, month, day, hour, minute, second,
    hour_offset, minute_offset) builds a PDF date string from individual
    components."""
    year, month, day, hour, minute, second, hour_offset, minute_offset = cs
    r = string_at(libc.pycpdf_dateStringOfComponents(year, month, day, hour,
                                                     minute, second,
                                                     hour_offset,
                                                     minute_offset)).decode()
    checkerror()
    return r


def getPageRotation(pdf, pagenumber):
    """getPageRotation(pdf, pagenumber) gets the viewing rotation for a given
    page."""
    r = libc.pycpdf_getPageRotation(pdf.pdf, pagenumber)
    checkerror()
    return r


def hasBox(pdf, pagenumber, boxname):
    """hasBox(pdf, pagenumber, boxname) returns True, if that page has the
    given box. E.g "/CropBox" """
    r = libc.pycpdf_hasBox(pdf.pdf, pagenumber, str.encode(boxname))
    checkerror()
    return r


def getMediaBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x,
    min y, max y in points. Only suceeds if such a box exists, as checked by
    hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getMediaBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getCropBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x,
    min y, max y in points. Only suceeds if such a box exists, as checked by
    hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getCropBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getTrimBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x,
    min y, max y in points. Only suceeds if such a box exists, as checked by
    hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getTrimBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getArtBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x,
    min y, max y in points. Only suceeds if such a box exists, as checked by
    hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getArtBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getBleedBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x,
    min y, max y in points. Only suceeds if such a box exists, as checked by
    hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getBleedBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def setMediaBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x,
    min y, max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setMediaBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def setCropBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x,
    min y, max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setCropBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def setTrimBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x,
    min y, max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setTrimBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def setArtBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x,
    min y, max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setArtBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def setBleedBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x,
    min y, max y in points."""
    rn = range_of_list(r)
    libc.pycpdf_setBleedBox(pdf.pdf, rn, minx, maxx, miny, maxy)
    deleteRange(rn)
    checkerror()
    return


def markTrapped(pdf):
    """markTrapped(pdf) marks a document as trapped."""
    libc.pycpdf_markTrapped(pdf.pdf)
    checkerror()
    return


def markUntrapped(pdf):
    """markUntrapped(pdf) marks a document as untrapped."""
    libc.pycpdf_markUntrapped(pdf.pdf)
    checkerror()
    return


def markTrappedXMP(pdf):
    """markTrappedXMP(pdf) marks a document as trapped in XMP metadata."""
    libc.pycpdf_markTrappedXMP(pdf.pdf)
    checkerror()
    return


def markUntrappedXMP(pdf):
    """markUntrappedXMP(pdf) marks a document as untrapped in XMP metadata."""
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
    """setPageLayout(pdf, layout) sets the page layout for a document."""
    libc.pycpdf_setPageLayout(pdf.pdf, layout)
    checkerror()
    return

"""Page modes."""
useNone = 0
useOutlines = 1
useThumbs = 2
useOC = 3
useAttachments = 4


def setPageMode(pdf, mode):
    """setPageMode(pdf, mode) sets the page mode for a document."""
    libc.pycpdf_setPageMode(pdf.pdf, mode)
    checkerror()
    return


def hideToolbar(pdf, flag):
    """hideToolbar(pdf, flag) sets the hide toolbar flag"""
    libc.pycpdf_hideToolbar(pdf.pdf, flag)
    checkerror()
    return


def hideMenubar(pdf, flag):
    """hideMenubar(pdf, flag) sets the hide menu bar flag"""
    libc.pycpdf_hideMenubar(pdf.pdf, flag)
    checkerror()
    return


def hideWindowUi(pdf, flag):
    """hideWindowUi(pdf, flag) sets the hide window UI flag"""
    libc.pycpdf_hideWindowUi(pdf.pdf, flag)
    checkerror()
    return


def fitWindow(pdf, flag):
    """fitWindow(pdf, flag) sets the fit window flag"""
    libc.pycpdf_fitWindow(pdf.pdf, flag)
    checkerror()
    return


def centerWindow(pdf, flag):
    """centerWindow(pdf, flag) sets the center window flag"""
    libc.pycpdf_centerWindow(pdf.pdf, flag)
    checkerror()
    return


def displayDocTitle(pdf, flag):
    """displayDocTitle(pdf, flag) sets the display doc title flag"""
    libc.pycpdf_displayDocTitle(pdf.pdf, flag)
    checkerror()
    return


def openAtPage(pdf, flag, pagenumber):
    """openAtPage(pdf, fit, pagenumber)"""
    libc.pycpdf_openAtPage(pdf.pdf, flag, pagenumber)
    checkerror()
    return


def setMetadataFromFile(pdf, filename):
    """setMetadataFromFile(pdf, filename) set the XMP metadata of a document,
    given a file name."""
    libc.pycpdf_setMetadataFromFile(pdf.pdf, str.encode(filename))
    checkerror()
    return


def setMetadataFromByteArray(pdf, data):
    """setMetadataFromByteArray(pdf, data, length) set the XMP metadata from
    an array of bytes."""
    libc.pycpdf_setMetadataFromByteArray(pdf.pdf, str.encode(data), len(data))
    checkerror()
    return


def getMetadata(pdf):
    """getMetadata(pdf, &length) returns the XMP metadata as a byte array of
    type bytes"""
    length = c_int32()
    data = libc.pycpdf_getMetadata(pdf.pdf, byref(length))
    out_data = create_string_buffer(length.value)
    memmove(out_data, data, length.value)
    libc.pycpdf_getMetadataFree()
    checkerror()
    return out_data.raw


def removeMetadata(pdf):
    """removeMetadata(pdf) removes the XMP metadata from a document"""
    libc.pycpdf_removeMetadata(pdf.pdf)
    checkerror()
    return


def createMetadata(pdf):
    """createMetadata(pdf) builds fresh metadata as best it can from existing
    metadata in the document."""
    libc.pycpdf_createMetadata(pdf.pdf)
    checkerror()
    return


def setMetadataDate(pdf, date):
    """setMetadataDate(pdf, date) sets the metadata date for a PDF. The date
    is given in PDF date format -- cpdf will convert it to XMP format. The date
    'now' means now."""
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
    from one:

    labelstyle = LowercaseRoman
    labelprefix = ""
    startpage = 1
    startvalue = 1

    labelstyle = DecimalArabic
    labelprefix = ""
    startpage = 6
    startvalue = 1 """
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
    """Add page labels.

    addPageLabels(pdf, style, prefix, offset, range, progress)

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
    """removePageLabels(pdf) removes the page labels from the document."""
    libc.pycpdf_removePageLabels(pdf.pdf)
    checkerror()
    return


def getPageLabelStringForPage(pdf, pagenumber):
    """getPageLabelStringForPage(pdf, page number) calculates the full label
    string for a given page, and returns it"""
    r = string_at(libc.pycpdf_getPageLabelStringForPage(
        pdf.pdf, pagenumber)).decode()
    checkerror()
    return r

# CHAPTER 12. File Attachments


def attachFile(filename, pdf):
    """attachFile(filename, pdf) attaches a file to the pdf. It is attached at
    document level."""
    libc.pycpdf_attachFile(str.encode(filename), pdf.pdf)
    checkerror()


def attachFileToPage(filename, pdf, pagenumber):
    """attachFileToPage(filename, pdf, pagenumber) attaches a file, given its
    file name, pdf, and the page number to which it should be attached."""
    libc.pycpdf_attachFileToPage(str.encode(filename), pdf.pdf, pagenumber)
    checkerror()


def attachFileFromMemory(data, filename, pdf):
    """attachFileFromMemory(memory, length, filename, pdf) attaches from
    memory, just like attachFile."""
    libc.pycpdf_attachFileFromMemory(
        data, len(data), str.encode(filename), pdf.pdf)
    checkerror()


def attachFileToPageFromMemory(data, filename, pdf, pagenumber):
    """attachFileToPageFromMemory(memory, length, filename, pdf, pagenumber)
    attaches from memory, just like attachFileToPage."""
    libc.pycpdf_attachFileToPageFromMemory(
        data, len(data), str.encode(filename), pdf.pdf, pagenumber)
    checkerror()


def removeAttachedFiles(pdf):
    """Remove all page- and document-level attachments from a document"""
    libc.pycpdf_removeAttachedFiles(pdf.pdf)
    checkerror()


def getAttachments(pdf):
    """List information about attachements. Returns a list of tuples
    (name, page number, byte array of data)"""
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


def getImageResolution(pdf, min_required_resolution):
    """Return a list of all uses of images in the PDF which do not meet the
    minimum required resolution in dpi"""
    n = libc.pycpdf_startGetImageResolution(pdf.pdf, min_required_resolution)
    l = []
    for x in range(n):
        pagenumber = libc.pycpdf_getImageResolutionPageNumber(x)
        imagename = string_at(
            libc.pycpdf_getImageResolutionImageName(x)).decode()
        xp = libc.pycpdf_getImageResolutionXPixels(x)
        yp = libc.pycpdf_getImageResolutionYPixels(x)
        xr = libc.pycpdf_getImageResolutionXRes(x)
        yr = libc.pycpdf_getImageResolutionYRes(x)
        l.append((pagenumber, imagename, xp, yp, xr, yr))
    libc.pycpdf_endGetImageResolution()
    checkerror()
    return l

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


def removeFonts(pdf):
    """removeFonts(pdf) removes all font data from a file."""
    libc.pycpdf_removeFonts(pdf.pdf)
    checkerror()


def copyFont(pdf, pdf2, r, pagenumber, fontname):
    """copyFont(from, to, range, pagenumber, fontname) copies the given font
    from the given page in the 'from' PDF to every page in the 'to' PDF. The
    new font is stored under it's font name."""
    r = range_of_list(r)
    libc.pycpdf_copyFont(pdf.pdf, pdf2.pdf, r,
                         pagenumber, str.encode(fontname))
    deleteRange(r)
    checkerror()

# CHAPTER 15. PDF and JSON


def outputJSON(filename, parse_content, no_stream_data, pdf):
    """outputJSON(filename, parse_content, no_stream_data, pdf) outputs a PDF
    in JSON format to the given filename. If parse_content is True, page
    content is parsed. If no_stream_data is True, all stream data is suppressed
    entirely."""
    libc.pycpdf_outputJSON(str.encode(filename),
                           parse_content, no_stream_data, pdf.pdf)
    checkerror()

# CHAPTER 16. Optional Content Groups


def getOCGList(pdf):
    """Return a list of Optional Content Groups in the given pdf."""
    l = []
    n = libc.pycpdf_startGetOCGList(pdf.pdf)
    for x in range(n):
        l.append(string_at(libc.pycpdf_OCGListEntry(x)).decode())
    libc.pycpdf_endGetOCGList()
    checkerror()
    return l


def OCGRename(pdf, n_from, n_to):
    """OCGRename(pdf, n_from, n_to) will rename an optional content group."""
    libc.pycpdf_OCGRename(pdf.pdf, str.encode(n_from), str.encode(n_to))
    checkerror()


def OCGOrderAll(pdf):
    """Ensure that every optional content group appears in the OCG order list."""
    libc.pycpdf_OCGOrderAll(pdf.pdf)
    checkerror()


def OCGCoalesce(pdf):
    """Coalesce optional content groups. For example, if we merge or stamp two
    files both with an OCG called "Layer 1", we will have two different
    optional content groups. This function will merge the two into a single
    optional content group."""
    libc.pycpdf_OCGCoalesce(pdf.pdf)
    checkerror()


# CHAPTER 17. Miscellaneous


def draft(pdf, r, boxes):
    """draft(pdf, range, boxes) removes images on the given pages, replacing
    them with crossed boxes if 'boxes' is true"""
    r = range_of_list(r)
    libc.pycpdf_draft(pdf.pdf, r, boxes)
    deleteRange(r)
    checkerror()


def removeAllText(pdf, r):
    """removeAllText(pdf, range) removes all text from the given pages in a
    given document."""
    r = range_of_list(r)
    libc.pycpdf_removeAllText(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def blackText(pdf, r):
    """blackText(pdf, range) blackens all text on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackText(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def blackLines(pdf, r):
    """blackLines(pdf, range) blackens all lines on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackLines(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def blackFills(pdf, r):
    """blackFills(pdf, range) blackens all fills on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackFills(pdf.pdf, r)
    deleteRange(r)
    checkerror()


def thinLines(pdf, r, linewidth):
    """thinLines(pdf, range, min_thickness) thickens every line less than
    min_thickness to min_thickness. Thickness given in points."""
    r = range_of_list(r)
    libc.pycpdf_thinLines(pdf.pdf, r, linewidth)
    deleteRange(r)
    checkerror()


def copyId(pdf, pdf2):
    """copyId(from, to) copies the /ID from one document to another."""
    libc.pycpdf_copyId(pdf.pdf, pdf2.pdf)
    checkerror()


def removeId(pdf):
    """removeId(pdf) removes a document's /ID"""
    libc.pycpdf_removeId(pdf.pdf)
    checkerror()


def setVersion(pdf, version):
    """setVersion(pdf, version) sets the minor version number of a document."""
    libc.pycpdf_setVersion(pdf.pdf, version)
    checkerror()


def setFullVersion(pdf, major, minor):
    """setFullVersion(pdf, version) sets the major and minor version number of
    a document."""
    libc.pycpdf_setFullVersion(pdf.pdf, major, minor)
    checkerror()


def removeDictEntry(pdf, key):
    """removeDictEntry(pdf, key) removes any dictionary entry with the given
    key anywhere in the document"""
    libc.pycpdf_removeDictEntry(pdf.pdf, str.encode(key))
    checkerror()


def removeClipping(pdf, r):
    """removeClipping(pdf, range) removes all clipping from pages in the given
    range"""
    r = range_of_list(r)
    libc.pycpdf_removeClipping(pdf.pdf, r)
    deleteRange(r)
    checkerror()

# CHAPTER X. Undocumented or Internal


def setDemo(v):
    """Internal."""
    libc.pycpdf_setDemo(v)
    checkerror()


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
