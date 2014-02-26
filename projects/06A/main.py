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
    hack_file     = open(hack_filename, 'w')

    ann_filename  = filename.replace('asm', 'ann')
    ann_file      = open(ann_filename, 'w')


    while parser.has_more_commands():
      parser.advance()
      machine_command = ''

      if parser.command_type() is 'A_COMMAND':
        machine_command = '{0:016b}\n'.format(int(parser.symbol()))

        hack_file.write(machine_command)
      elif parser.command_type() is 'C_COMMAND':
        dest = Code.dest(parser.dest())
        comp = Code.comp(parser.comp())
        jump = Code.jump(parser.jump())

        machine_command = '111{0}{1}{2}\n'.format(comp, dest, jump)

        hack_file.write(machine_command)

      # elif parser.command_type() is 'L_COMMAND':
      #   parser.symbol()

      assembly = parser.original_command().strip()

      mc = machine_command.strip()

      annotated_machine = '{} {} {} {}'.format(mc[0:4], mc[4:8], mc[8:12], mc[12:16])
      annotated_command = '{:<39} // {:<11} {}\n'.format(assembly, parser.command, annotated_machine)

      ann_file.write(annotated_command)

    hack_file.close()
    ann_file.close()
