import pycpdf

pycpdf.loadDLL("/Users/john/repos/python-libcpdf/libpycpdf.so")
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
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
pdf2 = pycpdf.fromFileLazy('testinputs/cpdfmanual.pdf', '')
fh = open('testinputs/cpdfmanual.pdf', mode='rb')
data = fh.read()
pdf3 = pycpdf.fromMemory(data, '')
pdf4 = pycpdf.fromMemoryLazy(data, '')
pdf5 = pycpdf.blankDocument(200.5, 100.0, 50)
pycpdf.toFile(pdf5, 'testoutputs/blank.pdf', False, False)
pdf6 = pycpdf.blankDocumentPaper(pycpdf.a3landscape, 50)
pycpdf.toFile(pdf6, 'testoutputs/blank2.pdf', False, False)
pycpdf.deletePdf(pdf)
pycpdf.replacePdf(pdf2, pdf3)
pdfs = pycpdf.enumeratePDFs()
for k, i in pdfs:
  print(k, i)
print(pycpdf.ptOfCm(1.0))
print(pycpdf.ptOfMm(1.0))
print(pycpdf.ptOfIn(1.0))
print(pycpdf.cmOfPt(1.0))
print(pycpdf.mmOfPt(1.0))
print(pycpdf.inOfPt(1.0))
"""
r = pycpdf.parsePagespec(pdf, "1-3,end")
valid = pycpdf.validatePagespec("1-4,5,6")
pagespecstr = pycpdf.stringOfPagespec(pdf, valid)
blankrange = pycpdf.blankRange()
pycpdf.deleteRange(blankrange)
fromto = pycpdf.range(3, 7)
rall = pycpdf.all(pdf4)
even = pycpdf.even(rall)
odd = pycpdf.odd(rall)
union = pycpdf.rangeUnion(even, odd)
difference = pycpdf.rangeDifference(even, odd)
nodeps = pycpdf.removeDuplicates(rall)
rangel = pycpdf.rangeLength(union)
got = pycpdf.rangeGet(odd, 1)
added = pycpdf.rangeAdd(odd, 9)
inrange = pycpdf.isInRange(odd, 1)
pages = pycpdf.pages(pdf5)
pagesf = pycpdf.pagesFast('cpdfmanual.pdf', '')
pycpdf.toFile(pdf, 'out.pdf', False, False)
pycpdf.toFileExt(pdf, 'out.pdf', False, False, False, False, False)
mem, memlength = pycpdf.toMemory(pdf5, False, False)
isenc = pycpdf.isEncrypted(pdf)
decrypted = pycpdf.decryptPdf(pdf, 'foo')
owner = pycpdf.decryptPdfOwner(pdf, 'foo')
pycpdf.toFileEncrypted(pdf, pycpdf.pdf40bit, [pycpdf.noEdit], 'owner', 'user', False, False, 'enc.pdf')
pycpdf.toFileEncryptedEnc(pdf, pycpdf.pdf40bit, [pycpdf.noEdit], 'owner', 'user', False, False, False, False, False, 'enc2.pdf')
hasperm = pycpdf.hasPermission(pdf, pycpdf.noEdit)
encmethod = pycpdf.encryptionKind(pdf)

# CHAPTER 2. Merging and Splitting
pycpdf.mergeSimple([pdf, pdf2, pdf3])
pycpdf.merge([pdf, pdf2, pdf3], True, False, [[1, 2], [3, 4], [5, 6]])
pycpdf.mergeSame([pdf, pdf2, pdf], True, False, [[1, 2], [3, 4], [5, 6]])
pycpdf.selectPages(pdf, pycpdf.range_even(pdf))

# CHAPTER 3. Pages
r = pycpdf.range_all(pdf)
pycpdf.scalePages(pdf, r, 0.5, 0.7)
pycpdf.scaleToFit(pdf, r, 0.5, 0.7, 0.5)
pycpdf.scaleToFitPaper(pdf, r, pycpdf.a3landscape, 0.5)
pycpdf.scaleContents(pdf, r, (pycpdf.top, 10, 10), 1.0)
pycpdf.shiftContents(pdf, r, 100, -100)
pycpdf.rotate(pdf, r, 90)
pycpdf.rotateBy(pdf, r, 180)
pycpdf.rotateContents(pdf, r, 43.3)
pycpdf.upright(pdf, r)
pycpdf.hFlip(pdf, r)
pycpdf.vFlip(pdf, r)
pycpdf.crop(pdf, r, 100.0, 100.0, 400.0, 400.0)
pycpdf.removeCrop(pdf, r)
pycpdf.removeTrim(pdf, r)
pycpdf.removeArt(pdf, r)
pycpdf.removeBleed(pdf, r)
pycpdf.trimMarks(pdf, r)
pycpdf.showBoxes(pdf, r)
pycpdf.hardBox(pdf, r, "/TrimBox")

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression

pycpdf.compress(pdf)
pycpdf.decompres(pdf)
pycpdf.squeezeInMemory(pdf)

# CHAPTER 6. Bookmarks

pycpdf.getBookmarks(pdf)
pycpdf.setBookmarks(pdf)

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps

pycpdf.stampOn(pdf, pdf2, r)
pycpdf.stampUnder(pdf, pdf2, r)
pycpdf.stampExtended(pdf, pdf2, r, True, True, pycpdf.topLeft, False)
pycpdf.combinePages(pdf, pdf2)
pycpdf.addText(False, pdf, r, 'The text', 1.0, 0, 12, 0.5, 0.5, 0.5, 0.6, cpdf.JustifyCentre, True, False, 'foo.pdf', 2.0, False)
pycpdf.addTextSimple(pdf, r, 'The text', pycpdf.centre, pycpdf.TimesNewRoman, 12.0)
pycpdf.removeText(pdf)
pycpdf.textWidth(pycpdf.TimesNewRoman, 'Some text')

# CHAPTER 9. Mulitpage facilities
pycpdf.twoUp(pdf)
pycpdf.towUpStack(pdf)
pycpdf.padBefore(pdf, r)
pycpdf.padAfter(pdf, r)
pycpdf.padEvery(pdf, r)
pycpdf.padMulitple(pdf, 10)
pycpdf.padMultipleBefore(pdf, 10)

# CHAPTER 10. Annotations

# Not in the library version.

# CHAPTER 11. Document Information and Metadata

pycpdf.isLinearized('cpdfmanual.pdf')
version = pycpdf.getVersion(pdf)
version2 = pycpdf.getMajorVersion(pdf)
title = pycpdf.getTitle(pdf)
author = pycpdf.getAuthor(pdf)
subject = pycpdf.getSubject(pdf)
keywords = pycpdf.getKeywords(pdf)
creator = pycpdf.getCreator(pdf)
producer = pycpdf.getProducer(pdf)
creationDate = pycpdf.getCreationDate(pdf)
modificationDate = pycpdf.getModificationDate(pdf)
titleXMP = pycpdf.getTitleXMP(pdf)
authorXMP = pycpdf.getAuthorXMP(pdf)
subjectXMP = pycpdf.getSubjectXMP(pdf)
keywordsXMP = pycpdf.getKeywordsXMP(pdf)
creatorXMP = pycpdf.getCreatorXMP(pdf)
producerXMP = pycpdf.getProducerXMP(pdf)
creationDateXMP = pycpdf.getCreationDateXMP(pdf)
modificationDateXMP = pycpdf.getModificationDateXMP(pdf)
pycpdf.setTitle(pdf, 'title')
pycpdf.setAuthor(pdf, 'author')
pycpdf.setSubject(pdf, 'subject')
pycpdf.setKeywords(pdf, 'keywords')
pycpdf.setCreator(pdf, 'creator')
pycpdf.setProducer(pdf, 'producer')
pycpdf.setCreationDate(pdf, 'DATE')
pycpdf.setModificationDate(pdf, 'DATE')
pycpdf.setTitleXMP(pdf, 'title')
pycpdf.setAuthorXMP(pdf. 'author')
pycpdf.setSubjectXMP(pdf, 'subject')
pycpdf.setKeywordsXMP(pdf, 'keywords')
pycpdf.setCreatorXMP(pdf, 'creator')
pycpdf.setProducerXMP(pdf, 'producer')
pycpdf.setCreationDateXMP(pdf, 'DATE')
pycpdf.setModificationDateXMP(pdf, 'DATE')
components = pycpdf.getDateComponents('DATE')
dateString = pycpdf.dateStringOfComponents(1, 2, 3, 4, 5, 6, 7, 8, 9)
rot = pycpdf.getPageRotation(pdf, r)
hasBox = pycpdf.hasBox(pdf, 1, '/TrimBox')
mediaBox = pycpdf.getMediaBox(pdf, 1)
cropBox = pycpdf.getCropBox(pdf, 1)
trimBox = pycpdf.getTrimBox(pdf, 1)
artBox = pycpdf.getArtBox(pdf, 1)
bleedBox = pycpdf.getBleedBox(pdf, 1)
pycpdf.setMediaBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
pycpdf.setCropBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
pycpdf.setTrimBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
pycpdf.setArtBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
pycpdf.setBleedBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)

pycpdf.markTrapped(pdf)
pycpdf.markUntrapped(pdf)
pycpdf.markTrappedXMP(pdf)
pycpdf.markUntrappedXMP(pdf)
pycpdf.setPageLayout(pdf, pycpdf.singlePage)
pycpdf.setPageMode(pdf, pycpdf.useThumbs)
pycpdf.hideToolbar(pdf, True)
pycpdf.hideMenubar(pdf, False)
pycpdf.hideWindowUi(pdf, True)
pycpdf.fitWindow(pdf, True)
pycpdf.centerWindow(pdf, True)
pycpdf.displayDocTitle(pdf, True)
pycpdf.openAtPage(pdf, True, 5)
pycpdf.setMetadataFromFile(pdf, 'metadata.txt')
pycpdf.setMetadataFromByteArray(pdf, b'data')
metadata = pycpdf.getMetadata(pdf)
pycpdf.removeMetadata(pdf)
pycpdf.createMetadata(pdf)
pycpdf.setMetadataDate(pdf, 'DATE')
labels = []
pycpdf.addPageLabels(pdf, labels)
pycpdf.removePageLabels(pdf)
labelString = pycpdf.getPageLabelStringForPage(pdf, 1)
labels = pycpdf.getPageLabels(pdf)

# CHAPTER 12. File Attachments

pycpdf.attachFile('attach.txt', pdf)
pycpdf.attachFileToPage('attach.txt', pdf, 1)
pycpdf.attachFileFromMemory(b'data', 'filename.txt', pdf)
pycpdf.attachFileToPageFromMemory(b'data', 'filename.txt', pdf, 1)
pycpdf.removeAttachedFiles(pdf)
attachments = pycpdf.getAttachments(pdf)

# CHAPTER 13. Images

images = pycpdf.getImageResolution(pdf, 300)

# CHAPTER 14. Fonts

fonts = pycpdf.getFontInfo(pdf)
pycpdf.removeFonts(pdf)
pycpdf.copyFont(pdf, pdf2, r, 1, "/Font")

# CHAPTER 15. Miscellaneous

pycpdf.draft(pdf, r, True)
pycpdf.removeAllText(pdf, r)
pycpdf.blackText(pdf, r)
pycpdf.blackLines(pdf, r)
pycpdf.blackFills(pdf, r)
pycpdf.thinLines(pdf, r, 2.0)
pycpdf.copyId(pdf, pdf2)
pycpdf.removeId(pdf)
pycpdf.setVersion(pdf, 6)
pycpdf.removeDictEntry(pdf, '/Key')
pycpdf.removeClipping(pdf, 1)

# CHAPTER UNDOC (To come in v2.4)

pycpdf.addContent(b'content', pdf, 1, True)
pycpdf.outputJSON('filename.txt', pdf, 1, True)
pycpdf.OCGCoalesce(pdf)
pycpdf.OCGRename(pdf, 'one', 'two')
pycpdf.OCGOrderAll(pdf)
name = pycpdf.stampAsXObject(pdf, pdf2, True)
pycpdf.setDemo(True)
"""
