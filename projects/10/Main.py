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

class Main:
  XML_CONVSERSIONS = {
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;'
  }

  @staticmethod
  def main():
    path = Util.getCommandLineArgument(1)

    if os.path.isdir(path):
      files = FileSet(path, 'jack')

      while files.hasMoreFiles():
        filename = files.nextFile()
        Main.compile_jack(filename)

    elif os.path.isfile(path):
      Main.compile_jack(path)

    else:
      print '{} is not a file or dir'.format(path)

  @staticmethod
  def compile_jack(jack_file_name):
    token_file_name = Main.create_token_file(jack_file_name)
    Main.create_compiled_filei(jack_file_name, token_file_name)

  @staticmethod
  def create_token_file(jack_file_name):
    token_file_name = jack_file_name.replace('.jack', 'T.xml')
    token_file      = open(token_file_name, 'w')
    jack_file       = open(jack_file_name, 'rU')
    tokenizer       = JackTokenizer(jack_file)

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

    return token_file_name

  @staticmethod
  def create_compiled_file(jack_file_name, token_file_name):
    token_file      = open(token_file_name, 'rU')
    engine_file     = open(jack_file_name.replace('.jack', '') + '.xml', 'w')
    engine          = CompilationEngine(engine_file, token_file)

    engine.compileClass()

    engine_file.close()
