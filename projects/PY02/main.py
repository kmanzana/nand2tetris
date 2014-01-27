#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY02
# FILENAME:....... main.py
# PYTHON VERSION:. 2.7.2
#============================================================

from util import Util
from file_set import FileSet
from os import path

class Main:
  def main(self):
    print self.main_output()

  @classmethod
  def main_output(cls):
    if Util.number_of_args() >= 2:
      source  = Util.getCommandLineArg(1)
      level   = int(Util.getCommandLineArg(2) or '0')

      return cls.build_main_output(source, level)
    else:
      return '$ python py02.py source level'

  @staticmethod
  def build_main_output(source, level):
    instance = FileSet(source, 'jack')
    include_size  = level == 1 or level == 3
    include_lines = level == 2 or level == 3

    size_header  = 'Size (Bytes)' if include_size  else ''
    lines_header = 'Lines'        if include_lines else ''

    def add_file_info(file):
      file_path = source + '/' + file
      size_info = path.getsize(file_path) if include_size else ''
      lines_info = len(open(file_path, 'rU').readlines()) if include_lines else ''

      return '{:20}{:>20}{:>20}'.format(file, size_info, lines_info)

    file_info = map(add_file_info, instance.file_set)

    lines = [
      '=' * 60,
      '{:20}{:>20}{:>20}'.format('File Name', size_header, lines_header),
      '-' * 60,
      '\n'.join(file_info),
      '-' * 60,
      'FILES: ' + str(len(instance.file_set)),
      '=' * 60
    ]

    return '\n'.join(lines)
