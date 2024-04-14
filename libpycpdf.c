#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cpdflibwrapper.h"

/* CHAPTER 0. Preliminaries */

int pycpdf_startup(char **argv) {
  // char *argv[] = {"program_name", NULL};
  cpdf_startup(argv);
  return 0;
}

char* pycpdf_version() {
  return cpdf_version();
}

void pycpdf_setFast() {
  return cpdf_setFast();
}

void pycpdf_setSlow() {
  return cpdf_setSlow();
}

void pycpdf_embedStd14(int embed) {
  return cpdf_embedStd14(embed);
}

void pycpdf_embedStd14Dir(char* d) {
  return cpdf_embedStd14Dir(d);
}

void pycpdf_JSONUTF8(int utf8) {
  return cpdf_JSONUTF8(utf8);
}


int pycpdf_lastError(void) {
  return cpdf_lastError;
}

char *pycpdf_lastErrorString(void) {
  // printf("cpdf_lastErrorString is %s\n", cpdf_lastErrorString);
  return cpdf_lastErrorString;
}

void pycpdf_clearError(void) {
  cpdf_clearError();
  cpdf_lastError = 0;
  cpdf_lastErrorString = "";
  // printf("after clearerror, cpdf_lastErrorString is %s\n",
  // cpdf_lastErrorString);
  return;
}

void pycpdf_onExit() {
  return cpdf_onExit();
}


/* CHAPTER 1. Basics */

int pycpdf_fromFile(char *filename, char *userpw) {
  return cpdf_fromFile(filename, userpw);
}

int pycpdf_fromFileLazy(char *filename, char *userpw) {
  return cpdf_fromFileLazy(filename, userpw);
}

int pycpdf_fromMemory(void *data, int len, char *userpw) {
  return cpdf_fromMemory(data, len, userpw);
}

int pycpdf_fromMemoryLazy(void *data, int len, char *userpw) {
  return cpdf_fromMemoryLazy(data, len, userpw);
}

void pycpdf_deletePdf(int pdf) {
  return cpdf_deletePdf(pdf);
}

void pycpdf_replacePdf(int pdf, int pdf2) {
  return cpdf_replacePdf(pdf, pdf2);
}

double pycpdf_ptOfCm(double i) {
  return cpdf_ptOfCm(i);
}

double pycpdf_ptOfMm(double i) {
  return cpdf_ptOfMm(i);
}

double pycpdf_ptOfIn(double i) {
  return cpdf_ptOfIn(i);
}

double pycpdf_cmOfPt(double i) {
  return cpdf_cmOfPt(i);
}

double pycpdf_mmOfPt(double i) {
  return cpdf_mmOfPt(i);
}

double pycpdf_inOfPt(double i) {
  return cpdf_inOfPt(i);
}

void pycpdf_startEnumeratePDFs() {
  return cpdf_startEnumeratePDFs();
}

int pycpdf_enumeratePDFsKey(int n) {
  return cpdf_enumeratePDFsKey(n);
}

char* pycpdf_enumeratePDFsInfo(int n) {
  return cpdf_enumeratePDFsInfo(n);
}

void pycpdf_endEnumeratePDFs() {
  return cpdf_endEnumeratePDFs();
}

int pycpdf_parsePagespec(int pdf, char *pagespec) {
  return cpdf_parsePagespec(pdf, pagespec);
}

int pycpdf_validatePagespec(char *pagespec) {
  return cpdf_validatePagespec(pagespec);
}

char* pycpdf_stringOfPagespec(int pdf, int range) {
  return cpdf_stringOfPagespec(pdf, range);
}

int pycpdf_blankRange() {
  return cpdf_blankRange();
}

void pycpdf_deleteRange(int r) {
  return cpdf_deleteRange(r);
}


int pycpdf_pageRange(int f, int t) { return cpdf_range(f, t); }

int pycpdf_all(int r) {
  return cpdf_all(r);
}

int pycpdf_even(int r) {
  return cpdf_even(r);
}

int pycpdf_odd(int r) {
  return cpdf_odd(r);
}

int pycpdf_rangeUnion(int a, int b) {
  return cpdf_rangeUnion(a, b);
}

int pycpdf_difference(int a, int b) {
  return cpdf_difference(a, b);
}

int pycpdf_removeDuplicates(int r) {
  return cpdf_removeDuplicates(r);
}

int pycpdf_rangeLength(int r) {
  return cpdf_rangeLength(r);
}

int pycpdf_rangeGet(int r, int n) {
  return cpdf_rangeGet(r, n);
}

int pycpdf_rangeAdd(int r, int p) {
  return cpdf_rangeAdd(r, p);
}

int pycpdf_isInRange(int r, int p) {
  return cpdf_isInRange(r, p);
}

int pycpdf_pages(int pdf) {
  return cpdf_pages(pdf);
}

int pycpdf_pagesFast(char *filename, char *userpw) {
  return cpdf_pagesFast(filename, userpw);
}

void pycpdf_toFile(int pdf, char *filename, int linearize, int make_id) {
  return cpdf_toFile(pdf, filename, linearize, make_id);
}

void pycpdf_toFileExt(int pdf, char *filename, int linearize, int make_id, int preserve_objstm, int generate_objstm, int compress_objstm) {
  return cpdf_toFileExt(pdf, filename, linearize, make_id, preserve_objstm, generate_objstm, compress_objstm);
}


// We want to return a piece of memory which will be copied into a python
// string, and the C string deallocated.
void *toMemoryData;

void *pycpdf_toMemory(int pdf, int linearize, int make_id, int *length) {
  toMemoryData = cpdf_toMemory(pdf, linearize, make_id, length);
  return toMemoryData;
}

void pycpdf_toMemoryFree(void) {
  free(toMemoryData);
  return;
}

int pycpdf_isEncrypted(int pdf) {
  return cpdf_isEncrypted(pdf);
}

void pycpdf_toFileEncrypted(int pdf, int method, int *permissions, int permlength, char *ownerpw, char *userpw, int linearize, int makeid, char *filename) {
  return cpdf_toFileEncrypted(pdf, method, permissions, permlength, ownerpw, userpw, linearize, makeid, filename);
}

void pycpdf_toFileEncryptedExt(int pdf, int method, int *permissions, int permlength, char *ownerpw, char *userpw, int linearize, int makeid, int preserve_objstm, int generate_objstm, int compress_objstm, char *filename) {
  return cpdf_toFileEncryptedExt(pdf, method, permissions, permlength, ownerpw, userpw, linearize, makeid, preserve_objstm, generate_objstm, compress_objstm, filename);
}

void pycpdf_decryptPdf(int pdf, char *userpw) {
  return cpdf_decryptPdf(pdf, userpw);
}

void pycpdf_decryptPdfOwner(int pdf, char *ownerpw) {
  return cpdf_decryptPdfOwner(pdf, ownerpw);
}

int pycpdf_hasPermission(int pdf, int perm) {
  return cpdf_hasPermission(pdf, perm);
}

int pycpdf_encryptionKind(int pdf) {
  return cpdf_encryptionKind(pdf);
}

void pycpdf_loadFont(char* name, char* filename) {
  return cpdf_loadFont(name, filename);
}


/* CHAPTER 2. Merging and Splitting */

int pycpdf_mergeSimple(int *pdfs, int len) {
  return cpdf_mergeSimple(pdfs, len);
}

int pycpdf_merge(int *pdfs, int len, int retain_numbering, int remove_duplicate_fonts) {
  return cpdf_merge(pdfs, len, retain_numbering, remove_duplicate_fonts);
}

int pycpdf_mergeSame(int *pdfs, int len, int retain_numbering, int remove_duplicate_fonts, int *ranges) {
  return cpdf_mergeSame(pdfs, len, retain_numbering, remove_duplicate_fonts, ranges);
}

int pycpdf_selectPages(int pdf, int r) {
  return cpdf_selectPages(pdf, r);
}


/* CHAPTER 3. Pages */

void pycpdf_scalePages(int pdf, int r, double sx, double sy) {
  return cpdf_scalePages(pdf, r, sx, sy);
}

void pycpdf_scaleToFit(int pdf, int r, double sx, double sy, double scale_to_fit_scale) {
  return cpdf_scaleToFit(pdf, r, sx, sy, scale_to_fit_scale);
}

void pycpdf_scaleToFitPaper(int pdf, int r, int papersize, double scale_to_fit_scale) {
  return cpdf_scaleToFitPaper(pdf, r, papersize, scale_to_fit_scale);
}


void pycpdf_scaleContents(int pdf, int r, int pos, double p1, double p2, double scale) {
  struct cpdf_position p = {
      .cpdf_anchor = pos, .cpdf_coord1 = p1, .cpdf_coord2 = p2};
  cpdf_scaleContents(pdf, r, p, scale);
}

void pycpdf_shiftContents(int pdf, int r, double dx, double dy) {
  return cpdf_shiftContents(pdf, r, dx, dy);
}

void pycpdf_shiftBoxes(int pdf, int r, double dx, double dy) {
  return cpdf_shiftBoxes(pdf, r, dx, dy);
}

void pycpdf_rotate(int pdf, int r, int rotation) {
  return cpdf_rotate(pdf, r, rotation);
}

void pycpdf_rotateBy(int pdf, int r, int rotation) {
  return cpdf_rotateBy(pdf, r, rotation);
}

void pycpdf_rotateContents(int pdf, int r, double rotation) {
  return cpdf_rotateContents(pdf, r, rotation);
}

void pycpdf_upright(int pdf, int r) {
  return cpdf_upright(pdf, r);
}

void pycpdf_hFlip(int pdf, int r) {
  return cpdf_hFlip(pdf, r);
}

void pycpdf_vFlip(int pdf, int r) {
  return cpdf_vFlip(pdf, r);
}

void pycpdf_crop(int pdf, int r, double x, double y, double w, double h) {
  return cpdf_crop(pdf, r, x, y, w, h);
}

void pycpdf_removeCrop(int pdf, int r) {
  return cpdf_removeCrop(pdf, r);
}

void pycpdf_removeTrim(int pdf, int r) {
  return cpdf_removeTrim(pdf, r);
}

void pycpdf_removeArt(int pdf, int r) {
  return cpdf_removeArt(pdf, r);
}

void pycpdf_removeBleed(int pdf, int r) {
  return cpdf_removeBleed(pdf, r);
}

void pycpdf_trimMarks(int pdf, int r) {
  return cpdf_trimMarks(pdf, r);
}

void pycpdf_showBoxes(int pdf, int r) {
  return cpdf_showBoxes(pdf, r);
}

void pycpdf_hardBox(int pdf, int r, char *boxname) {
  return cpdf_hardBox(pdf, r, boxname);
}


/* CHAPTER 4. Encryption */

/* Encryption covered under Chapter 1 in cpdflib. */

/* CHAPTER 5. Compression */

void pycpdf_compress(int pdf) {
  return cpdf_compress(pdf);
}

void pycpdf_decompress(int pdf) {
  return cpdf_decompress(pdf);
}

void pycpdf_squeezeInMemory(int pdf) {
  return cpdf_squeezeInMemory(pdf);
}


/* CHAPTER 6. Bookmarks */

void pycpdf_startGetBookmarkInfo(int pdf) {
  return cpdf_startGetBookmarkInfo(pdf);
}

int pycpdf_numberBookmarks() {
  return cpdf_numberBookmarks();
}

int pycpdf_getBookmarkLevel(int n) {
  return cpdf_getBookmarkLevel(n);
}

int pycpdf_getBookmarkPage(int pdf, int page) {
  return cpdf_getBookmarkPage(pdf, page);
}

char* pycpdf_getBookmarkText(int n) {
  return cpdf_getBookmarkText(n);
}

int pycpdf_getBookmarkOpenStatus(int n) {
  return cpdf_getBookmarkOpenStatus(n);
}

void pycpdf_endGetBookmarkInfo() {
  return cpdf_endGetBookmarkInfo();
}

void pycpdf_startSetBookmarkInfo(int n) {
  return cpdf_startSetBookmarkInfo(n);
}

void pycpdf_setBookmarkLevel(int n, int level) {
  return cpdf_setBookmarkLevel(n, level);
}

void pycpdf_setBookmarkPage(int pdf, int n, int targetpage) {
  return cpdf_setBookmarkPage(pdf, n, targetpage);
}

void pycpdf_setBookmarkOpenStatus(int n, int status) {
  return cpdf_setBookmarkOpenStatus(n, status);
}

void pycpdf_setBookmarkText(int n, char *text) {
  return cpdf_setBookmarkText(n, text);
}

void pycpdf_endSetBookmarkInfo(int pdf) {
  return cpdf_endSetBookmarkInfo(pdf);
}


void *getBookmarksJSONData;

void *pycpdf_getBookmarksJSON(int pdf, int *length) {
  getBookmarksJSONData = cpdf_getBookmarksJSON(pdf, length);
  return getBookmarksJSONData;
}

void pycpdf_getBookmarksJSONFree(void) {
  free(getBookmarksJSONData);
  return;
}

void pycpdf_setBookmarksJSON(int pdf, void* data, int length) {
  return cpdf_setBookmarksJSON(pdf, data, length);
}

void pycpdf_tableOfContents(int pdf, char* font, double fontsize, char* title, int bookmark) {
  return cpdf_tableOfContents(pdf, font, fontsize, title, bookmark);
}


/* CHAPTER 7. Presentations */

/* Not included in the library version */

/* CHAPTER 8. Logos, Watermarks and Stamps */

void pycpdf_stampOn(int pdf, int pdf2, int r) {
  return cpdf_stampOn(pdf, pdf2, r);
}

void pycpdf_stampUnder(int pdf, int pdf2, int r) {
  return cpdf_stampUnder(pdf, pdf2, r);
}


void pycpdf_stampExtended(int pdf, int pdf2, int r, int isover,
                          int scale_stamp_to_fit, int pos, int c1, int c2,
                          int relative_to_cropbox) {
  struct cpdf_position position = {
      .cpdf_anchor = pos, .cpdf_coord1 = c1, .cpdf_coord2 = c2};
  cpdf_stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, position,
                     relative_to_cropbox);
  return;
}

void pycpdf_combinePages(int pdf, int pdf2) {
  return cpdf_combinePages(pdf, pdf2);
}


void pycpdf_addText(int metrics, int pdf, int r, char *text, int pos, double p1,
                    double p2, double line_spacing, int bates, char* font,
                    double size, double red, double green, double blue,
                    int underneath, int relative_to_cropbox, int outline,
                    double opacity, int justification, int midline, int topline,
                    char *filename, double line_width, int embed_fonts) {
  struct cpdf_position position = {
      .cpdf_anchor = pos, .cpdf_coord1 = p1, .cpdf_coord2 = p2};
  cpdf_addText(metrics, pdf, r, text, position, line_spacing, bates, font, size,
               red, green, blue, underneath, relative_to_cropbox, outline,
               opacity, justification, midline, topline, filename, line_width,
               embed_fonts);
  return;
}

void pycpdf_addTextSimple(int pdf, int r, char *text, int pos, double p1,
                          double p2, char* font, double size) {
  struct cpdf_position position = {
      .cpdf_anchor = pos, .cpdf_coord1 = p1, .cpdf_coord2 = p2};
  cpdf_addTextSimple(pdf, r, text, position, font, size);
  return;
}

void pycpdf_removeText(int pdf, int r) {
  return cpdf_removeText(pdf, r);
}

int pycpdf_textWidth(char* font, char* string) {
  return cpdf_textWidth(font, string);
}

void pycpdf_addContent(char* content, int before, int pdf, int r) {
  return cpdf_addContent(content, before, pdf, r);
}

char* pycpdf_stampAsXObject(int pdf, int r, int stamp_pdf) {
  return cpdf_stampAsXObject(pdf, r, stamp_pdf);
}


/* CHAPTER 9. Multipage facilities */

void pycpdf_impose(int pdf, double x, double y, int fit, int columns, int rtl, int btt, int center, double margin, double spacing, double linewidth) {
  return cpdf_impose(pdf, x, y, fit, columns, rtl, btt, center, margin, spacing, linewidth);
}

void pycpdf_chop(int pdf, int range, int x, int y, int columns, int rtl, int btt) {
  return cpdf_chop(pdf, range, x, y, columns, rtl, btt);
}

void pycpdf_chopH(int pdf, int range, int columns, double y) {
  return cpdf_chopH(pdf, range, columns, y);
}

void pycpdf_chopV(int pdf, int range, int columns, double x) {
  return cpdf_chopV(pdf, range, columns, x);
}

void pycpdf_twoUp(int pdf) {
  return cpdf_twoUp(pdf);
}

void pycpdf_twoUpStack(int pdf) {
  return cpdf_twoUpStack(pdf);
}

void pycpdf_padBefore(int pdf, int r) {
  return cpdf_padBefore(pdf, r);
}

void pycpdf_padAfter(int pdf, int r) {
  return cpdf_padAfter(pdf, r);
}

void pycpdf_padEvery(int pdf, int r) {
  return cpdf_padEvery(pdf, r);
}

void pycpdf_padMultiple(int pdf, int n) {
  return cpdf_padMultiple(pdf, n);
}

void pycpdf_padMultipleBefore(int pdf, int n) {
  return cpdf_padMultipleBefore(pdf, n);
}


/* CHAPTER 10. Annotations */
void *annotationsJSONData;

void *pycpdf_annotationsJSON(int pdf, int *length) {
  annotationsJSONData = cpdf_annotationsJSON(pdf, length);
  return annotationsJSONData;
}

void pycpdf_annotationsJSONFree(void) {
  free(annotationsJSONData);
  return;
}

void pycpdf_removeAnnotations(int pdf, int range) {
  return cpdf_removeAnnotations(pdf, range);
}

void pycpdf_setAnnotationsJSON(int pdf, void* data, int length) {
  return cpdf_setAnnotationsJSON(pdf, data, length);
}


/* CHAPTER 11. Document Information and Metadata */

int pycpdf_isLinearized(char *filename) {
  return cpdf_isLinearized(filename);
}

int pycpdf_hasObjectStreams(int pdf) {
  return cpdf_hasObjectStreams(pdf);
}

char* pycpdf_id1(int pdf) {
  return cpdf_id1(pdf);
}

char* pycpdf_id2(int pdf) {
  return cpdf_id2(pdf);
}

int pycpdf_hasAcroForm(int pdf) {
  return cpdf_hasAcroForm(pdf);
}

int pycpdf_startGetSubformats(int pdf) {
  return cpdf_startGetSubformats(pdf);
}

char* pycpdf_getSubformat(int s) {
  return cpdf_getSubformat(s);
}

void pycpdf_endGetSubformats() {
  return cpdf_endGetSubformats();
}

int pycpdf_getVersion(int pdf) {
  return cpdf_getVersion(pdf);
}

int pycpdf_getMajorVersion(int pdf) {
  return cpdf_getMajorVersion(pdf);
}

char* pycpdf_getTitle(int pdf) {
  return cpdf_getTitle(pdf);
}

char* pycpdf_getAuthor(int pdf) {
  return cpdf_getAuthor(pdf);
}

char* pycpdf_getSubject(int pdf) {
  return cpdf_getSubject(pdf);
}

char* pycpdf_getKeywords(int pdf) {
  return cpdf_getKeywords(pdf);
}

char* pycpdf_getCreator(int pdf) {
  return cpdf_getCreator(pdf);
}

char* pycpdf_getProducer(int pdf) {
  return cpdf_getProducer(pdf);
}

char* pycpdf_getCreationDate(int pdf) {
  return cpdf_getCreationDate(pdf);
}

char* pycpdf_getModificationDate(int pdf) {
  return cpdf_getModificationDate(pdf);
}

char* pycpdf_getTitleXMP(int pdf) {
  return cpdf_getTitleXMP(pdf);
}

char* pycpdf_getAuthorXMP(int pdf) {
  return cpdf_getAuthorXMP(pdf);
}

char* pycpdf_getSubjectXMP(int pdf) {
  return cpdf_getSubjectXMP(pdf);
}

char* pycpdf_getKeywordsXMP(int pdf) {
  return cpdf_getKeywordsXMP(pdf);
}

char* pycpdf_getCreatorXMP(int pdf) {
  return cpdf_getCreatorXMP(pdf);
}

char* pycpdf_getProducerXMP(int pdf) {
  return cpdf_getProducerXMP(pdf);
}

char* pycpdf_getCreationDateXMP(int pdf) {
  return cpdf_getCreationDateXMP(pdf);
}

char* pycpdf_getModificationDateXMP(int pdf) {
  return cpdf_getModificationDateXMP(pdf);
}

void pycpdf_setTitle(int pdf, char *s) {
  return cpdf_setTitle(pdf, s);
}

void pycpdf_setAuthor(int pdf, char *s) {
  return cpdf_setAuthor(pdf, s);
}

void pycpdf_setSubject(int pdf, char *s) {
  return cpdf_setSubject(pdf, s);
}

void pycpdf_setKeywords(int pdf, char *s) {
  return cpdf_setKeywords(pdf, s);
}

void pycpdf_setCreator(int pdf, char *s) {
  return cpdf_setCreator(pdf, s);
}

void pycpdf_setProducer(int pdf, char *s) {
  return cpdf_setProducer(pdf, s);
}

void pycpdf_setCreationDate(int pdf, char *s) {
  return cpdf_setCreationDate(pdf, s);
}

void pycpdf_setModificationDate(int pdf, char *s) {
  return cpdf_setModificationDate(pdf, s);
}

void pycpdf_setTitleXMP(int pdf, char *s) {
  return cpdf_setTitleXMP(pdf, s);
}

void pycpdf_setAuthorXMP(int pdf, char *s) {
  return cpdf_setAuthorXMP(pdf, s);
}

void pycpdf_setSubjectXMP(int pdf, char *s) {
  return cpdf_setSubjectXMP(pdf, s);
}

void pycpdf_setKeywordsXMP(int pdf, char *s) {
  return cpdf_setKeywordsXMP(pdf, s);
}

void pycpdf_setCreatorXMP(int pdf, char *s) {
  return cpdf_setCreatorXMP(pdf, s);
}

void pycpdf_setProducerXMP(int pdf, char *s) {
  return cpdf_setProducerXMP(pdf, s);
}

void pycpdf_setCreationDateXMP(int pdf, char *s) {
  return cpdf_setCreationDateXMP(pdf, s);
}

void pycpdf_setModificationDateXMP(int pdf, char *s) {
  return cpdf_setModificationDateXMP(pdf, s);
}

void pycpdf_getDateComponents(char *str, int *year, int *month, int *day, int *hour, int *minute, int *second, int *hour_offset, int *minute_offset) {
  return cpdf_getDateComponents(str, year, month, day, hour, minute, second, hour_offset, minute_offset);
}

char* pycpdf_dateStringOfComponents(int year, int month, int day, int hour, int minute, int second, int hour_offset, int minute_offset) {
  return cpdf_dateStringOfComponents(year, month, day, hour, minute, second, hour_offset, minute_offset);
}

int pycpdf_getPageRotation(int pdf, int pagenumber) {
  return cpdf_getPageRotation(pdf, pagenumber);
}

int pycpdf_hasBox(int pdf, int pagenumber, char *box) {
  return cpdf_hasBox(pdf, pagenumber, box);
}

int pycpdf_numAnnots(int pdf, int pagenumber) {
  return cpdf_numAnnots(pdf, pagenumber);
}

void pycpdf_getMediaBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) {
  return cpdf_getMediaBox(pdf, pagenumber, minx, maxx, miny, maxy);
}

void pycpdf_getCropBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) {
  return cpdf_getCropBox(pdf, pagenumber, minx, maxx, miny, maxy);
}

void pycpdf_getTrimBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) {
  return cpdf_getTrimBox(pdf, pagenumber, minx, maxx, miny, maxy);
}

void pycpdf_getArtBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) {
  return cpdf_getArtBox(pdf, pagenumber, minx, maxx, miny, maxy);
}

void pycpdf_getBleedBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) {
  return cpdf_getBleedBox(pdf, pagenumber, minx, maxx, miny, maxy);
}


void pycpdf_setMediaBox(int pdf, int range, double minx, double maxx,
                        double miny, double maxy) {
  cpdf_setMediabox(pdf, range, minx, maxx, miny, maxy);
  return;
}

void pycpdf_setCropBox(int pdf, int range, double minx, double maxx, double miny, double maxy) {
  return cpdf_setCropBox(pdf, range, minx, maxx, miny, maxy);
}

void pycpdf_setTrimBox(int pdf, int range, double minx, double maxx, double miny, double maxy) {
  return cpdf_setTrimBox(pdf, range, minx, maxx, miny, maxy);
}

void pycpdf_setArtBox(int pdf, int range, double minx, double maxx, double miny, double maxy) {
  return cpdf_setArtBox(pdf, range, minx, maxx, miny, maxy);
}

void pycpdf_setBleedBox(int pdf, int range, double minx, double maxx, double miny, double maxy) {
  return cpdf_setBleedBox(pdf, range, minx, maxx, miny, maxy);
}



void *pageInfoJSONData;

void *pycpdf_pageInfoJSON(int pdf, int *length) {
  pageInfoJSONData = cpdf_pageInfoJSON(pdf, length);
  return pageInfoJSONData;
}

void pycpdf_pageInfoJSONFree(void) {
  free(pageInfoJSONData);
  return;
}

void pycpdf_markTrapped(int pdf) {
  return cpdf_markTrapped(pdf);
}

void pycpdf_markUntrapped(int pdf) {
  return cpdf_markUntrapped(pdf);
}

void pycpdf_markTrappedXMP(int pdf) {
  return cpdf_markTrappedXMP(pdf);
}

void pycpdf_markUntrappedXMP(int pdf) {
  return cpdf_markUntrappedXMP(pdf);
}

void pycpdf_setPageLayout(int pdf, int layout) {
  return cpdf_setPageLayout(pdf, layout);
}

int pycpdf_getPageLayout(int pdf) {
  return cpdf_getPageLayout(pdf);
}

void pycpdf_setPageMode(int pdf, int mode) {
  return cpdf_setPageMode(pdf, mode);
}

int pycpdf_getPageMode(int pdf) {
  return cpdf_getPageMode(pdf);
}

void pycpdf_hideToolbar(int pdf, int flag) {
  return cpdf_hideToolbar(pdf, flag);
}

int pycpdf_getHideToolbar(int pdf) {
  return cpdf_getHideToolbar(pdf);
}

void pycpdf_hideMenubar(int pdf, int flag) {
  return cpdf_hideMenubar(pdf, flag);
}

int pycpdf_getHideMenubar(int pdf) {
  return cpdf_getHideMenubar(pdf);
}

void pycpdf_hideWindowUi(int pdf, int flag) {
  return cpdf_hideWindowUi(pdf, flag);
}

int pycpdf_getHideWindowUi(int pdf) {
  return cpdf_getHideWindowUi(pdf);
}

void pycpdf_fitWindow(int pdf, int flag) {
  return cpdf_fitWindow(pdf, flag);
}

int pycpdf_getFitWindow(int pdf) {
  return cpdf_getFitWindow(pdf);
}

void pycpdf_centerWindow(int pdf, int flag) {
  return cpdf_centerWindow(pdf, flag);
}

int pycpdf_getCenterWindow(int pdf) {
  return cpdf_getCenterWindow(pdf);
}

void pycpdf_displayDocTitle(int pdf, int flag) {
  return cpdf_displayDocTitle(pdf, flag);
}

int pycpdf_getDisplayDocTitle(int pdf) {
  return cpdf_getDisplayDocTitle(pdf);
}

void pycpdf_nonFullScreenPageMode(int pdf, int flag) {
  return cpdf_nonFullScreenPageMode(pdf, flag);
}

int pycpdf_getNonFullScreenPageMode(int pdf) {
  return cpdf_getNonFullScreenPageMode(pdf);
}

void pycpdf_openAtPage(int pdf, int flag, int pagenumber) {
  return cpdf_openAtPage(pdf, flag, pagenumber);
}

void pycpdf_openAtPageCustom(int pdf, char* custom) {
  return cpdf_openAtPageCustom(pdf, custom);
}

void pycpdf_setMetadataFromFile(int pdf, char* filename) {
  return cpdf_setMetadataFromFile(pdf, filename);
}

void pycpdf_setMetadataFromByteArray(int pdf, void* data, int len) {
  return cpdf_setMetadataFromByteArray(pdf, data, len);
}


void *getMetadataData;

void *pycpdf_getMetadata(int pdf, int *length) {
  getMetadataData = cpdf_getMetadata(pdf, length);
  return getMetadataData;
}

void pycpdf_getMetadataFree(void) {
  free(getMetadataData);
  return;
}

void pycpdf_removeMetadata(int pdf) {
  return cpdf_removeMetadata(pdf);
}

void pycpdf_createMetadata(int pdf) {
  return cpdf_createMetadata(pdf);
}

void pycpdf_setMetadataDate(int pdf, char* date) {
  return cpdf_setMetadataDate(pdf, date);
}

int pycpdf_startGetPageLabels(int pdf) {
  return cpdf_startGetPageLabels(pdf);
}

int pycpdf_getPageLabelStyle(int n) {
  return cpdf_getPageLabelStyle(n);
}

char* pycpdf_getPageLabelPrefix(int n) {
  return cpdf_getPageLabelPrefix(n);
}

int pycpdf_getPageLabelOffset(int n) {
  return cpdf_getPageLabelOffset(n);
}

int pycpdf_getPageLabelRange(int n) {
  return cpdf_getPageLabelRange(n);
}

void pycpdf_endGetPageLabels() {
  return cpdf_endGetPageLabels();
}

void pycpdf_addPageLabels(int pdf, int style, char *prefix, int offset, int range, int progress) {
  return cpdf_addPageLabels(pdf, style, prefix, offset, range, progress);
}

void pycpdf_removePageLabels(int pdf) {
  return cpdf_removePageLabels(pdf);
}

char* pycpdf_getPageLabelStringForPage(int pdf, int pagenumber) {
  return cpdf_getPageLabelStringForPage(pdf, pagenumber);
}


void *compositionJSONData;

void *pycpdf_compositionJSON(int filesize, int pdf, int *length) {
  compositionJSONData = cpdf_compositionJSON(filesize, pdf, length);
  return compositionJSONData;
}

void pycpdf_compositionJSONFree(void) {
  free(compositionJSONData);
  return;
}

/* CHAPTER 12. File Attachments */

void pycpdf_attachFile(char* filename, int pdf) {
  return cpdf_attachFile(filename, pdf);
}

void pycpdf_attachFileToPage(char* filename, int pdf, int pagenumber) {
  return cpdf_attachFileToPage(filename, pdf, pagenumber);
}

void pycpdf_attachFileFromMemory(void* data, int len, char* filename, int pdf) {
  return cpdf_attachFileFromMemory(data, len, filename, pdf);
}

void pycpdf_attachFileToPageFromMemory(void* data, int len, char* filename, int pdf, int pagenumber) {
  return cpdf_attachFileToPageFromMemory(data, len, filename, pdf, pagenumber);
}

void pycpdf_removeAttachedFiles(int pdf) {
  return cpdf_removeAttachedFiles(pdf);
}

void pycpdf_startGetAttachments(int pdf) {
  return cpdf_startGetAttachments(pdf);
}

int pycpdf_numberGetAttachments() {
  return cpdf_numberGetAttachments();
}

char* pycpdf_getAttachmentName(int n) {
  return cpdf_getAttachmentName(n);
}

int pycpdf_getAttachmentPage(int n) {
  return cpdf_getAttachmentPage(n);
}


void *getAttachmentData;

void *pycpdf_getAttachmentData(int n, int *length) {
  getAttachmentData = cpdf_getAttachmentData(n, length);
  return getAttachmentData;
}

void pycpdf_getAttachmentFree(void) {
  free(getAttachmentData);
  return;
}

void pycpdf_endGetAttachments() {
  return cpdf_endGetAttachments();
}


/* CHAPTER 13. Images. */

int pycpdf_startGetImageResolution(int pdf, double min_required_resolution) {
  return cpdf_startGetImageResolution(pdf, min_required_resolution);
}

int pycpdf_getImageResolutionPageNumber(int n) {
  return cpdf_getImageResolutionPageNumber(n);
}

char* pycpdf_getImageResolutionImageName(int n) {
  return cpdf_getImageResolutionImageName(n);
}

int pycpdf_getImageResolutionXPixels(int n) {
  return cpdf_getImageResolutionXPixels(n);
}

int pycpdf_getImageResolutionYPixels(int n) {
  return cpdf_getImageResolutionYPixels(n);
}

double pycpdf_getImageResolutionXRes(int n) {
  return cpdf_getImageResolutionXRes(n);
}

double pycpdf_getImageResolutionYRes(int n) {
  return cpdf_getImageResolutionYRes(n);
}

int pycpdf_getImageResolutionObjNum(int n) {
  return cpdf_getImageResolutionObjNum(n);
}

void pycpdf_endGetImageResolution() {
  return cpdf_endGetImageResolution();
}

int pycpdf_startGetImages(int pdf) {
  return cpdf_startGetImages(pdf);
}

int pycpdf_getImageObjNum(int serial) {
  return cpdf_getImageObjNum(serial);
}

char* pycpdf_getImagePages(int serial) {
  return cpdf_getImagePages(serial);
}

char* pycpdf_getImageName(int serial) {
  return cpdf_getImageName(serial);
}

int pycpdf_getImageWidth(int serial) {
  return cpdf_getImageWidth(serial);
}

int pycpdf_getImageHeight(int serial) {
  return cpdf_getImageHeight(serial);
}

int pycpdf_getImageSize(int serial) {
  return cpdf_getImageSize(serial);
}

int pycpdf_getImageBPC(int serial) {
  return cpdf_getImageBPC(serial);
}

char* pycpdf_getImageColSpace(int serial) {
  return cpdf_getImageColSpace(serial);
}

char* pycpdf_getImageFilter(int serial) {
  return cpdf_getImageFilter(serial);
}

void pycpdf_endGetImages() {
  return cpdf_endGetImages();
}


void *imageResolutionJSONData;

void *pycpdf_imageResolutionJSON(int pdf, int *length, float resolution) {
  imageResolutionJSONData = cpdf_imageResolutionJSON(pdf, length, resolution);
  return imageResolutionJSONData;
}

void pycpdf_imageResolutionJSONFree(void) {
  free(imageResolutionJSONData);
  return;
}

void *imagesJSONData;

void *pycpdf_imagesJSON(int pdf, int *length) {
  imagesJSONData = cpdf_imagesJSON(pdf, length);
  return imagesJSONData;
}

void pycpdf_imagesJSONFree(void) {
  free(imagesJSONData);
  return;
}

/* CHAPTER 14. Fonts */

void pycpdf_removeFonts(int pdf) {
  return cpdf_removeFonts(pdf);
}

void pycpdf_copyFont(int pdf, int pdf2, int range, int pagenumber, char *fontname) {
  return cpdf_copyFont(pdf, pdf2, range, pagenumber, fontname);
}

void pycpdf_startGetFontInfo(int pdf) {
  return cpdf_startGetFontInfo(pdf);
}

int pycpdf_numberFonts() {
  return cpdf_numberFonts();
}

int pycpdf_getFontPage(int n) {
  return cpdf_getFontPage(n);
}

char* pycpdf_getFontName(int n) {
  return cpdf_getFontName(n);
}

char* pycpdf_getFontType(int n) {
  return cpdf_getFontType(n);
}

char* pycpdf_getFontEncoding(int n) {
  return cpdf_getFontEncoding(n);
}

void pycpdf_endGetFontInfo() {
  return cpdf_endGetFontInfo();
}


void *fontsJSONData;

void *pycpdf_fontsJSON(int pdf, int *length) {
  fontsJSONData = cpdf_fontsJSON(pdf, length);
  return fontsJSONData;
}

void pycpdf_fontsJSONFree(void) {
  free(fontsJSONData);
  return;
}

/* CHAPTER 15. PDF and JSON */

void pycpdf_outputJSON(char* filename, int parse_content, int no_stream_data, int decompress_streams, int pdf) {
  return cpdf_outputJSON(filename, parse_content, no_stream_data, decompress_streams, pdf);
}


void *outputJSONData;

void *pycpdf_outputJSONMemory(int pdf, int parse_content, int no_stream_data,
                              int decompress_stream, int *retlen) {
  outputJSONData = cpdf_outputJSONMemory(pdf, parse_content, no_stream_data,
                                         decompress_stream, retlen);
  return outputJSONData;
}

void pycpdf_outputJSONMemoryFree(void) {
  free(outputJSONData);
  return;
}

int pycpdf_fromJSON(char *filename) {
  return cpdf_fromJSON(filename);
}

int pycpdf_fromJSONMemory(void *data, int len) {
  return cpdf_fromJSONMemory(data, len);
}


/* CHAPTER 16. Optional Content Groups */

int pycpdf_startGetOCGList(int pdf) {
  return cpdf_startGetOCGList(pdf);
}

char* pycpdf_OCGListEntry(int i) {
  return cpdf_OCGListEntry(i);
}

void pycpdf_endGetOCGList() {
  return cpdf_endGetOCGList();
}

void pycpdf_OCGCoalesce(int pdf) {
  return cpdf_OCGCoalesce(pdf);
}

void pycpdf_OCGRename(int pdf, char* n_from, char* n_to) {
  return cpdf_OCGRename(pdf, n_from, n_to);
}

void pycpdf_OCGOrderAll(int pdf) {
  return cpdf_OCGOrderAll(pdf);
}


/* CHAPTER 17. Creating New PDFs */

int pycpdf_blankDocument(double w, double h, int pages) {
  return cpdf_blankDocument(w, h, pages);
}

int pycpdf_blankDocumentPaper(int papersize, int pages) {
  return cpdf_blankDocumentPaper(papersize, pages);
}

int pycpdf_textToPDF(double w, double h, char* font, double fontsize, char *filename) {
  return cpdf_textToPDF(w, h, font, fontsize, filename);
}

int pycpdf_textToPDFMemory(double w, double h, char* font, double fontsize, void* data, int len) {
  return cpdf_textToPDFMemory(w, h, font, fontsize, data, len);
}

int pycpdf_textToPDFPaper(int papersize, char* font, double fontsize, char *filename) {
  return cpdf_textToPDFPaper(papersize, font, fontsize, filename);
}

int pycpdf_textToPDFPaperMemory(int papersize, char* font, double fontsize, void* data, int len) {
  return cpdf_textToPDFPaperMemory(papersize, font, fontsize, data, len);
}

int pycpdf_fromPNG(char* filename) {
  return cpdf_fromPNG(filename);
}

int pycpdf_fromPNGMemory(void* data, int len) {
  return cpdf_fromPNGMemory(data, len);
}

int pycpdf_fromJPEG(char* filename) {
  return cpdf_fromJPEG(filename);
}

int pycpdf_fromJPEGMemory(void* data, int len) {
  return cpdf_fromJPEGMemory(data, len);
}


/* CHAPTER 18. Drawing on PDFs */

void pycpdf_drawBegin() {
  return cpdf_drawBegin();
}

void pycpdf_drawEnd(int pdf, int range) {
  return cpdf_drawEnd(pdf, range);
}

void pycpdf_drawEndExtended(int pdf, int range, int underneath, int bates, char* filename) {
  return cpdf_drawEndExtended(pdf, range, underneath, bates, filename);
}

void pycpdf_drawRect(double x, double y, double w, double h) {
  return cpdf_drawRect(x, y, w, h);
}

void pycpdf_drawTo(double x, double y) {
  return cpdf_drawTo(x, y);
}

void pycpdf_drawLine(double x, double y) {
  return cpdf_drawLine(x, y);
}

void pycpdf_drawBez(double x1, double y1, double x2, double y2, double x3, double y3) {
  return cpdf_drawBez(x1, y1, x2, y2, x3, y3);
}

void pycpdf_drawBez23(double x2, double y2, double x3, double y3) {
  return cpdf_drawBez23(x2, y2, x3, y3);
}

void pycpdf_drawBez13(double x1, double y1, double x3, double y3) {
  return cpdf_drawBez13(x1, y1, x3, y3);
}

void pycpdf_drawCircle(double x, double y, double r) {
  return cpdf_drawCircle(x, y, r);
}

void pycpdf_drawStroke() {
  return cpdf_drawStroke();
}

void pycpdf_drawFill() {
  return cpdf_drawFill();
}

void pycpdf_drawFillEo() {
  return cpdf_drawFillEo();
}

void pycpdf_drawStrokeFill() {
  return cpdf_drawStrokeFill();
}

void pycpdf_drawStrokeFillEo() {
  return cpdf_drawStrokeFillEo();
}

void pycpdf_drawClose() {
  return cpdf_drawClose();
}

void pycpdf_drawClip() {
  return cpdf_drawClip();
}

void pycpdf_drawClipEo() {
  return cpdf_drawClipEo();
}

void pycpdf_drawStrokeColGrey(double g) {
  return cpdf_drawStrokeColGrey(g);
}

void pycpdf_drawStrokeColRGB(double r, double g, double b) {
  return cpdf_drawStrokeColRGB(r, g, b);
}

void pycpdf_drawStrokeColCYMK(double c, double y, double m, double k) {
  return cpdf_drawStrokeColCYMK(c, y, m, k);
}

void pycpdf_drawFillColGrey(double g) {
  return cpdf_drawFillColGrey(g);
}

void pycpdf_drawFillColRGB(double r, double g, double b) {
  return cpdf_drawFillColRGB(r, g, b);
}

void pycpdf_drawFillColCYMK(double c, double y, double m, double k) {
  return cpdf_drawFillColCYMK(c, y, m, k);
}

void pycpdf_drawThick(double thickness) {
  return cpdf_drawThick(thickness);
}

void pycpdf_drawCap(int captype) {
  return cpdf_drawCap(captype);
}

void pycpdf_drawJoin(int jointype) {
  return cpdf_drawJoin(jointype);
}

void pycpdf_drawMiter(double m) {
  return cpdf_drawMiter(m);
}

void pycpdf_drawDash(char* description) {
  return cpdf_drawDash(description);
}

void pycpdf_drawPush() {
  return cpdf_drawPush();
}

void pycpdf_drawPop() {
  return cpdf_drawPop();
}

void pycpdf_drawMatrix(double a, double b, double c, double d, double e, double f) {
  return cpdf_drawMatrix(a, b, c, d, e, f);
}

void pycpdf_drawMTrans(double tx, double ty) {
  return cpdf_drawMTrans(tx, ty);
}

void pycpdf_drawMRot(double x, double y, double a) {
  return cpdf_drawMRot(x, y, a);
}

void pycpdf_drawMScale(double x, double y, double sx, double sy) {
  return cpdf_drawMScale(x, y, sx, sy);
}

void pycpdf_drawMShearX(double x, double y, double a) {
  return cpdf_drawMShearX(x, y, a);
}

void pycpdf_drawMShearY(double x, double y, double a) {
  return cpdf_drawMShearY(x, y, a);
}

void pycpdf_drawXObjBBox(double x, double y, double w, double h) {
  return cpdf_drawXObjBBox(x, y, w, h);
}

void pycpdf_drawXObj(char* name) {
  return cpdf_drawXObj(name);
}

void pycpdf_drawUse(char* name) {
  return cpdf_drawUse(name);
}

void pycpdf_drawEndXObj() {
  return cpdf_drawEndXObj();
}

void pycpdf_drawJPEG(char* name, char* fontname) {
  return cpdf_drawJPEG(name, fontname);
}

void pycpdf_drawJPEGMemory(char* name, void* data, int len) {
  return cpdf_drawJPEGMemory(name, data, len);
}

void pycpdf_drawPNG(char* name, char* fontname) {
  return cpdf_drawPNG(name, fontname);
}

void pycpdf_drawPNGMemory(char* name, void* data, int len) {
  return cpdf_drawPNGMemory(name, data, len);
}

void pycpdf_drawImage(char* name) {
  return cpdf_drawImage(name);
}

void pycpdf_drawFillOpacity(double n) {
  return cpdf_drawFillOpacity(n);
}

void pycpdf_drawStrokeOpacity(double n) {
  return cpdf_drawStrokeOpacity(n);
}

void pycpdf_drawBT() {
  return cpdf_drawBT();
}

void pycpdf_drawET() {
  return cpdf_drawET();
}

void pycpdf_drawFont(char* name) {
  return cpdf_drawFont(name);
}

void pycpdf_drawFontSize(double n) {
  return cpdf_drawFontSize(n);
}

void pycpdf_drawText(char* text) {
  return cpdf_drawText(text);
}

void pycpdf_drawSText(char* text) {
  return cpdf_drawSText(text);
}

void pycpdf_drawLeading(double n) {
  return cpdf_drawLeading(n);
}

void pycpdf_drawCharSpace(double n) {
  return cpdf_drawCharSpace(n);
}

void pycpdf_drawWordSpace(double n) {
  return cpdf_drawWordSpace(n);
}

void pycpdf_drawTextScale(double n) {
  return cpdf_drawTextScale(n);
}

void pycpdf_drawRenderMode(int n) {
  return cpdf_drawRenderMode(n);
}

void pycpdf_drawRise(double n) {
  return cpdf_drawRise(n);
}

void pycpdf_drawNL() {
  return cpdf_drawNL();
}

void pycpdf_drawNewPage() {
  return cpdf_drawNewPage();
}


/* CHAPTER 19. Miscellaneous */

void pycpdf_draft(int pdf, int r, int boxes) {
  return cpdf_draft(pdf, r, boxes);
}

void pycpdf_removeAllText(int pdf, int r) {
  return cpdf_removeAllText(pdf, r);
}

void pycpdf_blackText(int pdf, int r) {
  return cpdf_blackText(pdf, r);
}

void pycpdf_blackLines(int pdf, int r) {
  return cpdf_blackLines(pdf, r);
}

void pycpdf_blackFills(int pdf, int r) {
  return cpdf_blackFills(pdf, r);
}

void pycpdf_thinLines(int pdf, int r, double linewidth) {
  return cpdf_thinLines(pdf, r, linewidth);
}

void pycpdf_copyId(int pdf, int pdf2) {
  return cpdf_copyId(pdf, pdf2);
}

void pycpdf_removeId(int pdf) {
  return cpdf_removeId(pdf);
}

void pycpdf_setVersion(int pdf, int version) {
  return cpdf_setVersion(pdf, version);
}

void pycpdf_setFullVersion(int pdf, int major, int minor) {
  return cpdf_setFullVersion(pdf, major, minor);
}

void pycpdf_removeDictEntry(int pdf, char *key) {
  return cpdf_removeDictEntry(pdf, key);
}

void pycpdf_removeDictEntrySearch(int pdf, char *key, char *searchterm) {
  return cpdf_removeDictEntrySearch(pdf, key, searchterm);
}

void pycpdf_replaceDictEntry(int pdf, char *key, char *newvalue) {
  return cpdf_replaceDictEntry(pdf, key, newvalue);
}

void pycpdf_replaceDictEntrySearch(int pdf, char *key, char *newvalue, char *searchterm) {
  return cpdf_replaceDictEntrySearch(pdf, key, newvalue, searchterm);
}

void pycpdf_removeClipping(int pdf, int r) {
  return cpdf_removeClipping(pdf, r);
}


void *getDictEntriesData;

void *pycpdf_getDictEntries(int pdf, char *key, int *length) {
  getDictEntriesData = cpdf_getDictEntries(pdf, key, length);
  return getDictEntriesData;
}

void pycpdf_getDictEntriesFree(void) {
  free(getDictEntriesData);
  return;
}
