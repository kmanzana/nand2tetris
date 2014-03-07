#!/usr/bin/env python
import unittest
from code_writer import CodeWriter

class TestCodeWriter(unittest.TestCase):
  def setUp(self):
    self.filename = './StackArithmetic/SimpleAdd/SimpleAdd.asm'
    self.code_writer = CodeWriter(self.filename)

  def tearDown(self):
    self.code_writer.Close()

  def assertion(self, actual, expected):
    asserted = actual == expected
    if not asserted:
      print 'FAILED: assert {} == {}'.format(actual, expected)
    assert asserted

  def test_constructor_sets_attributes(self):
    assert self.code_writer.output.__class__.__name__ == 'file'

  def test_write_arthmetic(self):
    # self.assertion(self.code_writer.writeArithmetic('add'), '')
    assert '@SP' in self.code_writer.writeArithmetic('add')

unittest.main()
