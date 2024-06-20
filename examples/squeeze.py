#Squeeze example
import os
import platform
import sys
sys.path.insert(0,'..')
import pycpdflib

# DLL loading depends on your own platform.
# The following DLL loading code assumes you've run:
#   git clone https://github.com/coherentgraphics/cpdflib-binary
#   git clone https://github.com/johnwhitington/cpdflib-source
#   git clone https://github.com/coherentgraphics/python-libcpdf
#   cd python-libcpdf/examples
dll_root = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "cpdflib-binary"))
if sys.platform.startswith('darwin'):
    if platform.processor().startswith("arm"):
        dll_dir = os.path.join(dll_root, "macosx-arm")
    else:
        dll_dir = os.path.join(dll_root, "macosx")
    pycpdflib.loadDLL(os.path.join(dll_dir, "libpycpdf.so"))
elif sys.platform.startswith('linux'):
    if sys.maxsize > 2**32:
        dll_dir = os.path.join(dll_root, "linux64")
    else:
        dll_dir = os.path.join(dll_root, "linux32")
    pycpdflib.loadDLL(os.path.join(dll_dir, "libpycpdf.so"))
elif os.name == "nt": # win32, cygwin, msys2, mingw, etc.
    if sys.maxsize > 2**32:
        dll_dir = os.path.join(dll_root, "windows64")
    else:
        dll_dir = os.path.join(dll_root, "windows32")
    # pylint: disable=no-member
    os.add_dll_directory(dll_dir) # type: ignore
    pycpdflib.loadDLL("libpycpdf.dll")

#Load file
pdf = pycpdflib.fromFile('../pycpdflibmanual.pdf', '')

#Squeeze it
pycpdflib.squeezeInMemory(pdf)

#Write output. We make sure to use toFileExt, and make object streams.
pycpdflib.toFileExt(pdf, 'squeezed.pdf', False, False, True, True, True)
