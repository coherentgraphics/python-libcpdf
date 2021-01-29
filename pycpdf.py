from ctypes import *

libc = None

def loadDLL(f):
  global libc
  libc = CDLL(f)
  libc.pycpdf_version.restype = POINTER(c_char)
  libc.pycpdf_lastErrorString.restype = POINTER(c_char)

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

def toFile(pdf, filename, linearize, make_id):
  libc.pycpdf_toFile(pdf, str.encode(filename), False, False)

