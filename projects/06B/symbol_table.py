#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ 06B
# FILENAME:....... symbol_table.py
# PYTHON VERSION:. 2.7.2
#============================================================

class SymbolTable:
  def __init__(self):
    self.symbol_table = {
      'SP':     [0, 'VAR'],
      'LCL':    [1, 'VAR'],
      'ARG':    [2, 'VAR'],
      'THIS':   [3, 'VAR'],
      'THAT':   [4, 'VAR'],
      'R0':     [0, 'VAR'],
      'R1':     [1, 'VAR'],
      'R2':     [2, 'VAR'],
      'R3':     [3, 'VAR'],
      'R4':     [4, 'VAR'],
      'R5':     [5, 'VAR'],
      'R6':     [6, 'VAR'],
      'R7':     [7, 'VAR'],
      'R8':     [8, 'VAR'],
      'R9':     [9, 'VAR'],
      'R10':    [10, 'VAR'],
      'R11':    [11, 'VAR'],
      'R12':    [12, 'VAR'],
      'R13':    [13, 'VAR'],
      'R14':    [14, 'VAR'],
      'R15':    [15, 'VAR'],
      'SCREEN': [16384, 'VAR'],
      'KBD':    [24576, 'VAR']
    }

  def add_entry(self, symbol, address, type):
    self.symbol_table[symbol] = [address, type]

  def contains(self, symbol):
    return symbol in self.symbol_table

  def get_address(self, symbol):
    return self.symbol_table[symbol][0]
