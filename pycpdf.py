from ctypes import *

libc = None

def loadDLL(f):
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
  libc.pycpdf_scaleToFit.argtypes = [c_int, c_int, c_double, c_double, c_double]
  libc.pycpdf_scaleToFitPaper.argtypes = [c_int, c_int, c_int, c_double]
  libc.pycpdf_scaleContents.argtypes = [c_int, c_int, c_int, c_double, c_double, c_double]
  libc.pycpdf_shiftContents.argtypes = [c_int, c_int, c_double, c_double]
  libc.pycpdf_rotateContents.argtypes = [c_int, c_int, c_double]
  libc.pycpdf_crop.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]
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
  libc.pycpdf_setMediaBox.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]
  libc.pycpdf_setCropBox.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]
  libc.pycpdf_setTrimBox.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]
  libc.pycpdf_setArtBox.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]
  libc.pycpdf_setBleedBox.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]
  libc.pycpdf_getBookmarkText.restype = POINTER(c_char)
  libc.pycpdf_addText.argtypes = [c_int, c_int, c_int, POINTER(c_char), c_int, c_double, c_int, c_int, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_int, c_int, c_int, POINTER(c_char), c_double, c_int]
  #libc.pycpdf_addTextSimple.argtypes = [c_int, c_int, POINTER(c_char), c_int, c_int, c_double]
  libc.pycpdf_getMetadata.restype = POINTER(c_uint8)
  libc.pycpdf_getAttachmentData.restype = POINTER(c_uint8)
  libc.pycpdf_startGetImageResolution.argtypes = [c_int, c_double]

#CHAPTER 0. Preliminaries
def startup():
  libc.pycpdf_startup()

def version():
  return string_at(libc.pycpdf_version()).decode()

def setFast():
  libc.pycpdf_setFast()

def setSlow():
  libc.pycpdf_setSlow()

def lastError():
  return libc.pycpdf_lastError()

def lastErrorString():
  return string_at(libc.pycpdf_lastErrorString()).decode()

def clearError():
  libc.pycpdf_clearError()

def onExit():
  libc.pycpdf_onExit()

#CHAPTER 1. Basics
def fromFile(filename, userpw):
  return libc.pycpdf_fromFile(str.encode(filename), str.encode(userpw))

def fromFileLazy(filename, userpw):
  return libc.pycpdf_fromFileLazy(str.encode(filename), str.encode(userpw))

def fromMemory(data, userpw):
  return libc.pycpdf_fromMemory(data, len(data), str.encode(userpw))

def fromMemoryLazy(data, userpw):
  return libc.pycpdf_fromMemoryLazy(data, len(data), str.encode(userpw))

def blankDocument(w, h, pages):
  return libc.pycpdf_blankDocument(w, h, pages)

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
  return libc.pycpdf_blankDocumentPaper(papersize, pages)

def deletePdf(pdf):
  libc.pycpdf_deletePdf(pdf)

def replacePdf(pdf, pdf2):
  libc.pycpdf_replacePdf(pdf, pdf2)

def ptOfCm(i):
  return libc.pycpdf_ptOfCm(i)

def ptOfMm(i):
  return libc.pycpdf_ptOfMm(i)

def ptOfIn(i):
  return libc.pycpdf_ptOfIn(i)

def cmOfPt(i):
  return libc.pycpdf_cmOfPt(i)

def mmOfPt(i):
  return libc.pycpdf_mmOfPt(i)

def inOfPt(i):
  return libc.pycpdf_inOfPt(i)

def enumeratePDFs():
  pdfs = []
  n = libc.pycpdf_startEnumeratePDFs()
  for x in range(n):
    key = libc.pycpdf_enumeratePDFsKey(x)
    info = string_at(libc.pycpdf_enumeratePDFsInfo(x)).decode()
    pdfs.append((key, info))
  libc.pycpdf_endEnumeratePDFs()
  return pdfs

def parsePagespec(pdf, pagespec):
  return libc.pycpdf_parsePagespec(pdf, str.encode(pagespec))

def validatePagespec(pagespec):
  return libc.pycpdf_validatePagespec(str.encode(pagespec))

def stringOfPagespec(pdf, r):
  return string_at(libc.pycpdf_stringOfPagespec(pdf, r)).decode()

def blankRange():
  return libc.pycpdf_blankRange()

def deleteRange(r):
  return libc.pycpdf_deleteRange(r)

def pageRange(f, t):
  return libc.pycpdf_pageRange(f, t)

def all(r):
  return libc.pycpdf_all(r)

def even(r):
  return libc.pycpdf_even(r)

def odd(r):
  return libc.pycpdf_odd(r)

def rangeUnion(a, b):
  return libc.pycpdf_rangeUnion(a, b)

def difference(a, b):
  return libc.pycpdf_difference(a, b)

def removeDuplicates(r):
  return libc.pycpdf_removeDuplicates(r)

def rangeLength(r):
  return libc.pycpdf_rangeLength(r)

def rangeGet(r, n):
  return libc.pycpdf_rangeGet(r, n)

def rangeAdd(r, p):
  return libc.pycpdf_rangeAdd(r, p)

def isInRange(r, p):
  return libc.pycpdf_isInRange(r, p)

def pages(pdf):
  return libc.pycpdf_pages(pdf)

def pagesFast(userpw, filename):
  return libc.pycpdf_pagesFast(str.encode(userpw), str.encode(filename))

def toFile(pdf, filename, linearize, make_id):
  libc.pycpdf_toFile(pdf, str.encode(filename), False, False)

def toFileExt(pdf, filename, linearize, make_id, preserve_objstm, generate_objstm, compress_objstm):
  libc.pycpdf_toFileExt(pdf, str.encode(filename), linearize, make_id, preserve_objstm, generate_objstm, compress_objstm)

def toMemory(pdf, linearize, make_id):
  length = c_int32()
  data = libc.pycpdf_toMemory(pdf, linearize, make_id, byref(length))
  s = string_at(data)
  libc.pycpdf_toMemoryFree()
  return s

def isEncrypted(pdf):
  libc.pycpdf_isEncrypted(pdf)

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
  libc.pycpdf_toFileEncrypted(pdf, method, c_perms, len(permissions), str.encode(ownerpw),
                            str.encode(userpw), linearize, makeid, str.encode(filename))

def toFileEncryptedExt(pdf, method, permissions, ownerpw, userpw, linearize, makeid,
                       preserve_objstm, generate_objstm, compress_objstm, filename):
  c_perms = (c_uint8 * len(permissions))(*permissions)
  libc.pycpdf_toFileEncryptedExt(pdf, method, c_perms, len(permissions), str.encode(ownerpw),
                                 str.encode(userpw), linearize, makeid, preserve_objstm,
                                 generate_objstm, compress_objstm, str.encode(filename))

def decryptPdf(pdf, userpw):
  libc.pycpdf_decryptPdf(pdf, str.encode(userpw))

def decryptPdfOwner(pdf, ownerpw):
  libc.pycpdf_decryptPdfOwner(pdf, str.encode(ownerpw))

def hasPermission(pdf, perm):
  return libc.pycpdf_hasPermission(pdf, perm)

def encryptionKind(pdf):
  return libc.pycpdf_encryptionKind(pdf)

# CHAPTER 2. Merging and Splitting
def mergeSimple(pdfs):
  c_pdfs = (c_int * len(pdfs))(*pdfs)
  return libc.pycpdf_mergeSimple(c_pdfs, len(pdfs))

def merge(pdfs, retain_numbering, remove_duplicate_fonts):
  c_pdfs = (c_int * len(pdfs))(*pdfs)
  return libc.pycpdf_merge(c_pdfs, len(pdfs), retain_numbering, remove_duplicate_fonts)

def mergeSame(pdfs, retain_numbering, remove_duplicate_fonts, ranges):
  c_pdfs = (c_int * len(pdfs))(*pdfs)
  c_ranges = (c_int * len(ranges))(*ranges)
  return libc.pycpdf_mergeSame(c_pdfs, len(pdfs), retain_numbering, remove_duplicate_fonts, c_ranges) 

def selectPages(pdf, r):
  return libc.pycpdf_selectPages(pdf, r)

# CHAPTER 3. Pages
def scalePages(pdf, r, sx, sy):
  libc.pycpdf_scalePages(pdf, r, sx, sy)

def scaleToFit(pdf, r, sx, sy, scale_to_fit_scale):
  libc.pycpdf_scaleToFit(pdf, r, sx, sy, scale_to_fit_scale)

def scaleToFitPaper(pdf, r, papersize, scale_to_fit_scale):
  libc.pycpdf_scaleToFitPaper(pdf, r, papersize, scale_to_fit_scale)

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
  if p[0] == diagonal: return (p[0], 0.0, 0.0)
  if p[0] == reverseDiagonal: return (p[0], 0.0, 0.0)
  if p[0] == top: return (p[0], p[1], 0.0)
  if p[0] == topLeft: return (p[0], p[1], 0.0)
  if p[0] == topRight: return (p[0], p[1], 0.0)
  if p[0] == left: return (p[0], p[1], 0.0)
  if p[0] == bottomLeft: return (p[0], p[1], 0.0)
  if p[0] == bottomRight: return (p[0], p[1], 0.0)
  if p[0] == right: return (p[0], p[1], 0.0)
  if p[0] == posCentre: return (p[0], p[1], p[2])
  if p[0] == posLeft: return (p[0], p[1], p[2])
  if p[0] == posRight: return (p[0], p[1], p[2])

def scaleContents(pdf, r, p, scale):
  a, b, c = tripleOfPosition(p); 
  libc.pycpdf_scaleContents(pdf, r, a, b, c, scale)

def shiftContents(pdf, r, dx, dy):
  libc.pycpdf_shiftContents(pdf, r, dx, dy)

def rotate(pdf, r, rotation):
  libc.pycpdf_rotate(pdf, r, rotation)

def rotateBy(pdf, r, rotation):
  libc.pycpdf_rotateBy(pdf, r, rotation)

def rotateContents(pdf, r, rotation):
  libc.pycpdf_rotateContents(pdf, r, rotation)

def upright(pdf, r):
  libc.pycpdf_upright(pdf, r)

def hFlip(pdf, r):
  libc.pycpdf_hFlip(pdf, r)

def vFlip(pdf, r):
  libc.pycpdf_vFlip(pdf, r)

def crop(pdf, r, x, y, w, h):
  libc.pycpdf_crop(pdf, r, x, y, w, h)

def removeCrop(pdf, r):
  libc.pycpdf_removeCrop(pdf, r)

def removeTrim(pdf, r):
  libc.pycpdf_removeTrim(pdf, r)

def removeArt(pdf, r):
  libc.pycpdf_removeArt(pdf, r)

def removeBleed(pdf, r):
  libc.pycpdf_removeBleed(pdf, r)

def trimMarks(pdf, r):
  libc.pycpdf_trimMarks(pdf, r)

def showBoxes(pdf, r):
  libc.pycpdf_showBoxes(pdf, r)

def hardBox(pdf, r, boxname):
  libc.pycpdf_hardBox(pdf, r, str.encode(boxname))

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression

def compress(pdf):
  libc.pycpdf_compress(pdf)

def decompress(pdf):
  libc.pycpdf_decompress(pdf)

def squeezeInMemory(pdf):
  libc.pycpdf_squeezeInMemory(pdf)


# CHAPTER 6. Bookmarks

# Format: list of tuples. (level : int, page : int, text : string, openstatus : int/bool) 

def getBookmarks(pdf):
  l = []
  libc.pycpdf_startGetBookmarkInfo(pdf);
  n = libc.pycpdf_numberBookmarks();
  for x in range(n):
      level = libc.pycpdf_getBookmarkLevel(x)
      page = libc.pycpdf_getBookmarkPage(pdf, x)
      text = string_at(libc.pycpdf_getBookmarkText(x)).decode()
      openStatus = libc.pycpdf_getBookmarkOpenStatus(x)
      l.append((level, page, text, openStatus))
  libc.pycpdf_endGetBookmarkInfo(pdf);
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
  libc.pycpdf_endSetBookmarkInfo(pdf)

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps

def stampOn(pdf, pdf2, r):
  libc.pycpdf_stampOn(pdf, pdf2, r)

def stampUnder(pdf, pdf2, r):
  libc.pycpdf_stampUnder(pdf, pdf2, r)

def stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, pos, relative_to_cropbox):
  libc.pycpdf_stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, pos, relative_to_cropbox)

def combinePages(pdf, pdf2):
  libc.pycpdf_combinePages(pdf, pdf)

leftJustify = 0
centreJustify = 1
rightJustify = 2

def addText(metrics, pdf, r, text, pos, line_spacing, bates, font, size, red, green, blue, underneath, relative_to_cropbox, outline, opacity, justification, midline, topline, filename, line_width, embed_fonts):
  libc.pycpdf_addText(metrics, pdf, r, str.encode(text), pos, line_spacing, bates, font, size, red, green, blue, underneath, relative_to_cropbox, outline, opacity, justification, midline, topline, str.encode(filename), line_width, embed_fonts)

def addTextSimple(pdf, r, text, position, font, size):
  libc.pycpdf_addTextSimple(pdf, r, str.encode(text), position, font, size)

def removeText(pdf, r):
  libc.pycpdf_removeText(pdf, r)

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
  libc.pycpdf_textWidth(font, str.encode(string))

# CHAPTER 9. Mulitpage facilities

def twoUp(pdf):
  libc.pycpdf_twoUp(pdf)

def twoUpStack(pdf):
  libc.pycpdf_twoUpStack(pdf)

def padBefore(pdf, r):
  libc.pycpdf_padBefore(pdf, r)

def padAfter(pdf, r):
  libc.pycpdf_padAfter(pdf, r)

def padEvery(pdf, r):
  libc.pycpdf_padEvery(pdf, r)

def padMultiple(pdf, n):
  libc.pycpdf_padMultiple(pdf, n)

def padMultipleBefore(pdf, n):
  libc.pycpdf_padMultipleBefore(pdf, n)


# CHAPTER 11. Document Information and Metadata
def isLinearized(filename):
  return libc.pycpdf_isLinearized(str.encode(filename))

def getVersion(pdf):
  return libc.pycpdf_getVersion(pdf)

def getMajorVersion(pdf):
  return libc.pycpdf_getMajorVersion(pdf)

def getTitle(pdf):
  return string_at(libc.pycpdf_getTitle(pdf)).decode()

def getAuthor(pdf):
  return string_at(libc.pycpdf_getAuthor(pdf)).decode()

def getSubject(pdf):
  return string_at(libc.pycpdf_getSubject(pdf)).decode()

def getKeywords(pdf):
  return string_at(libc.pycpdf_getKeywords(pdf)).decode()

def getCreator(pdf):
  return string_at(libc.pycpdf_getCreator(pdf)).decode()

def getProducer(pdf):
  return string_at(libc.pycpdf_getProducer(pdf)).decode()

def getCreationDate(pdf):
  return string_at(libc.pycpdf_getCreationDate(pdf)).decode()

def getModificationDate(pdf):
  return string_at(libc.pycpdf_getModificationDate(pdf)).decode()

def getTitleXMP(pdf):
  return string_at(libc.pycpdf_getTitleXMP(pdf)).decode()

def getAuthorXMP(pdf):
  return string_at(libc.pycpdf_getAuthorXMP(pdf)).decode()

def getSubjectXMP(pdf):
  return string_at(libc.pycpdf_getSubjectXMP(pdf)).decode()

def getKeywordsXMP(pdf):
  return string_at(libc.pycpdf_getKeywordsXMP(pdf)).decode()

def getCreatorXMP(pdf):
  return string_at(libc.pycpdf_getCreatorXMP(pdf)).decode()

def getProducerXMP(pdf):
  return string_at(libc.pycpdf_getProducerXMP(pdf)).decode()

def getCreationDateXMP(pdf):
  return string_at(libc.pycpdf_getCreationDateXMP(pdf)).decode()

def getModificationDateXMP(pdf):
  return string_at(libc.pycpdf_getModificationDateXMP(pdf)).decode()

def setTitle(pdf, s):
  libc.pycpdf_setTitle(pdf, str.encode(s))
  return

def setAuthor(pdf, s):
  libc.pycpdf_setAuthor(pdf, str.encode(s))
  return

def setSubject(pdf, s):
  libc.pycpdf_setSubject(pdf, str.encode(s))
  return

def setKeywords(pdf, s):
  libc.pycpdf_setKeywords(pdf, str.encode(s))
  return

def setCreator(pdf, s):
  libc.pycpdf_setCreator(pdf, str.encode(s))
  return

def setProducer(pdf, s):
  libc.pycpdf_setProducer(pdf, str.encode(s))
  return

def setCreationDate(pdf, s):
  libc.pycpdf_setCreationDate(pdf, str.encode(s))
  return

def setModificationDate(pdf, s):
  libc.pycpdf_setModificationDate(pdf, str.encode(s))
  return

def setTitleXMP(pdf, s):
  libc.pycpdf_setTitleXMP(pdf, str.encode(s))
  return

def setAuthorXMP(pdf, s):
  libc.pycpdf_setAuthorXMP(pdf, str.encode(s))
  return

def setSubjectXMP(pdf, s):
  libc.pycpdf_setSubjectXMP(pdf, str.encode(s))
  return

def setKeywordsXMP(pdf, s):
  libc.pycpdf_setKeywordsXMP(pdf, str.encode(s))
  return

def setCreatorXMP(pdf, s):
  libc.pycpdf_setCreatorXMP(pdf, str.encode(s))
  return

def setProducerXMP(pdf, s):
  libc.pycpdf_setProducerXMP(pdf, str.encode(s))
  return

def setCreationDateXMP(pdf, s):
  libc.pycpdf_setCreationDateXMP(pdf, str.encode(s))
  return

def setModificationDateXMP(pdf, s):
  libc.pycpdf_setModificationDateXMP(pdf, str.encode(s))
  return

def getPageRotation(pdf, pagenumber):
  return libc.pycpdf_getPageRotation(pdf, pagenumber)

def hasBox(pdf, pagenumber, boxname):
  return libc.pycpdf_hasBox(pdf, pagenumber, str.encode(boxname))

def getMediaBox(pdf, pagenumber):
  minx = c_double(0.0)
  maxx = c_double(0.0)
  miny = c_double(0.0)
  maxy = c_double(0.0)
  libc.pycpdf_getMediaBox(pdf, pagenumber, byref(minx), byref(maxx), byref(miny), byref(maxy))
  return (minx.value, maxx.value, miny.value, maxy.value)

def getCropBox(pdf, pagenumber):
  minx = c_double(0.0)
  maxx = c_double(0.0)
  miny = c_double(0.0)
  maxy = c_double(0.0)
  libc.pycpdf_getCropBox(pdf, pagenumber, byref(minx), byref(maxx), byref(miny), byref(maxy))
  return (minx.value, maxx.value, miny.value, maxy.value)

def getTrimBox(pdf, pagenumber):
  minx = c_double(0.0)
  maxx = c_double(0.0)
  miny = c_double(0.0)
  maxy = c_double(0.0)
  libc.pycpdf_getTrimBox(pdf, pagenumber, byref(minx), byref(maxx), byref(miny), byref(maxy))
  return (minx.value, maxx.value, miny.value, maxy.value)

def getArtBox(pdf, pagenumber):
  minx = c_double(0.0)
  maxx = c_double(0.0)
  miny = c_double(0.0)
  maxy = c_double(0.0)
  libc.pycpdf_getArtBox(pdf, pagenumber, byref(minx), byref(maxx), byref(miny), byref(maxy))
  return (minx.value, maxx.value, miny.value, maxy.value)

def getBleedBox(pdf, pagenumber):
  minx = c_double(0.0)
  maxx = c_double(0.0)
  miny = c_double(0.0)
  maxy = c_double(0.0)
  libc.pycpdf_getBleedBox(pdf, pagenumber, byref(minx), byref(maxx), byref(miny), byref(maxy))
  return (minx.value, maxx.value, miny.value, maxy.value)

def setMediaBox(pdf, r, minx, maxx, miny, maxy):
  libc.pycpdf_setMediaBox(pdf, r, minx, maxx, miny, maxy)
  return

def setCropBox(pdf, r, minx, maxx, miny, maxy):
  libc.pycpdf_setCropBox(pdf, r, minx, maxx, miny, maxy)
  return

def setTrimBox(pdf, r, minx, maxx, miny, maxy):
  libc.pycpdf_setTrimBox(pdf, r, minx, maxx, miny, maxy)
  return

def setArtBox(pdf, r, minx, maxx, miny, maxy):
  libc.pycpdf_setArtBox(pdf, r, minx, maxx, miny, maxy)
  return

def setBleedBox(pdf, r, minx, maxx, miny, maxy):
  libc.pycpdf_setBleedBox(pdf, r, minx, maxx, miny, maxy)
  return

def markTrapped(pdf):
  libc.pycpdf_markTrapped(pdf)
  return

def markUntrapped(pdf):
  libc.pycpdf_markUntrapped(pdf)
  return

def markTrappedXMP(pdf):
  libc.pycpdf_markTrappedXMP(pdf)
  return

def markUntrappedXMP(pdf):
  libc.pycpdf_markUntrappedXMP(pdf)
  return

singlePage = 0
oneColumn = 1
twoColumnLeft = 2
twoColumnRight = 3
twoPageLeft = 4
twoPageRight = 5

def setPageLayout(pdf, layout):
  libc.pycpdf_setPageLayout(pdf, layout)
  return

useNone = 0
useOutlines = 1
useThumbs = 2
useOC = 3
useAttachments = 4

def setPageMode(pdf, mode):
  libc.pycpdf_setPageMode(pdf, mode)
  return

def hideToolbar(pdf, flag):
  libc.pycpdf_hideToolbar(pdf, flag)
  return

def hideMenubar(pdf, flag):
  libc.pycpdf_hideMenubar(pdf, flag)
  return

def hideWindowUi(pdf, flag):
  libc.pycpdf_hideWindowUi(pdf, flag)
  return

def fitWindow(pdf, flag):
  libc.pycpdf_fitWindow(pdf, flag)
  return

def centerWindow(pdf, flag):
  libc.pycpdf_centerWindow(pdf, flag)
  return

def displayDocTitle(pdf, flag):
  libc.pycpdf_displayDocTitle(pdf, flag)
  return

def openAtPage(pdf, flag, pagenumber):
  libc.pycpdf_openAtPage(pdf, flag, pagenumber)
  return

def setMetadataFromFile(pdf, filename):
  libc.pycpdf_setMetadataFromFile(pdf, str.encode(filename))
  return

def setMetadataFromByteArray(pdf, data):
  libc.pycpdf_setMetadataFromByteArray(pdf, data, len(data))
  return

def getMetadata(pdf):
  length = c_int32()
  data = libc.pycpdf_getMetadata(pdf, byref(length))
  s = string_at(data)
  libc.pycpdf_getMetadataFree()
  return s

def removeMetadata(pdf):
  libc.pycpdf_removeMetadata(pdf)
  return

def createMetadata(pdf):
  libc.pycpdf_createMetadata(pdf)
  return

def setMetadataDate(pdf, date):
  libc.pycpdf_setMetadataDate(pdf, str.encode(date))
  return

# CHAPTER 12. File Attachments

def attachFile(filename, pdf):
  libc.pycpdf_attachFile(str.encode(filename), pdf)

def attachFileToPage(filename, pdf, pagenumber):
  libc.pycpdf_attachFileToPage(str.encode(filename), pdf, pagenumber)

def attachFileFromMemory(data, filename, pdf):
  libc.pycpdf_attachFileFromMemory(data, len(data), filename, pdf)

def attachFileToPageFromMemory(data, filename, pdf, pagenumber):
  libc.pycpdf_attachFileToPageFromMemory(data, len(data), filename, pdf, pagenumber)

def removeAttachedFiles(pdf):
  libc.pycpdf_removeAttachedFiles(pdf)

def getAttachments(pdf):
  libc.pycpdf_startGetAttachments(pdf)
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


# CHAPTER 13. Images
def getImageResolution(pdf, min_required_resolution):
  n = libc.pycpdf_startGetImageResolution(pdf, min_required_resolution)
  l = []
  for x in range(n):
    pagenumber = libc.pycpdf_getImageResolutionPageNumber(x)
    imagename = string_at(libc.pycpdf_getImageResolutionImageName(x)).decode()
    xp = libc.pycpdf_getImageResolutionXPixels(x)
    yp = libc.pycpdf_getImageResolutionYPixels(x)
    xr = libc.pycpdf_getImageResolutionXRes(x)
    yr = libc.pycpdf_getImageResolutionYRes(x)
    l.append((pagenumber, imagename, xp, yp, xr, yr))
  libc.pycpdf_endGetImageResolution()
  return l

# CHAPTER 14. Fonts
def getFontInfo(pdf):
  libc.pycpdf_startGetFontInfo(pdf)
  n = libc.pycpdf_numberFonts()
  print("fonts:", n)
  l = []
  for x in range(n):
      pagenumber = libc.pycpdf_getFontPage(x)
      fontname = string_at(libc.pycpdf_getFontName(x)).decode()
      #fonttype = string_at(libc.pycpdf_getFontType(x)).decode()
      #fontencoding = string_at(libc.pycpdf_getFontEncoding(x)).decode()
      l.append((pagenumber))
  libc.pycpdf_endGetFontInfo(pdf)
  return l

def removeFonts(pdf):
  libc.pycpdf_removeFonts(pdf)

def copyFont(pdf, pdf2, r, pagenumber, fontname):
  libc.pycpdf_copyFont(pdf, pdf2, r, pagenumber, str.encode(fontname))

# CHAPTER 15. Miscellaneous
def draft(pdf, r, boxes):
  libc.pycpdf_draft(pdf, r, boxes)

def removeAllText(pdf, r):
  libc.pycpdf_removeAllText(pdf, r)

def blackText(pdf, r):
  libc.pycpdf_blackText(pdf, r)

def blackLines(pdf, r):
  libc.pycpdf_blackLines(pdf, r)

def blackFills(pdf, r):
  libc.pycpdf_blackFills(pdf, r)

def thinLines(pdf, r, linewidth):
  libc.pycpdf_thinLines(pdf, r, linewidth)

def copyId(pdf, pdf2):
  libc.pycpdf_copyId(pdf, pdf2)

def removeId(pdf):
  libc.pycpdf_removeId(pdf)

def setVersion(pdf, version):
  libc.pycpdf_setVersion(pdf, version)

def removeDictEntry(pdf, key):
  libc.pycpdf_removeDictEntry(pdf, str.encode(key))

def removeClipping(pdf, r):
  libc.pycpdf_removeClipping(pdf, r)

# CHAPTER UNDOC (To come in v2.4)

def addContent(content, before, pdf, r):
  libc.pycpdf_addContent(str.encode(content), before, pdf, r)

def outputJSON(filename, parse_content, no_stream_data, pdf):
  libc.pycpdf_outputJSON(str.encode(filename), parse_content, no_stream_data, pdf)

def OCGCoalesce(pdf):
  libc.pycpdf_OCGCoalesce(pdf)

def OCGRename(pdf, n_from, n_to):
  libc.pycpdf_OCGRename(pdf, str.encode(n_from), str.encode(n_to))

def OCGOrderAll(pdf):
  libc.pycpdf_OCGOrderAll(pdf)

def stampAsXObject(pdf, r, stamp_pdf):
  string_at(libc.pycpdf_stampAsXObject(pdf, r, stamp_pdf)).decode()

def setDemo(v):
  libc.pycpdf_setDemo(v)

