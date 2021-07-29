#Squeeze example
import sys
sys.path.insert(0,'..')
import pycpdf

#DLL loading depends on your own platform. These are the author's settings.
if sys.platform.startswith('darwin'):
    pycpdf.loadDLL("/Users/john/repos/python-libcpdf/libpycpdf.so")
elif sys.platform.startswith('linux'):
    pycpdf.loadDLL("../libpycpdf.so")
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    os.add_dll_directory("C:\\\\OCaml64/home/JohnWhitington/python-libcpdf/")
    pycpdf.loadDLL("libpycpdf.dll")

#Prepare cpdf for use
pycpdf.startup()

#Load file
pdf = pycpdf.fromFile('../cpdflibmanual.pdf', '')

#Squeeze it
pycpdf.squeezeInMemory(pdf)

#Write output. We make sure to use toFileExt, and make object streams.
pycpdf.toFileExt(pdf, 'squeezed.pdf', False, False, True, True, True)
