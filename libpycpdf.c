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

void pycpdf_toFile(int pdf, char *filename, int linearize, int make_id)
{
  cpdf_toFile(pdf, filename, linearize, make_id);
  return;
}
