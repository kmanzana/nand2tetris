#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS08B
# FILENAME:....... code_writer.py
# PYTHON VERSION:. 2.7.2
#============================================================

COMMANDS = {
  'add': '@SP\n'
    'A=M-1\n'
    'D=M\n'
    'A=A-1\n'
    'M=M+D\n'
    '@SP\n'
    'M=M-1\n',
  'sub': '@SP\n'
    'A=M-1\n'
    'D=M\n'
    'A=A-1\n'
    'M=M-D\n'
    '@SP\n'
    'M=M-1\n',
  'neg': '@0\n'
    'D=A\n'
    '@SP\n'
    'A=M-1\n'
    'M=D-M\n',
  'and': '@SP\n'
    'A=M-1\n'
    'D=M\n'
    'A=A-1\n'
    'M=M&D\n'
    '@SP\n'
    'M=M-1\n',
  'or': '@SP\n'
    'A=M-1\n'
    'D=M\n'
    'A=A-1\n'
    'M=M|D\n'
    '@SP\n'
    'M=M-1\n',
  'or': '@SP\n'
    'A=M-1\n'
    'D=M\n'
    'A=A-1\n'
    'M=M|D\n'
    '@SP\n'
    'M=M-1\n',
  'not': '@0\n'
    'D=A\n'
    '@SP\n'
    'A=M-1\n'
    'M=D-M\n'
    'M=M-1\n'
}

class CodeWriter:
  def __init__(self, output_filename):
    self.output = open(output_filename, 'w')
    self.filename = output_filename.split('/')[-1].replace('.asm', '')

    self.output.write('//============================================================\n'
      '// USERID:........ KMANZANA\n'
      '// PROGRAMMER:.... Manzanares, Kelton M.\n'
      '// COURSE:........ CSCI-410\n'
      '// TERM:.......... SP14\n'
      '// PROJECT:....... translated\n'
      '// FILENAME:...... {}\n'.format(self.filename + '.asm') +
      '//============================================================\n\n')

    self.count = 0

  def setFileName(self, file_name):
    self.output = open(file_name)

  def writeArithmetic(self, command):
    if command in ['eq', 'lt', 'gt']:
      if command == 'eq':
        self.output.write('@SP\n'
          'A=M-1\n'
          'D=M\n'
          'A=A-1\n'
          'D=M-D\n'
          '@{}_EQ_{}\n'.format(self.filename, self.count) +
          'D;JEQ\n'
          '@0\n'
          'D=A\n'
          '@{}_EQ_END_{}\n'.format(self.filename, self.count) +
          '0;JMP\n'
          '({}_EQ_{})\n'.format(self.filename, self.count) +
          '@0\n'
          'D=A-1\n'
          '({}_EQ_END_{})\n'.format(self.filename, self.count) +
          '@SP\n'
          'A=M-1\n'
          'A=A-1\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')
      elif command == 'lt':
        self.output.write('@SP\n'
          'A=M-1\n'
          'D=M\n'
          'A=A-1\n'
          'D=M-D\n'
          '@{}_LT_{}\n'.format(self.filename, self.count) +
          'D;JLT\n'
          '@0\n'
          'D=A\n'
          '@{}_LT_END_{}\n'.format(self.filename, self.count) +
          '0;JMP\n'
          '({}_LT_{})\n'.format(self.filename, self.count) +
          '@0\n'
          'D=A-1\n'
          '({}_LT_END_{})\n'.format(self.filename, self.count) +
          '@SP\n'
          'A=M-1\n'
          'A=A-1\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')
      elif command == 'gt':
        self.output.write('@SP\n'
          'A=M-1\n'
          'D=M\n'
          'A=A-1\n'
          'D=M-D\n'
          '@{}_GT_{}\n'.format(self.filename, self.count) +
          'D;JGT\n'
          '@0\n'
          'D=A\n'
          '@{}_GT_END_{}\n'.format(self.filename, self.count) +
          '0;JMP\n'
          '({}_GT_{})\n'.format(self.filename, self.count) +
          '@0\n'
          'D=A-1\n'
          '({}_GT_END_{})\n'.format(self.filename, self.count) +
          '@SP\n'
          'A=M-1\n'
          'A=A-1\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')

      self.count += 1
    else:
      self.output.write(COMMANDS[command])

  def WritePushPop(self, command, segment, index):
    if command == 'push':
      if segment == 'constant':
        self.output.write('@{}\n'.format(index) +
          'D=A\n'
          '@SP\n'
          'A=M\n'
          'M=D\n'
          '@SP\n'
          'M=M+1\n')
      elif segment == 'local':
        self.output.write('')
    elif command == 'pop':
      if segment == 'local':
        self.output.write(
          '@SP\n'
          'AM=M-1\n'
          'D=M\n'
          '@R13\n'
          'M=D\n'
          '@LCL\n'
          'D=M\n'
          '@{}\n'.format(index) +
          'D=D+A\n'
          'A=M\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')
      elif segment == 'argument':
        self.output.write('@ARG\n'
          'D=A\n'
          '@{}\n'.format(index) +
          'A=D+A\n'
          'D=M\n'
          '@SP\n'
          'A=M\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')
      elif segment == 'this':
        self.output.write('@THIS\n'
          'D=A\n'
          '@{}\n'.format(index) +
          'A=D+A\n'
          'D=M\n'
          '@SP\n'
          'A=M\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')
      elif segment == 'that':
        self.output.write('@THAT\n'
          'D=A\n'
          '@{}\n'.format(index) +
          'A=D+A\n'
          'D=M\n'
          '@SP\n'
          'A=M\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')
      elif segment == 'temp':
        self.output.write('@THAT\n'
          'D=A\n'
          '@{}\n'.format(5 + index) +
          'A=D+A\n'
          'D=M\n'
          '@SP\n'
          'A=M\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')
      elif segment == 'temp':
        self.output.write('@THAT\n'
          'D=A\n'
          '@{}\n'.format(3 + index) +
          'A=D+A\n'
          'D=M\n'
          '@SP\n'
          'A=M\n'
          'M=D\n'
          '@SP\n'
          'M=M-1\n')

  def Close(self):
    self.output.close()
