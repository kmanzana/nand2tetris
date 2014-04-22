#!/usr/bin/env python
import unittest
from SymbolTable import SymbolTable

class TestSymbolTable(unittest.TestCase):
  def setUp(self):
    self.symbol_table = SymbolTable()

  def tearDown(self):
    pass

  # def assertion(self, actual, expected):
  #   asserted = actual == expected
  #   if not asserted:
  #     print 'FAILED: assert {} == {}'.format(actual, expected)
  #   assert asserted

  def test_constructor(self):
    assert self.symbol_table.__class__.__name__ == 'SymbolTable'

  def test_define_var(self):
    self.symbol_table.define('foo', 'int', 'STATIC')

    assert self.symbol_table.counts['STATIC'] == 1
    assert self.symbol_table.class_scope['foo'] == ('int', 'STATIC', 1)

  def test_define_field(self):
    self.symbol_table.define('bar', 'Snake', 'VAR')
    self.symbol_table.define('foo', 'int', 'FIELD')

    assert self.symbol_table.counts['VAR'] == 1
    assert self.symbol_table.subroutine_scope['bar'] == ('Snake', 'VAR', 1)

  def test_varCount(self):
    self.symbol_table.define('foo', 'int', 'FIELD')

    assert self.symbol_table.varCount('FIELD')  == 1
    assert self.symbol_table.varCount('ARG')    == 0
    assert self.symbol_table.varCount('STATIC') == 2
    assert self.symbol_table.varCount('VAR')    == 1

  def test_kindOf(self):
    self.symbol_table.define('foo', 'int', 'FIELD')

    assert self.symbol_table.kindOf('foo') == 'FIELD'
    assert self.symbol_table.kindOf('bar') == 'NONE'

  def test_typeOf(self):
    self.symbol_table.define('foo', 'Square', 'FIELD')

    assert self.symbol_table.typeOf('foo') == 'Square'
    assert self.symbol_table.typeOf('bar') == 'NONE'

  def test_indexOf(self):
    self.symbol_table.define('foo', 'boolean', 'FIELD')
    self.symbol_table.define('bar', 'char', 'FIELD')
    self.symbol_table.define('qaz', 'char', 'STATIC')

    assert self.symbol_table.indexOf('foo') == 1
    assert self.symbol_table.indexOf('bar') == 2
    assert self.symbol_table.indexOf('qaz') == 2
    assert self.symbol_table.indexOf('quz') == 'NONE'

unittest.main()
