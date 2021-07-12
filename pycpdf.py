"""This is the introduction summary line

and here is the elaboration text.
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
    libc.pycpdf_enumeratePDFsInfo.restype = POINTER(c_char)
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
        [c_int, c_int, c_int, POINTER(c_char), c_int, c_double, c_double, c_double,
         c_int, c_int, c_double, c_double, c_double, c_double, c_int, c_int, c_int,
         c_double, c_int, c_int, c_int, POINTER(c_char), c_double, c_int]
    libc.pycpdf_addTextSimple.argtypes =\
        [c_int, c_int, POINTER(c_char), c_int, c_double,
         c_double, c_int, c_double]
    libc.pycpdf_getMetadata.restype = POINTER(c_uint8)
    libc.pycpdf_getAttachmentData.restype = POINTER(c_uint8)
    libc.pycpdf_startGetImageResolution.argtypes = [c_int, c_double]
    libc.pycpdf_getFontName.restype = POINTER(c_char)
    libc.pycpdf_getFontType.restype = POINTER(c_char)
    libc.pycpdf_getFontEncoding.restype = POINTER(c_char)
    libc.pycpdf_getPageLabelStringForPage.restype = POINTER(c_char)
    libc.pycpdf_getPageLabelPrefix.restype = POINTER(c_char)
    libc.pycpdf_dateStringOfComponents.restype = POINTER(c_char)


class CPDFError(Exception):
    """Any pycpdflib function may raise an exception CPDFError, carrying a string describing what went wrong"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def lastError():
    """Return the last error. Not usually used directly, since cdpflib functions raise exceptions"""
    return libc.pycpdf_lastError()


def lastErrorString():
    """Return the last error string. Not usually used directly, since cpdflib functions raise exceptions"""
    return string_at(libc.pycpdf_lastErrorString()).decode()


def checkerror():
    """Raise an exception if the last function call resulted in an error. Not used directly, since cpdflib functions will raise the exception directly."""
    if lastError() != 0:
        s = lastErrorString()
        clearError()
        raise CPDFError(s)

# CHAPTER 0. Preliminaries


def startup():
    """To be called after loadDLL, before any other function. Sets up cpdflib."""
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


def version():
    """Returns the version number of the cpdflib library"""
    v = string_at(libc.pycpdf_version()).decode()
    checkerror()
    return v


def setFast():
    """ Some operations have a fast mode. The default is 'slow' mode, which works
    even on old-fashioned files. For more details, see section 1.13 of the CPDF
    manual. These functions set the mode globally. """
    libc.pycpdf_setFast()
    checkerror()


def setSlow():
    """ Some operations have a fast mode. The default is 'slow' mode, which works
    even on old-fashioned files. For more details, see section 1.13 of the CPDF
    manual. These functions set the mode globally. """
    libc.pycpdf_setSlow()
    checkerror()


def clearError():
    """ cpdf_clearError clears the current error state. """
    libc.pycpdf_clearError()
    checkerror()


def onExit():
    """ cpdf_onExit is a debug function which prints some information about
    resource usage. This can be used to detect if PDFs or ranges are being
    deallocated properly."""
    libc.pycpdf_onExit()
    checkerror()

# CHAPTER 1. Basics


def fromFile(filename, userpw):
    """ cpdf_fromFile(filename, userpw) loads a PDF file from a given file. Supply a
    user password (possibly blank) in case the file is encypted. It won't be
    decrypted, but sometimes the password is needed just to load the file."""
    pdf = Pdf(libc.pycpdf_fromFile(str.encode(filename), str.encode(userpw)))
    checkerror()
    return pdf


def fromFileLazy(filename, userpw):
    """ cpdf_fromFileLazy(pdf, userpw) loads a PDF from a file, doing only minimal
    parsing. The objects will be read and parsed when they are actually needed.
    Use this when the whole file won't be required. Also supply a user password
    (possibly blank) in case the file is encypted. It won't be decrypted, but
    sometimes the password is needed just to load the file."""
    pdf = Pdf(libc.pycpdf_fromFileLazy(
        str.encode(filename), str.encode(userpw)))
    checkerror()
    return pdf


def fromMemory(data, userpw):
    """cpdf_fromMemory(data, length, userpw) loads a file from memory, given a
    pointer and a length, and the user password."""
    pdf = Pdf(libc.pycpdf_fromMemory(data, len(data), str.encode(userpw)))
    checkerror()
    return pdf


def fromMemoryLazy(data, userpw):
    """ cpdf_fromMemory(data, length, userpw) loads a file from memory, given a
    pointer and a length, and the user password, but lazily like
    cpdf_fromFileLazy."""
    pdf = Pdf(libc.pycpdf_fromMemoryLazy(data, len(data), str.encode(userpw)))
    checkerror()
    return pdf


def blankDocument(w, h, pages):
    """ cpdf_blankDocument(width, height, num_pages) creates a blank document with
    pages of the given width (in points), height (in points), and number of
    pages."""
    pdf = Pdf(libc.pycpdf_blankDocument(w, h, pages))
    checkerror()
    return pdf


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
    """cpdf_blankDocument(width, height, num_pages) creates a blank document with
    pages of the given width (in points), height (in points), and number of
    pages. """
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


def enumeratePDFs():
    """FIXME What does this do?"""
    pdfs = []
    n = libc.pycpdf_startEnumeratePDFs()
    for x in range(n):
        key = libc.pycpdf_enumeratePDFsKey(x)
        info = string_at(libc.pycpdf_enumeratePDFsInfo(x)).decode()
        pdfs.append((key, info))
    libc.pycpdf_endEnumeratePDFs()
    checkerror()
    return pdfs


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
        r = libc.pycpdf_rangeAdd(r, x)
    checkerror()
    return r


def parsePagespec(pdf, pagespec):
    """cpdf_parsePagespec(pdf, range) parses a page specification with reference to
    a given PDF (the PDF is supplied so that page ranges which reference pages
    which do not exist are rejected)."""
    r = list_of_range(libc.pycpdf_parsePagespec(pdf.pdf, str.encode(pagespec)))
    checkerror()
    return r


def validatePagespec(pagespec):
    """cpdf_validatePagespec(range) validates a page specification so far as is
    possible in the absence of the actual document."""
    r = libc.pycpdf_validatePagespec(str.encode(pagespec))
    checkerror()
    return r


def stringOfPagespec(pdf, r):
    """cpdf_stringOfPagespec(pdf, range) builds a page specification from a page
    range. For example, the range containing 1,2,3,6,7,8 in a document of 8
    pages might yield "1-3,6-end" """
    rn = range_of_list(r)
    r = string_at(libc.pycpdf_stringOfPagespec(pdf.pdf, rn)).decode()
    checkerror()
    return r


def blankRange():
    """cpdf_blankRange() creates a range with no pages in."""
    r = libc.pycpdf_blankRange()
    checkerror()
    return r


def pageRange(f, t):
    """ cpdf_range(from, to) build a range from one page to another inclusive. For example,
    cpdf_range(3,7) gives the range 3,4,5,6,7 """
    r = list_of_range(libc.pycpdf_pageRange(f, t))
    checkerror()
    return r


def all(pdf):
    """cpdf_all(pdf) is the range containing all the pages in a given document."""
    r = list_of_range(libc.pycpdf_all(pdf.pdf))
    checkerror()
    return r


def even(r):
    """cpdf_even(range) makes a range which contains just the even pages of another
    range"""
    rn = range_of_list(r)
    r = list_of_range(libc.pycpdf_even(rn))
    checkerror()
    return r


def odd(r):
    """cpdf_odd(range) makes a range which contains just the odd pages of another
    range"""
    rn = range_of_list(r)
    r = list_of_range(libc.pycpdf_odd(rn))
    checkerror()
    return r


def rangeUnion(a, b):
    """cpdf_rangeUnion(a, b) makes the union of two ranges giving a range containing the
    pages in range a and range b."""
    r = list_of_range(libc.pycpdf_rangeUnion(
        range_of_list(a), range_of_list(b)))
    checkerror()
    return r


def difference(a, b):
    """cpdf_difference(a, b) makes the difference of two ranges, giving a range
    containing all the pages in a except for those which are also in b."""
    r = list_of_range(libc.pycpdf_difference(
        range_of_list(a), range_of_list(b)))
    checkerror()
    return r


def removeDuplicates(r):
    """cpdf_removeDuplicates(range) deduplicates a range, making a new one."""
    r = list_of_range(libc.pycpdf_removeDuplicates(range_of_list(r)))
    checkerror()
    return r


def rangeLength(r):
    """cpdf_rangeLength gives the number of pages in a range."""
    r = libc.pycpdf_rangeLength(range_of_list(r))
    checkerror()
    return r


def rangeGet(r, n):
    """cpdf_rangeGet(range, n) gets the page number at position n in a range, where
    n runs from 0 to rangeLength - 1."""
    rn = range_of_list(r)
    r2 = libc.pycpdf_rangeGet(rn, n)
    checkerror()
    return r2


def rangeAdd(r, p):
    """cpdf_rangeAdd(range, page) adds the page to a range, if it is not already
    there."""
    rn = range_of_list(r)
    r2 = list_of_range(libc.pycpdf_rangeAdd(rn, p))
    checkerror()
    return r2


def isInRange(r, p):
    """cpdf_isInRange(range, page) returns true if the page is in the range, false
    otherwise."""
    rn = range_of_list(r)
    r2 = libc.pycpdf_isInRange(rn, p)
    checkerror()
    return r2


def pages(pdf):
    """cpdf_pages(pdf) returns the number of pages in a PDF."""
    r = libc.pycpdf_pages(pdf.pdf)
    checkerror()
    return r


def pagesFast(userpw, filename):
    """cpdf_pagesFast(password, filename) returns the number of pages in a given
    PDF, with given user encryption password. It tries to do this as fast as
    possible, without loading the whole file."""
    r = libc.pycpdf_pagesFast(str.encode(userpw), str.encode(filename))
    checkerror()
    return r


def toFile(pdf, filename, linearize, make_id):
    """cpdf_toFile (pdf, filename, linearize, make_id) writes the file to a given
    filename. If linearize is true, it will be linearized. If make_id is true,
    it will be given a new ID."""
    libc.pycpdf_toFile(pdf.pdf, str.encode(filename), False, False)
    checkerror()


def toFileExt(pdf, filename, linearize, make_id, preserve_objstm, generate_objstm, compress_objstm):
    """cpdf_toFile (pdf, filename, linearize, make_id, preserve_objstm,
    generate_objstm, compress_objstm) writes the file to a given filename. If
    make_id is true, it will be given a new ID.  If preserve_objstm is true,
    existing object streams will be preserved. If generate_objstm is true,
    object streams will be generated even if not originally present. If
    compress_objstm is true, object streams will be compressed (what we usually
    want). WARNING: the pdf argument will be invalid after this call, and should
    be discarded."""
    libc.pycpdf_toFileExt(pdf.pdf, str.encode(
        filename), linearize, make_id, preserve_objstm, generate_objstm, compress_objstm)
    checkerror()


def toMemory(pdf, linearize, make_id):
    """Given a buffer of the correct size, cpdf_toFileMemory (pdf, linearize,
    make_id, &length) writes it and returns the buffer. The buffer length is
    filled in &length."""
    length = c_int32()
    data = libc.pycpdf_toMemory(pdf.pdf, linearize, make_id, byref(length))
    s = string_at(data)
    libc.pycpdf_toMemoryFree()
    checkerror()
    return s


def isEncrypted(pdf):
    """cpdf_isEncrypted(pdf) returns true if a documented is encrypted, false otherwise."""
    r = libc.pycpdf_isEncrypted(pdf.pdf)
    checkerror()
    return r


noEdit = 0
noPrint = 1
noCopy = 2
noAnnot = 3
noForms = 4
noExtract = 5
noAssemble = 6
noHqPrint = 7

pdf40bit = 0
pdf128bit = 1
aes128bitfalse = 2
aes128bittrue = 3
aes256bitfalse = 4
aes256bittrue = 5
aes256bitisofalse = 6
aes256bitisotrue = 7


def toFileEncrypted(pdf, method, permissions, ownerpw, userpw, linearize, makeid, filename):
    """cpdf_toFileEncrypted(pdf, encryption_method, permissions, permission_length,
    owner_password, user password, linearize, makeid, filename) writes a file as
    encrypted."""
    c_perms = (c_uint8 * len(permissions))(*permissions)
    libc.pycpdf_toFileEncrypted(pdf.pdf, method, c_perms, len(permissions), str.encode(ownerpw),
                                str.encode(userpw), linearize, makeid, str.encode(filename))
    checkerror()


def toFileEncryptedExt(pdf, method, permissions, ownerpw, userpw, linearize, makeid,
                       preserve_objstm, generate_objstm, compress_objstm, filename):
    """cpdf_toFileEncryptedExt(pdf, encryption_method, permissions,
    permission_length, owner_password, user_password, linearize, makeid,
    preserve_objstm, generate_objstm, compress_objstm, filename) WARNING: the
    pdf argument will be invalid after this call, and should be discarded."""
    c_perms = (c_uint8 * len(permissions))(*permissions)
    libc.pycpdf_toFileEncryptedExt(pdf.pdf, method, c_perms, len(permissions), str.encode(ownerpw),
                                   str.encode(
                                       userpw), linearize, makeid, preserve_objstm,
                                   generate_objstm, compress_objstm, str.encode(filename))
    checkerror()


def decryptPdf(pdf, userpw):
    """cpdf_decryptPdf(pdf, userpw) attempts to decrypt a PDF using the given user
    password. The error code is non-zero if the decryption fails."""
    libc.pycpdf_decryptPdf(pdf.pdf, str.encode(userpw))
    checkerror()


def decryptPdfOwner(pdf, ownerpw):
    """cpdf_decryptPdfOwner(pdf, ownerpw) attempts to decrypt a PDF using the given
    owner password. The error code is non-zero if the decryption fails."""
    libc.pycpdf_decryptPdfOwner(pdf.pdf, str.encode(ownerpw))
    checkerror()


def hasPermission(pdf, perm):
    """cpdf_hasPermission(pdf, permission) returns true if the given permission
    (restriction) is present."""
    r = libc.pycpdf_hasPermission(pdf.pdf, perm)
    checkerror()
    return r


def encryptionKind(pdf):
    """cpdf_encryptionMethod(pdf) return the encryption method currently in use on
    a document."""
    r = libc.pycpdf_encryptionKind(pdf.pdf)
    checkerror()
    return r

# CHAPTER 2. Merging and Splitting


def mergeSimple(pdfs):
    """cpdf_mergeSimple(pdfs, length) given an array of PDFs, and its length,
    merges the files into a new one, which is returned."""
    raw_pdfs = list(map(lambda p: p.pdf, pdfs))
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    r = Pdf(libc.pycpdf_mergeSimple(c_pdfs, len(pdfs)))
    checkerror()
    return r


def merge(pdfs, retain_numbering, remove_duplicate_fonts):
    """cpdf_merge(pdfs, len, retain_numbering, remove_duplicate_fonts) merges
    the PDFs. If retain_numbering is true page labels are not rewritten. If
    remove_duplicate_fonts is true, duplicate fonts are merged. This is useful
    when the source documents for merging originate from the same source."""
    raw_pdfs = map(lambda p: p.pdf, pdfs)
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    r = Pdf(libc.pycpdf_merge(c_pdfs, len(pdfs),
            retain_numbering, remove_duplicate_fonts))
    checkerror()
    return r


def mergeSame(pdfs, retain_numbering, remove_duplicate_fonts, ranges):
    """cpdf_mergeSame(pdfs, len, retain_numbering, remove_duplicate_fonts, ranges)
    is the same as cpdf_merge, except that it has an additional argument
    - an array of page ranges. This is used to select the pages to pick from
    each PDF. This avoids duplication of information when multiple discrete
    parts of a source PDF are included."""
    ranges = list(map(range_of_list, ranges))
    raw_pdfs = map(lambda p: p.pdf, pdfs)
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    c_ranges = (c_int * len(ranges))(*ranges)
    r = Pdf(libc.pycpdf_mergeSame(c_pdfs, len(pdfs),
            retain_numbering, remove_duplicate_fonts, c_ranges))
    checkerror()
    return r


def selectPages(pdf, r):
    """ cpdf_selectPages(pdf, range) returns a new document which just those pages
    in the page range."""
    rn = range_of_list(r)
    r = Pdf(libc.pycpdf_selectPages(pdf.pdf, rn))
    checkerror()
    return r

# CHAPTER 3. Pages


def scalePages(pdf, r, sx, sy):
    """cpdf_scalePages(pdf, range, x scale, y scale) scales the page dimensions
    and content by the given scale, about (0, 0). Other boxes (crop etc. are
    altered as appropriate)"""
    r = range_of_list(r)
    libc.pycpdf_scalePages(pdf.pdf, r, sx, sy)
    checkerror()


def scaleToFit(pdf, r, sx, sy, scale_to_fit_scale):
    """cpdf_scaleToFit(pdf, range, width height, scale) scales the content to fit
    new page dimensions (width x height) multiplied by scale (typically 1.0).
    Other boxed (crop etc. are altered as appropriate)"""
    r = range_of_list(r)
    libc.pycpdf_scaleToFit(pdf.pdf, r, sx, sy, scale_to_fit_scale)
    checkerror()


def scaleToFitPaper(pdf, r, papersize, scale_to_fit_scale):
    """cpdf_scaleToFitPaper(pdf, range, papersize, scale) scales the page content
    to fit the given page size, possibly multiplied by scale (typically 1.0)"""
    r = range_of_list(r)
    libc.pycpdf_scaleToFitPaper(pdf.pdf, r, papersize, scale_to_fit_scale)
    checkerror()


posCentre = 0
posLeft = 1
posRight = 2
top = 3
topLeft = 4
topRight = 5
left = 6
bottomLeft = 7
bottomRight = 8
right = 9
diagonal = 10
reverseDiagonal = 11


def tripleOfPosition(p):
    if p[0] == diagonal:
        return (p[0], 0.0, 0.0)
    if p[0] == reverseDiagonal:
        return (p[0], 0.0, 0.0)
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


def scaleContents(pdf, r, p, scale):
    """cpdf_scaleContents(pdf, range, position, scale) scales the contents of the
    pages in the range about the point given by the cpdf_position, by the
    scale given."""
    r = range_of_list(r)
    a, b, c = tripleOfPosition(p)
    libc.pycpdf_scaleContents(pdf.pdf, r, a, b, c, scale)
    checkerror()


def shiftContents(pdf, r, dx, dy):
    """cpdf_shiftContents(pdf, range, dx, dy) shifts the content of the pages in
    the range."""
    r = range_of_list(r)
    libc.pycpdf_shiftContents(pdf.pdf, r, dx, dy)
    checkerror()


def rotate(pdf, r, rotation):
    """cpdf_rotate(pdf, range, rotation) changes the viewing rotation to an
    absolute value. Appropriate rotations are 0, 90, 180, 270."""
    r = range_of_list(r)
    libc.pycpdf_rotate(pdf.pdf, r, rotation)
    checkerror()


def rotateBy(pdf, r, rotation):
    """cpdf_rotateBy(pdf, range, rotation) changes the viewing rotation by a
    given number of degrees. Appropriate values are 90, 180, 270."""
    r = range_of_list(r)
    libc.pycpdf_rotateBy(pdf.pdf, r, rotation)
    checkerror()


def rotateContents(pdf, r, rotation):
    """cpdf_rotateContents(pdf, range, angle) rotates the content about the centre
    of the page by the given number of degrees, in a clockwise direction."""
    r = range_of_list(r)
    libc.pycpdf_rotateContents(pdf.pdf, r, rotation)
    checkerror()


def upright(pdf, r):
    """cpdf_upright(pdf, range) changes the viewing rotation of the pages in the
    range, counter-rotating the dimensions and content such that there is no
    visual change."""
    r = range_of_list(r)
    libc.pycpdf_upright(pdf.pdf, r)
    checkerror()


def hFlip(pdf, r):
    """cpdf_hFlip(pdf, range) flips horizontally the pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_hFlip(pdf.pdf, r)
    checkerror()


def vFlip(pdf, r):
    """cpdf_vFlip(pdf, range) flips vertically the pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_vFlip(pdf.pdf, r)
    checkerror()


def crop(pdf, r, x, y, w, h):
    """cpdf_crop(pdf, range, x, y, w, h) crops a page, replacing any existing
    crop box. The dimensions are in points."""
    r = range_of_list(r)
    libc.pycpdf_crop(pdf.pdf, r, x, y, w, h)
    checkerror()


def removeCrop(pdf, r):
    """cpdf_removeCrop(pdf, range) removes any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeCrop(pdf.pdf, r)
    checkerror()


def removeTrim(pdf, r):
    """cpdf_removeTrim(pdf, range) removes any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeTrim(pdf.pdf, r)
    checkerror()


def removeArt(pdf, r):
    """cpdf_removeArt(pdf, range) removes any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeArt(pdf.pdf, r)
    checkerror()


def removeBleed(pdf, r):
    """cpdf_removeBleed(pdf, range) removes any crop box from pages in the range."""
    r = range_of_list(r)
    libc.pycpdf_removeBleed(pdf.pdf, r)
    checkerror()


def trimMarks(pdf, r):
    """cpdf_trimMarks(pdf, range) adds trim marks to the given pages, if the trimbox exists."""
    r = range_of_list(r)
    libc.pycpdf_trimMarks(pdf.pdf, r)
    checkerror()


def showBoxes(pdf, r):
    """cpdf_showBoxes(pdf, range) shows the boxes on the given pages, for debug."""
    r = range_of_list(r)
    libc.pycpdf_showBoxes(pdf.pdf, r)
    checkerror()


def hardBox(pdf, r, boxname):
    """cpdf_hardBox make a given box a 'hard box' i.e clips it explicitly."""
    r = range_of_list(r)
    libc.pycpdf_hardBox(pdf.pdf, r, str.encode(boxname))
    checkerror()

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression


def compress(pdf):
    """cpdf_compress(pdf) compresses any uncompressed streams in the given PDF
    using the Flate algorithm."""
    libc.pycpdf_compress(pdf.pdf)
    checkerror()


def decompress(pdf):
    """cpdf_uncompress(pdf) uncompresses any streams in the given PDF, so long as
    the compression method is supported."""
    libc.pycpdf_decompress(pdf.pdf)
    checkerror()


def squeezeInMemory(pdf):
    """cpdf_squeezeToMemory(pdf) squeezes a pdf in memory."""
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
    print(f'There are {len(marks)} marks')
    libc.pycpdf_startSetBookmarkInfo(len(marks))
    for n, m in enumerate(marks):
        print(f'n = {n}')
        level, page, text, openStatus = m
        print(level, page, text, openStatus)
        libc.pycpdf_setBookmarkLevel(n, level)
        print('level done')
        libc.pycpdf_setBookmarkPage(pdf, n, page)
        print('page done')
        libc.pycpdf_setBookmarkOpenStatus(n, openStatus)
        print('openstatus done')
        libc.pycpdf_setBookmarkText(n, text)
        print('text done')
    libc.pycpdf_endSetBookmarkInfo(pdf.pdf)
    checkerror()

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps


def stampOn(pdf, pdf2, r):
    """cpdf_stampOn(stamp_pdf, pdf, range) stamps stamp_pdf on top of all the
    pages in the document which are in the range. The stamp is placed with its
    origin at the origin of the target document."""
    r = range_of_list(r)
    libc.pycpdf_stampOn(pdf.pdf, pdf2.pdf, r)
    checkerror()


def stampUnder(pdf, pdf2, r):
    """cpdf_stampUnder(stamp_pdf, pdf, range) stamps stamp_pdf under all the pages
    in the document which are in the range. The stamp is placed with its origin
    at the origin of the target document."""
    r = range_of_list(r)
    libc.pycpdf_stampUnder(pdf.pdf, pdf2.pdf, r)
    checkerror()


def stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, pos, relative_to_cropbox):
    """cpdf_stampExtended(pdf, pdf2, range, isover, scale_stamp_to_fit, pos,
    relative_to_cropbox) is a stamping function with extra features.
     - isover true, pdf goes over pdf2, isover false, pdf goes under pdf2
     - scale_stamp_to_fit scales the stamp to fit the page
     - pos gives the position to put the stamp
     - relative_to_cropbox: if true, pos is relative to cropbox not mediabox"""
    r = range_of_list(r)
    libc.pycpdf_stampExtended(
        pdf.pdf, pdf2.pdf, r, isover, scale_stamp_to_fit, pos, relative_to_cropbox)
    checkerror()


def combinePages(pdf, pdf2):
    """cpdf_combinePages(under, over) combines the PDFs page-by-page, putting
    each page of 'over' over each page of 'under'"""
    libc.pycpdf_combinePages(pdf.pdf, pdf2.pdf)
    checkerror()


leftJustify = 0
centreJustify = 1
rightJustify = 2


def addText(metrics, pdf, r, text, p, line_spacing, bates, font, size, red,
            green, blue, underneath, relative_to_cropbox, outline, opacity,
            justification, midline, topline, filename, line_width,
            embed_fonts):
    """Adding text. Adds text to a PDF, if the characters exist in the font.

         * metrics: If true, don't actually add text but collect metrics.
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
         * underneath: If true, text is added underneath rather than on top
         * relative_to_cropbox: If true, position is relative to crop box not media box
         * outline: If true, text is outline rather than filled
         * opacity: Opacity, 1.0 = opaque, 0.0 = wholly transparent
         * justification: Justification
         * midline: If true, position is relative to midline of text, not baseline
         * topline: If true, position is relative to topline of text, not baseline
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
    checkerror()


def removeText(pdf, r):
    """cpdf_removeText(pdf, range) will remove any text added by libcpdf from the
    given pages."""
    r = range_of_list(r)
    libc.pycpdf_removeText(pdf.pdf, r)
    checkerror()


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


def textWidth(font, string):
    """Return the width of a given string in the given font in thousandths of a
    point."""
    r = libc.pycpdf_textWidth(font, str.encode(string))
    checkerror()
    return r


# CHAPTER 9. Mulitpage facilities
def twoUp(pdf):
    """Impose a document two up. cpdf_twoUp does so by retaining the existing page
    size, scaling pages down. cpdf_twoUpStack does so by doubling the page size,
    to fit two pages on one."""
    libc.pycpdf_twoUp(pdf.pdf)
    checkerror()


def twoUpStack(pdf):
    """Impose a document two up. cpdf_twoUp does so by retaining the existing page
    size, scaling pages down. cpdf_twoUpStack does so by doubling the page size,
    to fit two pages on one."""
    libc.pycpdf_twoUpStack(pdf.pdf)
    checkerror()


def padBefore(pdf, r):
    """cpdf_padBefore(pdf, range) adds a blank page before each page in the given range"""
    r = range_of_list(r)
    libc.pycpdf_padBefore(pdf.pdf, r)
    checkerror()


def padAfter(pdf, r):
    """cpdf_padAfter(pdf, range) adds a blank page after each page in the given range"""
    r = range_of_list(r)
    libc.pycpdf_padAfter(pdf.pdf, r)
    checkerror()


def padEvery(pdf, n):
    """cpdf_pageEvery(pdf, n) adds a blank page after every n pages"""
    libc.pycpdf_padEvery(pdf.pdf, n)
    checkerror()


def padMultiple(pdf, n):
    """cpdf_padMultiple(pdf, n) adds pages at the end to pad the file to a multiple
    of n pages in length."""
    libc.pycpdf_padMultiple(pdf.pdf, n)
    checkerror()


def padMultipleBefore(pdf, n):
    """cpdf_padMultiple(pdf, n) adds pages at the beginning to pad the file to a
    multiple of n pages in length."""
    libc.pycpdf_padMultipleBefore(pdf.pdf, n)
    checkerror()

# CHAPTER 10. Annotations

# Not in the library version.

# CHAPTER 11. Document Information and Metadata


def isLinearized(filename):
    """cpdf_isLinearized(filename) finds out if a document is linearized as quickly
    as possible without loading it."""
    r = libc.pycpdf_isLinearized(str.encode(filename))
    checkerror()
    return r


def getVersion(pdf):
    """cpdf_vetVersion(pdf) returns the minor version number of a document."""
    r = libc.pycpdf_getVersion(pdf.pdf)
    checkerror()
    return r


def getMajorVersion(pdf):
    """cpdf_vetMajorVersion(pdf) returns the minor version number of a document."""
    r = libc.pycpdf_getMajorVersion(pdf.pdf)
    checkerror()
    return r


def getTitle(pdf):
    """cpdf_getTitle(pdf) returns the title of a document."""
    r = string_at(libc.pycpdf_getTitle(pdf.pdf)).decode()
    checkerror()
    return r


def getAuthor(pdf):
    """cpdf_getSubject(pdf) returns the subject of a document."""
    r = string_at(libc.pycpdf_getAuthor(pdf.pdf)).decode()
    checkerror()
    return r


def getSubject(pdf):
    """cpdf_getSubject(pdf) returns the subject of a document."""
    r = string_at(libc.pycpdf_getSubject(pdf.pdf)).decode()
    checkerror()
    return r


def getKeywords(pdf):
    """cpdf_getKeywords(pdf) returns the keywords of a document."""
    r = string_at(libc.pycpdf_getKeywords(pdf.pdf)).decode()
    checkerror()
    return r


def getCreator(pdf):
    """cpdf_getCreator(pdf) returns the creator of a document."""
    r = string_at(libc.pycpdf_getCreator(pdf.pdf)).decode()
    checkerror()
    return r


def getProducer(pdf):
    """cpdf_getProducer(pdf) returns the producer of a document."""
    r = string_at(libc.pycpdf_getProducer(pdf.pdf)).decode()
    checkerror()
    return r


def getCreationDate(pdf):
    """cpdf_getCreationDate(pdf) returns the creation date of a document."""
    r = string_at(libc.pycpdf_getCreationDate(pdf.pdf)).decode()
    checkerror()
    return r


def getModificationDate(pdf):
    """cpdf_getModificationDate(pdf) returns the modification date of a document."""
    r = string_at(libc.pycpdf_getModificationDate(pdf.pdf)).decode()
    checkerror()
    return r


def getTitleXMP(pdf):
    """cpdf_getTitleXMP(pdf) returns the XMP title of a document."""
    r = string_at(libc.pycpdf_getTitleXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getAuthorXMP(pdf):
    """cpdf_getAuthorXMP(pdf) returns the XMP author of a document."""
    r = string_at(libc.pycpdf_getAuthorXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getSubjectXMP(pdf):
    """cpdf_getSubjectXMP(pdf) returns the XMP subject of a document."""
    r = string_at(libc.pycpdf_getSubjectXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getKeywordsXMP(pdf):
    """cpdf_getKeywordsXMP(pdf) returns the XMP keywords of a document."""
    r = string_at(libc.pycpdf_getKeywordsXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getCreatorXMP(pdf):
    """cpdf_getCreatorXMP(pdf) returns the XMP creator of a document."""
    r = string_at(libc.pycpdf_getCreatorXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getProducerXMP(pdf):
    """cpdf_getProducerXMP(pdf) returns the XMP producer of a document."""
    r = string_at(libc.pycpdf_getProducerXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getCreationDateXMP(pdf):
    """cpdf_getCreationDateXMP(pdf) returns the XMP creation date of a document."""
    r = string_at(libc.pycpdf_getCreationDateXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getModificationDateXMP(pdf):
    """cpdf_getModificationDateXMP(pdf) returns the XMP modification date of a document."""
    r = string_at(libc.pycpdf_getModificationDateXMP(pdf.pdf)).decode()
    checkerror()
    return r


def setTitle(pdf, s):
    """cpdf_setTitle(pdf) sets the title of a document."""
    libc.pycpdf_setTitle(pdf.pdf, str.encode(s))
    checkerror()
    return


def setAuthor(pdf, s):
    """cpdf_setAuthor(pdf) sets the author of a document."""
    libc.pycpdf_setAuthor(pdf.pdf, str.encode(s))
    checkerror()
    return


def setSubject(pdf, s):
    """cpdf_setSubject(pdf) sets the subject of a document."""
    libc.pycpdf_setSubject(pdf.pdf, str.encode(s))
    checkerror()
    return


def setKeywords(pdf, s):
    """cpdf_setKeywords(pdf) sets the keywords of a document."""
    libc.pycpdf_setKeywords(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreator(pdf, s):
    """cpdf_setCreator(pdf) sets the creator of a document."""
    libc.pycpdf_setCreator(pdf.pdf, str.encode(s))
    checkerror()
    return


def setProducer(pdf, s):
    """cpdf_setProducer(pdf) sets the producer of a document."""
    libc.pycpdf_setProducer(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreationDate(pdf, s):
    """cpdf_setCreationDate(pdf) sets the creation date of a document."""
    libc.pycpdf_setCreationDate(pdf.pdf, str.encode(s))
    checkerror()
    return


def setModificationDate(pdf, s):
    """cpdf_setModificationDate(pdf) sets the modifcation date of a document."""
    libc.pycpdf_setModificationDate(pdf.pdf, str.encode(s))
    checkerror()
    return


def setTitleXMP(pdf, s):
    """cpdf_setTitleXMP(pdf) set the XMP title of a document."""
    libc.pycpdf_setTitleXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setAuthorXMP(pdf, s):
    """cpdf_setAuthorXMP(pdf) set the XMP author of a document."""
    libc.pycpdf_setAuthorXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setSubjectXMP(pdf, s):
    """cpdf_setSubjectXMP(pdf) set the XMP subject of a document."""
    libc.pycpdf_setSubjectXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setKeywordsXMP(pdf, s):
    """cpdf_setKeywordsXMP(pdf) set the XMP keywords of a document."""
    libc.pycpdf_setKeywordsXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreatorXMP(pdf, s):
    """cpdf_setCreatorXMP(pdf) set the XMP creator of a document."""
    libc.pycpdf_setCreatorXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setProducerXMP(pdf, s):
    """cpdf_setProducerXMP(pdf) set the XMP producer of a document."""
    libc.pycpdf_setProducerXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreationDateXMP(pdf, s):
    """cpdf_setCreationDateXMP(pdf) set the XMP creation date of a document."""
    libc.pycpdf_setCreationDateXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setModificationDateXMP(pdf, s):
    """cpdf_setModificationDateXMP(pdf) set the XMP modification date of a document."""
    libc.pycpdf_setModificationDateXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def getDateComponents(string):
    """Dates: Month 1-31, day 1-31, hours (0-23), minutes (0-59), seconds (0-59),
     hour_offset is the offset from UT in hours (-23 to 23); minute_offset is the
     offset from UT in minutes (-59 to 59).

    cpdf_getDateComponents(datestring, year, month, day, hour, minute, second,
    hour_offset, minute_offset) returns the components from a PDF date string."""
    year = c_int(0)
    month = c_int(0)
    day = c_int(0)
    hour = c_int(0)
    minute = c_int(0)
    second = c_int(0)
    hour_offset = c_int(0)
    minute_offset = c_int(0)
    libc.pycpdf_getDateComponents(str.encode(string), byref(year), byref(month), byref(day), byref(
        hour), byref(minute), byref(second), byref(hour_offset), byref(minute_offset))
    checkerror()
    return (year.value, month.value, day.value, hour.value, minute.value, second.value, hour_offset.value, minute_offset.value)


def dateStringOfComponents(components):
    """Dates: Month 1-31, day 1-31, hours (0-23), minutes (0-59), seconds (0-59),
     hour_offset is the offset from UT in hours (-23 to 23); minute_offset is the
     offset from UT in minutes (-59 to 59).

    cpdf_dateStringOfComponents(year, month, day, hour, minute, second,
    hour_offset, minute_offset) builds a PDF date string from individual
    components."""
    year, month, day, hour, minute, second, hour_offset, minute_offset = components
    r = string_at(libc.pycpdf_dateStringOfComponents(
        year, month, day, hour, minute, second, hour_offset, minute_offset)).decode()
    checkerror()
    return r


def getPageRotation(pdf, pagenumber):
    """cpdf_getPageRotation(pdf, pagenumber) gets the viewing rotation for a given
    page."""
    r = libc.pycpdf_getPageRotation(pdf.pdf, pagenumber)
    checkerror()
    return r


def hasBox(pdf, pagenumber, boxname):
    """cpdf_hasBox(pdf, pagenumber, boxname) returns true, if that page has the
    given box. E.g "/CropBox" """
    r = libc.pycpdf_hasBox(pdf.pdf, pagenumber, str.encode(boxname))
    checkerror()
    return r


def getMediaBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x, min y, max y in
    points. Only suceeds if such a box exists, as checked by cpdf_hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getMediaBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getCropBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x, min y, max y in
    points. Only suceeds if such a box exists, as checked by cpdf_hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getCropBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getTrimBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x, min y, max y in
    points. Only suceeds if such a box exists, as checked by cpdf_hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getTrimBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getArtBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x, min y, max y in
    points. Only suceeds if such a box exists, as checked by cpdf_hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getArtBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getBleedBox(pdf, pagenumber):
    """These functions get a box given the document, page range, min x, max x, min y, max y in
    points. Only suceeds if such a box exists, as checked by cpdf_hasBox"""
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getBleedBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def setMediaBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x, min y,
    max y in points."""
    libc.pycpdf_setMediaBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def setCropBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x, min y,
    max y in points."""
    libc.pycpdf_setCropBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def setTrimBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x, min y,
    max y in points."""
    libc.pycpdf_setTrimBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def setArtBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x, min y,
    max y in points."""
    libc.pycpdf_setArtBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def setBleedBox(pdf, r, minx, maxx, miny, maxy):
    """These functions set a box given the document, page range, min x, max x, min y,
    max y in points."""
    libc.pycpdf_setBleedBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def markTrapped(pdf):
    """cpdf_markTrapped(pdf) marks a document as trapped."""
    libc.pycpdf_markTrapped(pdf.pdf)
    checkerror()
    return


def markUntrapped(pdf):
    """cpdf_markUntrapped(pdf) marks a document as untrapped."""
    libc.pycpdf_markUntrapped(pdf.pdf)
    checkerror()
    return


def markTrappedXMP(pdf):
    """cpdf_markTrappedXMP(pdf) marks a document as trapped in XMP metadata."""
    libc.pycpdf_markTrappedXMP(pdf.pdf)
    checkerror()
    return


def markUntrappedXMP(pdf):
    """cpdf_markUntrappedXMP(pdf) marks a document as untrapped in XMP metadata."""
    libc.pycpdf_markUntrappedXMP(pdf.pdf)
    checkerror()
    return


singlePage = 0
oneColumn = 1
twoColumnLeft = 2
twoColumnRight = 3
twoPageLeft = 4
twoPageRight = 5


def setPageLayout(pdf, layout):
    """cpdf_setPageLayout(pdf, layout) sets the page layout for a document."""
    libc.pycpdf_setPageLayout(pdf.pdf, layout)
    checkerror()
    return


useNone = 0
useOutlines = 1
useThumbs = 2
useOC = 3
useAttachments = 4


def setPageMode(pdf, mode):
    """cpdf_setPageMode(pdf, mode) sets the page mode for a document."""
    libc.pycpdf_setPageMode(pdf.pdf, mode)
    checkerror()
    return


def hideToolbar(pdf, flag):
    """cpdf_hideToolbar(pdf, flag) sets the hide toolbar flag"""
    libc.pycpdf_hideToolbar(pdf.pdf, flag)
    checkerror()
    return


def hideMenubar(pdf, flag):
    """cpdf_hideMenubar(pdf, flag) sets the hide menu bar flag"""
    libc.pycpdf_hideMenubar(pdf.pdf, flag)
    checkerror()
    return


def hideWindowUi(pdf, flag):
    """cpdf_hideWindowUi(pdf, flag) sets the hide window UI flag"""
    libc.pycpdf_hideWindowUi(pdf.pdf, flag)
    checkerror()
    return


def fitWindow(pdf, flag):
    """cpdf_fitWindow(pdf, flag) sets the fit window flag"""
    libc.pycpdf_fitWindow(pdf.pdf, flag)
    checkerror()
    return


def centerWindow(pdf, flag):
    """cpdf_centerWindow(pdf, flag) sets the center window flag"""
    libc.pycpdf_centerWindow(pdf.pdf, flag)
    checkerror()
    return


def displayDocTitle(pdf, flag):
    """cpdf_displayDocTitle(pdf, flag) sets the display doc title flag"""
    libc.pycpdf_displayDocTitle(pdf.pdf, flag)
    checkerror()
    return


def openAtPage(pdf, flag, pagenumber):
    """cpdf_openAtPage(pdf, fit, pagenumber)"""
    libc.pycpdf_openAtPage(pdf.pdf, flag, pagenumber)
    checkerror()
    return


def setMetadataFromFile(pdf, filename):
    """cpdf_setMetadataFromFile(pdf, filename) set the XMP metadata of a document,
    given a file name."""
    libc.pycpdf_setMetadataFromFile(pdf.pdf, str.encode(filename))
    checkerror()
    return


def setMetadataFromByteArray(pdf, data):
    """cpdf_setMetadataFromByteArray(pdf, data, length) set the XMP metadata from
    an array of bytes."""
    libc.pycpdf_setMetadataFromByteArray(pdf.pdf, data, len(data))
    checkerror()
    return


def getMetadata(pdf):
    """cpdf_getMetadata(pdf, &length) returns the XMP metadata and fills in length."""
    length = c_int32()
    data = libc.pycpdf_getMetadata(pdf.pdf, byref(length))
    s = string_at(data)
    libc.pycpdf_getMetadataFree()
    checkerror()
    return s


def removeMetadata(pdf):
    """cpdf_removeMetadata(pdf) removes the XMP metadata from a document"""
    libc.pycpdf_removeMetadata(pdf.pdf)
    checkerror()
    return


def createMetadata(pdf):
    """cpdf_createMetadata(pdf) builds fresh metadata as best it can from existing
    metadata in the document."""
    libc.pycpdf_createMetadata(pdf.pdf)
    checkerror()
    return


def setMetadataDate(pdf, date):
    """cpdf_setMetadataDate(pdf, date) sets the metadata date for a PDF. The date
    is given in PDF date format -- cpdf will convert it to XMP format. The date
    'now' means now."""
    libc.pycpdf_setMetadataDate(pdf.pdf, str.encode(date))
    checkerror()
    return


decimalArabic = 0
uppercaseRoman = 1
lowercaseRoman = 2
uppercaseLetters = 3
lowercaseLetters = 4


def getPageLabels(pdf):
    """Get page labels as a list of tuples (style, prefix, offset, startvalue)"""
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

    cpdf_addPageLabels(pdf, style, prefix, offset, range, progress)

    The prefix is prefix text for each label. The range is the page range the
    labels apply to. Offset can be used to shift the numbering up or down."""
    style, prefix, offset, plrange = label
    libc.pycpdf_addPageLabels(pdf.pdf, style, str.encode(
        prefix), offset, range_of_list(plrange), progress)
    checkerror()
    return


def removePageLabels(pdf):
    """cpdf_removePageLabels(pdf) removes the page labels from the document."""
    libc.pycpdf_removePageLabels(pdf.pdf)
    checkerror()
    return


def getPageLabelStringForPage(pdf, pagenumber):
    """cpdf_getPageLabelStringForPage(pdf, page number) calculates the full label
    string for a given page, and returns it"""
    r = string_at(libc.pycpdf_getPageLabelStringForPage(
        pdf.pdf, pagenumber)).decode()
    checkerror()
    return r

# CHAPTER 12. File Attachments


def attachFile(filename, pdf):
    """cpdf_attachFile(filename, pdf) attaches a file to the pdf. It is attached at
    document level."""
    libc.pycpdf_attachFile(str.encode(filename), pdf.pdf)
    checkerror()


def attachFileToPage(filename, pdf, pagenumber):
    """cpdf_attachFileToPage(filename, pdf, pagenumber) attaches a file, given its
    file name, pdf, and the page number to which it should be attached."""
    libc.pycpdf_attachFileToPage(str.encode(filename), pdf.pdf, pagenumber)
    checkerror()


def attachFileFromMemory(data, filename, pdf):
    """cpdf_attachFileFromMemory(memory, length, filename, pdf) attaches from
    memory, just like cpdf_attachFile."""
    libc.pycpdf_attachFileFromMemory(data, len(data), filename, pdf.pdf)
    checkerror()


def attachFileToPageFromMemory(data, filename, pdf, pagenumber):
    """cpdf_attachFileToPageFromMemory(memory, length, filename, pdf, pagenumber)
    attaches from memory, just like cpdf_attachFileToPage."""
    libc.pycpdf_attachFileToPageFromMemory(
        data, len(data), filename, pdf.pdf, pagenumber)
    checkerror()


def removeAttachedFiles(pdf):
    """Remove all page- and document-level attachments from a document"""
    libc.pycpdf_removeAttachedFiles(pdf.pdf)
    checkerror()


def getAttachments(pdf):
    """List information about attachements. Returns a list of tuples
    (name, page number, data)"""
    libc.pycpdf_startGetAttachments(pdf.pdf)
    n = libc.pycpdf_numberGetAttachments()
    l = []
    for i in range(n):
        name = string_at(libc.pycpdf_getAttachmentName(n)).decode()
        page = libc.pycpdf_getAttachmentPage(n)
        length = c_int32()
        data = libc.pycpdf_getAttachmentData(n, byref(length))
        s = string_at(data)
        libc.pycpdf_getAttachmentDataFree()
        l.append((name, page, data))
    libc.pycpdf_endGetAttachments()
    checkerror()
    return l

# CHAPTER 13. Images


def getImageResolution(pdf, min_required_resolution):
    """Return a list of all uses of images in the PDF which do not meet the minimum required resolution in dpi"""
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
    print("fonts:", n)
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
    """cpdf_removeFonts(pdf) removes all font data from a file."""
    libc.pycpdf_removeFonts(pdf.pdf)
    checkerror()


def copyFont(pdf, pdf2, r, pagenumber, fontname):
    """cpdf_copyFont(from, to, range, pagenumber, fontname) copies the given font
    from the given page in the 'from' PDF to every page in the 'to' PDF. The new
    font is stored under it's font name."""
    r = range_of_list(r)
    libc.pycpdf_copyFont(pdf.pdf, pdf2.pdf, r,
                         pagenumber, str.encode(fontname))
    checkerror()

# CHAPTER 15. Miscellaneous


def draft(pdf, r, boxes):
    """cpdf_draft(pdf, range, boxes) removes images on the given pages, replacing
    them with crossed boxes if 'boxes' is true"""
    r = range_of_list(r)
    libc.pycpdf_draft(pdf.pdf, r, boxes)
    checkerror()


def removeAllText(pdf, r):
    """cpdf_removeAllText(pdf, range) removes all text from the given pages in a
    given document."""
    r = range_of_list(r)
    libc.pycpdf_removeAllText(pdf.pdf, r)
    checkerror()


def blackText(pdf, r):
    """cpdf_blackText(pdf, range) blackens all text on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackText(pdf.pdf, r)
    checkerror()


def blackLines(pdf, r):
    """cpdf_blackLines(pdf, range) blackens all lines on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackLines(pdf.pdf, r)
    checkerror()


def blackFills(pdf, r):
    """cpdf_blackFills(pdf, range) blackens all fills on the given pages."""
    r = range_of_list(r)
    libc.pycpdf_blackFills(pdf.pdf, r)
    checkerror()


def thinLines(pdf, r, linewidth):
    """cpdf_thinLines(pdf, range, min_thickness) thickens every line less than
    min_thickness to min_thickness. Thickness given in points."""
    r = range_of_list(r)
    libc.pycpdf_thinLines(pdf.pdf, r, linewidth)
    checkerror()


def copyId(pdf, pdf2):
    """cpdf_copyId(from, to) copies the /ID from one document to another."""
    libc.pycpdf_copyId(pdf.pdf, pdf2.pdf)
    checkerror()


def removeId(pdf):
    """cpdf_removeId(pdf) removes a document's /ID"""
    libc.pycpdf_removeId(pdf.pdf)
    checkerror()


def setVersion(pdf, version):
    """cpdf_setVersion(pdf, version) sets the minor version number of a document."""
    libc.pycpdf_setVersion(pdf.pdf, version)
    checkerror()


def removeDictEntry(pdf, key):
    """cpdf_removeDictEntry(pdf, key) removes any dictionary entry with the given
    key anywhere in the document"""
    libc.pycpdf_removeDictEntry(pdf.pdf, str.encode(key))
    checkerror()


def removeClipping(pdf, r):
    """cpdf_removeClipping(pdf, range) removes all clipping from pages in the given
    range"""
    r = range_of_list(r)
    libc.pycpdf_removeClipping(pdf.pdf, r)
    checkerror()

# CHAPTER UNDOC (To come in v2.4)


def addContent(content, before, pdf, r):
    r = range_of_list(r)
    libc.pycpdf_addContent(str.encode(content), before, pdf.pdf, r)
    checkerror()


def outputJSON(filename, parse_content, no_stream_data, pdf):
    libc.pycpdf_outputJSON(str.encode(filename),
                           parse_content, no_stream_data, pdf.pdf)
    checkerror()


def OCGCoalesce(pdf):
    libc.pycpdf_OCGCoalesce(pdf.pdf)
    checkerror()


def OCGRename(pdf, n_from, n_to):
    libc.pycpdf_OCGRename(pdf.pdf, str.encode(n_from), str.encode(n_to))
    checkerror()

#Add ocg list

def OCGOrderAll(pdf):
    libc.pycpdf_OCGOrderAll(pdf.pdf)
    checkerror()


def stampAsXObject(pdf, r, stamp_pdf):
    r = range_of_list(r)
    r2 = string_at(libc.pycpdf_stampAsXObject(
        pdf.pdf, r, stamp_pdf.pdf)).decode()
    checkerror()
    return r2


def setDemo(v):
    libc.pycpdf_setDemo(v)
    checkerror()
