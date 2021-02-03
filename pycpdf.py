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
  print(f'toMemory returned {length} bytes')
  outdata = ...
  libc.pycpdf_toMemoryFree();
  return outdata
