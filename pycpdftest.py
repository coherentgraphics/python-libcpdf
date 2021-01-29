from ctypes import *

libc = CDLL("/home/john/python-libcpdf/libclib1.so")

libc.pycpdf_version.restype = POINTER(c_char)
libc.pycpdf_lastErrorString.restype = POINTER(c_char)

#CHAPTER 0. Preliminaries
libc.pycpdf_startup()
print('Library version is ' + string_at(libc.pycpdf_version()).decode())
libc.pycpdf_setFast()
libc.pycpdf_setSlow()
print('LastError is ' + str(libc.pycpdf_lastError()))
print('LastErrorString is ' + string_at(libc.pycpdf_lastErrorString()).decode())
libc.pycpdf_clearError()
libc.pycpdf_onExit()

#CHAPTER 1. Basics
pdf = libc.pycpdf_fromFile(b'cpdfmanual.pdf', b'')
print('pdf = ' + str(pdf))

libc.pycpdf_toFile(pdf, b'out.pdf', False, False)

