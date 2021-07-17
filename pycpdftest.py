import pycpdf
import sys
import os
import traceback

# DLL loading depends on your own platform. These are the author's settings.
if sys.platform.startswith('darwin'):
    pycpdf.loadDLL("/Users/john/repos/python-libcpdf/libpycpdf.so")
elif sys.platform.startswith('linux'):
    pycpdf.loadDLL("libpycpdf.so")
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    os.add_dll_directory("C:\\\\OCaml64/home/JohnWhitington/python-libcpdf/")
    pycpdf.loadDLL("libpycpdf.dll")


def prerr():
    print("*** EXCEPTION RAISED")
    print(f'({pycpdf.lastError()} | {pycpdf.lastErrorString()})')
    print(traceback.format_exc())
    pycpdf.clearError()


def fatal_prerr():
    prerr()
    print('Fatal error; exiting')
    sys.exit(1)


# CHAPTER 0. Preliminaries
print('***** CHAPTER 0. Preliminaries')
print('---cpdf_startup()')
try:
    pycpdf.startup()
except:
    prerr()
print('---cpdf_version()')
try:
    print('version = ' + pycpdf.version())
except:
    prerr()
print('---cpdf_setFast()')
try:
    pycpdf.setFast()
except:
    prerr()
print('---cpdf_setSlow()')
try:
    pycpdf.setSlow()
except:
    prerr()
print('---cpdf_clearError()')
try:
    pycpdf.clearError()
except:
    prerr()
print('---cpdf_onExit()')
try:
    pycpdf.onExit()
except:
    prerr()

# CHAPTER 1. Basics
print('***** CHAPTER 1. Basics')
print('---cpdf_fromFile()')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
print('---cpdf_fromFileLazy')
try:
    pdf2 = pycpdf.fromFileLazy('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
fh = open('cpdflibmanual.pdf', mode='rb')
data = fh.read()
print('---cpdf_fromMemory')
try:
    pdf3 = pycpdf.fromMemory(data, '')
except:
    fatal_prerr()
try:
    pycpdf.toFile(pdf3, 'testoutputs/01fromMemory.pdf', False, False)
except:
    prerr()
print('---cpdf_fromMemoryLazy')
try:
    pdf4 = pycpdf.fromMemoryLazy(data, '')
except:
    fatal_prerr()
try:
    pycpdf.toFile(pdf4, 'testoutputs/01fromMemoryLazy.pdf', False, False)
except:
    prerr()
print('---cpdf_blankDocument')
try:
    pdf5 = pycpdf.blankDocument(100.0, 200.0, 20)
except:
    fatal_prerr()
print('---cpdf_toFile')
try:
    pycpdf.toFile(pdf5, 'testoutputs/01blank.pdf', False, False)
except:
    prerr()
print('---cpdf_blankDocumentPaper')
try:
    pdf6 = pycpdf.blankDocumentPaper(pycpdf.a4portrait, 10)
except:
    fatal_prerr()
try:
    pycpdf.toFile(pdf6, 'testoutputs/01blanka4.pdf', False, False)
except:
    prerr()
print('---cpdf_enumeratePDFs')
try:
    pdfs = pycpdf.enumeratePDFs()
except:
    fatal_prerr()
for k, i in pdfs:
    print(k, i)
print('---cpdf_ptOfCm')
try:
    print(pycpdf.ptOfCm(1.0))
except:
    prerr()
print('---cpdf_ptOfMm')
try:
    print(pycpdf.ptOfMm(1.0))
except:
    prerr()
print('---cpdf_ptOfIn')
try:
    print(pycpdf.ptOfIn(1.0))
except:
    prerr()
print('---cpdf_cmOfPt')
try:
    print(pycpdf.cmOfPt(1.0))
except:
    prerr()
print('---cpdf_ptOfCm')
try:
    print(pycpdf.mmOfPt(1.0))
except:
    prerr()
print('---cpdf_ptOfCm')
try:
    print(pycpdf.inOfPt(1.0))
except:
    prerr()
print('---cpdf_parsePagespec')
try:
    r = pycpdf.parsePagespec(pdf4, "1-3,end")
except:
    fatal_prerr()
print('---cpdf_valiadatePagespec')
try:
    valid = pycpdf.validatePagespec("1-4,5,6")
except:
    fatal_prerr()
print('---cpdf_all')
try:
    allpdf4 = pycpdf.all(pdf4)
except:
    fatal_prerr()
print(allpdf4)
print('---cpdf_stringOfPagespec')
try:
    pagespecstr = pycpdf.stringOfPagespec(pdf4, allpdf4)
except:
    fatal_prerr()
print(pagespecstr)
print('---cpdf_blankRange')
try:
    blankrange = pycpdf.blankRange()
except:
    fatal_prerr()
print('---cpdf_pageRange')
try:
    fromto = pycpdf.pageRange(3, 7)
except:
    fatal_prerr()
print('---cpdf_all')
try:
    rall = pycpdf.all(pdf4)
except:
    fatal_prerr()
print("all", rall)
print('---cpdf_even')
try:
    even = pycpdf.even(rall)
except:
    fatal_prerr()
print('---cpdf_odd')
try:
    odd = pycpdf.odd(rall)
except:
    fatal_prerr()
print('---cpdf_rangeUnion')
try:
    union = pycpdf.rangeUnion(even, odd)
except:
    fatal_prerr()
print('---cpdf_difference')
try:
    difference = pycpdf.difference(even, odd)
except:
    fatal_prerr()
print('---cpdf_removeDuplicates')
try:
    nodeps = pycpdf.removeDuplicates(rall)
except:
    fatal_prerr()
print('---cpdf_rangeLength')
try:
    rangel = pycpdf.rangeLength(union)
except:
    fatal_prerr()
print('---cpdf_rangeGet')
try:
    got = pycpdf.rangeGet(odd, 1)
except:
    fatal_prerr()
print('---cpdf_rangeAdd')
try:
    added = pycpdf.rangeAdd(odd, 9)
except:
    fatal_prerr()
print('---cpdf_isInRange')
try:
    inrange = pycpdf.isInRange(odd, 1)
except:
    fatal_prerr()
print('---cpdf_pages')
try:
    pages = pycpdf.pages(pdf5)
except:
    fatal_prerr()
print('---cpdf_pagesFast')
try:
    pagesf = pycpdf.pagesFast('', 'testinputs/cpdfmanual.pdf')
except:
    fatal_prerr()
print('---cpdf_toFile')
try:
    pycpdf.toFile(pdf4, 'testoutputs/01tofile.pdf', False, False)
except:
    prerr()
print('---cpdf_toFileExt')
try:
    pycpdf.toFileExt(pdf4, 'testoutputs/01tofileext.pdf',
                     False, False, False, False, False)
except:
    prerr()
print('---cpdf_toMemory')
try:
    tomembytes = pycpdf.toMemory(pdf5, False, False)
except:
    prerr()
print('---cpdf_isEncrypted')
try:
    isenc = pycpdf.isEncrypted(pdf5)
except:
    fatal_prerr()
print('---cpdf_toFileEncrypted')
try:
    pdf5 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    prerr()
try:
    pycpdf.toFileEncrypted(pdf5, pycpdf.pdf40bit, [
                           pycpdf.noEdit], 'owner', 'user', False, False, 'testoutputs/01encrypted.pdf')
except:
    prerr()
print('---cpdf_toFileEncryptedExt')
try:
    pycpdf.toFileEncryptedExt(pdf5, pycpdf.pdf40bit, [
                              pycpdf.noEdit], 'owner', 'user', False, False, False, False, False, 'testoutputs/01encryptedext.pdf')
except:
    prerr()
try:
    encpdf = pycpdf.fromFile('testoutputs/01encrypted.pdf', 'user')
except:
    fatal_prerr()
print('---cpdf_decryptPdf')
try:
    decrypted = pycpdf.decryptPdf(encpdf, 'user')
except:
    fatal_prerr()
try:
    encpdf2 = pycpdf.fromFile('testoutputs/01encrypted.pdf', 'user')
except:
    fatal_prerr()
print('---cpdf_decryptPdfOwner')
try:
    owner = pycpdf.decryptPdfOwner(encpdf2, 'owner')
except:
    fatal_prerr()
print('---cpdf_hasPermission')
try:
    hasperm = pycpdf.hasPermission(encpdf2, pycpdf.noEdit)
except:
    fatal_prerr()
print('---cpdf_encryptionKind')
try:
    encmethod = pycpdf.encryptionKind(encpdf2)
except:
    fatal_prerr()

# CHAPTER 2. Merging and Splitting
print('***** CHAPTER 2. Merging and Splitting')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pdf2 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
print('---cpdf_mergeSimple')
print(pdf, pdf2)
try:
    merged = pycpdf.mergeSimple([pdf, pdf, pdf])
except:
    fatal_prerr()
try:
    pycpdf.toFile(merged, 'testoutputs/02merged.pdf', False, False)
except:
    prerr()
print('---cpdf_merge')
try:
    merged2 = pycpdf.merge([pdf, pdf2], True, False)
except:
    fatal_prerr()
try:
    pycpdf.toFile(merged2, 'testoutputs/02merged2.pdf', False, False)
except:
    prerr()
print('---cpdf_mergeSame')
try:
    same = pycpdf.mergeSame([pdf, pdf2, pdf], True, False, [pycpdf.even(
        pycpdf.all(pdf)), pycpdf.all(pdf2), pycpdf.odd(pycpdf.all(pdf))])
except:
    fatal_prerr()
try:
    pycpdf.toFile(same, 'testoutputs/02merged3.pdf', False, False)
except:
    prerr()
print('---cpdf_selectPages')
try:
    selected = pycpdf.selectPages(pdf, pycpdf.even(pycpdf.all(pdf)))
except:
    fatal_prerr()
try:
    pycpdf.toFile(selected, 'testoutputs/02selected.pdf', False, False)
except:
    prerr()

# CHAPTER 3. Pages
print('***** CHAPTER 3. Pages')
try:
    pagespdf1 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf2 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf3 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf4 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf5 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf6 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf7 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf8 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf9 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf10 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf11 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf12 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf13 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf14 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf15 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf16 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf17 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf18 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    pagespdf19 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    r = pycpdf.all(pagespdf1)
except:
    fatal_prerr()
print('---cpdf_scalePages')
try:
    pycpdf.scalePages(pagespdf1, r, 1.5, 1.8)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf1, 'testoutputs/03scalepages.pdf', False, False)
except:
    prerr()
print('---cpdf_scaleToFit')
try:
    pycpdf.scaleToFit(pagespdf2, r, 1.5, 1.8, 0.9)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf2, 'testoutputs/03scaletofit.pdf', False, False)
except:
    prerr()
print('---cpdf_scaleToFitPaper')
try:
    pycpdf.scaleToFitPaper(pagespdf3, r, pycpdf.a4portrait, 0.8)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf3, 'testoutputs/03scaletofitpaper.pdf', False, False)
except:
    prerr()
print('---cpdf_scaleContents')
try:
    pycpdf.scaleContents(pagespdf4, r, (pycpdf.topLeft, 20, 20), 2.0)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf4, 'testoutputs/03scalecontents.pdf', False, False)
except:
    prerr()
print('---cpdf_shiftContents')
try:
    pycpdf.shiftContents(pagespdf5, r, 1.5, 1.25)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf5, 'testoutputs/03shiftcontents.pdf', False, False)
except:
    prerr()
print('---cpdf_rotate')
try:
    pycpdf.rotate(pagespdf6, r, 90)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf6, 'testoutputs/03rotate.pdf', False, False)
except:
    prerr()
print('---cpdf_rotateBy')
try:
    pycpdf.rotateBy(pagespdf7, r, 90)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf7, 'testoutputs/03rotateby.pdf', False, False)
except:
    prerr()
print('---cpdf_rotateContents')
try:
    pycpdf.rotateContents(pagespdf8, r, 35.0)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf8, 'testoutputs/03rotatecontents.pdf', False, False)
except:
    prerr()
print('---cpdf_upright')
try:
    pycpdf.upright(pagespdf9, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf9, 'testoutputs/03upright.pdf', False, False)
except:
    prerr()
print('---cpdf_hFlip')
try:
    pycpdf.hFlip(pagespdf10, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf10, 'testoutputs/03hflip.pdf', False, False)
except:
    prerr()
print('---cpdf_vFlip')
try:
    pycpdf.vFlip(pagespdf11, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf11, 'testoutputs/03vflip.pdf', False, False)
except:
    prerr()
print('---cpdf_crop')
try:
    pycpdf.crop(pagespdf12, r, 0.0, 0.0, 400.0, 500.0)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf12, 'testoutputs/03crop.pdf', False, False)
except:
    prerr()
print('---cpdf_removeCrop')
try:
    pycpdf.removeCrop(pagespdf13, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf13, 'testoutputs/03remove_crop.pdf', False, False)
except:
    prerr()
print('---cpdf_removeTrim')
try:
    pycpdf.removeTrim(pagespdf14, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf14, 'testoutputs/03remove_trim.pdf', False, False)
except:
    prerr()
print('---cpdf_removeArt')
try:
    pycpdf.removeArt(pagespdf15, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf15, 'testoutputs/03remove_art.pdf', False, False)
except:
    prerr()
print('---cpdf_removeBleed')
try:
    pycpdf.removeBleed(pagespdf16, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf16, 'testoutputs/03remove_bleed.pdf', False, False)
except:
    prerr()
print('---cpdf_trimMarks')
try:
    pycpdf.trimMarks(pagespdf17, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf17, 'testoutputs/03trim_marks.pdf', False, False)
except:
    prerr()
print('---cpdf_showBoxes')
try:
    pycpdf.showBoxes(pagespdf18, r)
except:
    prerr()
try:
    pycpdf.toFile(pagespdf18, 'testoutputs/03show_boxes.pdf', False, False)
except:
    prerr()
print('---cpdf_hardBox')
try:
    pycpdf.hardBox(pagespdf19, r, "/MediaBox")
except:
    prerr()
try:
    pycpdf.toFile(pagespdf19, 'testoutputs/03hard_box.pdf', False, False)
except:
    prerr()

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression
print('***** CHAPTER 5. Compression')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
print('---cpdf_compress')
try:
    pycpdf.compress(pdf)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/05compressed.pdf', False, False)
except:
    prerr()
print('---cpdf_decompress')
try:
    pycpdf.decompress(pdf)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/05decompressed.pdf', False, False)
except:
    prerr()
print('---cpdf_squeezeInMemory')
try:
    pycpdf.squeezeInMemory(pdf)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/05squeezedinmemory.pdf', False, False)
except:
    prerr()

# CHAPTER 6. Bookmarks

# Format: list of tuples. (level : int, page : int, text : string, openstatus : int/bool)
print('***** CHAPTER 6. Bookmarks')
print('---cpdf_getBookmarks')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    existing_marks = pycpdf.getBookmarks(pdf)
except:
    fatal_prerr()
print(existing_marks)
marks = [(0, 20, "New bookmark!", True)]
print('---cpdf_setBookmarks')
try:
    pycpdf.setBookmarks(pdf, marks)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/06newmarks.pdf', False, False)
except:
    prerr()

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps
print('***** CHAPTER 8. Logos, Watermarks and Stamps')
print('---cpdf_addText')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    prerr()
try:
    pycpdf.addText(False, pdf, pycpdf.all(pdf), 'Some Text~~~~~~~~~~!', (pycpdf.topLeft, 20.0, 20.0), 1.0, 1,
                   pycpdf.timesRoman, 20, 0.5, 0.5, 0.5, False, False, True, 0.5, pycpdf.leftJustify, False, False, '', 1.0, False)
except:
    prerr()
print('---cpdf_addTextSimple')
try:
    pycpdf.addTextSimple(
        pdf, r, 'The text', (pycpdf.posCentre, 100.0, 200.0), pycpdf.timesRoman, 12.0)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/08added_text.pdf', False, False)
except:
    prerr()
print('---cpdf_removeText')
try:
    pycpdf.removeText(pdf, r)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/08removed_text.pdf', False, False)
except:
    prerr()
print('---cpdf_textWidth')
try:
    pycpdf.textWidth(pycpdf.timesRoman, 'Some text')
except:
    prerr()
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
print('---cpdf_stampOn')
try:
    stamp = pycpdf.fromFile('logo.pdf', '')
except:
    prerr()
try:
    stampee = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    prerr()
try:
    pycpdf.stampOn(stamp, stampee, pycpdf.all(stamp))
except:
    prerr()
print('---cpdf_stampUnder')
try:
    pycpdf.stampUnder(stamp, stampee, pycpdf.all(stamp))
except:
    prerr()
print('---cpdf_stampExtended')
try:
    pycpdf.stampExtended(stamp, stampee, pycpdf.all(
        stamp), True, True, (pycpdf.topLeft, 20, 20), True)
except:
    prerr()
try:
    pycpdf.toFile(stamp, 'testoutputs/08stamp_after.pdf', False, False)
except:
    prerr()
try:
    pycpdf.toFile(stampee, 'testoutputs/08stampee_after.pdf', False, False)
except:
    prerr()
print('---cpdf_combinePages')
try:
    c1 = pycpdf.fromFile('logo.pdf', '')
except:
    prerr()
try:
    c2 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    prerr()
try:
    c3 = pycpdf.combinePages(c1, c2)
except:
    prerr()
try:
    pycpdf.toFile(c3, 'testoutputs/08c3after.pdf', False, False)
except:
    prerr()

try:
    logo = pycpdf.fromFile('logo.pdf', '')
except:
    prerr()
try:
    undoc = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    prerr()
print('---cpdf_stampAsXObject')
try:
    name = pycpdf.stampAsXObject(undoc, pycpdf.all(undoc), logo)
except:
    fatal_prerr()
print('---cpdf_addContent')
try:
    pycpdf.addContent(
        f'q 1 0 0 1 100 100 cm {name} Do Q q 1 0 0 1 300 300 cm {name} Do Q q 1 0 0 1 500 500 cm {name} Do Q', True, undoc, pycpdf.all(undoc))
except:
    prerr()
try:
    pycpdf.toFile(undoc, 'testoutputs/08demo.pdf', False, False)
except:
    prerr()


# CHAPTER 9. Multipage facilities
print('***** CHAPTER 9. Multipage facilities')
mp = pycpdf.fromFile('cpdflibmanual.pdf', '')
mp2 = pycpdf.fromFile('cpdflibmanual.pdf', '')
mp3 = pycpdf.fromFile('cpdflibmanual.pdf', '')
mp4 = pycpdf.fromFile('cpdflibmanual.pdf', '')
mp5 = pycpdf.fromFile('cpdflibmanual.pdf', '')
mp6 = pycpdf.fromFile('cpdflibmanual.pdf', '')
mp7 = pycpdf.fromFile('cpdflibmanual.pdf', '')
print('---cpdf_twoUp')
try:
    pycpdf.twoUp(mp)
except:
    prerr()
try:
    pycpdf.toFile(mp, 'testoutputs/09mp.pdf', False, False)
except:
    prerr()
print('---cpdf_twoUpStack')
try:
    pycpdf.twoUpStack(mp2)
except:
    prerr()
try:
    pycpdf.toFile(mp2, 'testoutputs/09mp2.pdf', False, False)
except:
    prerr()
print('---cpdf_padBefore')
r = list(range(1, 11))
try:
    pycpdf.padBefore(mp3, r)
except:
    prerr()
try:
    pycpdf.toFile(mp3, 'testoutputs/09mp3.pdf', False, False)
except:
    prerr()
print('---cpdf_padAfter')
try:
    pycpdf.padAfter(mp4, r)
except:
    prerr()
try:
    pycpdf.toFile(mp4, 'testoutputs/09mp4.pdf', False, False)
except:
    prerr()
print('---cpdf_padEvery')
try:
    pycpdf.padEvery(mp5, 5)
except:
    prerr()
try:
    pycpdf.toFile(mp5, 'testoutputs/09mp5.pdf', False, False)
except:
    prerr()
print('---cpdf_padMultiple')
try:
    pycpdf.padMultiple(mp6, 10)
except:
    prerr()
try:
    pycpdf.toFile(mp6, 'testoutputs/09mp6.pdf', False, False)
except:
    prerr()
print('---cpdf_padMultipleBefore')
try:
    pycpdf.padMultipleBefore(mp7, 23)
except:
    prerr()
try:
    pycpdf.toFile(mp7, 'testoutputs/09mp7.pdf', False, False)
except:
    prerr()

# CHAPTER 10. Annotations

# Not in the library version.

# CHAPTER 11. Document Information and Metadata
print('***** CHAPTER 11. Document Information and Metadata')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
print('---cpdf_isLinearized')
try:
    linearized = pycpdf.isLinearized('testinputs/cpdfmanual.pdf')
except:
    fatal_prerr()
print('---cpdf_getVersion')
try:
    version = pycpdf.getVersion(pdf)
except:
    fatal_prerr()
print('---cpdf_getMajorVersion')
try:
    version2 = pycpdf.getMajorVersion(pdf)
except:
    fatal_prerr()
print('---cpdf_getTitle')
try:
    title = pycpdf.getTitle(pdf)
except:
    fatal_prerr()
print(f'title: {title}')
print('---cpdf_getTitle')
try:
    author = pycpdf.getAuthor(pdf)
except:
    fatal_prerr()
print(f'author: {author}')
print('---cpdf_getSubject')
try:
    subject = pycpdf.getSubject(pdf)
except:
    fatal_prerr()
print(f'subject: {subject}')
print('---cpdf_getKeywords')
try:
    keywords = pycpdf.getKeywords(pdf)
except:
    fatal_prerr()
print(f'keywords: {keywords}')
print('---cpdf_getCreator')
try:
    creator = pycpdf.getCreator(pdf)
except:
    fatal_prerr()
print(f'creator: {creator}')
print('---cpdf_getProducer')
try:
    producer = pycpdf.getProducer(pdf)
except:
    fatal_prerr()
print(f'producer: {producer}')
print('---cpdf_getCreationDate')
try:
    creationDate = pycpdf.getCreationDate(pdf)
except:
    fatal_prerr()
print(f'creationDate: {creationDate}')
print('---cpdf_getModificationDate')
try:
    modificationDate = pycpdf.getModificationDate(pdf)
except:
    fatal_prerr()
print(f'modificationDate: {modificationDate}')
print('---cpdf_getTitleXMP')
try:
    titleXMP = pycpdf.getTitleXMP(pdf)
except:
    fatal_prerr()
print(f'titleXMP: {titleXMP}')
print('---cpdf_getAuthorXMP')
try:
    authorXMP = pycpdf.getAuthorXMP(pdf)
except:
    fatal_prerr()
print(f'authorXMP: {authorXMP}')
print('---cpdf_getSubjectXMP')
try:
    subjectXMP = pycpdf.getSubjectXMP(pdf)
except:
    fatal_prerr()
print(f'subjectXMP: {subjectXMP}')
print('---cpdf_getKeywordsXMP')
try:
    keywordsXMP = pycpdf.getKeywordsXMP(pdf)
except:
    fatal_prerr()
print(f'keywordsXMP: {keywordsXMP}')
print('---cpdf_getCreatorXMP')
try:
    creatorXMP = pycpdf.getCreatorXMP(pdf)
except:
    fatal_prerr()
print(f'creatorXMP: {creatorXMP}')
print('---cpdf_getProducerXMP')
try:
    producerXMP = pycpdf.getProducerXMP(pdf)
except:
    fatal_prerr()
print(f'producerXMP: {producerXMP}')
print('---cpdf_getCreationDateXMP')
try:
    creationDateXMP = pycpdf.getCreationDateXMP(pdf)
except:
    fatal_prerr()
print(f'creationDateXMP: {creationDateXMP}')
print('---cpdf_getModificationDate')
try:
    modificationDateXMP = pycpdf.getModificationDateXMP(pdf)
except:
    prerr()
print(f'modificationDateXMP: {modificationDateXMP}')
print('---cpdf_setTitle')
try:
    pycpdf.setTitle(pdf, 'title')
except:
    prerr()
print('---cpdf_setAuthor')
try:
    pycpdf.setAuthor(pdf, 'author')
except:
    prerr()
print('---cpdf_setSubject')
try:
    pycpdf.setSubject(pdf, 'subject')
except:
    prerr()
print('---cpdf_setKeywords')
try:
    pycpdf.setKeywords(pdf, 'keywords')
except:
    prerr()
print('---cpdf_setCreator')
try:
    pycpdf.setCreator(pdf, 'creator')
except:
    prerr()
print('---cpdf_setProducer')
try:
    pycpdf.setProducer(pdf, 'producer')
except:
    prerr()
print('---cpdf_setCreationDate')
try:
    pycpdf.setCreationDate(pdf, 'now')
except:
    prerr()
print('---cpdf_setModificationDate')
try:
    pycpdf.setModificationDate(pdf, 'now')
except:
    prerr()
print('---cpdf_setTitleXMP')
try:
    pycpdf.setTitleXMP(pdf, 'title')
except:
    prerr()
print('---cpdf_setAuthorXMP')
try:
    pycpdf.setAuthorXMP(pdf, 'author')
except:
    prerr()
print('---cpdf_setSubjectXMP')
try:
    pycpdf.setSubjectXMP(pdf, 'subject')
except:
    prerr()
print('---cpdf_setKeywordsXMP')
try:
    pycpdf.setKeywordsXMP(pdf, 'keywords')
except:
    prerr()
print('---cpdf_setCreatorXMP')
try:
    pycpdf.setCreatorXMP(pdf, 'creator')
except:
    prerr()
print('---cpdf_setProducerXMP')
try:
    pycpdf.setProducerXMP(pdf, 'producer')
except:
    prerr()
print('---cpdf_setCreationDateXMP')
try:
    pycpdf.setCreationDateXMP(pdf, 'now')
except:
    prerr()
print('---cpdf_setModificationDateXMP')
try:
    pycpdf.setModificationDateXMP(pdf, 'now')
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11setinfo.pdf', False, False)
except:
    prerr()
try:
    print('---cpdf_getDateComponents')
    components = pycpdf.getDateComponents('D:20061108125017Z')
    print(components)
    print('---cpdf_dateStringOfComponents')
    dateString = pycpdf.dateStringOfComponents(components)
except:
    fatal_prerr()
print('---cpdf_getPageRotation')
try:
    rot = pycpdf.getPageRotation(pdf, 1)
except:
    fatal_prerr()
print('---cpdf_hasBox')
try:
    hasBox = pycpdf.hasBox(pdf, 1, '/TrimBox')
except:
    fatal_prerr()
print('---cpdf_getMediaBox')
try:
    mediaBox = pycpdf.getMediaBox(pdf, 1)
except:
    fatal_prerr()
print(mediaBox)
print('---cpdf_getCropBox')
try:
    cropBox = pycpdf.getCropBox(pdf, 1)
except:
    fatal_prerr()
print(cropBox)
print('---cpdf_getTrimBox')
try:
    trimBox = pycpdf.getTrimBox(pdf, 1)
except:
    fatal_prerr()
print(trimBox)
print('---cpdf_getArtBox')
try:
    artBox = pycpdf.getArtBox(pdf, 1)
except:
    fatal_prerr()
print(artBox)
print('---cpdf_getBleedBox')
try:
    bleedBox = pycpdf.getBleedBox(pdf, 1)
except:
    fatal_prerr()
print(bleedBox)
print('---cpdf_setMediaBox')
try:
    pycpdf.setMediaBox(pdf, pycpdf.all(pdf), 100.0, 500.0, 150.0, 550.0)
except:
    fatal_prerr()
print('---cpdf_setCropBox')
try:
    pycpdf.setCropBox(pdf, pycpdf.all(pdf), 100.0, 500.0, 150.0, 550.0)
except:
    fatal_prerr()
print('---cpdf_setTrimBox')
try:
    pycpdf.setTrimBox(pdf, pycpdf.all(pdf), 100.0, 500.0, 150.0, 550.0)
except:
    prerr()
print('---cpdf_setArtBox')
try:
    pycpdf.setArtBox(pdf, pycpdf.all(pdf), 100.0, 500.0, 150.0, 550.0)
except:
    prerr()
print('---cpdf_setBleedBox')
try:
    pycpdf.setBleedBox(pdf, pycpdf.all(pdf), 100.0, 500.0, 150.0, 550.0)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11setboxes.pdf', False, False)
except:
    prerr()
print('---cpdf_markTrapped')
try:
    pycpdf.markTrapped(pdf)
except:
    prerr()
print('---cpdf_markTrappedXMP')
try:
    pycpdf.markTrappedXMP(pdf)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11trapped.pdf', False, False)
except:
    prerr()
print('---cpdf_markUntrapped')
try:
    pycpdf.markUntrapped(pdf)
except:
    prerr()
print('---cpdf_markUntrappedXMP')
try:
    pycpdf.markUntrappedXMP(pdf)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11untrapped.pdf', False, False)
except:
    prerr()
print('---cpdf_setPageLayout')
try:
    pycpdf.setPageLayout(pdf, pycpdf.twoColumnLeft)
except:
    prerr()
print('---cpdf_setPageMode')
try:
    pycpdf.setPageMode(pdf, pycpdf.useOutlines)
except:
    prerr()
print('---cpdf_hideToolbar')
try:
    pycpdf.hideToolbar(pdf, True)
except:
    prerr()
print('---cpdf_hideMenubar')
try:
    pycpdf.hideMenubar(pdf, True)
except:
    prerr()
print('---cpdf_hideWindowUi')
try:
    pycpdf.hideWindowUi(pdf, True)
except:
    prerr()
print('---cpdf_fitWindow')
try:
    pycpdf.fitWindow(pdf, True)
except:
    prerr()
print('---cpdf_centerWindow')
try:
    pycpdf.centerWindow(pdf, True)
except:
    prerr()
print('---cpdf_displayDocTitle')
try:
    pycpdf.displayDocTitle(pdf, True)
except:
    prerr()
print('---cpdf_openAtPage')
try:
    pycpdf.openAtPage(pdf, True, 4)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11open.pdf', False, False)
except:
    prerr()
print('---cpdf_setMetadataFromFile')
try:
    pycpdf.setMetadataFromFile(pdf, 'cpdflibmanual.pdf')
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11metadata1.pdf', False, False)
except:
    prerr()
print('---cpdf_setMetadataFromByteArray')
try:
    pycpdf.setMetadataFromByteArray(pdf, 'BYTEARRAY')
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11metadata2.pdf', False, False)
except:
    prerr()
print('---cpdf_getMetadata')
try:
    metadata = pycpdf.getMetadata(pdf)
except:
    fatal_prerr()
print('---cpdf_removeMetadata')
try:
    pycpdf.removeMetadata(pdf)
except:
    prerr()
print('---cpdf_createMetadata')
try:
    pycpdf.createMetadata(pdf)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11metadata3.pdf', False, False)
except:
    prerr()
print('---cpdf_setMetadataDate')
try:
    pycpdf.setMetadataDate(pdf, 'now')
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11metadata4.pdf', False, False)
except:
    prerr()
print('---cpdf_getPageLabels')
try:
    labels = pycpdf.getPageLabels(pdf)
except:
    fatal_prerr()
print(labels)
print('---cpdf_addPageLabels')
try:
    pycpdf.addPageLabels(
        pdf, (pycpdf.decimalArabic, "PREFIX-", 1, pycpdf.all(pdf)), False)
except:
    prerr()
print('---cpdf_removePageLabels')
try:
    pycpdf.removePageLabels(pdf)
except:
    prerr()
print('---cpdf_getPageLabelStringForPage')
try:
    labelString = pycpdf.getPageLabelStringForPage(pdf, 1)
except:
    fatal_prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/11pagelabels.pdf', False, False)
except:
    prerr()

# CHAPTER 12. File Attachments
print('***** CHAPTER 12. File Attachments')
try:
    pdf = pycpdf.fromFile('testinputs/has_attachments.pdf', '')
except:
    fatal_prerr()
print('---cpdf_attachFile')
try:
    pycpdf.attachFile('testinputs/image.pdf', pdf)
except:
    prerr()
print('---cpdf_attachFileToPage')
try:
    pycpdf.attachFileToPage('testinputs/image.pdf', pdf, 1)
except:
    prerr()
print('---cpdf_attachFileFromMemory')
try:
    pycpdf.attachFileFromMemory('', 'metadata.txt', pdf)
except:
    prerr()
print('---cpdf_attachFileToPageFromMemory')
try:
    pycpdf.attachFileToPageFromMemory('', 'metadata.txt', pdf, 1)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/12with_attachments.pdf', False, False)
except:
    prerr()
print('---cpdf_removeAttachedFiles')
try:
    pycpdf.removeAttachedFiles(pdf)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/12removed_attachments.pdf', False, False)
except:
    prerr()
print('---cpdf_getAttachments')
try:
    attachments = pycpdf.getAttachments(pdf)
except:
    fatal_prerr()

# CHAPTER 13. Images
print('***** CHAPTER 13. Images')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
print('---cpdf_getImageResolution')
try:
    images = pycpdf.getImageResolution(pdf, 300)
except:
    fatal_prerr()
print(images)

# CHAPTER 14. Fonts
print('***** CHAPTER 14. Fonts')
print('---cpdf_getFontInfo')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    fonts = pycpdf.getFontInfo(pdf)
except:
    fatal_prerr()
print(fonts)
print('---cpdf_removeFonts')
try:
    pycpdf.removeFonts(pdf)
except:
    prerr()
try:
    pycpdf.toFile(pdf, 'testoutputs/14remove_fonts.pdf', False, False)
except:
    prerr()
print('---cpdf_copyFont')
try:
    pycpdf.copyFont(pdf, pdf2, r, 1, "/Font")
except:
    prerr()

# CHAPTER 15. PDF and JSON
print('***** CHAPTER 15. PDF and JSON')
try:
    pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
print('---cpdf_outputJSON')
try:
    pycpdf.outputJSON('testoutputs/15json.json', False, False, pdf)
except:
    prerr()
try:
    pycpdf.outputJSON('testoutputs/15jsonnostream.json', False, True, pdf)
except:
    prerr()
try:
    pycpdf.outputJSON('testoutputs/15jsonparsed.json', True, False, pdf)
except:
    prerr()

# CHAPTER 16. Optional Content Groups
print('***** CHAPTER 16. Optional Content Groups')
try:
    pdf = pycpdf.fromFile('testinputs/has_ocgs.pdf', '')
except:
    fatal_prerr()
print('---cpdf_getOCGList')
try:
    ocgs = pycpdf.getOCGList(pdf)
    print(ocgs)
except:
    prerr()
print('---cpdf_OCGCoalesce')
try:
    pycpdf.OCGCoalesce(pdf)
except:
    prerr()
print('---cpdf_OCGRename')
try:
    pycpdf.OCGRename(pdf, 'one', 'two')
except:
    prerr()
print('---cpdf_OCGOrderAll')
try:
    pycpdf.OCGOrderAll(pdf)
except:
    prerr()

# CHAPTER 17. Miscellaneous
print('***** CHAPTER 17. Miscellaneous')
try:
    misc = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc2 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc3 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc4 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc5 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc6 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc7 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc8 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc9 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc10 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc11 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misc12 = pycpdf.fromFile('cpdflibmanual.pdf', '')
except:
    fatal_prerr()
try:
    misclogo = pycpdf.fromFile('logo.pdf', '')
except:
    fatal_prerr()
r = pycpdf.all(misc)
print('---cpdf_draft')
try:
    pycpdf.draft(misc, r, True)
except:
    prerr()
try:
    pycpdf.toFile(misc, 'testoutputs/17draft.pdf', False, False)
except:
    prerr()
print('---cpdf_removeAllText')
try:
    pycpdf.removeAllText(misc2, r)
except:
    prerr()
try:
    pycpdf.toFile(misc2, 'testoutputs/17removealltext.pdf', False, False)
except:
    prerr()
print('---cpdf_blackText')
try:
    pycpdf.blackText(misc3, r)
except:
    prerr()
try:
    pycpdf.toFile(misc3, 'testoutputs/17blacktext.pdf', False, False)
except:
    prerr()
print('---cpdf_blackLines')
try:
    pycpdf.blackLines(misc4, r)
except:
    prerr()
try:
    pycpdf.toFile(misc4, 'testoutputs/17blacklines.pdf', False, False)
except:
    prerr()
print('---cpdf_blackFills')
try:
    pycpdf.blackFills(misc5, r)
except:
    prerr()
try:
    pycpdf.toFile(misc5, 'testoutputs/17blackfills.pdf', False, False)
except:
    prerr()
print('---cpdf_thinLines')
try:
    pycpdf.thinLines(misc6, r, 2.0)
except:
    prerr()
try:
    pycpdf.toFile(misc6, 'testoutputs/17thinlines.pdf', False, False)
except:
    prerr()
print('---cpdf_copyId')
try:
    pycpdf.copyId(misclogo, misc7)
except:
    prerr()
try:
    pycpdf.toFile(misc7, 'testoutputs/17copyid.pdf', False, False)
except:
    prerr()
print('---cpdf_removeId')
try:
    pycpdf.removeId(misc8)
except:
    prerr()
try:
    pycpdf.toFile(misc8, 'testoutputs/17removeid.pdf', False, False)
except:
    prerr()
print('---cpdf_setVersion')
try:
    pycpdf.setVersion(misc9, 1)
except:
    prerr()
try:
    pycpdf.toFile(misc9, 'testoutputs/17setversion.pdf', False, False)
except:
    prerr()
print('---cpdf_setFullVersion')
try:
    pycpdf.setFullVersion(misc10, 2, 0)
except:
    prerr()
try:
    pycpdf.toFile(misc10, 'testoutputs/17setfullversion.pdf', False, False)
except:
    prerr()
print('---cpdf_removeDictEntry')
try:
    pycpdf.removeDictEntry(misc11, '/Producer')
except:
    prerr()
try:
    pycpdf.toFile(misc11, 'testoutputs/17removedictentry.pdf', False, False)
except:
    prerr()
print('---cpdf_removeClipping')
try:
    pycpdf.removeClipping(misc12, r)
except:
    prerr()
try:
    pycpdf.toFile(misc12, 'testoutputs/17removeclipping.pdf', False, False)
except:
    prerr()

# CHAPTER X. Undocumented or Internal
print('***** CHAPTER X. Undocumented or Internal')
print('---cpdf_setDemo')
try:
    pycpdf.setDemo(True)
except:
    prerr()
