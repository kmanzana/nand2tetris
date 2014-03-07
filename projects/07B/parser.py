#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS07B
# FILENAME:....... parser.py
# PYTHON VERSION:. 2.7.2
#============================================================

class Parser:
  def __init__(self, input_filename):
    self.input = open(input_filename, 'rU')

  def has_more_commands(self):
    return self.next_command != ''

  def advance(self):
    self.current_command = self.next_command
    self.next_command = self.file.readline()

  def command_type(self):
    pass

  def arg1(self):
    pass

  def arg2(self):
    pass
