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
import itertools

# do this by hand first
class JackTokenizer:
  KEYWORD = ('(class|constructor|function|method|field|static|var|int|char|'
    'boolean|void|true|false|null|this|let|do|if|else|while|return)')
  SYMBOL           = '([{}()[\].,;+\-*/&|<>=~])'
  INTEGER_CONSTANT = '([0-32767])'
  STRING_CONSTANT  = '\"([^\n]*)\"'
  IDENTIFIER       = '([A-Za-z_]\w*)'
  LEXICAL_ELEMENTS = '{}|{}|{}|{}|{}'.format(KEYWORD, SYMBOL, INTEGER_CONSTANT,
    STRING_CONSTANT, IDENTIFIER)

  KEYWORD_REGEX          = re.compile(KEYWORD)
  SYMBOL_REGEX           = re.compile(SYMBOL)
  INTEGER_CONSTANT_REGEX = re.compile(INTEGER_CONSTANT)
  STRING_CONSTANT_REGEX  = re.compile(STRING_CONSTANT)
  IDENTIFIER_REGEX       = re.compile(IDENTIFIER)
  LEXICAL_ELEMENTS_REGEX = re.compile(LEXICAL_ELEMENTS)

  INLINE_COMMENT_REGEX    = re.compile('//.*\n')
  MULTILINE_COMMENT_REGEX = re.compile('/\*.*?\*/', flags=re.S)

  def __init__(self, input_filename):
    self.input        = open(input_filename, 'rU').read()
    self.tokens       = self.tokenize()
    self.next_token   = ''

    print self.tokens
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
    input_without_comments = self.remove_comments()

    matches = self.LEXICAL_ELEMENTS_REGEX.findall(input_without_comments)
    flat_matches = list(itertools.chain(*matches))

    return [match for match in flat_matches if match]

  def remove_comments(self):
    without_multiline = re.sub(self.MULTILINE_COMMENT_REGEX, ' ', self.input)
    without_inline = re.sub(self.INLINE_COMMENT_REGEX, '\n', without_multiline)

    return without_inline
