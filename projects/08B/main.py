#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS08B
# FILENAME:....... main.py
# PYTHON VERSION:. 2.7.2
#============================================================

from parser      import Parser
from code_writer import CodeWriter
from Util        import Util
from FileSet     import FileSet
import os

class Main:
  @staticmethod
  def main():
    path = Util.getCommandLineArgument(1)
    code_writer = CodeWriter(path.replace('.vm', '') + '.asm')

    if os.path.isdir(path):
      files = FileSet(path, 'vm')

      while files.hasMoreFiles():
        filename = files.nextFile()
        Main.parse(filename, code_writer)
    elif os.path.isfile(path):
      Main.parse(path, code_writer)

    code_writer.Close()

  @staticmethod
  def parse(filename, code_writer):
    parser = Parser(filename)

    while parser.hasMoreCommands():
      parser.advance()

      if parser.commandType() in ['C_PUSH', 'C_POP']:
        code_writer.WritePushPop(parser.command(), parser.arg1(), parser.arg2())
      elif parser.commandType() == 'C_ARITHMETIC':
        code_writer.writeArithmetic(parser.command())
