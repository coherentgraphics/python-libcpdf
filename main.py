from ctypes import *

libc = CDLL("/home/john/python-libcpdf/libclib1.so")

libc.pycpdf_version.restype = POINTER(c_char)

libc.pycpdf_startup()

#FIXME: What is the proper decode here? UTF8?
print('Library version is ' + string_at(libc.pycpdf_version()).decode())

libc.pycpdf_setFast()
libc.pycpdf_setSlow()
