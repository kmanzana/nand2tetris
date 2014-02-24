#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY04
# FILENAME:....... Parser.py
# PYTHON VERSION:. 2.7.2
#============================================================

class Parser:
  # Prepares to read the .hack file bound to the stream.
  def __init__(self, file):
    self.file            = file
    self.address_count   = -1
    self.nextInstruction = ''
    self.advance()

  def hasMoreInstructions(self):
    return self.nextInstruction != ''

  def advance(self):
    self.address_count += 1
    self.currentInstruction = self.nextInstruction
    self.nextInstruction = self.file.readline()

  def address(self):
    return self.address_count

  def instruction(self):
    return self.currentInstruction

  def hexInstruction(self):
    return "{0:0>4X}".format(int(self.currentInstruction, 2))

  def parsedInstruction(self):
    if self.instructionType() == 'A_TYPE':
      return '0 {} {} {} {}'.format(self.currentInstruction[1:4],
                                    self.currentInstruction[4:8],
                                    self.currentInstruction[8:12],
                                    self.currentInstruction[12:16])
    elif self.instructionType() == 'C_TYPE':
      return '111 {} {} {} {}'.format(self.comp()[0:1],
                                      self.comp()[1:],
                                      self.dest(),
                                      self.jump())


  def instructionType(self):
    if self.currentInstruction[0] == '0':
      return 'A_TYPE'
    elif self.currentInstruction[0:3] == '111':
      return 'C_TYPE'
    else:
      return 'INVALID'

  def value(self):
    return self.currentInstruction

  def dest(self):
    return self.currentInstruction[10:13]

  def comp(self):
    return self.currentInstruction[3:10]

  def jump(self):
    return self.currentInstruction[13:16]
