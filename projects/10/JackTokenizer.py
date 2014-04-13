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
  LEXICAL_ELEMENTS_MATCHES = ['KEYWORD', 'SYMBOL', 'INT_CONST', 'STRING_CONST',
    'IDENTIFIER']

  KEYWORD          = ('(class|constructor|function|method|field|static|var|int|'
    'char|boolean|void|true|false|null|this|let|do|if|else|while|return)')
  SYMBOL           = '([{}()[\].,;+\-*/&|<>=~])'
  INT_CONST        = '(\d+)'
  STRING_CONST     = '\"([^\n]*)\"'
  IDENTIFIER       = '([A-Za-z_]\w*)'
  LEXICAL_ELEMENTS = '{}|{}|{}|{}|{}'.format(KEYWORD, SYMBOL, INT_CONST,
    STRING_CONST, IDENTIFIER)

  LEXICAL_ELEMENTS_REGEX = re.compile(LEXICAL_ELEMENTS)

  INLINE_COMMENT_REGEX    = re.compile('//.*\n')
  MULTILINE_COMMENT_REGEX = re.compile('/\*.*?\*/', flags=re.S)

  def __init__(self, input_filename):
    file = open(input_filename, 'rU')

    self.input        = file.read()
    self.tokens       = self.tokenize()
    self.next_token   = ''

    self.advance()
    file.close()

  def hasMoreTokens(self):
    return not not self.next_token

  def advance(self):
    self.current_token = self.next_token

    if len(self.tokens) is not 0:
      self.next_token = self.tokens.pop(0)
    else:
      self.next_token = False

  def tokenType(self):
    return self.current_token[1]

  def keyWord(self):
    return self.current_token[0].upper()

  def symbol(self):
    return self.current_token[0]

  def identifier(self):
    return self.current_token[0]

  def intVal(self):
    return self.current_token[0]

  def stringVal(self):
    return self.current_token[0]

  # private
  def tokenize(self):
    input_without_comments = self.remove_comments()

    matches = self.LEXICAL_ELEMENTS_REGEX.findall(input_without_comments)

    match_types = map(lambda element_matches: self.LEXICAL_ELEMENTS_MATCHES[next(index for index, element in enumerate(element_matches) if element)], matches)

    flat_matches = list(itertools.chain(*matches))

    tokens = [match for match in flat_matches if match]

    return zip(tokens, match_types)

  def remove_comments(self):
    without_multiline = re.sub(self.MULTILINE_COMMENT_REGEX, ' ', self.input)
    without_inline = re.sub(self.INLINE_COMMENT_REGEX, '\n', without_multiline)

    return without_inline
