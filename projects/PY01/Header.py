#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY01
# FILENAME:....... Header.py
# PYTHON VERSION:. 3.3.3
#============================================================

class Header:
  def gen(self, filename):
    header = []

    index = filename.index(".")
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

    return "\n".join(header)

  def setDividerLength(self, dl):
    self.dividerLength = dl

  def setValueColumn(self, vc):
    self.valueColumn = vc - 2

  def setUserID(self, uid):
    self.userID = uid

  def setProgrammer(self, p):
    self.programmer = p

  def setCourse(self, c):
    self.course = c

  def setTerm(self, t):
    self.term = t

  def setProject(self, p):
    self.project = p

  def setPython(self, p):
    self.python = p
