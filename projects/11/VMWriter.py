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
    self.output = output_file

  # Writes a VM push command
  def writePush(self, segment, index):
    self.output.write('push {} {}\n'.format(segment, index))

  # Writes a VM pop command
  def writePop(self, segment, index):
    self.output.write('pop {} {}\n'.format(segment, index))

  # Writes a VM arithmetic command
  # command (ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT)
  def writeArithmetic(self, command):
    self.output.write(command.lower() + '\n')

  # Writes a VM label command
  def writeLabel(self, label):
    self.output.write('label {}'.format(label))

  # Writes a VM label command
  def writeGoto(self, label):
    self.output.write('goto {}'.format(label))

  # Writes a VM If-goto command
  def writeIf(self, label):
    self.output.write('if-goto {}'.format(label))

  # Writes a VM call command
  def writeCall(self, name, nArgs):
    self.output.write('call {} {}\n'.format(name, nArgs))

  # Writes a VM function command
  def writeFunction(self, name, nLocals):
    self.output.write('function {} {}\n'.format(name, nLocals))

  # Writes a VM return command
  def writeReturn(self):
    self.output.write('return\n')

  # Closes the output file
  def close(self):
    self.output.close()

  # private
  def write(self, stuff):
    self.output.write(stuff)
