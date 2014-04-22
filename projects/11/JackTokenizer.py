#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS11
# FILENAME:....... JackTokenizer.py
# PYTHON VERSION:. 2.7.2
#============================================================

import re
import itertools

class JackTokenizer:
  XML_CONVSERSIONS = {
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;'
  }

  LEXICAL_ELEMENTS_MATCHES = ['KEYWORD', 'SYMBOL', 'INT_CONST', 'STRING_CONST',
    'IDENTIFIER']

  KEYWORD          = ('(class|constructor|function|method|field|static|var|int|'
    'char|boolean|void|true|false|null|this|let|do|if|else|while|return)'
    '(?=[^\w])')
  SYMBOL           = '([{}()[\].,;+\-*/&|<>=~])'
  INT_CONST        = '(\d+)'
  STRING_CONST     = '\"([^\n]*)\"'
  IDENTIFIER       = '([A-Za-z_]\w*)'
  LEXICAL_ELEMENTS = '{}|{}|{}|{}|{}'.format(KEYWORD, SYMBOL, INT_CONST,
    STRING_CONST, IDENTIFIER)

  LEXICAL_ELEMENTS_REGEX = re.compile(LEXICAL_ELEMENTS)

  INLINE_COMMENT_REGEX    = re.compile('//.*\n')
  MULTILINE_COMMENT_REGEX = re.compile('/\*.*?\*/', flags=re.S)

  def __init__(self, input_file, token_file):
    self.input        = input_file.read()
    self.tokens       = self.tokenize()
    self.token_file   = token_file
    self.next_token   = self.tokens.pop(0)
    self.buffer       = ''

    self.token_file.write('<tokens>\n')
    input_file.close()

  def hasMoreTokens(self):
    return not not self.next_token

  def advance(self):
    self.current_token = self.next_token

    if len(self.tokens) is not 0:
      self.next_token = self.tokens.pop(0)
      self.write_xml_token()
    else:
      self.write_xml_token()
      self.token_file.write('</tokens>\n')
      self.token_file.close()
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
  def write_xml_token(self):
    if self.tokenType() is 'KEYWORD':
      self.token_file.write('<keyword> {} </keyword>\n'.format(self.keyWord().lower()))
    elif self.tokenType() is 'SYMBOL':
      symbol = self.symbol()

      if symbol in ['<', '>', '&']:
        symbol = self.XML_CONVSERSIONS[symbol]

      self.token_file.write('<symbol> {} </symbol>\n'.format(symbol))
    elif self.tokenType() is 'IDENTIFIER':
      self.token_file.write('<identifier> {} </identifier>\n'.format(self.identifier()))
    elif self.tokenType() is 'INT_CONST':
      self.token_file.write('<integerConstant> {} </integerConstant>\n'.format(self.intVal()))
    elif self.tokenType() is 'STRING_CONST':
      self.token_file.write('<stringConstant> {} </stringConstant>\n'.format(self.stringVal()))

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
