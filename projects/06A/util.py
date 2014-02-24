#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY06A
# FILENAME:....... util.py
# PYTHON VERSION:. 2.7.2
#============================================================

import sys

class Util:
  @classmethod
  def getCommandLineArg(cls, argument_index):
    if cls.number_of_args() > argument_index:
      return sys.argv[argument_index]
    else:
      return

  @staticmethod
  def number_of_args():
    return len(sys.argv)
