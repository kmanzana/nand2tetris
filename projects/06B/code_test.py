import unittest
from code import Code


class TestParser(unittest.TestCase):
  def setUp(self):
    pass

  def test_comp_without_XHH_instructions(self):
    assert Code.comp('D+1') == '0011111'
    assert Code.comp('D&M') == '1000000'

  def test_xhh_type(self):
    assert Code.xhh_type('X7F') == '1111111'
    assert Code.xhh_type('X1D') == '0011101'

  def test_comp_with_XHH_instructions(self):
    # print '\n{} == \n{}'.format(Code.comp('D&A'), Code.comp('X00'))
    assert Code.comp('X7F') == '1111111'
    assert Code.comp('X3A') == '0111010'
    assert Code.comp('D&A') == Code.comp('X00')

unittest.main()
