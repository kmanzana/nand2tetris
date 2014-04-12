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
    # tokenizer = JackTokenizer('./projects/10/ArrayTest/Main.jack')
    tokenizer = JackTokenizer('./projects/10/Square/Square.jack')

    while tokenizer.hasMoreTokens():
      tokenizer.advance()

      if tokenizer.tokenType() is 'KEYWORD':
        print tokenizer.keyWord()
      elif tokenizer.tokenType() is 'SYMBOL':
        print tokenizer.symbol()
      elif tokenizer.tokenType() is 'IDENTIFIER':
        print tokenizer.identifier()
      elif tokenizer.tokenType() is 'INT_CONST':
        print tokenizer.intVal()
      elif tokenizer.tokenType() is 'STRING_CONST':
        print tokenizer.stringVal()

