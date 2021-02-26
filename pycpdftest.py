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
r = pycpdf.parsePagespec(pdf4, "1-3,end")
valid = pycpdf.validatePagespec("1-4,5,6")
pagespecstr = pycpdf.stringOfPagespec(pdf4, valid)
print(pagespecstr)
blankrange = pycpdf.blankRange()
pycpdf.deleteRange(blankrange)
fromto = pycpdf.pageRange(3, 7)
rall = pycpdf.all(pdf4)
even = pycpdf.even(rall)
odd = pycpdf.odd(rall)
union = pycpdf.rangeUnion(even, odd)
difference = pycpdf.difference(even, odd)
nodeps = pycpdf.removeDuplicates(rall)
rangel = pycpdf.rangeLength(union)
got = pycpdf.rangeGet(odd, 1)
added = pycpdf.rangeAdd(odd, 9)
inrange = pycpdf.isInRange(odd, 1)
pages = pycpdf.pages(pdf5)
pagesf = pycpdf.pagesFast('', 'testinputs/cpdfmanual.pdf')
pycpdf.toFile(pdf4, 'testoutputs/toFile.pdf', False, False)
pycpdf.toFileExt(pdf4, 'testoutputs/toFileExt.pdf', False, False, False, False, False)
tomembytes = pycpdf.toMemory(pdf5, False, False)
isenc = pycpdf.isEncrypted(pdf5)
pycpdf.toFileEncrypted(pdf5, pycpdf.pdf40bit, [pycpdf.noEdit], 'owner', 'user', False, False, 'testoutputs/enc.pdf')
pycpdf.toFileEncryptedExt(pdf5, pycpdf.pdf40bit, [pycpdf.noEdit], 'owner', 'user', False, False, False, False, False, 'testoutputs/enc2.pdf')
encpdf = pycpdf.fromFile('testoutputs/enc.pdf', 'user')
decrypted = pycpdf.decryptPdf(encpdf, 'user')
encpdf2 = pycpdf.fromFile('testoutputs/enc.pdf', 'user')
owner = pycpdf.decryptPdfOwner(encpdf2, 'owner')
hasperm = pycpdf.hasPermission(encpdf2, pycpdf.noEdit)
encmethod = pycpdf.encryptionKind(encpdf2)

# CHAPTER 2. Merging and Splitting
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
pdf2 = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
print(pdf, pdf2)
merged = pycpdf.mergeSimple([pdf, pdf2])
pycpdf.toFile(merged, 'testoutputs/merged.pdf', False, False)
merged2 = pycpdf.merge([pdf, pdf2], True, False)
pycpdf.toFile(merged2, 'testoutputs/merged2.pdf', False, False)
same = pycpdf.mergeSame([pdf, pdf2, pdf], True, False, [pycpdf.even(pdf), pycpdf.all(pdf2), pycpdf.odd(pdf)])
pycpdf.toFile(same, 'testoutputs/same.pdf', False, False)
selected = pycpdf.selectPages(pdf, pycpdf.even(pdf))
pycpdf.toFile(selected, 'testoutputs/selected.pdf', False, False)

# CHAPTER 3. Pages
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
r = pycpdf.all(pdf)
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
pycpdf.hardBox(pdf, r, "/MediaBox")

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression

pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
pycpdf.compress(pdf)
pycpdf.decompress(pdf)
pycpdf.squeezeInMemory(pdf)
pycpdf.toFile(pdf, 'testoutputs/squeezed.pdf', False, False)

# CHAPTER 6. Bookmarks

# Format: list of tuples. (level : int, page : int, text : string, openstatus : int/bool) 
existing_marks = pycpdf.getBookmarks(pdf)
print(existing_marks)
marks = [(0, 1, "new bookmark", True), (1, 3, "second, indented one", False)]
pycpdf.setBookmarks(pdf, marks)

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps

pycpdf.stampOn(pdf, pdf2, r)
pycpdf.stampUnder(pdf, pdf2, r)
pycpdf.stampExtended(pdf, pdf2, r, True, True, pycpdf.topLeft, False)
pycpdf.combinePages(pdf, pdf2)
"""
pycpdf.addText(False, pdf, r, 'The text', pycpdf.topLeft, 1.0, 0, pycpdf.timesRoman, 12, 0.5, 0.5, 0.5, False, False, False, 1.0, pycpdf.centreJustify, True, False, 'foo.pdf', 2.0, False)
pycpdf.addTextSimple(pdf, r, 'The text', pycpdf.centre, pycpdf.timesRoman, 12.0)
"""
pycpdf.removeText(pdf, r)
pycpdf.textWidth(pycpdf.timesRoman, 'Some text')

# CHAPTER 9. Multipage facilities
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
pycpdf.twoUp(pdf)
pycpdf.twoUpStack(pdf)
r = pycpdf.all(pdf)
pycpdf.padBefore(pdf, r)
pycpdf.padAfter(pdf, r)
pycpdf.padEvery(pdf, r)
pycpdf.padMultiple(pdf, 10)
pycpdf.padMultipleBefore(pdf, 10)
pycpdf.toFile(pdf, 'testoutputs/squeezed.pdf', False, False)

# CHAPTER 10. Annotations

# Not in the library version.

# CHAPTER 11. Document Information and Metadata
linearized = pycpdf.isLinearized('testinputs/cpdfmanual.pdf')
version = pycpdf.getVersion(pdf)
version2 = pycpdf.getMajorVersion(pdf)
title = pycpdf.getTitle(pdf)
print(f'title: {title}')
author = pycpdf.getAuthor(pdf)
print(f'author: {author}')
subject = pycpdf.getSubject(pdf)
print(f'subject: {subject}')
keywords = pycpdf.getKeywords(pdf)
print(f'keywords: {keywords}')
creator = pycpdf.getCreator(pdf)
print(f'creator: {creator}')
producer = pycpdf.getProducer(pdf)
print(f'producer: {producer}')
creationDate = pycpdf.getCreationDate(pdf)
print(f'creationDate: {creationDate}')
modificationDate = pycpdf.getModificationDate(pdf)
print(f'modificationDate: {modificationDate}')
titleXMP = pycpdf.getTitleXMP(pdf)
print(f'titleXMP: {titleXMP}')
authorXMP = pycpdf.getAuthorXMP(pdf)
print(f'authorXMP: {authorXMP}')
subjectXMP = pycpdf.getSubjectXMP(pdf)
print(f'subjectXMP: {subjectXMP}')
keywordsXMP = pycpdf.getKeywordsXMP(pdf)
print(f'keywordsXMP: {keywordsXMP}')
creatorXMP = pycpdf.getCreatorXMP(pdf)
print(f'creatorXMP: {creatorXMP}')
producerXMP = pycpdf.getProducerXMP(pdf)
print(f'producerXMP: {producerXMP}')
creationDateXMP = pycpdf.getCreationDateXMP(pdf)
print(f'creationDateXMP: {creationDateXMP}')
modificationDateXMP = pycpdf.getModificationDateXMP(pdf)
print(f'modificationDateXMP: {modificationDateXMP}')
pycpdf.setTitle(pdf, 'title')
pycpdf.setAuthor(pdf, 'author')
pycpdf.setSubject(pdf, 'subject')
pycpdf.setKeywords(pdf, 'keywords')
pycpdf.setCreator(pdf, 'creator')
pycpdf.setProducer(pdf, 'producer')
pycpdf.setCreationDate(pdf, 'now')
pycpdf.setModificationDate(pdf, 'now')
pycpdf.setTitleXMP(pdf, 'title')
pycpdf.setAuthorXMP(pdf, 'author')
pycpdf.setSubjectXMP(pdf, 'subject')
pycpdf.setKeywordsXMP(pdf, 'keywords')
pycpdf.setCreatorXMP(pdf, 'creator')
pycpdf.setProducerXMP(pdf, 'producer')
pycpdf.setCreationDateXMP(pdf, 'now')
pycpdf.setModificationDateXMP(pdf, 'now')
"""
components = pycpdf.getDateComponents('DATE')
dateString = pycpdf.dateStringOfComponents(1, 2, 3, 4, 5, 6, 7, 8, 9)
"""
rot = pycpdf.getPageRotation(pdf, 1)
hasBox = pycpdf.hasBox(pdf, 1, '/TrimBox')
"""
mediaBox = pycpdf.getMediaBox(pdf, 1)
cropBox = pycpdf.getCropBox(pdf, 1)
trimBox = pycpdf.getTrimBox(pdf, 1)
artBox = pycpdf.getArtBox(pdf, 1)
bleedBox = pycpdf.getBleedBox(pdf, 1)
"""
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
pycpdf.setMetadataFromFile(pdf, 'testinputs/metadata.txt')
pycpdf.setMetadataFromByteArray(pdf, 'data')

"""
metadata = pycpdf.getMetadata(pdf)
"""
pycpdf.removeMetadata(pdf)
pycpdf.createMetadata(pdf)
pycpdf.setMetadataDate(pdf, 'now')

"""
labels = []
pycpdf.addPageLabels(pdf, labels)
pycpdf.removePageLabels(pdf)
labelString = pycpdf.getPageLabelStringForPage(pdf, 1)
labels = pycpdf.getPageLabels(pdf)

# CHAPTER 12. File Attachments

"""
pycpdf.attachFile('testinputs/attach.txt', pdf)
pycpdf.attachFileToPage('testinputs/attach.txt', pdf, 1)
pycpdf.attachFileFromMemory('data', 'filename.txt', pdf)
pycpdf.attachFileToPageFromMemory('data', 'filename.txt', pdf, 1)
pycpdf.removeAttachedFiles(pdf)

"""
attachments = pycpdf.getAttachments(pdf)

# CHAPTER 13. Images

images = pycpdf.getImageResolution(pdf, 300)

# CHAPTER 14. Fonts

fonts = pycpdf.getFontInfo(pdf)
pycpdf.removeFonts(pdf)
pycpdf.copyFont(pdf, pdf2, r, 1, "/Font")

"""
# CHAPTER 15. Miscellaneous

pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
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
pycpdf.toFile(pdf, 'testoutputs/squeezed.pdf', False, False)

# CHAPTER UNDOC (To come in v2.4)

pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
pycpdf.addContent('content', True, pdf, pycpdf.all(pdf))
pycpdf.outputJSON('testoutputs/filename.txt', True, False, pdf)
pycpdf.OCGCoalesce(pdf)
pycpdf.OCGRename(pdf, 'one', 'two')
pycpdf.OCGOrderAll(pdf)
name = pycpdf.stampAsXObject(pdf, True, pdf2)
pycpdf.setDemo(True)
