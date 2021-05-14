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
    return libc.pycpdf_lastError()


def lastErrorString():
    return string_at(libc.pycpdf_lastErrorString()).decode()


def checkerror():
    if lastError() != 0:
        s = lastErrorString()
        clearError()
        raise CPDFError(s)

# CHAPTER 0. Preliminaries


def startup():
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
    v = string_at(libc.pycpdf_version()).decode()
    checkerror()
    return v


def setFast():
    libc.pycpdf_setFast()
    checkerror()


def setSlow():
    libc.pycpdf_setSlow()
    checkerror()


def clearError():
    libc.pycpdf_clearError()
    checkerror()


def onExit():
    libc.pycpdf_onExit()
    checkerror()

# CHAPTER 1. Basics


def fromFile(filename, userpw):
    pdf = Pdf(libc.pycpdf_fromFile(str.encode(filename), str.encode(userpw)))
    checkerror()
    return pdf


def fromFileLazy(filename, userpw):
    pdf = Pdf(libc.pycpdf_fromFileLazy(
        str.encode(filename), str.encode(userpw)))
    checkerror()
    return pdf


def fromMemory(data, userpw):
    pdf = Pdf(libc.pycpdf_fromMemory(data, len(data), str.encode(userpw)))
    checkerror()
    return pdf


def fromMemoryLazy(data, userpw):
    pdf = Pdf(libc.pycpdf_fromMemoryLazy(data, len(data), str.encode(userpw)))
    checkerror()
    return pdf


def blankDocument(w, h, pages):
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
    r = Pdf(libc.pycpdf_blankDocumentPaper(papersize, pages))
    checkerror()
    return r


def ptOfCm(i):
    r = libc.pycpdf_ptOfCm(i)
    checkerror()
    return r


def ptOfMm(i):
    r = libc.pycpdf_ptOfMm(i)
    checkerror()
    return r


def ptOfIn(i):
    r = libc.pycpdf_ptOfIn(i)
    checkerror()
    return r


def cmOfPt(i):
    r = libc.pycpdf_cmOfPt(i)
    checkerror()
    return r


def mmOfPt(i):
    r = libc.pycpdf_mmOfPt(i)
    checkerror()
    return r


def inOfPt(i):
    r = libc.pycpdf_inOfPt(i)
    checkerror()
    return r


def enumeratePDFs():
    pdfs = []
    n = libc.pycpdf_startEnumeratePDFs()
    for x in range(n):
        key = libc.pycpdf_enumeratePDFsKey(x)
        info = string_at(libc.pycpdf_enumeratePDFsInfo(x)).decode()
        pdfs.append((key, info))
    libc.pycpdf_endEnumeratePDFs()
    checkerror()
    return pdfs

# Convert between lists and ranges - these are internal functions, not for external use.


def list_of_range(r):
    l = []
    for x in range(libc.pycpdf_rangeLength(r)):
        l.append(libc.pycpdf_rangeGet(r, x))
    checkerror()
    return l


def range_of_list(l):
    r = libc.pycpdf_blankRange()
    for x in l:
        r = libc.pycpdf_rangeAdd(r, x)
    checkerror()
    return r


def parsePagespec(pdf, pagespec):
    r = list_of_range(libc.pycpdf_parsePagespec(pdf.pdf, str.encode(pagespec)))
    checkerror()
    return r


def validatePagespec(pagespec):
    r = libc.pycpdf_validatePagespec(str.encode(pagespec))
    checkerror()
    return r


def stringOfPagespec(pdf, r):
    rn = range_of_list(r)
    r = string_at(libc.pycpdf_stringOfPagespec(pdf.pdf, rn)).decode()
    checkerror()
    return r


def blankRange():
    r = libc.pycpdf_blankRange()
    checkerror()
    return r


def pageRange(f, t):
    r = list_of_range(libc.pycpdf_pageRange(f, t))
    checkerror()
    return r


def all(pdf):
    r = list_of_range(libc.pycpdf_all(pdf.pdf))
    checkerror()
    return r


def even(r):
    rn = range_of_list(r)
    r = list_of_range(libc.pycpdf_even(rn))
    checkerror()
    return r


def odd(r):
    rn = range_of_list(r)
    r = list_of_range(libc.pycpdf_odd(rn))
    checkerror()
    return r


def rangeUnion(a, b):
    r = list_of_range(libc.pycpdf_rangeUnion(
        range_of_list(a), range_of_list(b)))
    checkerror()
    return r


def difference(a, b):
    r = list_of_range(libc.pycpdf_difference(
        range_of_list(a), range_of_list(b)))
    checkerror()
    return r


def removeDuplicates(r):
    r = list_of_range(libc.pycpdf_removeDuplicates(range_of_list(r)))
    checkerror()
    return r


def rangeLength(r):
    r = libc.pycpdf_rangeLength(range_of_list(r))
    checkerror()
    return r


def rangeGet(r, n):
    rn = range_of_list(r)
    r2 = libc.pycpdf_rangeGet(rn, n)
    checkerror()
    return r2


def rangeAdd(r, p):
    rn = range_of_list(r)
    r2 = list_of_range(libc.pycpdf_rangeAdd(rn, p))
    checkerror()
    return r2


def isInRange(r, p):
    rn = range_of_list(r)
    r2 = libc.pycpdf_isInRange(rn, p)
    checkerror()
    return r2


def pages(pdf):
    r = libc.pycpdf_pages(pdf.pdf)
    checkerror()
    return r


def pagesFast(userpw, filename):
    r = libc.pycpdf_pagesFast(str.encode(userpw), str.encode(filename))
    checkerror()
    return r


def toFile(pdf, filename, linearize, make_id):
    libc.pycpdf_toFile(pdf.pdf, str.encode(filename), False, False)
    checkerror()


def toFileExt(pdf, filename, linearize, make_id, preserve_objstm, generate_objstm, compress_objstm):
    libc.pycpdf_toFileExt(pdf.pdf, str.encode(
        filename), linearize, make_id, preserve_objstm, generate_objstm, compress_objstm)
    checkerror()


def toMemory(pdf, linearize, make_id):
    length = c_int32()
    data = libc.pycpdf_toMemory(pdf.pdf, linearize, make_id, byref(length))
    s = string_at(data)
    libc.pycpdf_toMemoryFree()
    checkerror()
    return s


def isEncrypted(pdf):
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
    c_perms = (c_uint8 * len(permissions))(*permissions)
    libc.pycpdf_toFileEncrypted(pdf.pdf, method, c_perms, len(permissions), str.encode(ownerpw),
                                str.encode(userpw), linearize, makeid, str.encode(filename))
    checkerror()


def toFileEncryptedExt(pdf, method, permissions, ownerpw, userpw, linearize, makeid,
                       preserve_objstm, generate_objstm, compress_objstm, filename):
    c_perms = (c_uint8 * len(permissions))(*permissions)
    libc.pycpdf_toFileEncryptedExt(pdf.pdf, method, c_perms, len(permissions), str.encode(ownerpw),
                                   str.encode(
                                       userpw), linearize, makeid, preserve_objstm,
                                   generate_objstm, compress_objstm, str.encode(filename))
    checkerror()


def decryptPdf(pdf, userpw):
    libc.pycpdf_decryptPdf(pdf.pdf, str.encode(userpw))
    checkerror()


def decryptPdfOwner(pdf, ownerpw):
    libc.pycpdf_decryptPdfOwner(pdf.pdf, str.encode(ownerpw))
    checkerror()


def hasPermission(pdf, perm):
    r = libc.pycpdf_hasPermission(pdf.pdf, perm)
    checkerror()
    return r


def encryptionKind(pdf):
    r = libc.pycpdf_encryptionKind(pdf.pdf)
    checkerror()
    return r

# CHAPTER 2. Merging and Splitting


def mergeSimple(pdfs):
    raw_pdfs = list(map(lambda p: p.pdf, pdfs))
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    r = Pdf(libc.pycpdf_mergeSimple(c_pdfs, len(pdfs)))
    checkerror()
    return r


def merge(pdfs, retain_numbering, remove_duplicate_fonts):
    raw_pdfs = map(lambda p: p.pdf, pdfs)
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    r = Pdf(libc.pycpdf_merge(c_pdfs, len(pdfs),
            retain_numbering, remove_duplicate_fonts))
    checkerror()
    return r


def mergeSame(pdfs, retain_numbering, remove_duplicate_fonts, ranges):
    ranges = list(map(range_of_list, ranges))
    raw_pdfs = map(lambda p: p.pdf, pdfs)
    c_pdfs = (c_int * len(pdfs))(*raw_pdfs)
    c_ranges = (c_int * len(ranges))(*ranges)
    r = Pdf(libc.pycpdf_mergeSame(c_pdfs, len(pdfs),
            retain_numbering, remove_duplicate_fonts, c_ranges))
    checkerror()
    return r


def selectPages(pdf, r):
    rn = range_of_list(r)
    r = Pdf(libc.pycpdf_selectPages(pdf.pdf, rn))
    checkerror()
    return r

# CHAPTER 3. Pages


def scalePages(pdf, r, sx, sy):
    r = range_of_list(r)
    libc.pycpdf_scalePages(pdf.pdf, r, sx, sy)
    checkerror()


def scaleToFit(pdf, r, sx, sy, scale_to_fit_scale):
    r = range_of_list(r)
    libc.pycpdf_scaleToFit(pdf.pdf, r, sx, sy, scale_to_fit_scale)
    checkerror()


def scaleToFitPaper(pdf, r, papersize, scale_to_fit_scale):
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
    r = range_of_list(r)
    a, b, c = tripleOfPosition(p)
    libc.pycpdf_scaleContents(pdf.pdf, r, a, b, c, scale)
    checkerror()


def shiftContents(pdf, r, dx, dy):
    r = range_of_list(r)
    libc.pycpdf_shiftContents(pdf.pdf, r, dx, dy)
    checkerror()


def rotate(pdf, r, rotation):
    r = range_of_list(r)
    libc.pycpdf_rotate(pdf.pdf, r, rotation)
    checkerror()


def rotateBy(pdf, r, rotation):
    r = range_of_list(r)
    libc.pycpdf_rotateBy(pdf.pdf, r, rotation)
    checkerror()


def rotateContents(pdf, r, rotation):
    r = range_of_list(r)
    libc.pycpdf_rotateContents(pdf.pdf, r, rotation)
    checkerror()


def upright(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_upright(pdf.pdf, r)
    checkerror()


def hFlip(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_hFlip(pdf.pdf, r)
    checkerror()


def vFlip(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_vFlip(pdf.pdf, r)
    checkerror()


def crop(pdf, r, x, y, w, h):
    r = range_of_list(r)
    libc.pycpdf_crop(pdf.pdf, r, x, y, w, h)
    checkerror()


def removeCrop(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_removeCrop(pdf.pdf, r)
    checkerror()


def removeTrim(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_removeTrim(pdf.pdf, r)
    checkerror()


def removeArt(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_removeArt(pdf.pdf, r)
    checkerror()


def removeBleed(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_removeBleed(pdf.pdf, r)
    checkerror()


def trimMarks(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_trimMarks(pdf.pdf, r)
    checkerror()


def showBoxes(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_showBoxes(pdf.pdf, r)
    checkerror()


def hardBox(pdf, r, boxname):
    r = range_of_list(r)
    libc.pycpdf_hardBox(pdf.pdf, r, str.encode(boxname))
    checkerror()

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression


def compress(pdf):
    libc.pycpdf_compress(pdf.pdf)
    checkerror()


def decompress(pdf):
    libc.pycpdf_decompress(pdf.pdf)
    checkerror()


def squeezeInMemory(pdf):
    libc.pycpdf_squeezeInMemory(pdf.pdf)
    checkerror()

# CHAPTER 6. Bookmarks

# Format: list of tuples. (level : int, page : int, text : string, openstatus : int/bool)


def getBookmarks(pdf):
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
    libc.pycpdf_startSetBookmarkInfo(len(marks))
    for n, m in enumerate(marks):
        level, page, text, openStatus = m
        print(level, page, text, openStatus)
        libc.pycpdf_setBookmarkLevel(n, level)
        libc.pycpdf_setBookmarkPage(n, page)
        libc.pycpdf_setBookmarkOpenStatus(n, openStatus)
        libc.pycpdf_setBookmarkText(n, text)
    libc.pycpdf_endSetBookmarkInfo(pdf.pdf)
    checkerror()

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps


def stampOn(pdf, pdf2, r):
    r = range_of_list(r)
    libc.pycpdf_stampOn(pdf.pdf, pdf2.pdf, r)
    checkerror()


def stampUnder(pdf, pdf2, r):
    r = range_of_list(r)
    libc.pycpdf_stampUnder(pdf.pdf, pdf2.pdf, r)
    checkerror()


def stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, pos, relative_to_cropbox):
    r = range_of_list(r)
    libc.pycpdf_stampExtended(
        pdf.pdf, pdf2.pdf, r, isover, scale_stamp_to_fit, pos, relative_to_cropbox)
    checkerror()


def combinePages(pdf, pdf2):
    libc.pycpdf_combinePages(pdf.pdf, pdf2.pdf)
    checkerror()


leftJustify = 0
centreJustify = 1
rightJustify = 2


def addText(metrics, pdf, r, text, p, line_spacing, bates, font, size, red, green, blue, underneath, relative_to_cropbox, outline, opacity, justification, midline, topline, filename, line_width, embed_fonts):
    a, b, c = tripleOfPosition(p)
    r = range_of_list(r)
    libc.pycpdf_addText(metrics, pdf.pdf, r, str.encode(text), a, b, c, line_spacing, bates, font, size, red, green, blue, underneath,
                        relative_to_cropbox, outline, opacity, justification, midline, topline, str.encode(filename), line_width, embed_fonts)
    checkerror()


def addTextSimple(pdf, r, text, p, font, size):
    a, b, c = tripleOfPosition(p)
    r = range_of_list(r)
    libc.pycpdf_addTextSimple(
        pdf.pdf, r, str.encode(text), a, b, c, font, size)
    checkerror()


def removeText(pdf, r):
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
    r = libc.pycpdf_textWidth(font, str.encode(string))
    checkerror()
    return r


# CHAPTER 9. Mulitpage facilities
def twoUp(pdf):
    libc.pycpdf_twoUp(pdf.pdf)
    checkerror()


def twoUpStack(pdf):
    libc.pycpdf_twoUpStack(pdf.pdf)
    checkerror()


def padBefore(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_padBefore(pdf.pdf, r)
    checkerror()


def padAfter(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_padAfter(pdf.pdf, r)
    checkerror()


def padEvery(pdf, n):
    libc.pycpdf_padEvery(pdf.pdf, n)
    checkerror()


def padMultiple(pdf, n):
    libc.pycpdf_padMultiple(pdf.pdf, n)
    checkerror()


def padMultipleBefore(pdf, n):
    libc.pycpdf_padMultipleBefore(pdf.pdf, n)
    checkerror()

# CHAPTER 10. Annotations

# Not in the library version.

# CHAPTER 11. Document Information and Metadata


def isLinearized(filename):
    r = libc.pycpdf_isLinearized(str.encode(filename))
    checkerror()
    return r


def getVersion(pdf):
    r = libc.pycpdf_getVersion(pdf.pdf)
    checkerror()
    return r


def getMajorVersion(pdf):
    r = libc.pycpdf_getMajorVersion(pdf.pdf)
    checkerror()
    return r


def getTitle(pdf):
    r = string_at(libc.pycpdf_getTitle(pdf.pdf)).decode()
    checkerror()
    return r


def getAuthor(pdf):
    r = string_at(libc.pycpdf_getAuthor(pdf.pdf)).decode()
    checkerror()
    return r


def getSubject(pdf):
    r = string_at(libc.pycpdf_getSubject(pdf.pdf)).decode()
    checkerror()
    return r


def getKeywords(pdf):
    r = string_at(libc.pycpdf_getKeywords(pdf.pdf)).decode()
    checkerror()
    return r


def getCreator(pdf):
    r = string_at(libc.pycpdf_getCreator(pdf.pdf)).decode()
    checkerror()
    return r


def getProducer(pdf):
    r = string_at(libc.pycpdf_getProducer(pdf.pdf)).decode()
    checkerror()
    return r


def getCreationDate(pdf):
    r = string_at(libc.pycpdf_getCreationDate(pdf.pdf)).decode()
    checkerror()
    return r


def getModificationDate(pdf):
    r = string_at(libc.pycpdf_getModificationDate(pdf.pdf)).decode()
    checkerror()
    return r


def getTitleXMP(pdf):
    r = string_at(libc.pycpdf_getTitleXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getAuthorXMP(pdf):
    r = string_at(libc.pycpdf_getAuthorXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getSubjectXMP(pdf):
    r = string_at(libc.pycpdf_getSubjectXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getKeywordsXMP(pdf):
    r = string_at(libc.pycpdf_getKeywordsXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getCreatorXMP(pdf):
    r = string_at(libc.pycpdf_getCreatorXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getProducerXMP(pdf):
    r = string_at(libc.pycpdf_getProducerXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getCreationDateXMP(pdf):
    r = string_at(libc.pycpdf_getCreationDateXMP(pdf.pdf)).decode()
    checkerror()
    return r


def getModificationDateXMP(pdf):
    r = string_at(libc.pycpdf_getModificationDateXMP(pdf.pdf)).decode()
    checkerror()
    return r


def setTitle(pdf, s):
    libc.pycpdf_setTitle(pdf.pdf, str.encode(s))
    checkerror()
    return


def setAuthor(pdf, s):
    libc.pycpdf_setAuthor(pdf.pdf, str.encode(s))
    checkerror()
    return


def setSubject(pdf, s):
    libc.pycpdf_setSubject(pdf.pdf, str.encode(s))
    checkerror()
    return


def setKeywords(pdf, s):
    libc.pycpdf_setKeywords(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreator(pdf, s):
    libc.pycpdf_setCreator(pdf.pdf, str.encode(s))
    checkerror()
    return


def setProducer(pdf, s):
    libc.pycpdf_setProducer(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreationDate(pdf, s):
    libc.pycpdf_setCreationDate(pdf.pdf, str.encode(s))
    checkerror()
    return


def setModificationDate(pdf, s):
    libc.pycpdf_setModificationDate(pdf.pdf, str.encode(s))
    checkerror()
    return


def setTitleXMP(pdf, s):
    libc.pycpdf_setTitleXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setAuthorXMP(pdf, s):
    libc.pycpdf_setAuthorXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setSubjectXMP(pdf, s):
    libc.pycpdf_setSubjectXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setKeywordsXMP(pdf, s):
    libc.pycpdf_setKeywordsXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreatorXMP(pdf, s):
    libc.pycpdf_setCreatorXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setProducerXMP(pdf, s):
    libc.pycpdf_setProducerXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setCreationDateXMP(pdf, s):
    libc.pycpdf_setCreationDateXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def setModificationDateXMP(pdf, s):
    libc.pycpdf_setModificationDateXMP(pdf.pdf, str.encode(s))
    checkerror()
    return


def getDateComponents(string):
    year = c_int(0)
    month = c_int(0)
    day = c_int(0)
    hour = c_int(0)
    minute = c_int(0)
    second = c_int(0)
    hour_offset = c_int(0)
    minute_offset = c_int(0)
    libc.pycpdf_getDateComponents(string, byref(year), byref(month), byref(day), byref(
        hour), byref(minute), byref(second), byref(hour_offset), byref(minute_offset))
    checkerror()
    return (year, month, day, hour, minute, second, hour_offset, minute_offset)


def dateStringOfComponents(components):
    year, month, day, hour, minute, second, hour_offset, minute_offset = components
    r = string_at(libc.pycpdf_dateStringOfComponents(
        year, month, day, hour, minute, second, hour_offset, minute_offset)).decode()
    checkerror()
    return r


def getPageRotation(pdf, pagenumber):
    r = libc.pycpdf_getPageRotation(pdf.pdf, pagenumber)
    checkerror()
    return r


def hasBox(pdf, pagenumber, boxname):
    r = libc.pycpdf_hasBox(pdf.pdf, pagenumber, str.encode(boxname))
    checkerror()
    return r


def getMediaBox(pdf, pagenumber):
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getMediaBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getCropBox(pdf, pagenumber):
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getCropBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getTrimBox(pdf, pagenumber):
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getTrimBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getArtBox(pdf, pagenumber):
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getArtBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def getBleedBox(pdf, pagenumber):
    minx = c_double(0.0)
    maxx = c_double(0.0)
    miny = c_double(0.0)
    maxy = c_double(0.0)
    libc.pycpdf_getBleedBox(pdf.pdf, pagenumber, byref(
        minx), byref(maxx), byref(miny), byref(maxy))
    checkerror()
    return (minx.value, maxx.value, miny.value, maxy.value)


def setMediaBox(pdf, r, minx, maxx, miny, maxy):
    libc.pycpdf_setMediaBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def setCropBox(pdf, r, minx, maxx, miny, maxy):
    libc.pycpdf_setCropBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def setTrimBox(pdf, r, minx, maxx, miny, maxy):
    libc.pycpdf_setTrimBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def setArtBox(pdf, r, minx, maxx, miny, maxy):
    libc.pycpdf_setArtBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def setBleedBox(pdf, r, minx, maxx, miny, maxy):
    libc.pycpdf_setBleedBox(pdf.pdf, r, minx, maxx, miny, maxy)
    checkerror()
    return


def markTrapped(pdf):
    libc.pycpdf_markTrapped(pdf.pdf)
    checkerror()
    return


def markUntrapped(pdf):
    libc.pycpdf_markUntrapped(pdf.pdf)
    checkerror()
    return


def markTrappedXMP(pdf):
    libc.pycpdf_markTrappedXMP(pdf.pdf)
    checkerror()
    return


def markUntrappedXMP(pdf):
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
    libc.pycpdf_setPageLayout(pdf.pdf, layout)
    checkerror()
    return


useNone = 0
useOutlines = 1
useThumbs = 2
useOC = 3
useAttachments = 4


def setPageMode(pdf, mode):
    libc.pycpdf_setPageMode(pdf.pdf, mode)
    checkerror()
    return


def hideToolbar(pdf, flag):
    libc.pycpdf_hideToolbar(pdf.pdf, flag)
    checkerror()
    return


def hideMenubar(pdf, flag):
    libc.pycpdf_hideMenubar(pdf.pdf, flag)
    checkerror()
    return


def hideWindowUi(pdf, flag):
    libc.pycpdf_hideWindowUi(pdf.pdf, flag)
    checkerror()
    return


def fitWindow(pdf, flag):
    libc.pycpdf_fitWindow(pdf.pdf, flag)
    checkerror()
    return


def centerWindow(pdf, flag):
    libc.pycpdf_centerWindow(pdf.pdf, flag)
    checkerror()
    return


def displayDocTitle(pdf, flag):
    libc.pycpdf_displayDocTitle(pdf.pdf, flag)
    checkerror()
    return


def openAtPage(pdf, flag, pagenumber):
    libc.pycpdf_openAtPage(pdf.pdf, flag, pagenumber)
    checkerror()
    return


def setMetadataFromFile(pdf, filename):
    libc.pycpdf_setMetadataFromFile(pdf.pdf, str.encode(filename))
    checkerror()
    return


def setMetadataFromByteArray(pdf, data):
    libc.pycpdf_setMetadataFromByteArray(pdf.pdf, data, len(data))
    checkerror()
    return


def getMetadata(pdf):
    length = c_int32()
    data = libc.pycpdf_getMetadata(pdf.pdf, byref(length))
    s = string_at(data)
    libc.pycpdf_getMetadataFree()
    checkerror()
    return s


def removeMetadata(pdf):
    libc.pycpdf_removeMetadata(pdf.pdf)
    checkerror()
    return


def createMetadata(pdf):
    libc.pycpdf_createMetadata(pdf.pdf)
    checkerror()
    return


def setMetadataDate(pdf, date):
    libc.pycpdf_setMetadataDate(pdf.pdf, str.encode(date))
    checkerror()
    return


decimalArabic = 0
uppercaseRoman = 1
lowercaseRoman = 2
uppercaseLetters = 3
lowercaseLetters = 4


def getPageLabels(pdf):
    n = libc.pycpdf_startGetPageLabels(pdf.pdf)
    l = []
    for x in range(n):
        style = libc.pycpdf_getPageLabelStyle(x)
        prefix = string_at(libc.pycpdf_getPageLabelPrefix(x)).decode()
        offset = libc.pycpdf_getPageLabelOffset(x)
        plrange = libc.pycpdf_getPageLabelRange(x)
        l.append((style, prefix, offset, list_of_range(plrange)))
    libc.pycpdf_endGetPageLabels()
    checkerror()
    return l


def addPageLabels(pdf, label, progress):
    style, prefix, offset, plrange = label
    libc.pycpdf_addPageLabels(pdf.pdf, style, str.encode(
        prefix), offset, range_of_list(plrange), progress)
    checkerror()
    return


def removePageLabels(pdf):
    libc.pycpdf_removePageLabels(pdf.pdf)
    checkerror()
    return


def getPageLabelStringForPage(pdf, pagenumber):
    r = string_at(libc.pycpdf_getPageLabelStringForPage(
        pdf.pdf, pagenumber)).decode()
    checkerror()
    return r

# CHAPTER 12. File Attachments


def attachFile(filename, pdf):
    libc.pycpdf_attachFile(str.encode(filename), pdf.pdf)
    checkerror()


def attachFileToPage(filename, pdf, pagenumber):
    libc.pycpdf_attachFileToPage(str.encode(filename), pdf.pdf, pagenumber)
    checkerror()


def attachFileFromMemory(data, filename, pdf):
    libc.pycpdf_attachFileFromMemory(data, len(data), filename, pdf.pdf)
    checkerror()


def attachFileToPageFromMemory(data, filename, pdf, pagenumber):
    libc.pycpdf_attachFileToPageFromMemory(
        data, len(data), filename, pdf.pdf, pagenumber)
    checkerror()


def removeAttachedFiles(pdf):
    libc.pycpdf_removeAttachedFiles(pdf.pdf)
    checkerror()


def getAttachments(pdf):
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
    libc.pycpdf_removeFonts(pdf.pdf)
    checkerror()


def copyFont(pdf, pdf2, r, pagenumber, fontname):
    r = range_of_list(r)
    libc.pycpdf_copyFont(pdf.pdf, pdf2.pdf, r,
                         pagenumber, str.encode(fontname))
    checkerror()

# CHAPTER 15. Miscellaneous


def draft(pdf, r, boxes):
    r = range_of_list(r)
    libc.pycpdf_draft(pdf.pdf, r, boxes)
    checkerror()


def removeAllText(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_removeAllText(pdf.pdf, r)
    checkerror()


def blackText(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_blackText(pdf.pdf, r)
    checkerror()


def blackLines(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_blackLines(pdf.pdf, r)
    checkerror()


def blackFills(pdf, r):
    r = range_of_list(r)
    libc.pycpdf_blackFills(pdf.pdf, r)
    checkerror()


def thinLines(pdf, r, linewidth):
    r = range_of_list(r)
    libc.pycpdf_thinLines(pdf.pdf, r, linewidth)
    checkerror()


def copyId(pdf, pdf2):
    libc.pycpdf_copyId(pdf.pdf, pdf2.pdf)
    checkerror()


def removeId(pdf):
    libc.pycpdf_removeId(pdf.pdf)
    checkerror()


def setVersion(pdf, version):
    libc.pycpdf_setVersion(pdf.pdf, version)
    checkerror()


def removeDictEntry(pdf, key):
    libc.pycpdf_removeDictEntry(pdf.pdf, str.encode(key))
    checkerror()


def removeClipping(pdf, r):
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
