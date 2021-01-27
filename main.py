import ctypes
import os

libc = ctypes.CDLL("/home/john/python-libcpdf/libclib1.so")

libc.call_ocaml_startup()

