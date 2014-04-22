#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS11
# FILENAME:....... SymbolTable.py
# PYTHON VERSION:. 2.7.2
#============================================================

class SymbolTable:
  counts = {
    'STATIC': 0,
    'FIELD':  0,
    'ARG':    0,
    'VAR':    0
  }

  def __init__(self):
    self.counts['FIELD']  = 0

    self.subroutine_scope = {}
    self.class_scope      = {}

  def startSubroutine(self):
    self.subroutine_scope = {}
    self.counts['ARG']    = 0
    self.counts['VAR']    = 0

  def define(self, name, type, kind):
    number = None

    if kind == 'ARG' or kind == 'VAR':
      if kind == 'ARG':
        self.counts['ARG'] += 1
        number = self.counts['ARG']
      elif kind == 'VAR':
        self.counts['VAR'] += 1
        number = self.counts['VAR']

      self.subroutine_scope[name] = (type, kind, number)
    elif kind == 'STATIC' or kind == 'FIELD':
      if kind == 'STATIC':
        self.counts['STATIC'] += 1
        number = self.counts['STATIC']
      elif kind == 'FIELD':
        self.counts['FIELD'] += 1
        number = self.counts['FIELD']

      self.class_scope[name] = (type, kind, number)

  def varCount(self, kind):
    return self.counts[kind]

  def kindOf(self, name):
    if name in self.subroutine_scope.keys():
      return self.subroutine_scope[name][1]
    elif name in self.class_scope.keys():
      return self.class_scope[name][1]
    else:
      return 'NONE'

  def typeOf(self, name):
    if name in self.subroutine_scope.keys():
      return self.subroutine_scope[name][0]
    elif name in self.class_scope.keys():
      return self.class_scope[name][0]
    else:
      return 'NONE'

  def indexOf(self, name):
    if name in self.subroutine_scope.keys():
      return self.subroutine_scope[name][2]
    elif name in self.class_scope.keys():
      return self.class_scope[name][2]
    else:
      return'NONE'
