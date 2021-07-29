#Merge example
import sys
sys.path.insert(0,'..')
import pycpdf

# DLL loading depends on your own platform. These are the author's settings.
if sys.platform.startswith('darwin'):
    pycpdf.loadDLL("/Users/john/repos/python-libcpdf/libpycpdf.so")
elif sys.platform.startswith('linux'):
    pycpdf.loadDLL("../libpycpdf.so")
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    os.add_dll_directory("C:\\\\OCaml64/home/JohnWhitington/python-libcpdf/")
    pycpdf.loadDLL("libpycpdf.dll")

pycpdf.startup()

#We will take the input hello.pdf and repeat it three times
mergepdf = pycpdf.fromFile('../hello.pdf', '')

#The list of PDFs to merge
pdfs = [mergepdf, mergepdf, mergepdf]

#Merge them
merged = pycpdf.mergeSimple(pdfs)

#Write output
pycpdf.toFile(merged, 'merged.pdf', False, False)
