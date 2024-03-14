import pycpdflib
import sys
import os
import traceback
import gc

# DLL loading depends on your own platform. These are the author's settings.
if sys.platform.startswith('darwin'):
    pycpdflib.loadDLL("/Users/john/repos/python-libcpdf/libpycpdf.so")
elif sys.platform.startswith('linux'):
    pycpdflib.loadDLL("libpycpdf.so")
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    os.add_dll_directory("C:\\\\OCaml64/home/JohnWhitington/python-libcpdf/")
    pycpdflib.loadDLL("libpycpdf.dll")


def prerr():
    print("*** EXCEPTION RAISED")
    print(f'({pycpdflib.lastError()} | {pycpdflib.lastErrorString()})')
    print(traceback.format_exc())
    pycpdflib.clearError()


def fatal_prerr():
    prerr()
    print('Fatal error; exiting')
    sys.exit(1)


# CHAPTER 0. Preliminaries
def chapter0():
    print('***** CHAPTER 0. Preliminaries')
    print('---cpdf_startup()')
    print('---cpdf_version()')
    try:
        print('version = ' + pycpdflib.version())
    except:
        prerr()
    print('---cpdf_setFast()')
    try:
        pycpdflib.setFast()
    except:
        prerr()
    print('---cpdf_setSlow()')
    try:
        pycpdflib.setSlow()
    except:
        prerr()
    print('---cpdf_embedStd14()')
    try:
        pycpdflib.embedStd14(True)
    except:
        prerr()
    print('---cpdf_embedStd14Dir()')
    try:
        pycpdflib.embedStd14Dir('fonts')
    except:
        prerr()
    print('---cpdf_JSONUTF8()')
    try:
        pycpdflib.JSONUTF8(True)
    except:
        prerr()
    print('---cpdf_clearError()')
    try:
        pycpdflib.clearError()
    except:
        prerr()


def chapter1():
    # CHAPTER 1. Basics
    print('***** CHAPTER 1. Basics')
    print('---cpdf_fromFile()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_fromFileLazy()')
    try:
        pdf2 = pycpdflib.fromFileLazy('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_toMemory()')
    try:
        data = pycpdflib.toMemory(pdf, False, False)
    except:
        fatal_prerr()
    print('---cpdf_fromMemory()')
    try:
        pdf3 = pycpdflib.fromMemory(data, '')
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(pdf3, 'testoutputs/01fromMemory.pdf', False, False)
    except:
        prerr()
    print('---cpdf_fromMemoryLazy()')
    try:
        pdf4 = pycpdflib.fromMemoryLazy(data, '')
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(
            pdf4, 'testoutputs/01fromMemoryLazy.pdf', False, False)
    except:
        prerr()

    print('---cpdf: enumerate PDFs')
    print('---cpdf_ptOfIn()')
    try:
        print(f'One inch is {pycpdflib.ptOfIn(1.0):.6f} points')
    except:
        prerr()
    print('---cpdf_ptOfCm()')
    try:
        print(f'One centimetre is {pycpdflib.ptOfCm(1.0):.6f} points')
    except:
        prerr()
    print('---cpdf_ptOfMm()')
    try:
        print(f'One millimetre is {pycpdflib.ptOfMm(1.0):.6f} points')
    except:
        prerr()
    print('---cpdf_inOfPt()')
    try:
        print(f'One point is {pycpdflib.inOfPt(1.0):.6f} inches')
    except:
        prerr()
    print('---cpdf_cmOfPt()')
    try:
        print(f'One point is {pycpdflib.cmOfPt(1.0):.6f} centimetres')
    except:
        prerr()
    print('---cpdf_mmOfPt()')
    try:
        print(f'One point is {pycpdflib.mmOfPt(1.0):.6f} millimetres')
    except:
        prerr()
    print('---cpdf_range()')
    try:
        fromto = pycpdflib.pageRange(3, 7)
    except:
        fatal_prerr()
    print('---cpdf_all()')
    try:
        rall = pycpdflib.all(pdf4)
    except:
        fatal_prerr()
    print('---cpdf_even()')
    try:
        even = pycpdflib.even(rall)
    except:
        fatal_prerr()
    print('---cpdf_odd()')
    try:
        odd = pycpdflib.odd(rall)
    except:
        fatal_prerr()
    print('---cpdf_rangeUnion()')
    try:
        union = pycpdflib.rangeUnion(even, odd)
    except:
        fatal_prerr()
    print('---cpdf_difference()')
    try:
        difference = pycpdflib.difference(even, odd)
    except:
        fatal_prerr()
    print('---cpdf_removeDuplicates()')
    try:
        nodeps = pycpdflib.removeDuplicates(rall)
    except:
        fatal_prerr()
    print('---cpdf_rangeLength()')
    try:
        rangel = pycpdflib.rangeLength(union)
    except:
        fatal_prerr()
    print('---cpdf_rangeGet()')
    try:
        got = pycpdflib.rangeGet(odd, 1)
    except:
        fatal_prerr()
    print('---cpdf_rangeAdd()')
    try:
        added = pycpdflib.rangeAdd(odd, 9)
    except:
        fatal_prerr()
    print('---cpdf_isInRange()')
    try:
        inrange = pycpdflib.isInRange(odd, 1)
    except:
        fatal_prerr()
    print('---cpdf_parsePagespec()')
    try:
        r = pycpdflib.parsePagespec(pdf4, "1-3,end")
    except:
        fatal_prerr()
    print('---cpdf_validatePagespec()')
    try:
        valid = pycpdflib.validatePagespec("1-4,5,6")
    except:
        fatal_prerr()
    print(f'Validating pagespec gives {int(valid)}')
    try:
        allpdf4 = pycpdflib.all(pdf4)
    except:
        fatal_prerr()
    print('---cpdf_stringOfPagespec()')
    try:
        pagespecstr = pycpdflib.stringOfPagespec(pdf4, [1, 2, 3, 4, 5])
    except:
        fatal_prerr()
    print(f'String of pagespec is {pagespecstr}')
    print('---cpdf_blankRange()')
    try:
        blankrange = pycpdflib.blankRange()
    except:
        fatal_prerr()
    print('---cpdf_pages()')
    try:
        pdfpages = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        prerr()
    try:
        pages = pycpdflib.pages(pdfpages)
    except:
        fatal_prerr()
    print(f'Pages = {pages}')
    print('---cpdf_pagesFast()')
    try:
        pagesf = pycpdflib.pagesFast('', 'testinputs/cpdflibmanual.pdf')
    except:
        fatal_prerr()
    print(f'Pages = {pagesf}')
    print('---cpdf_toFile()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/01tofile.pdf', False, False)
    except:
        prerr()
    print('---cpdf_toFileExt()')
    try:
        pycpdflib.toFileExt(pdf, 'testoutputs/01tofileext.pdf',
                            False, True, True, True, True)
    except:
        prerr()
    print('---cpdf_isEncrypted()')
    try:
        pdf5 = pycpdflib.blankDocument(100.0, 200.0, 20)
    except:
        fatal_prerr()
    try:
        isenc = pycpdflib.isEncrypted(pdf5)
    except:
        fatal_prerr()
    print(f'isencrypted:{int(isenc)}')
    print('---cpdf_isLinearized()')
    try:
        linearized = pycpdflib.isLinearized('testinputs/cpdfmanual.pdf')
    except:
        fatal_prerr()
    print(f'islinearized:{int(linearized)}')
    print('---cpdf_hasObjectStreams()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
        hasobjectstreams = pycpdflib.hasObjectStreams(pdf)
    except:
        fatal_prerr()
    print(f'hasObjectStreams:{int(hasobjectstreams)}')
    print('---cpdf_id1()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
        id1 = pycpdflib.id1(pdf)
    except:
        fatal_prerr()
    print(f'id1:{id1}')
    print('---cpdf_id2()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
        id2 = pycpdflib.id2(pdf)
    except:
        fatal_prerr()
    print(f'id2:{id2}')
    print('---cpdf_hasAcroForm()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
        hasacroform = pycpdflib.hasAcroForm(pdf)
    except:
        fatal_prerr()
    print(f'hasAcroForm:{int(hasacroform)}')
    print(f'---cpdf_startGetSubformats()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
        subformats = pycpdflib.startGetSubformats(pdf)
        print(f'n subformats: {subformats}')
    except:
        fatal_prerr()
    #FIXME actually call this
    print(f'---cpdf_getSubformat()')
    print(f'---cpdf_endGetSubformats()')
    try:
        pycpdflib.endGetSubformats()
    except:
        fatal_prerr()
    print('---cpdf_toFileEncrypted()')
    try:
        pdf5 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        prerr()
    try:
        pycpdflib.toFileEncrypted(pdf5, pycpdflib.pdf40bit, [
            pycpdflib.noEdit], 'owner', 'user', False, False, 'testoutputs/01encrypted.pdf')
    except:
        prerr()
    print('---cpdf_toFileEncryptedExt()')
    try:
        pycpdflib.toFileEncryptedExt(pdf5, pycpdflib.pdf40bit, [
            pycpdflib.noEdit], 'owner', 'user', False, False, False, False, False, 'testoutputs/01encryptedext.pdf')
    except:
        prerr()
    try:
        encpdf = pycpdflib.fromFile('testoutputs/01encrypted.pdf', 'user')
    except:
        fatal_prerr()

    try:
        encpdf2 = pycpdflib.fromFile('testoutputs/01encrypted.pdf', 'user')
    except:
        fatal_prerr()
    print('---cpdf_hasPermission()')
    try:
        hasperm = pycpdflib.hasPermission(encpdf2, pycpdflib.noEdit)
        hasperm2 = pycpdflib.hasPermission(encpdf2, pycpdflib.noCopy)
    except:
        fatal_prerr()
    print(f'Haspermission {hasperm}, {hasperm2}')
    print('---cpdf_encryptionKind()')
    try:
        encmethod = pycpdflib.encryptionKind(encpdf2)
    except:
        fatal_prerr()
    print(f'encryption kind is {encmethod}')
    print('---cpdf_decryptPdf()')
    try:
        decrypted = pycpdflib.decryptPdf(encpdf, 'user')
    except:
        fatal_prerr()
    print('---cpdf_decryptPdfOwner()')
    try:
        owner = pycpdflib.decryptPdfOwner(encpdf2, 'owner')
    except:
        fatal_prerr()


# CHAPTER 2. Merging and Splitting
def chapter2():
    print('***** CHAPTER 2. Merging and Splitting')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pdf2 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_mergeSimple()')
    try:
        merged = pycpdflib.mergeSimple([pdf, pdf, pdf])
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(merged, 'testoutputs/02merged.pdf', False, False)
    except:
        prerr()
    print('---cpdf_merge()')
    try:
        merged2 = pycpdflib.merge([pdf, pdf, pdf], False, False)
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(merged2, 'testoutputs/02merged2.pdf', False, False)
    except:
        prerr()
    print('---cpdf_mergeSame()')
    try:
        same = pycpdflib.mergeSame([pdf, pdf, pdf], False, False, [
            pycpdflib.all(pdf), pycpdflib.all(pdf2), pycpdflib.all(pdf)])
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(same, 'testoutputs/02merged3.pdf', False, False)
    except:
        prerr()
    print('---cpdf_selectPages()')
    try:
        selected = pycpdflib.selectPages(pdf, [1, 2, 3])
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(selected, 'testoutputs/02selected.pdf', False, False)
    except:
        prerr()

# CHAPTER 3. Pages


def chapter3():
    print('***** CHAPTER 3. Pages')
    try:
        pagespdf1 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf2 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf3 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf4 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf5 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf6 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf7 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf8 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf9 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf10 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf11 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')

    except:
        fatal_prerr()
    try:
        pagespdf12 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf13 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf14 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf15 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf16 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf17 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf18 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pagespdf19 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        r = pycpdflib.all(pagespdf1)
    except:
        fatal_prerr()
    print('---cpdf_scalePages()')
    try:
        pycpdflib.scalePages(pagespdf1, r, 1.5, 1.8)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf1, 'testoutputs/03scalepages.pdf', False, False)
    except:
        prerr()
    print('---cpdf_scaleToFit()')
    try:
        pycpdflib.scaleToFit(pagespdf2, r, 1.5, 1.8, 0.9)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf2, 'testoutputs/03scaletofit.pdf', False, False)
    except:
        prerr()
    print('---cpdf_scaleToFitPaper()')
    try:
        pycpdflib.scaleToFitPaper(pagespdf3, r, pycpdflib.a4portrait, 0.8)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf3, 'testoutputs/03scaletofitpaper.pdf', False, False)
    except:
        prerr()
    print('---cpdf_scaleContents()')
    try:
        pycpdflib.scaleContents(pagespdf4, r, (pycpdflib.topLeft, 20, 20), 2.0)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf4, 'testoutputs/03scalecontents.pdf', False, False)
    except:
        prerr()
    print('---cpdf_shiftContents()')
    try:
        pycpdflib.shiftContents(pagespdf5, r, 1.5, 1.25)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf5, 'testoutputs/03shiftcontents.pdf', False, False)
    except:
        prerr()
    print('---cpdf_shiftBoxes()')
    try:
        pycpdflib.shiftBoxes(pagespdf5, r, 100, 100)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf5, 'testoutputs/03shiftboxes.pdf', False, False)
    except:
        prerr()
    print('---cpdf_rotate()')
    try:
        pycpdflib.rotate(pagespdf6, r, 90)
    except:
        prerr()
    try:
        pycpdflib.toFile(pagespdf6, 'testoutputs/03rotate.pdf', False, False)
    except:
        prerr()
    print('---cpdf_rotateBy()')
    try:
        pycpdflib.rotateBy(pagespdf7, r, 90)
    except:
        prerr()
    try:
        pycpdflib.toFile(pagespdf7, 'testoutputs/03rotateby.pdf', False, False)
    except:
        prerr()
    print('---cpdf_rotateContents()')
    try:
        pycpdflib.rotateContents(pagespdf8, r, 35.0)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf8, 'testoutputs/03rotatecontents.pdf', False, False)
    except:
        prerr()
    print('---cpdf_upright()')
    try:
        pycpdflib.upright(pagespdf9, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(pagespdf9, 'testoutputs/03upright.pdf', False, False)
    except:
        prerr()
    print('---cpdf_hFlip()')
    try:
        pycpdflib.hFlip(pagespdf10, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(pagespdf10, 'testoutputs/03hflip.pdf', False, False)
    except:
        prerr()
    print('---cpdf_vFlip()')
    try:
        pycpdflib.vFlip(pagespdf11, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(pagespdf11, 'testoutputs/03vflip.pdf', False, False)
    except:
        prerr()
    print('---cpdf_crop()')
    try:
        pycpdflib.crop(pagespdf12, r, 0.0, 0.0, 400.0, 500.0)
    except:
        prerr()
    try:
        pycpdflib.toFile(pagespdf12, 'testoutputs/03crop.pdf', False, False)
    except:
        prerr()
    print('---cpdf_trimMarks()')
    try:
        pycpdflib.trimMarks(pagespdf17, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf17, 'testoutputs/03trim_marks.pdf', False, False)
    except:
        prerr()
    print('---cpdf_showBoxes()')
    try:
        pycpdflib.showBoxes(pagespdf18, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf18, 'testoutputs/03show_boxes.pdf', False, False)
    except:
        prerr()
    print('---cpdf_hardBox()')
    try:
        pycpdflib.hardBox(pagespdf19, r, "/MediaBox")
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf19, 'testoutputs/03hard_box.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeCrop()')
    try:
        pycpdflib.removeCrop(pagespdf13, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf13, 'testoutputs/03remove_crop.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeTrim()')
    try:
        pycpdflib.removeTrim(pagespdf14, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf14, 'testoutputs/03remove_trim.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeArt()')
    try:
        pycpdflib.removeArt(pagespdf15, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf15, 'testoutputs/03remove_art.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeBleed()')
    try:
        pycpdflib.removeBleed(pagespdf16, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pagespdf16, 'testoutputs/03remove_bleed.pdf', False, False)
    except:
        prerr()

# CHAPTER 4. Encryption


def chapter4(): pass
# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression


def chapter5():
    print('***** CHAPTER 5. Compression')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_compress()')
    try:
        pycpdflib.compress(pdf)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/05compressed.pdf', False, False)
    except:
        prerr()
    print('---cpdf_decompress()')
    try:
        pycpdflib.decompress(pdf)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/05decompressed.pdf', False, False)
    except:
        prerr()
    print('---cpdf_squeezeInMemory()')
    try:
        pycpdflib.squeezeInMemory(pdf)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pdf, 'testoutputs/05squeezedinmemory.pdf', False, False)
    except:
        prerr()

# CHAPTER 6. Bookmarks


def chapter6():
    # Format: list of tuples. (level : int, page : int, text : string, openstatus : int/bool)
    print('***** CHAPTER 6. Bookmarks')
    print('---cpdf: get bookmarks')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        existing_marks = pycpdflib.getBookmarks(pdf)
    except:
        fatal_prerr()
    print(f'There are {len(existing_marks)} bookmarks')
    m = existing_marks[0];
    a, b, c, d = m
    print(f'Bookmark at level {a} points to page {b} and has text "{c}" and open {d}')
    marks = [(0, 20, "New bookmark!", True)]
    print('---cpdf: set bookmarks')
    try:
        pycpdflib.setBookmarks(pdf, marks)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/06newmarks.pdf', False, False)
    except:
        prerr()
    try:
        marks = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_getBookmarksJSON()')
    try:
        data = pycpdflib.getBookmarksJSON(marks)
        print(f'Contains {len(data)} bytes of data')
    except:
        prerr()
    print('---cpdf_setBookmarksJSON()')
    try:
        pycpdflib.setBookmarksJSON(marks, data)
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(marks, 'testoutputs/06jsonmarks.pdf', False, False)
    except:
        prerr()
    print('---cpdf_tableOfContents()')
    try:
        tocfile = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        pycpdflib.tableOfContents(
            tocfile, pycpdflib.timesRoman, 12.0, 'Table of Contents', False)
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(tocfile, 'testoutputs/06toc.pdf', False, False)
    except:
        prerr()

# CHAPTER 7. Presentations


def chapter7(): pass
# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps


def chapter8():
    print('***** CHAPTER 8. Logos, Watermarks and Stamps')
    print('---cpdf_addText()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        prerr()
    try:
        pycpdflib.addText(False, pdf, pycpdflib.all(pdf), 'Some Text~~~~~~~~~~!', (pycpdflib.topLeft, 20.0, 20.0), 1.0, 1,
                          pycpdflib.timesRoman, 20, 0.5, 0.5, 0.5, False, False, True, 0.5, pycpdflib.leftJustify, False, False, '', 1.0, False)
    except:
        prerr()
    print('---cpdf_addTextSimple()')
    r = pycpdflib.all(pdf)
    try:
        pycpdflib.addTextSimple(
            pdf, r, 'The text!', (pycpdflib.topLeft, 20.0, 20.0), pycpdflib.timesRoman, 50.0)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/08added_text.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeText()')
    try:
        pycpdflib.removeText(pdf, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/08removed_text.pdf', False, False)
    except:
        prerr()
    print('---cpdf_textWidth()')
    try:
        pycpdflib.textWidth(pycpdflib.timesRoman, 'Some text')
    except:
        prerr()
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_stampOn()')
    try:
        stamp = pycpdflib.fromFile('logo.pdf', '')
    except:
        prerr()
    try:
        stampee = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        prerr()
    try:
        pycpdflib.stampOn(stamp, stampee, pycpdflib.all(stamp))
    except:
        prerr()
    print('---cpdf_stampUnder()')
    try:
        pycpdflib.stampUnder(stamp, stampee, pycpdflib.all(stamp))
    except:
        prerr()
    print('---cpdf_stampExtended()')
    try:
        pycpdflib.stampExtended(stamp, stampee, pycpdflib.all(
            stamp), True, True, (pycpdflib.topLeft, 20, 20), True)
    except:
        prerr()
    try:
        pycpdflib.toFile(stamp, 'testoutputs/08stamp_after.pdf', False, False)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            stampee, 'testoutputs/08stampee_after.pdf', False, False)
    except:
        prerr()
    print('---cpdf_combinePages()')
    try:
        c1 = pycpdflib.fromFile('logo.pdf', '')
    except:
        prerr()
    try:
        c2 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        prerr()
    try:
        c3 = pycpdflib.combinePages(c1, c2)
    except:
        prerr()
    try:
        pycpdflib.toFile(c3, 'testoutputs/08c3after.pdf', False, False)
    except:
        prerr()
    try:
        logo = pycpdflib.fromFile('logo.pdf', '')
    except:
        prerr()
    try:
        undoc = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        prerr()
    print('---cpdf_stampAsXObject()')
    try:
        name = pycpdflib.stampAsXObject(undoc, pycpdflib.all(undoc), logo)
    except:
        fatal_prerr()
    print('---cpdf_addContent()')
    try:
        pycpdflib.addContent(
            f'q 1 0 0 1 100 100 cm {name} Do Q q 1 0 0 1 300 300 cm {name} Do Q q 1 0 0 1 500 500 cm {name} Do Q', True, undoc, pycpdflib.all(undoc))
    except:
        prerr()
    try:
        pycpdflib.toFile(undoc, 'testoutputs/08demo.pdf', False, False)
    except:
        prerr()


# CHAPTER 9. Multipage facilities
def chapter9():
    print('***** CHAPTER 9. Multipage facilities')
    mp = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    mp2 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    mp25 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    mp26 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    mp3 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    mp4 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    mp5 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    mp6 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    mp7 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    print('---cpdf_twoUp()')
    try:
        pycpdflib.twoUp(mp)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp, 'testoutputs/09mp.pdf', False, False)
    except:
        prerr()
    print('---cpdf_twoUpStack()')
    try:
        pycpdflib.twoUpStack(mp2)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp2, 'testoutputs/09mp2.pdf', False, False)
    except:
        prerr()
    print('---cpdf_impose()')
    try:
        pycpdflib.impose(mp25, 5.0, 4.0, False, False, False,
                         False, False, 40.0, 20.0, 2.0)
    except:
        prerr()
    print('---cpdf_chop()')
    try:
        pycpdflib.chop(mp25, pycpdflib.all(mp25), 2, 3, False, False, False)
    except:
        prerr()
    print('---cpdf_chopH()')
    try:
        pycpdflib.chopH(mp25, pycpdflib.all(mp25), False, 200)
    except:
        prerr()
    print('---cpdf_chopV()')
    try:
        pycpdflib.chopV(mp25, pycpdflib.all(mp25), True, 300)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp25, 'testoutputs/09mp25.pdf', False, False)
    except:
        prerr()
    try:
        pycpdflib.impose(mp26, 2000.0, 1000.0, True, False,
                         False, False, False, 40.0, 20.0, 2.0)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp26, 'testoutputs/09mp26.pdf', False, False)
    except:
        prerr()
    print('---cpdf_padBefore()')
    r = list(range(1, 11))
    try:
        pycpdflib.padBefore(mp3, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp3, 'testoutputs/09mp3.pdf', False, False)
    except:
        prerr()
    print('---cpdf_padAfter()')
    try:
        pycpdflib.padAfter(mp4, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp4, 'testoutputs/09mp4.pdf', False, False)
    except:
        prerr()
    print('---cpdf_padEvery()')
    try:
        pycpdflib.padEvery(mp5, 5)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp5, 'testoutputs/09mp5.pdf', False, False)
    except:
        prerr()
    print('---cpdf_padMultiple()')
    try:
        pycpdflib.padMultiple(mp6, 10)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp6, 'testoutputs/09mp6.pdf', False, False)
    except:
        prerr()
    print('---cpdf_padMultipleBefore()')
    try:
        pycpdflib.padMultipleBefore(mp7, 23)
    except:
        prerr()
    try:
        pycpdflib.toFile(mp7, 'testoutputs/09mp7.pdf', False, False)
    except:
        prerr()

# CHAPTER 10. Annotations


def chapter10():
    print('***** CHAPTER 10. Annotations')
    try:
        annots = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_annotationsJSON()')
    try:
        data = pycpdflib.annotationsJSON(annots)
        print(f'Contains {len(data)} bytes of data')
    except:
        prerr()
    print('---cpdf_removeAnnotations()')
    try:
        pycpdflib.removeAnnotations(annots, pycpdflib.all(annots))
    except:
        prerr()
    print('---cpdf_setAnnotationsJSON()')
    try:
        pycpdflib.setAnnotationsJSON(annots, data)
    except:
        fatal_prerr()

# CHAPTER 11. Document Information and Metadata


def chapter11():
    print('***** CHAPTER 11. Document Information and Metadata')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()

    print('---cpdf_getVersion()')
    try:
        version = pycpdflib.getVersion(pdf)
    except:
        fatal_prerr()
    print(f'minor version:{version}')
    print('---cpdf_getMajorVersion()')
    try:
        version2 = pycpdflib.getMajorVersion(pdf)
    except:
        fatal_prerr()
    print(f'major version:{version2}')
    print('---cpdf_getTitle()')
    try:
        title = pycpdflib.getTitle(pdf)
    except:
        fatal_prerr()
    print(f'title: {title}')
    print('---cpdf_getAuthor()')
    try:
        author = pycpdflib.getAuthor(pdf)
    except:
        fatal_prerr()
    print(f'author: {author}')
    print('---cpdf_getSubject()')
    try:
        subject = pycpdflib.getSubject(pdf)
    except:
        fatal_prerr()
    print(f'subject: {subject}')
    print('---cpdf_getKeywords()')
    try:
        keywords = pycpdflib.getKeywords(pdf)
    except:
        fatal_prerr()
    print(f'keywords: {keywords}')
    print('---cpdf_getCreator()')
    try:
        creator = pycpdflib.getCreator(pdf)
    except:
        fatal_prerr()
    print(f'creator: {creator}')
    print('---cpdf_getProducer()')
    try:
        producer = pycpdflib.getProducer(pdf)
    except:
        fatal_prerr()
    print(f'producer: {producer}')
    print('---cpdf_getCreationDate()')
    try:
        creationDate = pycpdflib.getCreationDate(pdf)
    except:
        fatal_prerr()
    print(f'creationdate: {creationDate}')
    print('---cpdf_getModificationDate()')
    try:
        modificationDate = pycpdflib.getModificationDate(pdf)
    except:
        fatal_prerr()
    print(f'modificationdate: {modificationDate}')
    print('---cpdf_getTitleXMP()')
    try:
        titleXMP = pycpdflib.getTitleXMP(pdf)
    except:
        fatal_prerr()
    print(f'titleXMP: {titleXMP}')
    print('---cpdf_getAuthorXMP()')
    try:
        authorXMP = pycpdflib.getAuthorXMP(pdf)
    except:
        fatal_prerr()
    print(f'authorXMP: {authorXMP}')
    print('---cpdf_getSubjectXMP()')
    try:
        subjectXMP = pycpdflib.getSubjectXMP(pdf)
    except:
        fatal_prerr()
    print(f'subjectXMP: {subjectXMP}')
    print('---cpdf_getKeywordsXMP()')
    try:
        keywordsXMP = pycpdflib.getKeywordsXMP(pdf)
    except:
        fatal_prerr()
    print(f'keywordsXMP: {keywordsXMP}')
    print('---cpdf_getCreatorXMP()')
    try:
        creatorXMP = pycpdflib.getCreatorXMP(pdf)
    except:
        fatal_prerr()
    print(f'creatorXMP: {creatorXMP}')
    print('---cpdf_getProducerXMP()')
    try:
        producerXMP = pycpdflib.getProducerXMP(pdf)
    except:
        fatal_prerr()
    print(f'producerXMP: {producerXMP}')
    print('---cpdf_getCreationDateXMP()')
    try:
        creationDateXMP = pycpdflib.getCreationDateXMP(pdf)
    except:
        fatal_prerr()
    print(f'creationdateXMP: {creationDateXMP}')
    print('---cpdf_getModificationDateXMP()')
    try:
        modificationDateXMP = pycpdflib.getModificationDateXMP(pdf)
    except:
        prerr()
    print(f'modificationdateXMP: {modificationDateXMP}')
    print('---cpdf_pageInfoJSON()')
    try:
        pageInfoJSON = pycpdflib.pageInfoJSON(pdf)
    except:
        prerr()
    print(f'Contains {len(pageInfoJSON)} bytes of data')
    print('---cpdf_setTitle()')
    try:
        pycpdflib.setTitle(pdf, 'title')
    except:
        prerr()
    print('---cpdf_setAuthor()')
    try:
        pycpdflib.setAuthor(pdf, 'author')
    except:
        prerr()
    print('---cpdf_setSubject()')
    try:
        pycpdflib.setSubject(pdf, 'subject')
    except:
        prerr()
    print('---cpdf_setKeywords()')
    try:
        pycpdflib.setKeywords(pdf, 'keywords')
    except:
        prerr()
    print('---cpdf_setCreator()')
    try:
        pycpdflib.setCreator(pdf, 'creator')
    except:
        prerr()
    print('---cpdf_setProducer()')
    try:
        pycpdflib.setProducer(pdf, 'producer')
    except:
        prerr()
    print('---cpdf_setCreationDate()')
    try:
        pycpdflib.setCreationDate(pdf, 'now')
    except:
        prerr()
    print('---cpdf_setModificationDate()')
    try:
        pycpdflib.setModificationDate(pdf, 'now')
    except:
        prerr()
    print('---cpdf_setTitleXMP()')
    try:
        pycpdflib.setTitleXMP(pdf, 'title')
    except:
        prerr()
    print('---cpdf_setAuthorXMP()')
    try:
        pycpdflib.setAuthorXMP(pdf, 'author')
    except:
        prerr()
    print('---cpdf_setSubjectXMP()')
    try:
        pycpdflib.setSubjectXMP(pdf, 'subject')
    except:
        prerr()
    print('---cpdf_setKeywordsXMP()')
    try:
        pycpdflib.setKeywordsXMP(pdf, 'keywords')
    except:
        prerr()
    print('---cpdf_setCreatorXMP()')
    try:
        pycpdflib.setCreatorXMP(pdf, 'creator')
    except:
        prerr()
    print('---cpdf_setProducerXMP()')
    try:
        pycpdflib.setProducerXMP(pdf, 'producer')
    except:
        prerr()
    print('---cpdf_setCreationDateXMP()')
    try:
        pycpdflib.setCreationDateXMP(pdf, 'now')
    except:
        prerr()
    print('---cpdf_setModificationDateXMP()')
    try:
        pycpdflib.setModificationDateXMP(pdf, 'now')
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11setinfo.pdf', False, False)
    except:
        prerr()
    try:
        print('---cpdf_getDateComponents()')
        components = pycpdflib.getDateComponents('D:20061108125017Z')
        a, b, c, d, e, f, g, h = components
        print(f'D:20061108125017Z = {a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}')
        print('---cpdf_dateStringOfComponents()')
        dateString = pycpdflib.dateStringOfComponents(components)
        print(dateString)
    except:
        fatal_prerr()
    print('---cpdf_getPageRotation()')
    try:
        rot = pycpdflib.getPageRotation(pdf, 1)
    except:
        fatal_prerr()
    print(f'/Rotate on page 1 = {rot}')
    print('---cpdf_hasBox()')
    try:
        hasBox = pycpdflib.hasBox(pdf, 1, '/TrimBox')
    except:
        fatal_prerr()
    print(f'hasbox: {int(hasBox)}')
    print('---cpdf_numAnnots()')
    try:
        numAnnots = pycpdflib.numAnnots(pdf, 1)
        print(f'numAnnots: {numAnnots}')
    except:
        fatal_prerr()
    print('---cpdf_getMediaBox()')
    try:
        mediaBox = pycpdflib.getMediaBox(pdf, 1)
    except:
        fatal_prerr()
    a, b, c, d = mediaBox
    print(f'Media: {a:.6f} {b:.6f} {c:.6f} {d:.6f}')
    print('---cpdf_getCropBox()')
    try:
        cropBox = pycpdflib.getCropBox(pdf, 1)
    except:
        fatal_prerr()
    a, b, c, d = cropBox
    print(f'Crop: {a:.6f} {b:.6f} {c:.6f} {d:.6f}')
    print('---cpdf_getBleedBox()')
    try:
        bleedBox = pycpdflib.getBleedBox(pdf, 1)
    except:
        fatal_prerr()
    a, b, c, d = bleedBox
    print(f'Bleed: {a:.6f} {b:.6f} {c:.6f} {d:.6f}')
    print('---cpdf_getArtBox()')
    try:
        artBox = pycpdflib.getArtBox(pdf, 1)
    except:
        fatal_prerr()
    a, b, c, d = artBox
    print(f'Art: {a:.6f} {b:.6f} {c:.6f} {d:.6f}')
    print('---cpdf_getTrimBox()')
    try:
        trimBox = pycpdflib.getTrimBox(pdf, 1)
    except:
        fatal_prerr()
    a, b, c, d = trimBox
    print(f'Trim: {a:.6f} {b:.6f} {c:.6f} {d:.6f}')
    print('---cpdf_setMediaBox()')
    try:
        pycpdflib.setMediaBox(pdf, pycpdflib.all(pdf),
                              100.0, 500.0, 150.0, 550.0)
    except:
        fatal_prerr()
    print('---cpdf_setCropBox()')
    try:
        pycpdflib.setCropBox(pdf, pycpdflib.all(
            pdf), 100.0, 500.0, 150.0, 550.0)
    except:
        fatal_prerr()
    print('---cpdf_setTrimBox()')
    try:
        pycpdflib.setTrimBox(pdf, pycpdflib.all(
            pdf), 100.0, 500.0, 150.0, 550.0)
    except:
        prerr()
    print('---cpdf_setArtBox()')
    try:
        pycpdflib.setArtBox(pdf, pycpdflib.all(
            pdf), 100.0, 500.0, 150.0, 550.0)
    except:
        prerr()
    print('---cpdf_setBleedBox()')
    try:
        pycpdflib.setBleedBox(pdf, pycpdflib.all(pdf),
                              100.0, 500.0, 150.0, 550.0)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11setboxes.pdf', False, False)
    except:
        prerr()
    print('---cpdf_markTrapped()')
    try:
        pycpdflib.markTrapped(pdf)
    except:
        prerr()
    print('---cpdf_markTrappedXMP()')
    try:
        pycpdflib.markTrappedXMP(pdf)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11trapped.pdf', False, False)
    except:
        prerr()
    print('---cpdf_markUntrapped()')
    try:
        pycpdflib.markUntrapped(pdf)
    except:
        prerr()
    print('---cpdf_markUntrappedXMP()')
    try:
        pycpdflib.markUntrappedXMP(pdf)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11untrapped.pdf', False, False)
    except:
        prerr()
    print('---cpdf_setPageLayout()')
    try:
        pycpdflib.setPageLayout(pdf, pycpdflib.twoColumnLeft)
    except:
        prerr()
    print('---cpdf_setPageMode()')
    try:
        pycpdflib.setPageMode(pdf, pycpdflib.useOutlines)
    except:
        prerr()
    print('---cpdf_hideToolbar()')
    try:
        pycpdflib.hideToolbar(pdf, True)
    except:
        prerr()
    print('---cpdf_hideMenubar()')
    try:
        pycpdflib.hideMenubar(pdf, True)
    except:
        prerr()
    print('---cpdf_hideWindowUi()')
    try:
        pycpdflib.hideWindowUi(pdf, True)
    except:
        prerr()
    print('---cpdf_fitWindow()')
    try:
        pycpdflib.fitWindow(pdf, True)
    except:
        prerr()
    print('---cpdf_centerWindow()')
    try:
        pycpdflib.centerWindow(pdf, True)
    except:
        prerr()
    print('---cpdf_displayDocTitle()')
    try:
        pycpdflib.displayDocTitle(pdf, True)
    except:
        prerr()
    print('---cpdf_openAtPage()')
    try:
        pycpdflib.openAtPage(pdf, True, 4)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11open.pdf', False, False)
    except:
        prerr()
    print('---cpdf_setMetadataFromFile()')
    try:
        pycpdflib.setMetadataFromFile(pdf, 'testinputs/cpdflibmanual.pdf')
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11metadata1.pdf', False, False)
    except:
        prerr()
    print('---cpdf_setMetadataFromByteArray()')
    try:
        pycpdflib.setMetadataFromByteArray(pdf, b'BYTEARRAY')
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11metadata2.pdf', False, False)
    except:
        prerr()
    print('---cpdf_getMetadata()')
    try:
        metadata = pycpdflib.getMetadata(pdf)
    except:
        fatal_prerr()
    print('---cpdf_removeMetadata()')
    try:
        pycpdflib.removeMetadata(pdf)
    except:
        prerr()
    print('---cpdf_createMetadata()')
    try:
        pycpdflib.createMetadata(pdf)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11metadata3.pdf', False, False)
    except:
        prerr()
    print('---cpdf_setMetadataDate()')
    try:
        pycpdflib.setMetadataDate(pdf, 'now')
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11metadata4.pdf', False, False)
    except:
        prerr()
    print('---cpdf_addPageLabels()')
    try:
        pycpdflib.addPageLabels(
            pdf, (pycpdflib.uppercaseRoman, "PREFIX-", 1, pycpdflib.all(pdf)), False)
    except:
        prerr()
    print('---cpdf: get page labels')
    try:
        labels = pycpdflib.getPageLabels(pdf)
    except:
        fatal_prerr()
    print(f'There are {len(labels)} labels')
    for l in labels:
        a, b, c, d = l
        print(f'Page label: {a}, {b}, {c}, {d}')
    print('---cpdf_removePageLabels()')
    try:
        pycpdflib.removePageLabels(pdf)
    except:
        prerr()
    print('---cpdf_getPageLabelStringForPage()')
    try:
        labelString = pycpdflib.getPageLabelStringForPage(pdf, 1)
    except:
        fatal_prerr()
    print(f'Label string is {labelString}')
    try:
        pycpdflib.toFile(pdf, 'testoutputs/11pagelabels.pdf', False, False)
    except:
        prerr()
    print(f'---cpdf_compositionJSON()')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
        data = pycpdflib.compositionJSON(1000000, pdf)
        print(f'Contains {len(data)} bytes of data')
    except:
        fatal_prerr()

# CHAPTER 12. File Attachments


def chapter12():
    print('***** CHAPTER 12. File Attachments')
    try:
        pdf = pycpdflib.fromFile('testinputs/has_attachments.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_attachFile()')
    try:
        pycpdflib.attachFile('testinputs/image.pdf', pdf)
    except:
        prerr()
    print('---cpdf_attachFileToPage()')
    try:
        pycpdflib.attachFileToPage('testinputs/image.pdf', pdf, 1)
    except:
        prerr()
    print('---cpdf_attachFileFromMemory()')
    try:
        pycpdflib.attachFileFromMemory(b'', 'metadata.txt', pdf)
    except:
        prerr()
    print('---cpdf_attachFileToPageFromMemory()')
    try:
        pycpdflib.attachFileToPageFromMemory(b'', 'metadata.txt', pdf, 1)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pdf, 'testoutputs/12with_attachments.pdf', False, False)
    except:
        prerr()
    print('---cpdf: get attachments')
    try:
        attachments = pycpdflib.getAttachments(pdf)
    except:
        fatal_prerr()
    print(f'There are {len(attachments)} attachments to get')
    for i, a in enumerate(attachments):
        name, page, data = a
        print(f'Attachment {i} is named {name}')
        print(f'It is on page {page}')
        print(f'Contains {len(data)} bytes of data')
    print('---cpdf_removeAttachedFiles()')
    try:
        pycpdflib.removeAttachedFiles(pdf)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            pdf, 'testoutputs/12removed_attachments.pdf', False, False)
    except:
        prerr()


# CHAPTER 13. Images
def chapter13():
    print('***** CHAPTER 13. Images')
    try:
        pdf = pycpdflib.fromFile('testinputs/image.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf: get image resolution')
    try:
        images = pycpdflib.getImageResolution(pdf, 500000.)
    except:
        fatal_prerr()
    for i in images:
        a, b, c, d, e, f = i
        print(f'IMAGE: {a}, {b}, {c}, {d}, {e:.6f}, {f:.6f}')
    print('---cpdf_imageResolutionJSON()')
    try:
        imageResolutionJSON = pycpdflib.imageResolutionJSON(pdf, 300)
    except:
        fatal_prerr()
    print(f'Contains {len(imageResolutionJSON)} bytes of data')
    print('---cpdf_imagesJSON()')
    try:
        imagesJSON = pycpdflib.imagesJSON(pdf)
    except:
        fatal_prerr()
    print(f'Contains {len(imagesJSON)} bytes of data')

# CHAPTER 14. Fonts


def chapter14():
    print('***** CHAPTER 14. Fonts')
    print('---cpdf: Get Fonts')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
        pdf2 = pycpdflib.fromFile('testinputs/frontmatter.pdf', '')
        r = pycpdflib.all(pdf)
    except:
        fatal_prerr()
    try:
        fonts = pycpdflib.getFontInfo(pdf)
    except:
        fatal_prerr()
    a, b, c, d = fonts[0]
    print(f'Page {a}, font {b} has type {c} and encoding {d}')
    print('---cpdf_fontsJSON()')
    try:
        fontsJSON = pycpdflib.fontsJSON(pdf)
    except:
        prerr()
    print(f'Contains {len(fontsJSON)} bytes of data')
    print('---cpdf_removeFonts()')
    try:
        pycpdflib.removeFonts(pdf)
    except:
        prerr()
    try:
        pycpdflib.toFile(pdf, 'testoutputs/14remove_fonts.pdf', False, False)
    except:
        prerr()
    print('---cpdf_copyFont()')
    try:
        pycpdflib.copyFont(pdf, pdf2, r, 1, "/Font")
    except:
        prerr()

# CHAPTER 15. PDF and JSON


def chapter15():
    print('***** CHAPTER 15. PDF and JSON')
    try:
        pdf = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf_outputJSON()')
    try:
        pycpdflib.outputJSON('testoutputs/15json.json',
                             False, False, False, pdf)
    except:
        prerr()
    try:
        pycpdflib.outputJSON(
            'testoutputs/15jsonnostream.json', False, True, False, pdf)
    except:
        prerr()
    try:
        pycpdflib.outputJSON(
            'testoutputs/15jsonparsed.json', True, False, False, pdf)
    except:
        prerr()
    try:
        pycpdflib.outputJSON(
            'testoutputs/15jsondecomp.json', False, False, True, pdf)
    except:
        prerr()
    print('---cpdf_fromJSON()')
    try:
        jsonpdf = pycpdflib.fromJSON('testoutputs/15jsonparsed.json')
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(jsonpdf, 'testoutputs/15fromjson.pdf', False, False)
    except:
        prerr()
    print('---cpdf_outputJSONMemory()')
    try:
        jbuf = pycpdflib.outputJSONMemory(jsonpdf, False, False, False)
    except:
        fatal_prerr()
    print('---cpdf_fromJSONMemory()')
    try:
        jfrommem = pycpdflib.fromJSONMemory(jbuf)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            jfrommem, 'testoutputs/15fromJSONMemory.pdf', False, False)
    except:
        prerr()


# CHAPTER 16. Optional Content Groups


def chapter16():
    print('***** CHAPTER 16. Optional Content Groups')
    try:
        pdf = pycpdflib.fromFile('testinputs/has_ocgs.pdf', '')
    except:
        fatal_prerr()
    print('---cpdf: Get OCG List')
    try:
        ocgs = pycpdflib.getOCGList(pdf)
    except:
        prerr()
    for x in ocgs:
        print(x)
    print('---cpdf_OCGCoalesce()')
    try:
        pycpdflib.OCGCoalesce(pdf)
    except:
        prerr()
    print('---cpdf_OCGRename()')
    try:
        pycpdflib.OCGRename(pdf, 'one', 'two')
    except:
        prerr()
    print('---cpdf_OCGOrderAll()')
    try:
        pycpdflib.OCGOrderAll(pdf)
    except:
        prerr()

# CHAPTER 17. Creating New PDFs


def chapter17():
    print('***** CHAPTER 17. Creating New PDFs')
    print('---cpdf_blankDocument()')
    try:
        pdf5 = pycpdflib.blankDocument(100.0, 200.0, 20)
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(pdf5, 'testoutputs/01blank.pdf', False, False)
    except:
        prerr()
    print('---cpdf_blankDocumentPaper()')
    try:
        pdf6 = pycpdflib.blankDocumentPaper(pycpdflib.a4portrait, 10)
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(pdf6, 'testoutputs/01blanka4.pdf', False, False)
    except:
        prerr()
    print('---cpdf_textToPDF()')
    try:
        ttpdf = pycpdflib.textToPDF(
            500.0, 600.0, pycpdflib.timesItalic, 8.0, '../cpdflib-source/cpdflibtest.c')
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(ttpdf, 'testoutputs/01ttpdf.pdf', False, False)
    except:
        prerr()
    print('---cpdf_textToPDFPaper()')
    try:
        ttpdfpaper = pycpdflib.textToPDFPaper(
            pycpdflib.a4portrait, pycpdflib.timesBoldItalic, 10.0, '../cpdflib-source/cpdflibtest.c')
    except:
        fatal_prerr()
    try:
        pycpdflib.toFile(
            ttpdfpaper, 'testoutputs/01ttpdfpaper.pdf', False, False)
    except:
        prerr()

def chapter18():
    print('***** CHAPTER 18. Drawing on PDFs')

def chapter19():
    print('***** CHAPTER 19. Miscellaneous')
    try:
        misc = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc2 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc3 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc4 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc5 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc6 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc7 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc8 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc9 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc10 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc11 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc12 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc13 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc14 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc15 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misc16 = pycpdflib.fromFile('testinputs/cpdflibmanual.pdf', '')
    except:
        fatal_prerr()
    try:
        misclogo = pycpdflib.fromFile('logo.pdf', '')
    except:
        fatal_prerr()
    r = pycpdflib.all(misc)
    print('---cpdf_draft()')
    try:
        pycpdflib.draft(misc, r, True)
    except:
        prerr()
    try:
        pycpdflib.toFile(misc, 'testoutputs/17draft.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeAllText()')
    try:
        pycpdflib.removeAllText(misc2, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            misc2, 'testoutputs/17removealltext.pdf', False, False)
    except:
        prerr()
    print('---cpdf_blackText()')
    try:
        pycpdflib.blackText(misc3, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(misc3, 'testoutputs/17blacktext.pdf', False, False)
    except:
        prerr()
    print('---cpdf_blackLines()')
    try:
        pycpdflib.blackLines(misc4, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(misc4, 'testoutputs/17blacklines.pdf', False, False)
    except:
        prerr()
    print('---cpdf_blackFills()')
    try:
        pycpdflib.blackFills(misc5, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(misc5, 'testoutputs/17blackfills.pdf', False, False)
    except:
        prerr()
    print('---cpdf_thinLines()')
    try:
        pycpdflib.thinLines(misc6, r, 2.0)
    except:
        prerr()
    try:
        pycpdflib.toFile(misc6, 'testoutputs/17thinlines.pdf', False, False)
    except:
        prerr()
    print('---cpdf_copyId()')
    try:
        pycpdflib.copyId(misclogo, misc7)
    except:
        prerr()
    try:
        pycpdflib.toFile(misc7, 'testoutputs/17copyid.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeId()')
    try:
        pycpdflib.removeId(misc8)
    except:
        prerr()
    try:
        pycpdflib.toFile(misc8, 'testoutputs/17removeid.pdf', False, False)
    except:
        prerr()
    print('---cpdf_setVersion()')
    try:
        pycpdflib.setVersion(misc9, 1)
    except:
        prerr()
    try:
        pycpdflib.toFile(misc9, 'testoutputs/17setversion.pdf', False, False)
    except:
        prerr()
    print('---cpdf_setFullVersion()')
    try:
        pycpdflib.setFullVersion(misc10, 2, 0)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            misc10, 'testoutputs/17setfullversion.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeDictEntry()')
    try:
        pycpdflib.removeDictEntry(misc11, '/Producer')
    except:
        prerr()
    try:
        pycpdflib.toFile(
            misc11, 'testoutputs/17removedictentry.pdf', False, False)
    except:
        prerr()
    print('---cpdf_removeDictEntrySearch()')
    try:
        pycpdflib.removeDictEntrySearch(misc13, '/Producer', '1')
    except:
        prerr()
    try:
        pycpdflib.toFile(
            misc13, 'testoutputs/17removedictentrysearch.pdf', False, False)
    except:
        prerr()
    print('---cpdf_replaceDictEntry()')
    try:
        pycpdflib.replaceDictEntry(misc14, '/Producer', '"NewProducer"')
    except:
        prerr()
    try:
        pycpdflib.toFile(
            misc14, 'testoutputs/17replacedictentry.pdf', False, False)
    except:
        prerr()
    print('---cpdf_replaceDictEntrySearch()')
    try:
        pycpdflib.replaceDictEntrySearch(misc15, '/Producer', '"NewProducer2"', '"pdfTeX-1.40.22"')
    except:
        prerr()
    try:
        pycpdflib.toFile(
            misc15, 'testoutputs/17replacedictentrysearch.pdf', False, False)
    except:
        prerr()
    print('---cpdf_getDictEntries()')
    try:
        data = pycpdflib.getDictEntries(misc16, '/Producer')
        print(f'length of entries data = {len(data)}')
    except:
        prerr()
    print('---cpdf_removeClipping()')
    try:
        pycpdflib.removeClipping(misc12, r)
    except:
        prerr()
    try:
        pycpdflib.toFile(
            misc12, 'testoutputs/17removeclipping.pdf', False, False)
    except:
        prerr()


# Run the tests
chapter0()
chapter1()
chapter2()
chapter3()
chapter4()
chapter5()
chapter6()
chapter7()
chapter8()
chapter9()
chapter10()
chapter11()
chapter12()
chapter13()
chapter14()
chapter15()
chapter16()
chapter17()
chapter18()
chapter19()
