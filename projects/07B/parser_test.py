#!/usr/bin/env python
import unittest
from parser import Parser

class TestParser(unittest.TestCase):
  def setUp(self):
    self.filename = './StackArithmetic/SimpleAdd/SimpleAdd.vm'
    self.parser = Parser(self.filename)

  def assertion(self, actual, expected):
    asserted = actual == expected
    if not asserted:
      print 'FAILED: assert {} == {}'.format(actual, expected)
    assert asserted

  def test_constructor_sets_attributes(self):
    assert self.parser.input.__class__.__name__ == 'file'

  def test_commandType_push(self):
    self.parser.fields = 'push constant 0'.split()
    self.assertion(self.parser.commandType(), 'C_PUSH')

  def test_commandType_pop(self):
    self.parser.fields = 'pop local 0'.split()
    self.assertion(self.parser.commandType(), 'C_POP')

  def test_commandType_arithmetic(self):
    self.parser.fields = 'add'.split()
    self.assertion(self.parser.commandType(), 'C_ARITHMETIC')

  def test_commandType_unknown(self):
    self.parser.fields = '// comment'.split()
    self.assertion(self.parser.commandType(), 'UNKNOWN')

    self.parser.fields = ''.split()
    self.assertion(self.parser.commandType(), 'UNKNOWN')

  def test_arg1(self):
    self.parser.fields = 'push constant 2'.split()
    self.assertion(self.parser.arg1(), 'constant')

    self.parser.fields = 'add'.split()
    self.assertion(self.parser.arg1(), '')

  def test_arg2(self):
    self.parser.fields = 'push constant 2'.split()
    self.assertion(self.parser.arg2(), 2)

    self.parser.fields = 'add'.split()
    self.assertion(self.parser.arg2(), '')

unittest.main()
