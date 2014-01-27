import unittest
from main import Main

class TestMain(unittest.TestCase):
  def test_main_output(self):
    source = '12'
    level  = None

    print Main.build_main_output(source, level)
    print (
    '============================================================\n'
    'File Name\n'
    '------------------------------------------------------------\n'
    'Array.jack\n'
    'Keyboard.jack\n'
    'Math.jack\n'
    'Memory.jack\n'
    'Output.jack\n'
    'Screen.jack\n'
    'String.jack\n'
    'Sys.jack\n'
    '------------------------------------------------------------\n'
    'FILES: 8\n'
    '============================================================\n')
    assert Main.build_main_output(source, level) == (
    '============================================================\n'
    'File Name\n'
    '------------------------------------------------------------\n'
    'Array.jack\n'
    'Keyboard.jack\n'
    'Math.jack\n'
    'Memory.jack\n'
    'Output.jack\n'
    'Screen.jack\n'
    'String.jack\n'
    'Sys.jack\n'
    '------------------------------------------------------------\n'
    'FILES: 8\n'
    '============================================================\n')

  # def test_main_output_level_1(self):
  #   source = '12'
  #   level  = 1

  #   print Main.build_main_output(source, level)
  #   assert Main.build_main_output(source, level) == (
  #   '============================================================\n'
  #   'File Name                   Size (Bytes)\n'
  #   '------------------------------------------------------------\n'
  #   'Array.jack\n'
  #   'Keyboard.jack\n'
  #   'Math.jack\n'
  #   'Memory.jack\n'
  #   'Output.jack\n'
  #   'Screen.jack\n'
  #   'String.jack\n'
  #   'Sys.jack\n'
  #   '------------------------------------------------------------\n'
  #   'FILES: 8\n'
  #   '============================================================\n')

unittest.main()
