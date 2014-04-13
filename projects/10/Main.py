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
from Util              import Util
from FileSet           import FileSet
import os
import dicttoxml

class Main:
  XML_CONVSERSIONS = {
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;'
  }

  @staticmethod
  def main():
    path = Util.getCommandLineArgument(1)
    # engine = CompilationEngine(path.replace('.jack', '') + '.xml')

    if os.path.isdir(path):
      files = FileSet(path, 'jack')

      while files.hasMoreFiles():
        filename = files.nextFile()
        Main.do_stuff(filename)

    elif os.path.isfile(path):
      Main.do_stuff(path)

    else:
      print '{} is not a file or dir'.format(path)



  @staticmethod
  def do_stuff(path):
    token_file = open(path.replace('.jack', 'T.xml'), 'w')
    tokenizer = JackTokenizer(path)

    token_file.write('<tokens>\n')

    while tokenizer.hasMoreTokens():
      tokenizer.advance()

      if tokenizer.tokenType() is 'KEYWORD':
        token_file.write('<keyword> {} </keyword>\n'.format(tokenizer.keyWord().lower()))
      elif tokenizer.tokenType() is 'SYMBOL':
        symbol = tokenizer.symbol()
        if symbol in ['<', '>', '&']:
          symbol = Main.XML_CONVSERSIONS[symbol]

        token_file.write('<symbol> {} </symbol>\n'.format(symbol))
      elif tokenizer.tokenType() is 'IDENTIFIER':
        token_file.write('<identifier> {} </identifier>\n'.format(tokenizer.identifier()))
      elif tokenizer.tokenType() is 'INT_CONST':
        token_file.write('<integerConstant> {} </integerConstant>\n'.format(tokenizer.intVal()))
      elif tokenizer.tokenType() is 'STRING_CONST':
        token_file.write('<stringConstant> {} </stringConstant>\n'.format(tokenizer.stringVal()))

    token_file.write('</tokens>\n')
    token_file.close()
