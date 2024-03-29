#Merge example
import sys
sys.path.insert(0,'..')
import pycpdflib

# DLL loading depends on your own platform. These are the author's settings.
if sys.platform.startswith('darwin'):
    pycpdflib.loadDLL("/Users/john/repos/python-libcpdf/libpycpdf.so")
elif sys.platform.startswith('linux'):
    pycpdflib.loadDLL("../libpycpdf.so")
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    os.add_dll_directory("C:\\\\OCaml64/home/JohnWhitington/python-libcpdf/")
    pycpdflib.loadDLL("libpycpdf.dll")

#We will take the input hello.pdf and repeat it three times
mergepdf = pycpdflib.fromFile('../hello.pdf', '')

#The list of PDFs to merge
pdfs = [mergepdf, mergepdf, mergepdf]

#Merge them
merged = pycpdflib.mergeSimple(pdfs)

#Write output
pycpdflib.toFile(merged, 'merged.pdf', False, False)
