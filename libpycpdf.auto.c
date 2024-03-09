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

/* __AUTO char* version() */
/* __AUTO void setFast() */
/* __AUTO void setSlow() */
/* __AUTO void embedStd14(int embed) */
/* __AUTO void embedStd14Dir(char* d) */
/* __AUTO void JSONUTF8(int utf8) */

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

/* __AUTO void onExit() */

/* CHAPTER 1. Basics */

/* __AUTO int fromFile(char *filename, char *userpw) */
/* __AUTO int fromFileLazy(char *filename, char *userpw) */
/* __AUTO int fromMemory(void *data, int len, char *userpw) */
/* __AUTO int fromMemoryLazy(void *data, int len, char *userpw) */
/* __AUTO void deletePdf(int pdf) */
/* __AUTO void replacePdf(int pdf, int pdf2) */
/* __AUTO double ptOfCm(double i) */
/* __AUTO double ptOfMm(double i) */
/* __AUTO double ptOfIn(double i) */
/* __AUTO double cmOfPt(double i) */
/* __AUTO double mmOfPt(double i) */
/* __AUTO double inOfPt(double i) */
/* __AUTO void startEnumeratePDFs() */
/* __AUTO int enumeratePDFsKey(int n) */
/* __AUTO char* enumeratePDFsInfo(int n) */
/* __AUTO void endEnumeratePDFs() */
/* __AUTO int parsePagespec(int pdf, char *pagespec) */
/* __AUTO int validatePagespec(char *pagespec) */
/* __AUTO char* stringOfPagespec(int pdf, int range) */
/* __AUTO int blankRange() */
/* __AUTO void deleteRange(int r) */

int pycpdf_pageRange(int f, int t) { return cpdf_range(f, t); }

/* __AUTO int all(int r) */
/* __AUTO int even(int r) */
/* __AUTO int odd(int r) */
/* __AUTO int rangeUnion(int a, int b) */
/* __AUTO int difference(int a, int b) */
/* __AUTO int removeDuplicates(int r) */
/* __AUTO int rangeLength(int r) */
/* __AUTO int rangeGet(int r, int n) */
/* __AUTO int rangeAdd(int r, int p) */
/* __AUTO int isInRange(int r, int p) */
/* __AUTO int pages(int pdf) */
/* __AUTO int pagesFast(char *filename, char *userpw) */
/* __AUTO void toFile(int pdf, char *filename, int linearize, int make_id) */
/* __AUTO void toFileExt(int pdf, char *filename, int linearize, int make_id, int preserve_objstm, int generate_objstm, int compress_objstm) */

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

/* __AUTO int isEncrypted(int pdf) */
/* __AUTO void toFileEncrypted(int pdf, int method, int *permissions, int permlength, char *ownerpw, char *userpw, int linearize, int makeid, char *filename) */
/* __AUTO void toFileEncryptedExt(int pdf, int method, int *permissions, int permlength, char *ownerpw, char *userpw, int linearize, int makeid, int preserve_objstm, int generate_objstm, int compress_objstm, char *filename) */
/* __AUTO void decryptPdf(int pdf, char *userpw) */
/* __AUTO void decryptPdfOwner(int pdf, char *ownerpw) */
/* __AUTO int hasPermission(int pdf, int perm) */
/* __AUTO int encryptionKind(int pdf) */
/* __AUTO int mergeSimple(int *pdfs, int len) */
/* __AUTO int merge(int *pdfs, int len, int retain_numbering, int remove_duplicate_fonts) */
/* __AUTO int mergeSame(int *pdfs, int len, int retain_numbering, int remove_duplicate_fonts, int *ranges) */
/* __AUTO int selectPages(int pdf, int r) */

/* CHAPTER 3. Pages */

/* __AUTO void scalePages(int pdf, int r, double sx, double sy) */
/* __AUTO void scaleToFit(int pdf, int r, double sx, double sy, double scale_to_fit_scale) */
/* __AUTO void scaleToFitPaper(int pdf, int r, int papersize, double scale_to_fit_scale) */

void pycpdf_scaleContents(int pdf, int r, int pos, double p1, double p2, double scale) {
  struct cpdf_position p = {
      .cpdf_anchor = pos, .cpdf_coord1 = p1, .cpdf_coord2 = p2};
  cpdf_scaleContents(pdf, r, p, scale);
}

/* __AUTO void shiftContents(int pdf, int r, double dx, double dy) */
/* __AUTO void shiftBoxes(int pdf, int r, double dx, double dy) */
/* __AUTO void rotate(int pdf, int r, int rotation) */
/* __AUTO void rotateBy(int pdf, int r, int rotation) */
/* __AUTO void rotateContents(int pdf, int r, double rotation) */
/* __AUTO void upright(int pdf, int r) */
/* __AUTO void hFlip(int pdf, int r) */
/* __AUTO void vFlip(int pdf, int r) */
/* __AUTO void crop(int pdf, int r, double x, double y, double w, double h) */
/* __AUTO void removeCrop(int pdf, int r) */
/* __AUTO void removeTrim(int pdf, int r) */
/* __AUTO void removeArt(int pdf, int r) */
/* __AUTO void removeBleed(int pdf, int r) */
/* __AUTO void trimMarks(int pdf, int r) */
/* __AUTO void showBoxes(int pdf, int r) */
/* __AUTO void hardBox(int pdf, int r, char *boxname) */

/* CHAPTER 4. Encryption */

/* Encryption covered under Chapter 1 in cpdflib. */

/* CHAPTER 5. Compression */

/* __AUTO void compress(int pdf) */
/* __AUTO void decompress(int pdf) */
/* __AUTO void squeezeInMemory(int pdf) */

/* CHAPTER 6. Bookmarks */

/* __AUTO void startGetBookmarkInfo(int pdf) */
/* __AUTO int numberBookmarks() */
/* __AUTO int getBookmarkLevel(int n) */
/* __AUTO int getBookmarkPage(int pdf, int page) */
/* __AUTO char* getBookmarkText(int n) */
/* __AUTO int getBookmarkOpenStatus(int n) */
/* __AUTO void endGetBookmarkInfo() */
/* __AUTO void startSetBookmarkInfo(int n) */
/* __AUTO void setBookmarkLevel(int n, int level) */
/* __AUTO void setBookmarkPage(int pdf, int n, int targetpage) */
/* __AUTO void setBookmarkOpenStatus(int n, int status) */
/* __AUTO void setBookmarkText(int n, char *text) */
/* __AUTO void endSetBookmarkInfo(int pdf) */

void *getBookmarksJSONData;

void *pycpdf_getBookmarksJSON(int pdf, int *length) {
  getBookmarksJSONData = cpdf_getBookmarksJSON(pdf, length);
  return getBookmarksJSONData;
}

void pycpdf_getBookmarksJSONFree(void) {
  free(getBookmarksJSONData);
  return;
}

/* __AUTO void setBookmarksJSON(int pdf, void* data, int length) */
/* __AUTO void tableOfContents(int pdf, int font, double fontsize, char* title, int bookmark) */

/* CHAPTER 7. Presentations */

/* Not included in the library version */

/* CHAPTER 8. Logos, Watermarks and Stamps */

/* __AUTO void stampOn(int pdf, int pdf2, int r) */
/* __AUTO void stampUnder(int pdf, int pdf2, int r) */

void pycpdf_stampExtended(int pdf, int pdf2, int r, int isover,
                          int scale_stamp_to_fit, int pos, int c1, int c2,
                          int relative_to_cropbox) {
  struct cpdf_position position = {
      .cpdf_anchor = pos, .cpdf_coord1 = c1, .cpdf_coord2 = c2};
  cpdf_stampExtended(pdf, pdf2, r, isover, scale_stamp_to_fit, position,
                     relative_to_cropbox);
  return;
}

/* __AUTO void combinePages(int pdf, int pdf2) */

void pycpdf_addText(int metrics, int pdf, int r, char *text, int pos, double p1,
                    double p2, double line_spacing, int bates, int font,
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
                          double p2, int font, double size) {
  struct cpdf_position position = {
      .cpdf_anchor = pos, .cpdf_coord1 = p1, .cpdf_coord2 = p2};
  cpdf_addTextSimple(pdf, r, text, position, font, size);
  return;
}

/* __AUTO void removeText(int pdf, int r) */
/* __AUTO int textWidth(int font, char* string) */
/* __AUTO void addContent(char* content, int before, int pdf, int r) */
/* __AUTO char* stampAsXObject(int pdf, int r, int stamp_pdf) */

/* CHAPTER 9. Multipage facilities */

/* __AUTO void impose(int pdf, double x, double y, int fit, int columns, int rtl, int btt, int center, double margin, double spacing, double linewidth) */
/* __AUTO void twoUp(int pdf) */
/* __AUTO void twoUpStack(int pdf) */
/* __AUTO void padBefore(int pdf, int r) */
/* __AUTO void padAfter(int pdf, int r) */
/* __AUTO void padEvery(int pdf, int r) */
/* __AUTO void padMultiple(int pdf, int n) */
/* __AUTO void padMultipleBefore(int pdf, int n) */

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

/* CHAPTER 11. Document Information and Metadata */

/* __AUTO int isLinearized(char *filename) */
/* __AUTO int hasObjectStreams(int pdf) */
/* __AUTO char* id1(int pdf) */
/* __AUTO char* id2(int pdf) */ 
/* __AUTO int hasAcroForm(int pdf) */
/* __AUTO int getVersion(int pdf) */
/* __AUTO int getMajorVersion(int pdf) */
/* __AUTO char* getTitle(int pdf) */
/* __AUTO char* getAuthor(int pdf) */
/* __AUTO char* getSubject(int pdf) */
/* __AUTO char* getKeywords(int pdf) */
/* __AUTO char* getCreator(int pdf) */
/* __AUTO char* getProducer(int pdf) */
/* __AUTO char* getCreationDate(int pdf) */
/* __AUTO char* getModificationDate(int pdf) */
/* __AUTO char* getTitleXMP(int pdf) */
/* __AUTO char* getAuthorXMP(int pdf) */
/* __AUTO char* getSubjectXMP(int pdf) */
/* __AUTO char* getKeywordsXMP(int pdf) */
/* __AUTO char* getCreatorXMP(int pdf) */
/* __AUTO char* getProducerXMP(int pdf) */
/* __AUTO char* getCreationDateXMP(int pdf) */
/* __AUTO char* getModificationDateXMP(int pdf) */
/* __AUTO void setTitle(int pdf, char *s) */
/* __AUTO void setAuthor(int pdf, char *s) */
/* __AUTO void setSubject(int pdf, char *s) */
/* __AUTO void setKeywords(int pdf, char *s) */
/* __AUTO void setCreator(int pdf, char *s) */
/* __AUTO void setProducer(int pdf, char *s) */
/* __AUTO void setCreationDate(int pdf, char *s) */
/* __AUTO void setModificationDate(int pdf, char *s) */
/* __AUTO void setTitleXMP(int pdf, char *s) */
/* __AUTO void setAuthorXMP(int pdf, char *s) */
/* __AUTO void setSubjectXMP(int pdf, char *s) */
/* __AUTO void setKeywordsXMP(int pdf, char *s) */
/* __AUTO void setCreatorXMP(int pdf, char *s) */
/* __AUTO void setProducerXMP(int pdf, char *s) */
/* __AUTO void setCreationDateXMP(int pdf, char *s) */
/* __AUTO void setModificationDateXMP(int pdf, char *s) */
/* __AUTO void getDateComponents(char *str, int *year, int *month, int *day, int *hour, int *minute, int *second, int *hour_offset, int *minute_offset) */
/* __AUTO char* dateStringOfComponents(int year, int month, int day, int hour, int minute, int second, int hour_offset, int minute_offset) */
/* __AUTO int getPageRotation(int pdf, int pagenumber) */
/* __AUTO int hasBox(int pdf, int pagenumber, char *box) */
/* __AUTO int numAnnots(int pdf, int pagenumber) */
/* __AUTO void getMediaBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) */
/* __AUTO void getCropBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) */
/* __AUTO void getTrimBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) */
/* __AUTO void getArtBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) */
/* __AUTO void getBleedBox(int pdf, int pagenumber, double *minx, double *maxx, double *miny, double *maxy) */

void pycpdf_setMediaBox(int pdf, int range, double minx, double maxx,
                        double miny, double maxy) {
  cpdf_setMediabox(pdf, range, minx, maxx, miny, maxy);
  return;
}

/* __AUTO void setCropBox(int pdf, int range, double minx, double maxx, double miny, double maxy) */
/* __AUTO void setTrimBox(int pdf, int range, double minx, double maxx, double miny, double maxy) */
/* __AUTO void setArtBox(int pdf, int range, double minx, double maxx, double miny, double maxy) */
/* __AUTO void setBleedBox(int pdf, int range, double minx, double maxx, double miny, double maxy) */
/* __AUTO void markTrapped(int pdf) */
/* __AUTO void markUntrapped(int pdf) */
/* __AUTO void markTrappedXMP(int pdf) */
/* __AUTO void markUntrappedXMP(int pdf) */
/* __AUTO void setPageLayout(int pdf, int layout) */
/* __AUTO void setPageMode(int pdf, int mode) */
/* __AUTO void hideToolbar(int pdf, int flag) */
/* __AUTO void hideMenubar(int pdf, int flag) */
/* __AUTO void hideWindowUi(int pdf, int flag) */
/* __AUTO void fitWindow(int pdf, int flag) */
/* __AUTO void centerWindow(int pdf, int flag) */
/* __AUTO void displayDocTitle(int pdf, int flag) */
/* __AUTO void openAtPage(int pdf, int flag, int pagenumber) */
/* __AUTO void setMetadataFromFile(int pdf, char* filename) */
/* __AUTO void setMetadataFromByteArray(int pdf, void* data, int len) */

void *getMetadataData;

void *pycpdf_getMetadata(int pdf, int *length) {
  getMetadataData = cpdf_getMetadata(pdf, length);
  return getMetadataData;
}

void pycpdf_getMetadataFree(void) {
  free(getMetadataData);
  return;
}

/* __AUTO void removeMetadata(int pdf) */
/* __AUTO void createMetadata(int pdf) */
/* __AUTO void setMetadataDate(int pdf, char* date) */
/* __AUTO int startGetPageLabels(int pdf) */
/* __AUTO int getPageLabelStyle(int n) */ 
/* __AUTO char* getPageLabelPrefix(int n) */
/* __AUTO int getPageLabelOffset(int n) */
/* __AUTO int getPageLabelRange(int n) */
/* __AUTO void endGetPageLabels() */
/* __AUTO void addPageLabels(int pdf, int style, char *prefix, int offset, int range, int progress) */
/* __AUTO void removePageLabels(int pdf) */
/* __AUTO char* getPageLabelStringForPage(int pdf, int pagenumber) */

/* CHAPTER 12. File Attachments */

/* __AUTO void attachFile(char* filename, int pdf) */
/* __AUTO void attachFileToPage(char* filename, int pdf, int pagenumber) */
/* __AUTO void attachFileFromMemory(void* data, int len, char* filename, int pdf) */
/* __AUTO void attachFileToPageFromMemory(void* data, int len, char* filename, int pdf, int pagenumber) */
/* __AUTO void removeAttachedFiles(int pdf) */
/* __AUTO void startGetAttachments(int pdf) */
/* __AUTO int numberGetAttachments() */
/* __AUTO char* getAttachmentName(int n) */
/* __AUTO int getAttachmentPage(int n) */

void *getAttachmentData;

void *pycpdf_getAttachmentData(int n, int *length) {
  getAttachmentData = cpdf_getAttachmentData(n, length);
  return getAttachmentData;
}

void pycpdf_getAttachmentFree(void) {
  free(getAttachmentData);
  return;
}

/* __AUTO void endGetAttachments() */

/* CHAPTER 13. Images. */

/* __AUTO int startGetImageResolution(int pdf, double min_required_resolution) */
/* __AUTO int getImageResolutionPageNumber(int n) */
/* __AUTO char* getImageResolutionImageName(int n) */
/* __AUTO int getImageResolutionXPixels(int n) */
/* __AUTO int getImageResolutionYPixels(int n) */
/* __AUTO double getImageResolutionXRes(int n) */
/* __AUTO double getImageResolutionYRes(int n) */
/* __AUTO void endGetImageResolution() */

/* CHAPTER 14. Fonts */

/* __AUTO void removeFonts(int pdf) */
/* __AUTO void copyFont(int pdf, int pdf2, int range, int pagenumber, char *fontname) */
/* __AUTO void startGetFontInfo(int pdf) */
/* __AUTO int numberFonts() */
/* __AUTO int getFontPage(int n) */
/* __AUTO char* getFontName(int n) */
/* __AUTO char* getFontType(int n) */
/* __AUTO char* getFontEncoding(int n) */
/* __AUTO void endGetFontInfo() */

/* CHAPTER 15. PDF and JSON */

/* __AUTO void outputJSON(char* filename, int parse_content, int no_stream_data, int decompress_streams, int pdf) */

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

/* __AUTO int fromJSON(char *filename) */
/* __AUTO int fromJSONMemory(void *data, int len) */

/* CHAPTER 16. Optional Content Groups */

/* __AUTO int startGetOCGList(int pdf) */
/* __AUTO char* OCGListEntry(int i) */
/* __AUTO void endGetOCGList() */
/* __AUTO void OCGCoalesce(int pdf) */
/* __AUTO void OCGRename(int pdf, char* n_from, char* n_to) */
/* __AUTO void OCGOrderAll(int pdf) */

/* CHAPTER 17. Creating New PDFs */

/* __AUTO int blankDocument(double w, double h, int pages) */
/* __AUTO int blankDocumentPaper(int papersize, int pages) */
/* __AUTO int textToPDF(double w, double h, int font, double fontsize, char *filename) */
/* __AUTO int textToPDFPaper(int papersize, int font, double fontsize, char *filename) */

/* CHAPTER 18. Miscellaneous */

/* __AUTO void draft(int pdf, int r, int boxes) */
/* __AUTO void removeAllText(int pdf, int r) */ 
/* __AUTO void blackText(int pdf, int r) */
/* __AUTO void blackLines(int pdf, int r) */
/* __AUTO void blackFills(int pdf, int r) */
/* __AUTO void thinLines(int pdf, int r, double linewidth) */
/* __AUTO void copyId(int pdf, int pdf2) */
/* __AUTO void removeId(int pdf) */
/* __AUTO void setVersion(int pdf, int version) */
/* __AUTO void setFullVersion(int pdf, int major, int minor) */
/* __AUTO void removeDictEntry(int pdf, char *key) */
/* __AUTO void removeDictEntrySearch(int pdf, char *key, char *searchterm) */
/* __AUTO void replaceDictEntry(int pdf, char *key, char *newvalue) */
/* __AUTO void replaceDictEntrySearch(int pdf, char *key, char *newvalue, char *searchterm) */
/* __AUTO void removeClipping(int pdf, int r) */

void *getDictEntriesData;

void *pycpdf_getDictEntries(int pdf, char *key, int *length) {
  getDictEntriesData = cpdf_getDictEntries(pdf, key, length);
  return getDictEntriesData;
}

void pycpdf_getDictEntriesFree(void) {
  free(getDictEntriesData);
  return;
}
