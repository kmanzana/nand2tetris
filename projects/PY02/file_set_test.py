import unittest
from file_set import FileSet

class TestFileSet(unittest.TestCase):
  def setUp(self):
    self.instance = FileSet('12', 'jack')

  def test_constructor_set_attributes(self):
    assert self.instance.filename == '12'
    assert self.instance.ext == 'jack'

  def test_baseName_for_directory(self):
    assert self.instance.baseName() == '12'

  def test_baseName_for_file(self):
    orig_filename = self.instance.filename
    self.instance.filename = 'foo.ext'

    assert self.instance.baseName() == 'foo'

  def test_hasMoreFiles_when_full(self):
    self.assertTrue(self.instance.hasMoreFiles())

  def test_hasMoreFiles_when_empty(self):
    self.assertFalse(FileSet('foo', 'bar').hasMoreFiles())

  def test_nextFile(self):
    assert self.instance.file_set[-1] == self.instance.nextFile()

  def test_build_report_no_such_file(self):
    no_such_file_instance = FileSet('not_here', 'jack')

    assert no_such_file_instance.build_report() == ('Processing FILE\n'
      'Base: not_here\n'
      'Type: jack\n'
      'Files: 0\n')

  def test_build_report_no_such_file(self):
    no_such_file_instance = FileSet('12', 'jack')

    print no_such_file_instance.build_report()
    assert no_such_file_instance.build_report() == ('Processing DIRECTORY\n'
      'Base: 12\n'
      'Type: jack\n'
      'Files: 8\n'
      ' Array.jack\n'
      ' Keyboard.jack\n'
      ' Math.jack\n'
      ' Memory.jack\n'
      ' Output.jack\n'
      ' Screen.jack\n'
      ' String.jack\n'
      ' Sys.jack\n')

class TestFileScanner(unittest.TestCase):
  def test_build_file_set_for_file(self):
    file_set = FileSet('util.py', 'py')
    assert file_set.file_set == ['util.py']

  def test_build_file_set_for_missing_file(self):
    file_set = FileSet('missing.py', 'py')
    assert file_set.file_set == []

  def test_build_file_set_for_file_with_mismatched_extension(self):
    file_set = FileSet('util.py', 'different')
    assert file_set.file_set == []

  def test_build_file_set_for_directory(self):
    file_set = FileSet('12', 'jack')

    expected = [
      'Array.jack',
      'Keyboard.jack',
      'Math.jack',
      'Memory.jack',
      'Output.jack',
      'Screen.jack',
      'String.jack',
      'Sys.jack'
    ]

    expected.sort()

    assert file_set.file_set == expected

  def test_build_file_set_for_missing_directory(self):
    file_set = FileSet('missing', 'py')
    assert file_set.file_set == []

unittest.main()
