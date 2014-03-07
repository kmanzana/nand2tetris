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
    self.input        = open(input_filename, 'rU')
    self.next_command = ''
    self.arithmetic_commands = [
      'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'
    ]

    self.advance()

  def hasMoreCommands(self):
    return self.next_command != ''

  def advance(self):
    self.current_command = self.next_command
    self.next_command = self.input.readline()
    self.fields = self.current_command.split()

  def commandType(self):
    if len(self.fields) > 0:
      if self.fields[0] == 'push':
        return 'C_PUSH'
      elif self.fields[0] == 'pop':
        return 'C_POP'
      elif self.fields[0] in self.arithmetic_commands:
        return 'C_ARITHMETIC'

    return 'UNKNOWN'

    # C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL
    pass

  def command(self):
    if len(self.fields) > 0:
      return self.fields[0]
    else:
      return ''

  def arg1(self):
    if len(self.fields) > 1:
      return self.fields[1]
    else:
      return ''

  def arg2(self):
    if len(self.fields) > 2:
      return int(self.fields[2])
    else:
      return ''
