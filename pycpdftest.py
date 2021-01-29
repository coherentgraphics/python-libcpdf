import pycpdf

pycpdf.loadDLL("/home/john/python-libcpdf/libpycpdf.so")
#CHAPTER 0. Preliminaries
pycpdf.startup()
print('Library version is ' + pycpdf.version())
pycpdf.setFast()
pycpdf.setSlow()
print('LastError is ' + str(pycpdf.lastError()))
print('LastErrorString is ' + pycpdf.lastErrorString())
pycpdf.clearError()
pycpdf.onExit()

#CHAPTER 1. Basics
pdf = pycpdf.fromFile('cpdfmanual.pdf', '')
print('pdf = ' + str(pdf))

pycpdf.toFile(pdf, 'out.pdf', False, False)
