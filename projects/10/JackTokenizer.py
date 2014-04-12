#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS10
# FILENAME:....... JackTokenizer.py
# PYTHON VERSION:. 2.7.2
#============================================================

import re

# do this by hand first
class JackTokenizer:
  KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static',
    'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this',
    'let', 'do', 'if', 'else', 'while', 'return']

  SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/',
    '&', ', ', '<', '>', '=',  '~']

  INTEGER_CONSTANT_MAX = 32767
  INTEGER_CONSTANT_MIN = 0

  STRING_CONSTANT_START = '"'

  IDENTIFIER_REGEX = re.compile('^[A-z_]+\w*$')

  def __init__(self, input_filename):
    self.input        = open(input_filename, 'rU').read()
    self.input_length = len(self.input)
    self.next_token   = ''
    self.tokens       = self.tokenize()

    print self.remove_comments()
    # self.advance()

  def hasMoreTokens(self):
    return self.next_token != ''

  def advance(self):
    self.current_token = self.next_token
    self.next_token = self.input.read()
    self.fields = self.current_token.split()

  def tokenType(self):
    pass

  def keyWord(self):
    # return upcase(self.current_token)
    pass

  def symbol(self):
    pass

  def identifier(self):
    pass

  def intVal(self):
    pass

  def stringVal(self):
    pass

  # private
  def tokenize(self):
    tokens = []
    current_token = ''

    for char in self.input:
      if self.is_identifier(current_token) and not self.is_identifier(current_token + char):
        tokens.push(current_token)
      elif self.is_whitespace(current_token):
        pass

  def is_identifier(self, token):
    pass

  def is_whitespace(self, token):
    pass

  def remove_comments(self):
    without_inline = re.sub(r'//.*\n', '', self.input)
    without_multiline = re.sub(r'/\*\*.*\*/', '', without_inline)

    return without_multiline
