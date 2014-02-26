#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ 06A
# FILENAME:....... parser.py
# PYTHON VERSION:. 2.7.2
#============================================================

import re

class Parser:
  def __init__(self, filename):
    self.commands = open(filename).readlines()
    self.command_number = -1

  def has_more_commands(self):
    return self.command_number < len(self.commands) - 1

  def advance(self):
    self.command_number += 1
    self.command = self.strip_white_space(self.strip_comments(self.commands[self.command_number]))

  def command_type(self):
    if '@' in self.command:
      return 'A_COMMAND'
    elif '=' in self.command or ';' in self.command:
      return 'C_COMMAND'
    # elif:
    #   return 'L_COMMAND'

  def symbol(self):
    return self.command.split('@')[1]

  def dest(self):
    if '=' in self.command:
      return self.command.split('=')[0]
    else:
      return ''

  def comp(self):
    partial = re.sub(r'.*=', '', self.command)
    return re.sub(r';.*', '', partial)

  def jump(self):
    if ';' in self.command:
      return self.command.split(';')[-1]
    else:
      return ''


  def original_command(self):
    return self.commands[self.command_number]

  # private

  def decimal_to_binary(self, line):
    pass

  def strip_comments(self, line):
    return line.split('//')[0]

  def strip_white_space(self, line):
    return ''.join(line.split())
