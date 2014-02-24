#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ 06A
# FILENAME:....... main.py
# PYTHON VERSION:. 2.7.2
#============================================================

from parser import Parser
from code   import Code
from util   import Util
import os

class Main:
  @staticmethod
  def main():
    filename      = os.path.join(os.getcwd(), Util.getCommandLineArg(1))
    parser        = Parser(filename)
    hack_filename = filename.replace('asm', 'hack')
    file          = open(hack_filename, 'w')

    while parser.has_more_commands():
      parser.advance()

      if parser.command_type() is 'A_COMMAND':
        file.write('{0:016b}\n'.format(int(parser.symbol())))
      elif parser.command_type() is 'C_COMMAND':
        dest = Code.dest(parser.dest())
        comp = Code.comp(parser.comp())
        jump = Code.jump(parser.jump())

        file.write('111{0}{1}{2}\n'.format(comp, dest, jump))

      # elif parser.command_type() is 'L_COMMAND':
      #   parser.symbol()

    file.close()
