#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS07B
# FILENAME:....... code_writer.py
# PYTHON VERSION:. 2.7.2
#============================================================

class CodeWriter:
  def __init__(self, output_filename):
    self.output = open(output_filename, 'w')

    self.output.write('//============================================================'
      '// USERID:........ KMANZANA'
      '// PROGRAMMER:.... Manzanares, Kelton M.'
      '// COURSE:........ CSCI-410'
      '// TERM:.......... SP14'
      '// PROJECT:....... translated'
      '// FILENAME:...... {}'.format(output_filename) +
      '//============================================================')

  def set_file_name(self, file_name):
    self.output = open(file_name)

  def write_arithmetic(self, command):
    pass

  def write_push_pop(self, command, segment, index):
    pass

  def close(self):
    self.output.close()
