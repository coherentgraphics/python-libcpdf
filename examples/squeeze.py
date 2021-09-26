#Squeeze example
import sys
sys.path.insert(0,'..')
import pycpdflib

#DLL loading depends on your own platform. These are the author's settings.
if sys.platform.startswith('darwin'):
    pycpdflib.loadDLL("/Users/john/repos/python-libcpdf/libpycpdf.so")
elif sys.platform.startswith('linux'):
    pycpdflib.loadDLL("../libpycpdf.so")
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    os.add_dll_directory("C:\\\\OCaml64/home/JohnWhitington/python-libcpdf/")
    pycpdflib.loadDLL("libpycpdf.dll")

#Prepare cpdf for use
pycpdflib.startup()

#Load file
pdf = pycpdflib.fromFile('../cpdflibmanual.pdf', '')

#Squeeze it
pycpdflib.squeezeInMemory(pdf)

#Write output. We make sure to use toFileExt, and make object streams.
pycpdflib.toFileExt(pdf, 'squeezed.pdf', False, False, True, True, True)
