#============================================================
# USERID:......... wbahn
# PROGRAMMER:..... Bahn, William L.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY02
# FILENAME:....... FileSet.py
# PYTHON VERSION:. 3.3.3
#============================================================

#============================================================
#
# This class is designed to facilitate the batch processing 
# of files in a fashion that is compatible with the 
# Nand2Tetris projects.
#
# USAGE SKELETON
#
# from FileSet import FileSet
#
# files = FileSet("fred", "txt")
#
# files.report()
#
# while files.hasMoreFiles():
#    filename = files.nextFile()
#    # Do whatever with filename
#
#============================================================

import os # For directory and path functions

class FileSet:

   def __init__(self, filename, ext):
      self.target_ext = "."+ext
      (self.fname, self.ext) = ("test", "") # default
      if (filename):
         (self.fname, self.ext) = os.path.splitext(filename)
         
      # Determine if a file or directory was supplied
      self.type_file = False
      self.type_dir = False
      if (self.ext):
         if (self.ext == self.target_ext):
            self.type_file = True
      else:
         self.type_dir = True

      self.fileList = []
      self.dirList = []
      
      # Supplied name is a file of the correct extension
      if (self.type_file):
         if (os.path.isfile(filename)):
            self.dirList = [filename]

      # Supplied name is a directory
      if (self.type_dir):
         if (os.path.isdir(self.fname)):
            #os.chdir(self.fname)
            #self.dirList = os.listdir('.')
            self.dirList = os.listdir(self.fname)

      for filename in self.dirList:
         if (os.path.splitext(filename)[1] == self.target_ext):
            if self.type_dir:
                filename = os.path.join(self.fname,filename)
            self.fileList.append(filename)

#------------------------------------------------------------
# Public Functions   
#------------------------------------------------------------

   def report(self):
      if (self.type_file):
         print("Processing FILE: %s" % self.fname)
      if (self.type_dir):
         print("Processing DIRECTORY: %s" % self.fname)

      print("Files: %i" % len(self.fileList))

      for filename in self.fileList:
         print("  %s" % os.path.basename(filename))
         
   def hasMoreFiles(self):
      if self.fileList:
         return True
      return False
   
   def nextFile(self):
      filename = None
      if self.fileList:
         filename = self.fileList[0]
         self.fileList.remove(filename)
      return filename

   def basename(self):
      return self.fname

#============================================================
