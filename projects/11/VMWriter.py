#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS11
# FILENAME:....... VMWriter.py
# PYTHON VERSION:. 2.7.2
#============================================================

class VMWriter:
  def __init__(self, output_file):
    pass

  # Writes a VM push command
  def writePush(self, segment, index):
    pass

  # Writes a VM pop command
  def writePop(self, segment, index):
    pass

  # Writes a VM arithmetic command
  # command (ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT)
  def WriteArithmetic(self, command):
    pass

  # Writes a VM label command
  def WriteLabel(self, label):
    pass

  # Writes a VM label command
  def WriteGoto(self, label):
    pass

  # Writes a VM If-goto command
  def WriteIf(self, label):
    pass

  # Writes a VM call command
  def writeCall(self, name, nArgs):
    pass

  # Writes a VM function command
  def writeFunction(self, name, nLocals):
    pass

  # Writes a VM return command
  def writeReturn(self):
    pass

  # Closes the output file
  def close(self):
    pass

  # private
