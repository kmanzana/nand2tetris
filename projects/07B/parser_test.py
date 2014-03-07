#!/usr/bin/env python
import unittest
from parser import Parser

class TestFileSet(unittest.TestCase):
  def setUp(self):
    self.filename = './StackArithmetic/SimpleAdd/SimpleAdd.vm'
    self.parser = Parser(self.filename)

  def test_constructor_sets_attributes(self):
    assert self.parser.input.__class__.__name__ == 'file'

unittest.main()
