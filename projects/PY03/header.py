#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY03
# FILENAME:....... header.py
# PYTHON VERSION:. 2.7.2
#============================================================

class Header:
  def __init__(self, project):
    self.dividerLength = 60
    self.valueColumn = 20 - 2
    self.userID = 'KMANZANA'
    self.programmer = 'Manzanares, Kelton M.'
    self.course = 'CSCI-410'
    self.term = 'SP14'
    self.project = project
    self.python = '2.7.2'

  def gen(self, filename):
    header = []

    index = filename.index('.')
    extension = filename.replace(filename[:index + 1], '')

    if extension == 'hack' or extension == 'xml':
      return ''

    if extension == 'py':
      comment = '#'
    else:
      comment = '//'

    header.append(comment + self.dividerLength * '=')

    row = comment + ' USERID:'
    row = row + (self.valueColumn - row.__len__()) * '.' + ' ' + self.userID
    header.append(row)

    row = comment + ' PROGRAMMER:'
    row = row + (self.valueColumn - row.__len__()) * '.' + ' ' + self.programmer
    header.append(row)

    row = comment + ' COURSE:'
    row = row + (self.valueColumn - row.__len__()) * '.' + ' ' + self.course
    header.append(row)

    row = comment + ' TERM:'
    row = row + (self.valueColumn - row.__len__()) * '.' + ' ' + self.term
    header.append(row)

    row = comment + ' PROJECT:'
    row = row + (self.valueColumn - row.__len__()) * '.' + ' ' + self.project
    header.append(row)

    row = comment + ' FILENAME:'
    row = row + (self.valueColumn - row.__len__()) * '.' + ' ' + filename
    header.append(row)

    if extension == 'py':
      header.append(comment + ' PYTHON VERSION:. ' + self.python)

    header.append(comment + self.dividerLength * '=')
    header.append('')

    return '\n'.join(header)
