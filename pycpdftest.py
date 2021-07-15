import pycpdf
import sys
import os
import traceback

#DLL loading depends on your own platform. These are the author's settings.
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

#CHAPTER 0. Preliminaries
print('***** CHAPTER 0. Preliminaries')
print('---cpdf_startup()')
try: pycpdf.startup()
except: prerr()
print('---cpdf_version()')
try: print('version = ' + pycpdf.version())
except: prerr()
print('---cpdf_setFast()')
try: pycpdf.setFast()
except: prerr()
print('---cpdf_setSlow()')
try: pycpdf.setSlow()
except: prerr()
print('---cpdf_clearError()')
try: pycpdf.clearError()
except: prerr()
print('---cpdf_onExit()')
try: pycpdf.onExit()
except: prerr()

#CHAPTER 1. Basics
print('***** CHAPTER 1. Basics')
print('---cpdf_fromFile()')
try: pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
except: fatal_prerr()
print('---cpdf_fromFileLazy')
try: pdf2 = pycpdf.fromFileLazy('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
fh = open('testinputs/cpdfmanual.pdf', mode='rb')
data = fh.read()
print('---cpdf_fromMemory')
try: pdf3 = pycpdf.fromMemory(data, '')
except: fatal_prerr()
try: pycpdf_toFile(pdf3, 'testoutputs/01fromMemory.pdf', False, False)
except: prerr()
print('---cpdf_fromMemoryLazy')
try: pdf4 = pycpdf.fromMemoryLazy(data, '')
except: fatal_prerr()
try: pycpdf_toFile(pdf4, 'testoutputs/01fromMemoryLazy.pdf', False, False)
except: prerr()
print('---cpdf_blankDocument')
try: pdf5 = pycpdf.blankDocument(200.5, 100.0, 50)
except: fatal_prerr()
print('---cpdf_toFile')
try: pycpdf.toFile(pdf5, 'testoutputs/01blank.pdf', False, False)
except: prerr()
print('---cpdf_blankDocumentPaper')
try: pdf6 = pycpdf.blankDocumentPaper(pycpdf.a4portrait, 50)
except: fatal_prerr()
try: pycpdf.toFile(pdf6, 'testoutputs/01blanka4.pdf', False, False)
except: prerr()
print('---cpdf_enumeratePDFs')
try: pdfs = pycpdf.enumeratePDFs()
except: fatal_prerr()
for k, i in pdfs:
  print(k, i)
print('---cpdf_ptOfCm')
try: print(pycpdf.ptOfCm(1.0))
except: prerr()
print('---cpdf_ptOfMm')
try: print(pycpdf.ptOfMm(1.0))
except: prerr()
print('---cpdf_ptOfIn')
try: print(pycpdf.ptOfIn(1.0))
except: prerr()
print('---cpdf_cmOfPt')
try: print(pycpdf.cmOfPt(1.0))
except: prerr()
print('---cpdf_ptOfCm')
try: print(pycpdf.mmOfPt(1.0))
except: prerr()
print('---cpdf_ptOfCm')
try: print(pycpdf.inOfPt(1.0))
except: prerr()
print('---cpdf_parsePagespec')
try: r = pycpdf.parsePagespec(pdf4, "1-3,end")
except: fatal_prerr()
print('---cpdf_valiadatePagespec')
try: valid = pycpdf.validatePagespec("1-4,5,6")
except: fatal_prerr()
print('---cpdf_all')
try: allpdf4 = pycpdf.all(pdf4)
except: fatal_prerr()
print(allpdf4)
print('---cpdf_stringOfPagespec')
try: pagespecstr = pycpdf.stringOfPagespec(pdf4, allpdf4)
except: fatal_prerr()
print(pagespecstr)
print('---cpdf_blankRange')
try: blankrange = pycpdf.blankRange()
except: fatal_prerr()
print('---cpdf_pageRange')
try: fromto = pycpdf.pageRange(3, 7)
except: fatal_prerr()
print('---cpdf_all')
try: rall = pycpdf.all(pdf4)
except: fatal_prerr()
print("all", rall)
print('---cpdf_even')
try: even = pycpdf.even(rall)
except: fatal_prerr()
print('---cpdf_odd')
try: odd = pycpdf.odd(rall)
except: fatal_prerr()
print('---cpdf_rangeUnion')
try: union = pycpdf.rangeUnion(even, odd)
except: fatal_prerr()
print('---cpdf_difference')
try: difference = pycpdf.difference(even, odd)
except: fatal_prerr()
print('---cpdf_removeDuplicates')
try: nodeps = pycpdf.removeDuplicates(rall)
except: fatal_prerr()
print('---cpdf_rangeLength')
try: rangel = pycpdf.rangeLength(union)
except: fatal_prerr()
print('---cpdf_rangeGet')
try: got = pycpdf.rangeGet(odd, 1)
except: fatal_prerr()
print('---cpdf_rangeAdd')
try: added = pycpdf.rangeAdd(odd, 9)
except: fatal_prerr()
print('---cpdf_isInRange')
try: inrange = pycpdf.isInRange(odd, 1)
except: fatal_prerr()
print('---cpdf_pages')
try: pages = pycpdf.pages(pdf5)
except: fatal_prerr()
print('---cpdf_pagesFast')
try: pagesf = pycpdf.pagesFast('', 'testinputs/cpdfmanual.pdf')
except: fatal_prerr()
print('---cpdf_toFile')
try: pycpdf.toFile(pdf4, 'testoutputs/01tofile.pdf', False, False)
except: prerr()
print('---cpdf_toFileExt')
try: pycpdf.toFileExt(pdf4, 'testoutputs/01tofileext.pdf', False, False, False, False, False)
except: prerr()
print('---cpdf_toMemory')
try: tomembytes = pycpdf.toMemory(pdf5, False, False)
except: prerr()
print('---cpdf_isEncrypted')
try: isenc = pycpdf.isEncrypted(pdf5)
except: fatal_prerr()
print('---cpdf_toFileEncrypted')
try: pycpdf.toFileEncrypted(pdf5, pycpdf.pdf40bit, [pycpdf.noEdit], 'owner', 'user', False, False, 'testoutputs/01encrypted.pdf')
except: prerr()
print('---cpdf_toFileEncryptedExt')
try: pycpdf.toFileEncryptedExt(pdf5, pycpdf.pdf40bit, [pycpdf.noEdit], 'owner', 'user', False, False, False, False, False, 'testoutputs/01encryptedext.pdf')
except: prerr()
try: encpdf = pycpdf.fromFile('testoutputs/01encrypted.pdf', 'user')
except: fatal_prerr()
print('---cpdf_decryptPdf')
try: decrypted = pycpdf.decryptPdf(encpdf, 'user')
except: fatal_prerr()
try: encpdf2 = pycpdf.fromFile('testoutputs/01encrypted.pdf', 'user')
except: fatal_prerr()
print('---cpdf_decryptPdfOwner')
try: owner = pycpdf.decryptPdfOwner(encpdf2, 'owner')
except: fatal_prerr()
print('---cpdf_hasPermission')
try: hasperm = pycpdf.hasPermission(encpdf2, pycpdf.noEdit)
except: fatal_prerr()
print('---cpdf_encryptionKind')
try: encmethod = pycpdf.encryptionKind(encpdf2)
except: fatal_prerr()

# CHAPTER 2. Merging and Splitting
print('***** CHAPTER 2. Merging and Splitting')
try: pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
try: pdf2 = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
print('---cpdf_mergeSimple')
print(pdf, pdf2)
try: merged = pycpdf.mergeSimple([pdf, pdf2])
except: fatal_prerr()
try: pycpdf.toFile(merged, 'testoutputs/02merged.pdf', False, False)
except: prerr()
print('---cpdf_merge')
try: merged2 = pycpdf.merge([pdf, pdf2], True, False)
except: fatal_prerr()
try: pycpdf.toFile(merged2, 'testoutputs/02merged2.pdf', False, False)
except: prerr()
print('---cpdf_mergeSame')
try: same = pycpdf.mergeSame([pdf, pdf2, pdf], True, False, [pycpdf.even(pycpdf.all(pdf)), pycpdf.all(pdf2), pycpdf.odd(pycpdf.all(pdf))])
except: fatal_prerr()
try: pycpdf.toFile(same, 'testoutputs/02merged3.pdf', False, False)
except: prerr()
print('---cpdf_selectPages')
try: selected = pycpdf.selectPages(pdf, pycpdf.even(pycpdf.all(pdf)))
except: fatal_prerr()
try: pycpdf.toFile(selected, 'testoutputs/02selected.pdf', False, False)
except: prerr()

# CHAPTER 3. Pages
print('***** CHAPTER 3. Pages')
try: pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
try: r = pycpdf.all(pdf)
except: fatal_prerr()
print('---cpdf_scalePages')
try: pycpdf.scalePages(pdf, r, 0.5, 0.7)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03scalepages.pdf', False, False)
except: prerr()
print('---cpdf_scaleToFit')
try: pycpdf.scaleToFit(pdf, r, 0.5, 0.7, 0.5)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03scaletofit.pdf', False, False)
except: prerr()
print('---cpdf_scaleToFitPaper')
try: pycpdf.scaleToFitPaper(pdf, r, pycpdf.a3landscape, 0.5)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03scaletofitpaper.pdf', False, False)
except: prerr()
print('---cpdf_scaleContents')
try: pycpdf.scaleContents(pdf, r, (pycpdf.top, 10, 10), 1.0)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03scalecontents.pdf', False, False)
except: prerr()
print('---cpdf_shiftContents')
try: pycpdf.shiftContents(pdf, r, 100, -100)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03shiftcontents.pdf', False, False)
except: prerr()
print('---cpdf_rotate')
try: pycpdf.rotate(pdf, r, 90)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03rotate.pdf', False, False)
except: prerr()
print('---cpdf_rotateBy')
try: pycpdf.rotateBy(pdf, r, 180)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03rotateby.pdf', False, False)
except: prerr()
print('---cpdf_rotateContents')
try: pycpdf.rotateContents(pdf, r, 43.3)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03rotatecontents.pdf', False, False)
except: prerr()
print('---cpdf_upright')
try: pycpdf.upright(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03upright.pdf', False, False)
except: prerr()
print('---cpdf_hFlip')
try: pycpdf.hFlip(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03hflip.pdf', False, False)
except: prerr()
print('---cpdf_vFlip')
try: pycpdf.vFlip(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03vflip.pdf', False, False)
except: prerr()
print('---cpdf_crop')
try: pycpdf.crop(pdf, r, 100.0, 100.0, 400.0, 400.0)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03crop.pdf', False, False)
except: prerr()
print('---cpdf_removeCrop')
try: pycpdf.removeCrop(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03remove_crop.pdf', False, False)
except: prerr()
print('---cpdf_removeTrim')
try: pycpdf.removeTrim(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03remove_trim.pdf', False, False)
except: prerr()
print('---cpdf_removeArt')
try: pycpdf.removeArt(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03remove_art.pdf', False, False)
except: prerr()
print('---cpdf_removeBleed')
try: pycpdf.removeBleed(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03remove_bleed.pdf', False, False)
except: prerr()
print('---cpdf_trimMarks')
try: pycpdf.trimMarks(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03trim_marks.pdf', False, False)
except: prerr()
print('---cpdf_showBoxes')
try: pycpdf.showBoxes(pdf, r)
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03show_boxes.pdf', False, False)
except: prerr()
print('---cpdf_hardBox')
try: pycpdf.hardBox(pdf, r, "/MediaBox")
except: prerr()
try: pycpdf.toFile(selected, 'testoutputs/03hard_box.pdf', False, False)
except: prerr()

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression
print('***** CHAPTER 5. Compression')
try: pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
print('---cpdf_compress')
try: pycpdf.compress(pdf)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/05compressed.pdf', False, False)
except: prerr()
print('---cpdf_decompress')
try: pycpdf.decompress(pdf)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/05decompressed.pdf', False, False)
except: prerr()
print('---cpdf_squeezeInMemory')
try: pycpdf.squeezeInMemory(pdf)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/05squeezedinmemory.pdf', False, False)
except: prerr()

# CHAPTER 6. Bookmarks

# Format: list of tuples. (level : int, page : int, text : string, openstatus : int/bool) 
print('***** CHAPTER 6. Bookmarks')
print('---cpdf_getBookmarks')
try: pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
try: existing_marks = pycpdf.getBookmarks(pdf)
except: fatal_prerr()
print(existing_marks)
marks = [(0, 20, "New bookmark!", True)]
print('---cpdf_setBookmarks')
try: pycpdf.setBookmarks(pdf, marks)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/06newmarks.pdf', False, False)
except: prerr()

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps
print('***** CHAPTER 8. Logos, Watermarks and Stamps')
print('---cpdf_stampOn')
try: pycpdf.stampOn(pdf, pdf2, r)
except: prerr()
print('---cpdf_stampUnder')
try: pycpdf.stampUnder(pdf, pdf2, r)
except: prerr()
print('---cpdf_stampExtended')
try: pycpdf.stampExtended(pdf, pdf2, r, True, True, pycpdf.topLeft, False)
except: prerr()
print('---cpdf_combinePages')
try: pycpdf.combinePages(pdf, pdf2)
except: prerr()
print('---cpdf_addText')
try: pycpdf.addText(False, pdf, r, 'The text', (pycpdf.topLeft, 1.0, 0.0), 1.0, 10, pycpdf.timesRoman, 12, 0.5, 0.5, 0.5, False, False, False, 1.0, pycpdf.centreJustify, True, False, 'foo.pdf', 2.0, False)
except: prerr()
print('---cpdf_addTextSimple')
try: pycpdf.addTextSimple(pdf, r, 'The text', (pycpdf.posCentre, 100.0, 200.0), pycpdf.timesRoman, 12.0)
except: prerr()
print('---cpdf_removeText')
try: pycpdf.removeText(pdf, r)
except: prerr()
print('---cpdf_textWidth')
try: pycpdf.textWidth(pycpdf.timesRoman, 'Some text')
except: prerr()
try: pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
print('---cpdf_addContent')
try: pycpdf.addContent('content', True, pdf, pycpdf.all(pdf))
except: prerr()
print('---cpdf_stampAsXObject')
try: name = pycpdf.stampAsXObject(pdf, pycpdf.all(pdf), pdf2)
except: fatal_prerr()

# CHAPTER 9. Multipage facilities
print('***** CHAPTER 9. Multipage facilities')
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
print('---cpdf_twoUp')
try: pycpdf.twoUp(pdf)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/09mp.pdf', False, False)
except: prerr()
print('---cpdf_twoUpStack')
try: pycpdf.twoUpStack(pdf)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/09mp2.pdf', False, False)
except: prerr()
try: r = pycpdf.all(pdf)
except: fatal_prerr()
print('---cpdf_padBefore')
try: pycpdf.padBefore(pdf, r)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/09mp3.pdf', False, False)
except: prerr()
print('---cpdf_padAfter')
try: pycpdf.padAfter(pdf, r)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/09mp4.pdf', False, False)
except: prerr()
print('---cpdf_padEvery')
try: pycpdf.padEvery(pdf, 10)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/09mp5.pdf', False, False)
except: prerr()
print('---cpdf_padMultiple')
try: pycpdf.padMultiple(pdf, 10)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/09mp6.pdf', False, False)
except: prerr()
print('---cpdf_padMultipleBefore')
try: pycpdf.padMultipleBefore(pdf, 10)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/09mp7.pdf', False, False)
except: prerr()

# CHAPTER 10. Annotations

# Not in the library version.

# CHAPTER 11. Document Information and Metadata
print('***** CHAPTER 11. Document Information and Metadata')
print('---cpdf_isLinearized')
try: linearized = pycpdf.isLinearized('testinputs/cpdfmanual.pdf')
except: fatal_prerr()
print('---cpdf_getVersion')
try: version = pycpdf.getVersion(pdf)
except: fatal_prerr()
print('---cpdf_getMajorVersion')
try: version2 = pycpdf.getMajorVersion(pdf)
except: fatal_prerr()
print('---cpdf_getTitle')
try: title = pycpdf.getTitle(pdf)
except: fatal_prerr()
print(f'title: {title}')
print('---cpdf_getTitle')
try: author = pycpdf.getAuthor(pdf)
except: fatal_prerr()
print(f'author: {author}')
print('---cpdf_getSubject')
try: subject = pycpdf.getSubject(pdf)
except: fatal_prerr()
print(f'subject: {subject}')
print('---cpdf_getKeywords')
try: keywords = pycpdf.getKeywords(pdf)
except: fatal_prerr()
print(f'keywords: {keywords}')
print('---cpdf_getCreator')
try: creator = pycpdf.getCreator(pdf)
except: fatal_prerr()
print(f'creator: {creator}')
print('---cpdf_getProducer')
try: producer = pycpdf.getProducer(pdf)
except: fatal_prerr()
print(f'producer: {producer}')
print('---cpdf_getCreationDate')
try: creationDate = pycpdf.getCreationDate(pdf)
except: fatal_prerr()
print(f'creationDate: {creationDate}')
print('---cpdf_getModificationDate')
try: modificationDate = pycpdf.getModificationDate(pdf)
except: fatal_prerr()
print(f'modificationDate: {modificationDate}')
print('---cpdf_getTitleXMP')
try: titleXMP = pycpdf.getTitleXMP(pdf)
except: fatal_prerr()
print(f'titleXMP: {titleXMP}')
print('---cpdf_getAuthorXMP')
try: authorXMP = pycpdf.getAuthorXMP(pdf)
except: fatal_prerr()
print(f'authorXMP: {authorXMP}')
print('---cpdf_getSubjectXMP')
try: subjectXMP = pycpdf.getSubjectXMP(pdf)
except: fatal_prerr()
print(f'subjectXMP: {subjectXMP}')
print('---cpdf_getKeywordsXMP')
try: keywordsXMP = pycpdf.getKeywordsXMP(pdf)
except: fatal_prerr()
print(f'keywordsXMP: {keywordsXMP}')
print('---cpdf_getCreatorXMP')
try: creatorXMP = pycpdf.getCreatorXMP(pdf)
except: fatal_prerr()
print(f'creatorXMP: {creatorXMP}')
print('---cpdf_getProducerXMP')
try: producerXMP = pycpdf.getProducerXMP(pdf)
except: fatal_prerr()
print(f'producerXMP: {producerXMP}')
print('---cpdf_getCreationDateXMP')
try: creationDateXMP = pycpdf.getCreationDateXMP(pdf)
except: fatal_prerr()
print(f'creationDateXMP: {creationDateXMP}')
print('---cpdf_getModificationDate')
try: modificationDateXMP = pycpdf.getModificationDateXMP(pdf)
except: prerr()
print(f'modificationDateXMP: {modificationDateXMP}')
print('---cpdf_setTitle')
try: pycpdf.setTitle(pdf, 'title')
except: prerr()
print('---cpdf_setAuthor')
try: pycpdf.setAuthor(pdf, 'author')
except: prerr()
print('---cpdf_setSubject')
try: pycpdf.setSubject(pdf, 'subject')
except: prerr()
print('---cpdf_setKeywords')
try: pycpdf.setKeywords(pdf, 'keywords')
except: prerr()
print('---cpdf_setCreator')
try: pycpdf.setCreator(pdf, 'creator')
except: prerr()
print('---cpdf_setProducer')
try: pycpdf.setProducer(pdf, 'producer')
except: prerr()
print('---cpdf_setCreationDate')
try: pycpdf.setCreationDate(pdf, 'now')
except: prerr()
print('---cpdf_setModificationDate')
try: pycpdf.setModificationDate(pdf, 'now')
except: prerr()
print('---cpdf_setTitleXMP')
try: pycpdf.setTitleXMP(pdf, 'title')
except: prerr()
print('---cpdf_setAuthorXMP')
try: pycpdf.setAuthorXMP(pdf, 'author')
except: prerr()
print('---cpdf_setSubjectXMP')
try: pycpdf.setSubjectXMP(pdf, 'subject')
except: prerr()
print('---cpdf_setKeywordsXMP')
try: pycpdf.setKeywordsXMP(pdf, 'keywords')
except: prerr()
print('---cpdf_setCreatorXMP')
try: pycpdf.setCreatorXMP(pdf, 'creator')
except: prerr()
print('---cpdf_setProducerXMP')
try: pycpdf.setProducerXMP(pdf, 'producer')
except: prerr()
print('---cpdf_setCreationDateXMP')
try: pycpdf.setCreationDateXMP(pdf, 'now')
except: prerr()
print('---cpdf_setModificationDateXMP')
try: pycpdf.setModificationDateXMP(pdf, 'now')
except: prerr()
try:
  print('---cpdf_getDateComponents')
  components = pycpdf.getDateComponents('D:20061108125017Z')
  print(components)
  print('---cpdf_dateStringOfComponents')
  dateString = pycpdf.dateStringOfComponents(components)
except:
  fatal_prerr()
print('---cpdf_getPageRotation')
try: rot = pycpdf.getPageRotation(pdf, 1)
except: fatal_prerr()
print('---cpdf_hasBox')
try: hasBox = pycpdf.hasBox(pdf, 1, '/TrimBox')
except: fatal_prerr()
print('---cpdf_getMediaBox')
try: mediaBox = pycpdf.getMediaBox(pdf, 1)
except: fatal_prerr()
print(mediaBox)
print('---cpdf_getCropBox')
try: cropBox = pycpdf.getCropBox(pdf, 1)
except: fatal_prerr()
print(cropBox)
print('---cpdf_getTrimBox')
try: trimBox = pycpdf.getTrimBox(pdf, 1)
except: fatal_prerr()
print(trimBox)
print('---cpdf_getArtBox')
try: artBox = pycpdf.getArtBox(pdf, 1)
except: fatal_prerr()
print(artBox)
print('---cpdf_getBleedBox')
try: bleedBox = pycpdf.getBleedBox(pdf, 1)
except: fatal_prerr()
print(bleedBox)
print('---cpdf_setMediaBox')
try: pycpdf.setMediaBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
except: fatal_prerr()
print('---cpdf_setCropBox')
try: pycpdf.setCropBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
except: fatal_prerr()
print('---cpdf_setTrimBox')
try: pycpdf.setTrimBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
except: prerr()
print('---cpdf_setArtBox')
try: pycpdf.setArtBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
except: prerr()
print('---cpdf_setBleedBox')
try: pycpdf.setBleedBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
except: prerr()
print('---cpdf_markTrapped')
try: pycpdf.markTrapped(pdf)
except: prerr()
print('---cpdf_markUntrapped')
try: pycpdf.markUntrapped(pdf)
except: prerr()
print('---cpdf_markTrappedXMP')
try: pycpdf.markTrappedXMP(pdf)
except: prerr()
print('---cpdf_markUntrappedXMP')
try: pycpdf.markUntrappedXMP(pdf)
except: prerr()
print('---cpdf_setPageLayout')
try: pycpdf.setPageLayout(pdf, pycpdf.singlePage)
except: prerr()
print('---cpdf_setPageMode')
try: pycpdf.setPageMode(pdf, pycpdf.useThumbs)
except: prerr()
print('---cpdf_hideToolbar')
try: pycpdf.hideToolbar(pdf, True)
except: prerr()
print('---cpdf_hideMenubar')
try: pycpdf.hideMenubar(pdf, False)
except: prerr()
print('---cpdf_hideWindowUi')
try: pycpdf.hideWindowUi(pdf, True)
except: prerr()
print('---cpdf_fitWindow')
try: pycpdf.fitWindow(pdf, True)
except: prerr()
print('---cpdf_centerWindow')
try: pycpdf.centerWindow(pdf, True)
except: prerr()
print('---cpdf_displayDocTitle')
try: pycpdf.displayDocTitle(pdf, True)
except: prerr()
print('---cpdf_openAtPage')
try: pycpdf.openAtPage(pdf, True, 5)
except: prerr()
print('---cpdf_setMetadataFromFile')
try: pycpdf.setMetadataFromFile(pdf, 'testinputs/metadata.txt')
except: prerr()
print('---cpdf_setMetadataFromByteArray')
try: pycpdf.setMetadataFromByteArray(pdf, 'data')
except: prerr()
print('---cpdf_getMetadata')
try: metadata = pycpdf.getMetadata(pdf)
except: fatal_prerr()
print('---cpdf_removeMetadata')
try: pycpdf.removeMetadata(pdf)
except: prerr()
print('---cpdf_createMetadata')
try: pycpdf.createMetadata(pdf)
except: prerr()
print('---cpdf_setMetadataDate')
try: pycpdf.setMetadataDate(pdf, 'now')
except: prerr()
print('---cpdf_getPageLabels')
try: labels = pycpdf.getPageLabels(pdf)
except: fatal_prerr()
print(labels)
print('---cpdf_addPageLabels')
try: pycpdf.addPageLabels(pdf, (pycpdf.decimalArabic, "PRE-", 1, pycpdf.all(pdf)), False)
except: prerr()
print('---cpdf_removePageLabels')
try: pycpdf.removePageLabels(pdf)
except: prerr()
print('---cpdf_getPageLabelStringForPage')
try: labelString = pycpdf.getPageLabelStringForPage(pdf, 1)
except: fatal_prerr()

# CHAPTER 12. File Attachments
print('***** CHAPTER 12. File Attachments')
print('---cpdf_attachFile')
try: pycpdf.attachFile('testinputs/attach.txt', pdf)
except: prerr()
print('---cpdf_attachFileToPage')
try: pycpdf.attachFileToPage('testinputs/attach.txt', pdf, 1)
except: prerr()
print('---cpdf_attachFileFromMemory')
try: pycpdf.attachFileFromMemory('data', 'filename.txt', pdf)
except: prerr()
print('---cpdf_attachFileToPageFromMemory')
try: pycpdf.attachFileToPageFromMemory('data', 'filename.txt', pdf, 1)
except: prerr()
try: pycpdf.toFile('testoutputs/12with_attachments.pdf', False, False)
except: prerr()
print('---cpdf_removeAttachedFiles')
try: pycpdf.removeAttachedFiles(pdf)
except: prerr()
print('---cpdf_getAttachments')
try: attachments = pycpdf.getAttachments(pdf)
except: fatal_prerr()

# CHAPTER 13. Images
print('***** CHAPTER 13. Images')
print('---cpdf_getImageResolution')
try: images = pycpdf.getImageResolution(pdf, 300)
except: fatal_prerr()
print(images)

# CHAPTER 14. Fonts
print('***** CHAPTER 14. Fonts')
print('---cpdf_getFontInfo')
try: fonts = pycpdf.getFontInfo(pdf)
except: fatal_prerr()
print(fonts)
print('---cpdf_removeFonts')
try: pycpdf.removeFonts(pdf)
except: prerr()
try: pycpdf.toFile(fonts, 'testoutputs/14remove_fonts.pdf', False, False)
except: prerr()
print('---cpdf_copyFont')
try: pycpdf.copyFont(pdf, pdf2, r, 1, "/Font")
except: prerr()

# CHAPTER 15. PDF and JSON
print('***** CHAPTER 15. PDF and JSON')
try: pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
print('---cpdf_outputJSON')
try: pycpdf.outputjson('testoutputs/15json.json', false, false, pdf)
except: prerr()
try: pycpdf.outputjson('testoutputs/15jsonnostream.json', false, true, pdf)
except: prerr()
try: pycpdf.outputjson('testoutputs/15jsonparsed.json', true, false, pdf)
except: prerr()

# CHAPTER 16. Optional Content Groups
print('***** CHAPTER 16. Optional Content Groups')
try: pdf = pycpdf.fromFile('testinputs/has_ocgs.pdf', '')
except: fatal_prerr()
print('---cpdf_getOCGList')
try:
    ocgs = pycpdf.getOCGList(pdf)
    print(ocgs)
except: prerr()
print('---cpdf_OCGCoalesce')
try: pycpdf.OCGCoalesce(pdf)
except: prerr()
print('---cpdf_OCGRename')
try: pycpdf.OCGRename(pdf, 'one', 'two')
except: prerr()
print('---cpdf_OCGOrderAll')
try: pycpdf.OCGOrderAll(pdf)
except: prerr()

# CHAPTER 17. Miscellaneous
print('***** CHAPTER 17. Miscellaneous')
try: pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
except: fatal_prerr()
print('---cpdf_draft')
try: pycpdf.draft(pdf, r, True)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17draft.pdf', False, False)
except: prerr()
print('---cpdf_removeAllText')
try: pycpdf.removeAllText(pdf, r)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17removealltext.pdf', False, False)
except: prerr()
print('---cpdf_blackText')
try: pycpdf.blackText(pdf, r)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17blacktext.pdf', False, False)
except: prerr()
print('---cpdf_blackLines')
try: pycpdf.blackLines(pdf, r)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17blacklines.pdf', False, False)
except: prerr()
print('---cpdf_blackFills')
try: pycpdf.blackFills(pdf, r)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17blackfills.pdf', False, False)
except: prerr()
print('---cpdf_thinLines')
try: pycpdf.thinLines(pdf, r, 2.0)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17thinlines.pdf', False, False)
except: prerr()
print('---cpdf_copyId')
try: pycpdf.copyId(pdf, pdf2)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17copyid.pdf', False, False)
except: prerr()
print('---cpdf_removeId')
try: pycpdf.removeId(pdf)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17removeid.pdf', False, False)
except: prerr()
print('---cpdf_setVersion')
try: pycpdf.setVersion(pdf, 6)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17setversion.pdf', False, False)
except: prerr()
print('---cpdf_setFullVersion')
try: pycpdf.setFullVersion(pdf, 2, 0)
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17setfullversion.pdf', False, False)
except: prerr()
print('---cpdf_removeDictEntry')
try: pycpdf.removeDictEntry(pdf, '/Key')
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17removedictentry.pdf', False, False)
except: prerr()
print('---cpdf_removeClipping')
try: pycpdf.removeClipping(pdf, pycpdf.all(pdf))
except: prerr()
try: pycpdf.toFile(pdf, 'testoutputs/17removeclipping.pdf', False, False)
except: prerr()

# CHAPTER X. Undocumented or Internal
print('***** CHAPTER X. Undocumented or Internal')
print('---cpdf_setDemo')
try: pycpdf.setDemo(True)
except: prerr()
