#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ 06B
# FILENAME:....... main.py
# PYTHON VERSION:. 2.7.2
#============================================================

from parser       import Parser
from code         import Code
from util         import Util
from symbol_table import SymbolTable
import os

class Main:
  @staticmethod
  def main():
    filename      = os.path.join(os.getcwd(), Util.getCommandLineArg(1))
    first_parser  = Parser(filename)
    second_parser = Parser(filename)
    symbol_table  = SymbolTable()

    hack_filename = filename.replace('asm', 'hack')
    hack_file     = open(hack_filename, 'w')

    ann_filename  = filename.replace('asm', 'ann')
    ann_file      = open(ann_filename, 'w')

    rom_address = 0
    ram_address = 16

    assembly    = ''

    while first_parser.has_more_commands():
      first_parser.advance()

      if first_parser.command_type() is 'A_COMMAND' or first_parser.command_type() is 'C_COMMAND':
        rom_address += 1
      elif first_parser.command_type() is 'L_COMMAND':
        symbol_table.add_entry(first_parser.symbol(), rom_address, 'LAB')

    while second_parser.has_more_commands():
      second_parser.advance()
      machine_command = ''

      if second_parser.command_type() is 'A_COMMAND':
        if second_parser.symbol()[0].isdigit():
          binary = second_parser.symbol()
        else:
          if symbol_table.contains(second_parser.symbol()):
            binary = symbol_table.get_address(second_parser.symbol())
          else:
            binary = ram_address
            symbol_table.add_entry(second_parser.symbol(), ram_address, 'VAR')
            ram_address += 1

        machine_command = '{0:016b}\n'.format(int(binary))

        hack_file.write(machine_command)
      elif second_parser.command_type() is 'C_COMMAND':
        dest = Code.dest(second_parser.dest())
        comp = Code.comp(second_parser.comp())
        jump = Code.jump(second_parser.jump())

        machine_command = '111{0}{1}{2}\n'.format(comp, dest, jump)

        hack_file.write(machine_command)

      assembly = second_parser.original_command().strip()
      mc = machine_command.strip()

      annotated_machine = '{} {} {} {}'.format(mc[0:4], mc[4:8], mc[8:12], mc[12:16])

      symbolless_command = ''

      if second_parser.command_type() is 'L_COMMAND':
        symbolless_command = symbol_table.get_address(second_parser.symbol())
      elif second_parser.command_type() is 'A_COMMAND' and not second_parser.symbol().isdigit():
        symbolless_command = '@{}'.format(symbol_table.get_address(second_parser.symbol()))
      else:
        symbolless_command = second_parser.command

      annotated_command = '{:<39} {} {:<11} {}\n'.format(assembly, '//' if second_parser.command_type() else '', symbolless_command, annotated_machine)

      ann_file.write(annotated_command)

    ann_file.write('\n// Symbol Table:\n')

    for symbol, address in symbol_table.symbol_table.items():
      ann_file.write('// {}: {:<30} -> {}\n'.format(address[1], symbol, address[0]))

    hack_file.close()
    ann_file.close()
