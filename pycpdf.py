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

