#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cpdflibwrapper.h"

/* CHAPTER 0. Preliminaries */

int pycpdf_startup(void)
{
   char *argv[] = {"program_name", NULL};
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
  return cpdf_lastErrorString;
}

void pycpdf_clearError(void)
{
  cpdf_clearError();
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
