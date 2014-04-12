#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS10
# FILENAME:....... Main.py
# PYTHON VERSION:. 2.7.2
#============================================================

from JackTokenizer     import JackTokenizer
from CompilationEngine import CompilationEngine
import os
# from Util          import Util
# from FileSet       import FileSet

class Main:
  @staticmethod
  def main():
    # print os.path.isfile('./projects/10/ArrayTest/Main.jack')
    tokenizer = JackTokenizer('./projects/10/ArrayTest/Main.jack')
