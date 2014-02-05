#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY03
# FILENAME:....... file_set.py
# PYTHON VERSION:. 2.7.2
#============================================================

import os
from file_scanner import FileScanner

class FileSet:
  def __init__(self, filename, ext):
    self.filename = filename
    self.ext      = ext
    self.file_set = FileScanner.build_file_set(filename, ext)

  def baseName(self):
    return os.path.splitext(self.filename)[0]

  def hasMoreFiles(self):
    return not not self.file_set

  def nextFile(self):
    return self.file_set.pop()

  def report(self):
    print self.build_report()

  def build_report(self):
    processing = ('DIRECTORY' if os.path.isdir(self.filename) else 'FILE')

    return ('Processing ' + processing + '\n'
      'Base: ' + self.baseName() + '\n'
      'Type: ' + self.ext + '\n'
      'Files: ' + str(len(self.file_set)) + '\n'
      ' ' + '\n '.join(self.file_set) + '\n')
