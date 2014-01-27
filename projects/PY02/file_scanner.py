#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY02
# FILENAME:....... file_scanner.py
# PYTHON VERSION:. 2.7.2
#============================================================

import os
from os import path

class FileScanner:
  @classmethod
  def build_file_set(cls, filename, ext):
    if path.isfile(filename) and cls.has_ext(filename, ext):
      return [filename]
    elif path.isdir(filename):
      return cls.files_with_ext(filename, ext)
    else:
      return []

  @classmethod
  def files_with_ext(cls, filename, ext):
    dir = os.listdir(filename)

    return filter(lambda file: cls.has_ext(file, ext), dir)

  @staticmethod
  def has_ext(file, ext):
    return path.splitext(file)[1] == '.' + ext
