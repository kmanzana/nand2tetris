import unittest
from parser import Parser

class TestParser(unittest.TestCase):
  def setUp(self):
    self.filename = './add/Add.asm'
    self.parser = Parser(self.filename)

  def test_constructor_set_attributes(self):
    assert self.parser.commands == open(self.filename).readlines()
    assert self.parser.command_number == -1

  def test_strip_white_space(self):
    line = 'D = D + A // blah \r\n'
    expected_line = 'D=D+A//blah'

    actual_line = self.parser.strip_white_space(line)

    assert expected_line == actual_line

  def test_command_type_C_instruction(self):
    self.parser.command = '@192'
    assert self.parser.command_type() == 'A_COMMAND'

    self.parser.command = '@FOO'
    assert self.parser.command_type() == 'A_COMMAND'

  def test_command_type_C_instruction(self):
    self.parser.command = 'AD=M+D'
    assert self.parser.command_type() == 'C_COMMAND'

    self.parser.command = 'D;JGT'
    assert self.parser.command_type() == 'C_COMMAND'

    self.parser.command = 'D=X4C;JGT'
    assert self.parser.command_type() == 'C_COMMAND'

  def test_command_type_L_instruction(self):
    self.parser.command = '(Xxx)'
    assert self.parser.command_type() == 'L_COMMAND'

  def test_symbol(self):
    self.parser.command = '@foo'
    assert self.parser.symbol() == 'foo'

    self.parser.command = '@2'
    assert self.parser.symbol() == '2'

    self.parser.command = '(Xxx)'
    assert self.parser.symbol() == 'Xxx'

unittest.main()
