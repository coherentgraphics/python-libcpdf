#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cpdflibwrapper.h"

/* CHAPTER 0. Preliminaries */

int pycpdf_startup(char** argv)
{
   //char *argv[] = {"program_name", NULL};
   cpdf_startup(argv);
   return 0;
}

char *pycpdf_version(void)
{
  return cpdf_version();
}

void pycpdf_setFast(void)
{
  cpdf_setFast();
  return;
}

void pycpdf_setSlow(void)
{
  cpdf_setSlow();
  return;
}

int pycpdf_lastError(void)
{
  return cpdf_lastError;
}

char *pycpdf_lastErrorString(void)
{
  //printf("cpdf_lastErrorString is %s\n", cpdf_lastErrorString);
  return cpdf_lastErrorString;
}

void pycpdf_clearError(void)
{
  cpdf_clearError();
  cpdf_lastError = 0;
  cpdf_lastErrorString = "";
  //printf("after clearerror, cpdf_lastErrorString is %s\n", cpdf_lastErrorString);
  return;
}

void pycpdf_onExit(void)
{
  cpdf_onExit();
  return;
}

/* CHAPTER 1. Basics */
int pycpdf_fromFile(char *filename, char *userpw)
{
  return cpdf_fromFile(filename, userpw);
}

int pycpdf_fromFileLazy(char *filename, char *userpw)
{
  return cpdf_fromFileLazy(filename, userpw);
}

int pycpdf_fromMemory(void* data, int len, char *userpw)
{
  return cpdf_fromMemory(data, len, userpw);
}

int pycpdf_fromMemoryLazy(void* data, int len, char *userpw)
{
  return cpdf_fromMemoryLazy(data, len, userpw);
}

int pycpdf_blankDocument(double w, double h, int pages)
{
  return cpdf_blankDocument(w, h, pages);
}

int pycpdf_blankDocumentPaper(int papersize, int pages)
{
  return cpdf_blankDocumentPaper(papersize, pages);
}

void pycpdf_deletePdf(int pdf)
{
  return cpdf_deletePdf(pdf);
}

void pycpdf_replacePdf(int pdf, int pdf2)
{
  return cpdf_replacePdf(pdf, pdf2);
}

double pycpdf_ptOfCm(double i)
{
  return cpdf_ptOfCm(i);
}

double pycpdf_ptOfMm(double i)
{
  return cpdf_ptOfMm(i);
}

double pycpdf_ptOfIn(double i)
{
  return cpdf_ptOfIn(i);
}

double pycpdf_cmOfPt(double i)
{
  return cpdf_cmOfPt(i);
}

double pycpdf_mmOfPt(double i)
{
  return cpdf_mmOfPt(i);
}

double pycpdf_inOfPt(double i)
{
  return cpdf_inOfPt(i);
}

void pycpdf_startEnumeratePDFs(void)
{
  cpdf_startEnumeratePDFs();
  return;
}

int pycpdf_enumeratePDFsKey(int n)
{
  return cpdf_enumeratePDFsKey(n);
}

char *pycpdf_enumeratePDFsInfo(int n)
{
  return cpdf_enumeratePDFsInfo(n);
}

void pycpdf_endEnumeratePDFs(void)
{
  cpdf_endEnumeratePDFs();
  return;
}

int pycpdf_parsePagespec(int pdf, char *pagespec)
{
  return cpdf_parsePagespec(pdf, pagespec);
}

int pycpdf_validatePagespec(char *pagespec)
{
  return cpdf_validatePagespec(pagespec);
}

char *pycpdf_stringOfPagespec(int pdf, int range)
{
  return cpdf_stringOfPagespec(pdf, range);
}

int pycpdf_blankRange(void)
{
  return cpdf_blankRange();
}

void pycpdf_deleteRange(int r)
{
  return cpdf_deleteRange(r);
}

int pycpdf_pageRange(int f, int t)
{
  return cpdf_range(f, t);
}

int pycpdf_all(int r)
{
  return cpdf_all(r);
}

int pycpdf_even(int r)
{
  return cpdf_even(r);
}

int pycpdf_odd(int r)
{
  return cpdf_odd(r);
}

int pycpdf_rangeUnion(int a, int b)
{
  return cpdf_rangeUnion(a, b);
}

int pycpdf_difference(int a, int b)
{
  return cpdf_difference(a, b);
}

int pycpdf_removeDuplicates(int r)
{
  return cpdf_removeDuplicates(r);
}

int pycpdf_rangeLength(int r)
{
  return cpdf_rangeLength(r);
}

int pycpdf_rangeGet(int r, int n)
{
  return cpdf_rangeGet(r, n);
}

int pycpdf_rangeAdd(int r, int p)
{
  return cpdf_rangeAdd(r, p);
}

int pycpdf_isInRange(int r, int p)
{
  return cpdf_isInRange(r, p);
}

int pycpdf_pages(int pdf)
{
  return cpdf_pages(pdf);
}

int pycpdf_pagesFast(char *filename, char *userpw)
{
  return cpdf_pagesFast(filename, userpw);
}

void pycpdf_toFile(int pdf, char *filename, int linearize, int make_id)
{
  cpdf_toFile(pdf, filename, linearize, make_id);
  return;
}

void pycpdf_toFileExt(int pdf, char *filename, int linearize, int make_id, int preserve_objstm, int generate_objstm, int compress_objstm)
{
  cpdf_toFileExt(pdf, filename, linearize, make_id, preserve_objstm, generate_objstm, compress_objstm);
}

//We want to return a piece of memory which will be copied into a python string, and the C string deallocated.
void *toMemoryData;

void *pycpdf_toMemory(int pdf, int linearize, int make_id, int *length)
{
  toMemoryData = cpdf_toMemory(pdf, linearize, make_id, length);
  return toMemoryData;
}

void pycpdf_toMemoryFree(void)
{
  free(toMemoryData);
  return;
}

int pycpdf_isEncrypted(int pdf)
{
  return cpdf_isEncrypted(pdf);
}

void pycpdf_toFileEncrypted(int pdf, int method, int *permissions, int permlength, char *ownerpw, char *userpw, int linearize, int makeid, char *filename)
{
  cpdf_toFileEncrypted(pdf, method, permissions, permlength, ownerpw, userpw, linearize, makeid, filename);
  return;
}

void pycpdf_toFileEncryptedExt(int pdf, int method, int *permissions, int permlength, char* ownerpw, char *userpw,
                               int linearize, int makeid, int preserve_objstm, int generate_objstm, int compress_objstm, char* filename)
{
  cpdf_toFileEncryptedExt(pdf, method, permissions, permlength, ownerpw, userpw, linearize, makeid, preserve_objstm, generate_objstm, compress_objstm, filename);
  return;
}

void pycpdf_decryptPdf(int pdf, char *userpw)
{
  cpdf_decryptPdf(pdf, userpw);
  return;
}

void pycpdf_decryptPdfOwner(int pdf, char *ownerpw)
{
  cpdf_decryptPdfOwner(pdf, ownerpw);
  return;
}

int pycpdf_hasPermission(int pdf, int perm)
{
  return cpdf_hasPermission(pdf, perm);
}

int pycpdf_encryptionKind(int pdf)
{
  return cpdf_encryptionKind(pdf);
}

int pycpdf_mergeSimple(int *pdfs, int len)
{
  return cpdf_mergeSimple(pdfs, len);
}

int pycpdf_merge(int *pdfs, int len, int retain_numbering, int remove_duplicate_fonts)
{
  return cpdf_merge(pdfs, len, retain_numbering, remove_duplicate_fonts);
}

int pycpdf_mergeSame(int *pdfs, int len, int retain_numbering, int remove_duplicate_fonts, int *ranges)
{
  return cpdf_mergeSame(pdfs, len, retain_numbering, remove_duplicate_fonts, ranges);
}

int pycpdf_selectPages(int pdf, int r)
{
  return cpdf_selectPages(pdf, r);
}

/* CHAPTER 3. Pages */

void pycpdf_scalePages(int pdf, int r, double sx, double sy)
{
  cpdf_scalePages(pdf, r, sx, sy);
}

void pycpdf_scaleToFit(int pdf, int r, double sx, double sy, double scale_to_fit_scale)
{
  cpdf_scaleToFit(pdf, r, sx, sy, scale_to_fit_scale);
}

void pycpdf_scaleToFitPaper(int pdf, int r, int papersize, double scale_to_fit_scale)
{
  cpdf_scaleToFitPaper(pdf, r, papersize, scale_to_fit_scale);
}

void pycpdf_scaleContents(int pdf, int r, int pos, double p1, double p2, double scale)
{
  struct cpdf_position p = {.cpdf_anchor = pos,.cpdf_coord1 = p1,.cpdf_coord2 = p2};
  cpdf_scaleContents(pdf, r, p, scale);
}

void pycpdf_shiftContents(int pdf, int r, double dx, double dy)
{
  cpdf_shiftContents(pdf, r, dx, dy);
}

void pycpdf_rotate(int pdf, int r, int rotation)
{
  cpdf_rotate(pdf, r, rotation);
}

void pycpdf_rotateBy(int pdf, int r, int rotation)
{
  cpdf_rotateBy(pdf, r, rotation);
}

void pycpdf_rotateContents(int pdf, int r, double rotation)
{
  cpdf_rotateContents(pdf, r, rotation);
}

void pycpdf_upright(int pdf, int r)
{
  cpdf_upright(pdf, r);
}

void pycpdf_hFlip(int pdf, int r)
{
  cpdf_hFlip(pdf, r);
}

void pycpdf_vFlip(int pdf, int r)
{
  cpdf_vFlip(pdf, r);
}

void pycpdf_crop(int pdf, int r, double x, double y, double w, double h)
{
  cpdf_crop(pdf, r, x, y, w, h);
}

void pycpdf_removeCrop(int pdf, int r)
{
  cpdf_removeCrop(pdf, r);
}

void pycpdf_removeTrim(int pdf, int r)
{
  cpdf_removeTrim(pdf, r);
}

void pycpdf_removeArt(int pdf, int r)
{
  cpdf_removeArt(pdf, r);
}

void pycpdf_removeBleed(int pdf, int r)
{
  cpdf_removeBleed(pdf, r);
}

void pycpdf_trimMarks(int pdf, int r)
{
  cpdf_trimMarks(pdf, r);
}

void pycpdf_showBoxes(int pdf, int r)
{
  cpdf_showBoxes(pdf, r);
}

void pycpdf_hardBox(int pdf, int r, char *boxname)
{
  cpdf_hardBox(pdf, r, boxname);
}


/* CHAPTER 4. Encryption */

/* Encryption covered under Chapter 1 in cpdflib. */


/* CHAPTER 5. Compression */

void pycpdf_compress(int pdf)
{
  cpdf_compress(pdf);
  return;
}

void pycpdf_decompress(int pdf)
{
  cpdf_decompress(pdf);
  return;
}

void pycpdf_squeezeInMemory(int pdf)
{
  cpdf_squeezeInMemory(pdf);
  return;
}


/* CHAPTER 6. Bookmarks */

void pycpdf_startGetBookmarkInfo(int pdf)
{
  cpdf_startGetBookmarkInfo(pdf);
  return;
}

int pycpdf_numberBookmarks()
{
  return cpdf_numberBookmarks();
}

int pycpdf_getBookmarkLevel(int n)
{
  return cpdf_getBookmarkLevel(n);
}

int pycpdf_getBookmarkPage(int pdf, int page)
{
  return cpdf_getBookmarkPage(pdf, page);
}

char *pycpdf_getBookmarkText(int n)
{
  return cpdf_getBookmarkText(n);
}

int pycpdf_getBookmarkOpenStatus(int n)
{
  return cpdf_getBookmarkOpenStatus(n);
}

void pycpdf_endGetBookmarkInfo()
{
  cpdf_endGetBookmarkInfo();
  return;
}

void pycpdf_startSetBookmarkInfo(int n)
{
  cpdf_startSetBookmarkInfo(n);
  return;
}

void pycpdf_setBookmarkLevel(int n, int level)
{
  cpdf_setBookmarkLevel(n, level);
  return;
}

void pycpdf_setBookmarkPage(int pdf, int n, int targetpage)
{
  cpdf_setBookmarkPage(pdf, n, targetpage);
  return;
}

void pycpdf_setBookmarkOpenStatus(int n, int status)
{
  cpdf_setBookmarkOpenStatus(n, status);
  return;
}

void pycpdf_setBookmarkText(int n, char *text)
{
  cpdf_setBookmarkText(n, text);
  return;
}

void pycpdf_endSetBookmarkInfo(int pdf)
{
  cpdf_endSetBookmarkInfo(pdf);
  return;
}

/* CHAPTER 7. Presentations */

/* Not included in the library version */

/* CHAPTER 8. Logos, Watermarks and Stamps */

void pycpdf_stampOn(int pdf, int pdf2, int r)
{
  cpdf_stampOn(pdf, pdf2, r);
  return;
}

void pycpdf_stampUnder(int pdf, int pdf2, int r)
{
  cpdf_stampUnder(pdf, pdf2, r);
  return;
}

void pycpdf_stampExtended(int pdf, int pdf2, int r, int isover, int scale_stamp_to_fit, int pos, int relative_to_cropbox)
{
  struct cpdf_position position = {.cpdf_anchor = pos,.cpdf_coord1 = 0.0,.cpdf_coord2 = 0.0};
  cpdf_stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, position, relative_to_cropbox);
  return;
}

void pycpdf_combinePages(int pdf, int pdf2)
{
  cpdf_combinePages(pdf, pdf2);
  return;
}

void pycpdf_addText(int metrics, int pdf, int r, char *text, int pos, double p1, double p2, double line_spacing, int bates, int font, double size, double red, double green, double blue, int underneath, int relative_to_cropbox, int outline, double opacity, int justification, int midline, int topline, char* filename, double line_width, int embed_fonts)
{
  struct cpdf_position position = {.cpdf_anchor = pos,.cpdf_coord1 = p1,.cpdf_coord2 = p2};
  cpdf_addText(metrics, pdf, r, text, position, line_spacing, bates, font, size, red, green, blue, underneath, relative_to_cropbox, outline, opacity, justification, midline, topline, filename, line_width, embed_fonts);
  return;

}

void pycpdf_addTextSimple(int pdf, int r, char *text, int pos, double p1, double p2, int font, double size)
{
  struct cpdf_position position = {.cpdf_anchor = pos,.cpdf_coord1 = p1,.cpdf_coord2 = p2};
  cpdf_addTextSimple(pdf, r, text, position, font, size);
  return;
}

void pycpdf_removeText(int pdf, int r)
{
  cpdf_removeText(pdf, r);
  return;
}

int pycpdf_textWidth(int font, char *string)
{
  return cpdf_textWidth(font, string);
}


/* CHAPTER 9. Multipage facilities */
void pycpdf_twoUp(int pdf)
{
  cpdf_twoUp(pdf);
  return;
}

void pycpdf_twoUpStack(int pdf)
{
  cpdf_twoUp(pdf);
  return;
}

void pycpdf_padBefore(int pdf, int r)
{
  cpdf_padBefore(pdf, r);
  return;
}

void pycpdf_padAfter(int pdf, int r)
{
  cpdf_padAfter(pdf, r);
  return;
}

void pycpdf_padEvery(int pdf, int r)
{
  cpdf_padEvery(pdf, r);
  return;
}

void pycpdf_padMultiple(int pdf, int n)
{
  cpdf_padMultiple(pdf, n);
  return;
}

void pycpdf_padMultipleBefore(int pdf, int n)
{
  cpdf_padMultiple(pdf, n);
  return;
}

/* CHAPTER 11. Document Information and Metadata */
int pycpdf_isLinearized(char *filename)
{
  return cpdf_isLinearized(filename);
}

int pycpdf_getVersion(int pdf)
{
  return cpdf_getVersion(pdf);
}

int pycpdf_getMajorVersion(int pdf)
{
  return cpdf_getMajorVersion(pdf);
}

char* pycpdf_getTitle(int pdf)
{
  return cpdf_getTitle(pdf);
}

char* pycpdf_getAuthor(int pdf)
{
  return cpdf_getAuthor(pdf);
}

char* pycpdf_getSubject(int pdf)
{
  return cpdf_getSubject(pdf);
}

char* pycpdf_getKeywords(int pdf)
{
  return cpdf_getKeywords(pdf);
}

char* pycpdf_getCreator(int pdf)
{
  return cpdf_getCreator(pdf);
}

char* pycpdf_getProducer(int pdf)
{
  return cpdf_getProducer(pdf);
}

char* pycpdf_getCreationDate(int pdf)
{
  return cpdf_getCreationDate(pdf);
}

char* pycpdf_getModificationDate(int pdf)
{
  return cpdf_getModificationDate(pdf);
}

char* pycpdf_getTitleXMP(int pdf)
{
  return cpdf_getTitleXMP(pdf);
}

char* pycpdf_getAuthorXMP(int pdf)
{
  return cpdf_getAuthorXMP(pdf);
}

char* pycpdf_getSubjectXMP(int pdf)
{
  return cpdf_getSubjectXMP(pdf);
}

char* pycpdf_getKeywordsXMP(int pdf)
{
  return cpdf_getKeywordsXMP(pdf);
}

char* pycpdf_getCreatorXMP(int pdf)
{
  return cpdf_getCreatorXMP(pdf);
}

char* pycpdf_getProducerXMP(int pdf)
{
  return cpdf_getProducerXMP(pdf);
}

char* pycpdf_getCreationDateXMP(int pdf)
{
  return cpdf_getCreationDateXMP(pdf);
}

char* pycpdf_getModificationDateXMP(int pdf)
{
  return cpdf_getModificationDateXMP(pdf);
}

void pycpdf_setTitle(int pdf, char *s)
{
  cpdf_setTitle(pdf, s);
  return;
}

void pycpdf_setAuthor(int pdf, char *s)
{
  cpdf_setAuthor(pdf, s);
  return;
}

void pycpdf_setSubject(int pdf, char *s)
{
  cpdf_setSubject(pdf, s);
  return;
}

void pycpdf_setKeywords(int pdf, char *s)
{
  cpdf_setKeywords(pdf, s);
  return;
}

void pycpdf_setCreator(int pdf, char *s)
{
  cpdf_setCreator(pdf, s);
  return;
}

void pycpdf_setProducer(int pdf, char *s)
{
  cpdf_setProducer(pdf, s);
  return;
}

void pycpdf_setCreationDate(int pdf, char *s)
{
  cpdf_setCreationDate(pdf, s);
  return;
}

void pycpdf_setModificationDate(int pdf, char *s)
{
  cpdf_setModificationDate(pdf, s);
  return;
}

void pycpdf_setTitleXMP(int pdf, char *s)
{
  cpdf_setTitleXMP(pdf, s);
  return;
}

void pycpdf_setAuthorXMP(int pdf, char *s)
{
  cpdf_setAuthorXMP(pdf, s);
  return;
}

void pycpdf_setSubjectXMP(int pdf, char *s)
{
  cpdf_setSubjectXMP(pdf, s);
  return;
}

void pycpdf_setKeywordsXMP(int pdf, char *s)
{
  cpdf_setKeywordsXMP(pdf, s);
  return;
}

void pycpdf_setCreatorXMP(int pdf, char *s)
{
  cpdf_setCreatorXMP(pdf, s);
  return;
}

void pycpdf_setProducerXMP(int pdf, char *s)
{
  cpdf_setProducerXMP(pdf, s);
  return;
}

void pycpdf_setCreationDateXMP(int pdf, char *s)
{
  cpdf_setCreationDateXMP(pdf, s);
  return;
}

void pycpdf_setModificationDateXMP(int pdf, char *s)
{
  cpdf_setModificationDateXMP(pdf, s);
  return;
}

void pycpdf_getDateComponents(char *str, int *year, int *month, int *day, int *hour, int *minute, int *second, int *hour_offset, int *minute_offset)
{
  cpdf_getDateComponents(str, year, month, day, hour, minute, second, hour_offset, minute_offset);
  return;
}

char *pycpdf_dateStringOfComponents(int year, int month, int day, int hour, int minute, int second, int hour_offset, int minute_offset)
{
  return cpdf_dateStringOfComponents(year, month, day, hour, minute, second, hour_offset, minute_offset);
}

int pycpdf_getPageRotation(int pdf, int pagenumber)
{
  return cpdf_getPageRotation(pdf, pagenumber);
}

int pycpdf_hasBox(int pdf, int pagenumber, char *box)
{
  return cpdf_hasBox(pdf, pagenumber, box);
}

void pycpdf_getMediaBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy)
{
  cpdf_getMediaBox(pdf, pagenumber, minx, maxx, miny, maxy);
  return;
}

void pycpdf_getCropBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy)
{
  cpdf_getCropBox(pdf, pagenumber, minx, maxx, miny, maxy);
  return;
}

void pycpdf_getTrimBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy)
{
  cpdf_getTrimBox(pdf, pagenumber, minx, maxx, miny, maxy);
  return;
}

void pycpdf_getArtBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy)
{
  cpdf_getArtBox(pdf, pagenumber, minx, maxx, miny, maxy);
  return;
}

void pycpdf_getBleedBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy)
{
  cpdf_getBleedBox(pdf, pagenumber, minx, maxx, miny, maxy);
  return;
}

void pycpdf_setMediaBox(int pdf, int range, double minx, double maxx, double miny, double maxy)
{
  cpdf_setMediabox(pdf, range, minx, maxx, miny, maxy);
  return;
}

void pycpdf_setCropBox(int pdf, int range, double minx, double maxx, double miny, double maxy)
{
  cpdf_setCropBox(pdf, range, minx, maxx, miny, maxy);
  return;
}

void pycpdf_setTrimBox(int pdf, int range, double minx, double maxx, double miny, double maxy)
{
  cpdf_setTrimBox(pdf, range, minx, maxx, miny, maxy);
  return;
}

void pycpdf_setArtBox(int pdf, int range, double minx, double maxx, double miny, double maxy)
{
  cpdf_setArtBox(pdf, range, minx, maxx, miny, maxy);
  return;
}

void pycpdf_setBleedBox(int pdf, int range, double minx, double maxx, double miny, double maxy)
{
  cpdf_setBleedBox(pdf, range, minx, maxx, miny, maxy);
  return;
}

void pycpdf_markTrapped(int pdf)
{
  cpdf_markTrapped(pdf);
  return;
}

void pycpdf_markUntrapped(int pdf)
{
  cpdf_markUntrapped(pdf);
  return;
}

void pycpdf_markTrappedXMP(int pdf)
{
  cpdf_markTrappedXMP(pdf);
  return;
}

void pycpdf_markUntrappedXMP(int pdf)
{
  cpdf_markUntrappedXMP(pdf);
  return;
}

void pycpdf_setPageLayout(int pdf, int layout)
{
  cpdf_setPageLayout(pdf, layout);
  return;
}

void pycpdf_setPageMode(int pdf, int mode)
{
  cpdf_setPageMode(pdf, mode);
  return;
}

void pycpdf_hideToolbar(int pdf, int flag)
{
  cpdf_hideToolbar(pdf, flag);
  return;
}

void pycpdf_hideMenubar(int pdf, int flag)
{
  cpdf_hideMenubar(pdf, flag);
  return;
}

void pycpdf_hideWindowUi(int pdf, int flag)
{
  cpdf_hideWindowUi(pdf, flag);
  return;
}

void pycpdf_fitWindow(int pdf, int flag)
{
  cpdf_fitWindow(pdf, flag);
  return;
}

void pycpdf_centerWindow(int pdf, int flag)
{
  cpdf_centerWindow(pdf, flag);
  return;
}

void pycpdf_displayDocTitle(int pdf, int flag)
{
  cpdf_displayDocTitle(pdf, flag);
  return;
}

void pycpdf_openAtPage(int pdf, int flag, int pagenumber)
{
  cpdf_openAtPage(pdf, flag, pagenumber);
  return;
}

void pycpdf_setMetadataFromFile(int pdf, char *filename)
{
  cpdf_setMetadataFromFile(pdf, filename);
  return;
}

void pycpdf_setMetadataFromByteArray(int pdf, void* data, int len)
{
  cpdf_setMetadataFromByteArray(pdf, data, len);
  return;
}

void *getMetadataData;

void *pycpdf_getMetadata(int pdf, int *length)
{
  toMemoryData = cpdf_getMetadata(pdf, length);
  return toMemoryData;
}

void pycpdf_getMetadataFree(void)
{
  free(getMetadataData);
  return;
}

void pycpdf_removeMetadata(int pdf)
{
  cpdf_removeMetadata(pdf);
  return;
}

void pycpdf_createMetadata(int pdf)
{
  cpdf_createMetadata(pdf);
  return;
}

void pycpdf_setMetadataDate(int pdf, char *date)
{
  cpdf_setMetadataDate(pdf, date);
  return;
}

int pycpdf_startGetPageLabels(int pdf)
{
  return cpdf_startGetPageLabels(pdf);
}

int pycpdf_getPageLabelStyle(int n)
{
  return cpdf_getPageLabelStyle(n);
}

char *pycpdf_getPageLabelPrefix(int n)
{
  return cpdf_getPageLabelPrefix(n);
}

int pycpdf_getPageLabelOffset(int n)
{
  return cpdf_getPageLabelOffset(n);
}

int pycpdf_getPageLabelRange(int n)
{
  return cpdf_getPageLabelRange(n);
}

void pycpdf_endGetPageLabels(void)
{
  cpdf_endGetPageLabels();
  return;
}

void pycpdf_addPageLabels(int pdf, int style, char *prefix, int offset, int range, int progress)
{
  cpdf_addPageLabels(pdf, style, prefix, offset, range, progress);
  return;
}

void pycpdf_removePageLabels(int pdf)
{
  cpdf_removePageLabels(pdf);
  return;
}

char *pycpdf_getPageLabelStringForPage(int pdf, int pagenumber)
{
  return cpdf_getPageLabelStringForPage(pdf, pagenumber);
}

/* CHAPTER 12. File Attachments */
void pycpdf_attachFile(char* filename, int pdf)
{
  cpdf_attachFile(filename, pdf);
  return;
}

void pycpdf_attachFileToPage(char* filename, int pdf, int pagenumber)
{
  cpdf_attachFileToPage(filename, pdf, pagenumber);
  return;
}

void pycpdf_attachFileFromMemory(void* data, int len, char* filename, int pdf)
{
  cpdf_attachFileFromMemory(data, len, filename, pdf);
  return;
}

void pycpdf_attachFileToPageFromMemory(void* data, int len, char* filename, int pdf, int pagenumber)
{
  cpdf_attachFileToPageFromMemory(data, len, filename, pdf, pagenumber);
  return;
}

void pycpdf_removeAttachedFiles(int pdf)
{
  cpdf_removeAttachedFiles(pdf);
  return;
}

void pycpdf_startGetAttachments(int pdf)
{
  cpdf_startGetAttachments(pdf);
  return;
}

int pycpdf_numberGetAttachments()
{
  return cpdf_numberGetAttachments();
}

char *pycpdf_getAttachmentName(int n)
{
  return cpdf_getAttachmentName(n);
}

int pycpdf_getAttachmentPage(int n)
{
  return cpdf_getAttachmentPage(n);
}

void *getAttachmentData;

void *pycpdf_getAttachmentData(int n, int *length)
{
  return cpdf_getAttachmentData(n, length);
}

void pycpdf_getAttachmentFree(void)
{
  free(getAttachmentData);
  return;
}

void pycpdf_endGetAttachments()
{
  cpdf_endGetAttachments();
  return;
}

/* CHAPTER 13. Images. */
int pycpdf_startGetImageResolution(int pdf, double min_required_resolution)
{
  return cpdf_startGetImageResolution(pdf, min_required_resolution);
}

int pycpdf_getImageResolutionPageNumber(int n)
{
  return cpdf_getImageResolutionPageNumber(n);
}

char *pycpdf_getImageResolutionImageName(int n)
{
  return cpdf_getImageResolutionImageName(n);
}

int pycpdf_getImageResolutionXPixels(int n)
{
  return cpdf_getImageResolutionXPixels(n);
}

int pycpdf_getImageResolutionYPixels(int n)
{
  return cpdf_getImageResolutionYPixels(n);
}

double pycpdf_getImageResolutionXRes(int n)
{
  return cpdf_getImageResolutionXRes(n);
}

double pycpdf_getImageResolutionYRes(int n)
{
  return cpdf_getImageResolutionYRes(n);
}

void pycpdf_endGetImageResolution(void)
{
  return cpdf_endGetImageResolution();
}

/* CHAPTER 14. Fonts */
void pycpdf_removeFonts(int pdf)
{
    cpdf_removeFonts(pdf);
    return;
}

void pycpdf_copyFont(int pdf, int pdf2, int range, int pagenumber, char *fontname)
{
    cpdf_copyFont(pdf, pdf2, range, pagenumber, fontname);
    return;
}

void pycpdf_startGetFontInfo(int pdf)
{
    cpdf_startGetFontInfo(pdf);
    return;
}

int pycpdf_numberFonts(void)
{
    return cpdf_numberFonts();
}

int pycpdf_getFontPage(int n)
{
    return cpdf_getFontPage(n);
}

char *pycpdf_getFontName(int n)
{
    return cpdf_getFontName(n);
}

char *pycpdf_getFontType(int n)
{
    return cpdf_getFontType(n);
}

char *pycpdf_getFontEncoding(int n)
{
    return cpdf_getFontEncoding(n);
}

void pycpdf_endGetFontInfo(void)
{
    cpdf_endGetFontInfo();
    return;
}

/* CHAPTER 15. Miscellaneous */
void pycpdf_draft(int pdf, int r, int boxes)
{
  cpdf_draft(pdf, r, boxes);
  return;
}

void pycpdf_removeAllText(int pdf, int r)
{
  cpdf_removeAllText(pdf, r);
  return;
}

void pycpdf_blackText(int pdf, int r)
{
  cpdf_blackText(pdf, r);
  return;
}

void pycpdf_blackLines(int pdf, int r)
{
  cpdf_blackLines(pdf, r);
  return;
}

void pycpdf_blackFills(int pdf, int r)
{
  cpdf_blackFills(pdf, r);
  return;
}

void pycpdf_thinLines(int pdf, int r, double linewidth)
{
  cpdf_thinLines(pdf, r, linewidth);
  return;
}

void pycpdf_copyId(int pdf, int pdf2)
{
  cpdf_copyId(pdf, pdf2);
  return;
}

void pycpdf_removeId(int pdf)
{
  cpdf_removeId(pdf);
  return;
}

void pycpdf_setVersion(int pdf, int version)
{
  cpdf_setVersion(pdf, version);
  return;
}

void pycpdf_removeDictEntry(int pdf, char *key)
{
  cpdf_removeDictEntry(pdf, key);
  return;
}

void pycpdf_removeClipping(int pdf, int r)
{
  cpdf_removeClipping(pdf, r);
  return;
}

/* Undocumented. To come in v2.4 */
void pycpdf_addContent(char *content, int before, int pdf, int r)
{
  cpdf_addContent(content, before, pdf, r);
  return;
}

void pycpdf_outputJSON(char* filename, int parse_content, int no_stream_data, int pdf)
{
  cpdf_outputJSON(filename, parse_content, no_stream_data, pdf);
  return;
}

void pycpdf_OCGCoalesce(int pdf)
{
  cpdf_OCGCoalesce(pdf);
  return;
}

void pycpdf_OCGRename(int pdf, char *n_from, char *n_to)
{
  cpdf_OCGRename(pdf, n_from, n_to);
  return;
}

void pycpdf_OCGOrderAll(int pdf)
{
  cpdf_OCGOrderAll(pdf);
  return;
}

char *pycpdf_stampAsXObject(int pdf, int r, int stamp_pdf)
{
  return cpdf_stampAsXObject(pdf, r, stamp_pdf);
}

void pycpdf_setDemo(int v)
{
  cpdf_setDemo(v);
  return;
}

