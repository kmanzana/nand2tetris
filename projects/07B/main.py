#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS07B
# FILENAME:....... main.py
# PYTHON VERSION:. 2.7.2
#============================================================

from parser      import Parser
from code_writer import CodeWriter
import os

class Main:
  @staticmethod
  def main():
    code_writer = CodeWriter('./StackArithmetic/SimpleAdd/SimpleAdd.vm')

    # if isdir:
    #   for file in dirlist:
    #     Main.parse(file)
    # else
    #   Main.parse(file)

    code_writer.close()

  @staticmethod
  def parse(filename):
    parser = Parser(filename)

    if parser.has_more_commands():
      parser.advance()
