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

