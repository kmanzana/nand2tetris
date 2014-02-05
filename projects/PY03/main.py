#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY03
# FILENAME:....... main.py
# PYTHON VERSION:. 2.7.2
#============================================================

from file_set import FileSet
from header   import Header
import os

class Main:
  def main(self):
    self.header = Header('PY03')

    for ext in ['hdl', 'asm', 'vm', 'jack', 'py']:
      ext_file_set = FileSet('test', ext)

      while ext_file_set.hasMoreFiles():
        filename = ext_file_set.nextFile()
        basename = ext_file_set.baseName()

        self.create_bak_file(basename, filename)
        self.add_header(filename)

  def create_bak_file(self, basename, filename):
    with open(os.path.join(basename, filename)) as file:
      print file.read().splitlines()[0]


  def add_header(self, filename):
    print self.header.gen(filename)
