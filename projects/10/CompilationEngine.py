#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS10
# FILENAME:....... CompilationEngine.py
# PYTHON VERSION:. 2.7.2
#============================================================

import re

# do this by hand first
class CompilationEngine:
  def __init__(self, output_file, token_file):
    self.output_file  = output_file
    self.token_file   = token_file
    self.indent_count = 0
    self.written      = True

    self.token_file.readline() # skip <tokens> line

  # 'class' className '{' classVarDec* subroutineDec* '}'
  def compileClass(self):
    self.write_open_tag('class')
    self.write_next_token() # 'class'
    self.write_next_token() # className
    self.write_next_token() # '{'

    while self.is_class_var_dec():
      self.compileClassVarDec()
      self.save_token_if_written()

    while self.is_subroutine_dec():
      self.compileSubroutine()
      self.save_token_if_written()

    self.write_next_token() # '}'
    self.write_close_tag('class')

  # ('static' | 'field' ) type varName (',' varName)* ';'
  def compileClassVarDec(self):
    self.write_open_tag('classVarDec')
    self.write_next_token()                   # ('static' | 'field' )
    self.write_next_token()                   # type
    self.write_next_token()                   # varName
    self.compile_multiple(',', 'identifier')  # (',' varName)*
    self.write_next_token()                   # ';'
    self.write_close_tag('classVarDec')

  # subroutineDec: ('constructor' | 'function' | 'method') ('void' | type) subroutineName '(' parameterList ')' subroutineBody
  # subroutineBody: '{' varDec* statements '}'
  def compileSubroutine(self):
    self.write_open_tag('subroutineDec')
    self.write_next_token()    # ('constructor' | 'function' | 'method')
    self.write_next_token()       # ('void' | type)
    self.write_next_token()       # subroutineName
    self.write_next_token()       # '('
    self.compileParameterList()   # parameterList
    self.write_next_token()    # ')'
    self.write_open_tag('subroutineBody')
    self.write_next_token()       # '{'

    self.save_token_if_written()

    while 'var' in self.current_xml_token:
      self.compileVarDec() # varDec*
      self.save_token_if_written()

    self.compileStatements()      # statements
    self.write_next_token()       # '}'
    self.write_close_tag('subroutineBody')
    self.write_close_tag('subroutineDec')

  # ( (type varName) (',' type varName)*)?
  def compileParameterList(self):
    self.write_open_tag('parameterList')

    self.save_token_if_written()

    if ' ) ' not in self.current_xml_token:
      self.write_next_token()  # type
      self.write_next_token()  # varName
      self.save_token_if_written()

    while ' ) ' not in self.current_xml_token:
      self.write_next_token()  # ','
      self.write_next_token()  # type
      self.write_next_token()  # varName
      self.save_token_if_written()

    self.write_close_tag('parameterList')

  # 'var' type varName (',' varName)* ';'
  def compileVarDec(self):
    self.write_open_tag('varDec')
    self.write_next_token()                # 'var'
    self.write_next_token()                   # type
    self.write_next_token()                   # varName
    self.compile_multiple(',', 'identifier')  # (',' varName)*
    self.write_next_token()                # ';'
    self.write_close_tag('varDec')

  # statement*
  # letStatement | ifStatement | whileStatement | doStatement | returnStatement
  def compileStatements(self):
    self.write_open_tag('statements')

    while self.is_statement():
      if 'let' in self.current_xml_token:
        self.compileLet()
      elif ' if ' in self.current_xml_token:
        self.compileIf()
      elif 'while' in self.current_xml_token:
        self.compileWhile()
      elif 'do' in self.current_xml_token:
        self.compileDo()
      elif 'return' in self.current_xml_token:
        self.compileReturn()

      self.save_token_if_written()

    self.write_close_tag('statements')

  # 'do' subroutineCall ';'
  # subroutineCall: subroutineName '(' expressionList ')' | ( className | varName) '.' subroutineName '(' expressionList ')'
  def compileDo(self):
    self.write_open_tag('doStatement')
    self.write_next_token()    # 'do'
    self.write_next_token()       # (subroutineName | className | varName)

    self.save_token_if_written()

    if '.' in self.current_xml_token:
      self.write_next_token()     # '.'
      self.write_next_token()     # subroutineName

    self.write_next_token()       # '('
    self.compileExpressionList()  # expressionList
    self.write_next_token()       # ')'
    self.write_next_token()       # ';'
    self.write_close_tag('doStatement')

  # 'let' varName ('[' expression ']')? '=' expression ';'
  def compileLet(self):
    self.write_open_tag('letStatement')
    self.write_next_token()       # 'let'
    self.write_next_token()       # varName

    self.save_token_if_written()

    if ' [ ' in self.current_xml_token:      # ('[' expression ']')?
      self.write_next_token()     # '['
      self.compileExpression()    # expression
      self.write_next_token()     # ']'

    self.write_next_token()       # '='
    self.compileExpression()      # expression
    self.write_next_token()       # ';'
    self.write_close_tag('letStatement')

  # 'while' '(' expression ')' '{' statements '}'
  def compileWhile(self):
    self.write_open_tag('whileStatement')
    self.write_next_token()     # 'while'
    self.write_next_token()     # '('
    self.compileExpression()    # expression
    self.write_next_token()     # ')'
    self.write_next_token()     # '{'
    self.compileStatements()    # statements
    self.write_next_token()     # '}'
    self.write_close_tag('whileStatement')

  # 'return' expression? ';'
  def compileReturn(self):
    self.write_open_tag('returnStatement')
    self.write_next_token()     # 'return'

    self.save_token_if_written()

    if ' ; ' not in self.current_xml_token:    # expression?
      self.compileExpression()  # expression

    self.write_next_token()     # ';'
    self.write_close_tag('returnStatement')

  # 'if' '(' expression ')' '{' statements '}' ( 'else' '{' statements '}' )?
  def compileIf(self):
    self.write_open_tag('ifStatement')
    self.write_next_token()     # if
    self.write_next_token()     # '('
    self.compileExpression()    # expression
    self.write_next_token()     # ')'
    self.write_next_token()     # '{'
    self.compileStatements()    # statements
    self.write_next_token()     # '}'

    self.save_token_if_written()

    if 'else' in self.current_xml_token: # else?
      self.write_next_token()   # else
      self.write_next_token()   # '{'
      self.compileStatements()  # statements
      self.write_next_token()   # '}'

    self.write_close_tag('ifStatement')

  # term (op term)*
  def compileExpression(self):
    self.write_open_tag('expression')
    self.compileTerm() # term

    while self.is_op():
      self.write_next_token() # op
      self.compileTerm()      # term

    self.write_close_tag('expression')

  # integerConstant | stringConstant | keywordConstant | varName |
  # varName '[' expression ']' | subroutineCall | '(' expression ')' | unaryOp term
  def compileTerm(self):
    self.write_open_tag('term')

    self.save_token_if_written()

    if self.is_unary_op_term():
      self.write_next_token()   # unaryOp
      self.compileTerm()        # term
    elif ' ( ' in self.current_xml_token:
      self.write_next_token()   # '('
      self.compileExpression()  # expression
      self.write_next_token()   # ')'
    else: # first is an identifier
      self.write_next_token() # identifier

      self.save_token_if_written()

      if ' [ ' in self.current_xml_token:
        self.write_next_token() # '['
        self.compileExpression() # expression
        self.write_next_token() # ']'
      elif ' . ' in self.current_xml_token:
        self.write_next_token()       # '.'
        self.write_next_token()       # subroutineName
        self.write_next_token()       # '('
        self.compileExpressionList()  # expressionList
        self.write_next_token()       # ')'
      elif ' ( ' in self.current_xml_token:
        self.write_next_token()       # '('
        self.compileExpressionList()  # expressionList
        self.write_next_token()       # ')'

    self.write_close_tag('term')

  # (expression (',' expression)* )?
  def compileExpressionList(self):
    self.write_open_tag('expressionList')

    self.save_token_if_written()

    if ' ) ' not in self.current_xml_token:
      self.compileExpression()        # expression
      self.save_token_if_written() # for while

    while ' ) ' not in self.current_xml_token:
      self.write_next_token()         # ','
      self.compileExpression()        # expression
      self.save_token_if_written()

    self.write_close_tag('expressionList')

  # private
  def is_class_var_dec(self):
    self.save_token_if_written()

    return 'static' in self.current_xml_token or 'field' in self.current_xml_token

  def is_subroutine_dec(self):
    self.save_token_if_written()

    return 'constructor' in self.current_xml_token or 'function' in self.current_xml_token or 'method' in self.current_xml_token

  def is_statement(self):
    self.save_token_if_written()

    return 'let' in self.current_xml_token or 'if' in self.current_xml_token or 'while' in self.current_xml_token or 'do' in self.current_xml_token or 'return' in self.current_xml_token

  # op: '+'|'-'|'*'|'/'|'&'|'|'|'<'|'>'|'='
  def is_op(self):
    self.save_token_if_written()

    return re.search(r'> (\+|-|\*|/|&amp;|\||&lt;|&gt;|=) <', self.current_xml_token)

  # unaryOp: '-' | '~'
  def is_unary_op_term(self):
    self.save_token_if_written()

    return re.search(r'> (-|~) <', self.current_xml_token)

  def write_next_token(self):
    if self.written:
      self.current_xml_token = self.token_file.readline()
    else:
      self.written = True

    output_line = '{}{}'.format(self.current_indent(), self.current_xml_token)
    self.output_file.write(output_line)

  def save_token_if_written(self):
    if self.written:
      self.current_xml_token = self.token_file.readline()
      self.written = False

  def compile_multiple(self, first_identifier, second_identifier):
    self.save_token_if_written()

    while first_identifier in self.current_xml_token or second_identifier in self.current_xml_token:
      self.write_next_token()
      self.save_token_if_written()

  def write_open_tag(self, tag):
    self.output_file.write('{}<{}>\n'.format(self.current_indent(), tag))
    self.increase_indent()

  def write_close_tag(self, tag):
    self.decrease_indent()
    self.output_file.write('{}</{}>\n'.format(self.current_indent(), tag))

  def increase_indent(self):
    self.indent_count += 1

  def decrease_indent(self):
    self.indent_count -= 1

  def current_indent(self):
    return '  ' * self.indent_count
