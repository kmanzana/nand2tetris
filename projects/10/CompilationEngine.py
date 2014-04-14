#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS10
# FILENAME:....... CompilationEngine.py
# PYTHON VERSION:. 2.7.2
#============================================================

# do this by hand first
class CompilationEngine:
  # classVarDec =  'static|field' 'int' | 'char' | 'boolean' | identifier) identifier (',' identifier)* ';'

  def __init__(self, output_file, token_file):
    self.output_file    = output_file
    self.token_file     = token_file
    self.current_indent = 0

    self.save_token() # skip <tokens> line

  # 'class' className '{' classVarDec* subroutineDec* '}'
  def compileClass(self):
    self.output_file.write('<class>\n')
    self.write_next_token() # 'class'
    self.write_next_token() # className
    self.write_next_token() # '{'

    self.save_token()

    while self.is_class_var_dec():
      self.compileClassVarDec()
      self.save_token()

    while self.is_subroutine_dec():
      self.compileSubroutine()
      self.save_token()

    self.write_current_token() # '}'

    self.output_file.write('</class>\n')

  # ('static' | 'field' ) type varName (',' varName)* ';'
  def compileClassVarDec(self):
    self.output_file.write(self.current_xml_token)  # ('static' | 'field' )
    self.write_next_token()                         # type
    self.write_next_token()                         # varName
    self.compile_multiple(',', 'identifier')        # (',' varName)*
    self.write_current_token()                      # ';'

  # subroutineDec: ('constructor' | 'function' | 'method') ('void' | type) subroutineName '(' parameterList ')' subroutineBody
  # subroutineBody: '{' varDec* statements '}'
  def compileSubroutine(self):
    self.output_file.write('<subroutineDec>\n')
    self.write_current_token()    # ('constructor' | 'function' | 'method')
    self.write_next_token()       # ('void' | type)
    self.write_next_token()       # subroutineName
    self.write_next_token()       # '('
    self.compileParameterList()   # parameterList
    self.write_next_token()       # ')'
    self.output_file.write('<subroutineBody>\n')
    self.write_next_token()       # '{'

    self.save_token()

    while 'var' in self.current_xml_token:
      self.compileVarDec() # varDec*
      self.save_token()

    self.compileStatements()      # statements
    self.write_current_token()    # '}'
    self.output_file.write('</subroutineBody>\n')
    self.output_file.write('</subroutineDec>\n')

  # ( (type varName) (',' type varName)*)?
  def compileParameterList(self):
    self.output_file.write('<parameterList>\n')
    self.output_file.write('</parameterList>\n')

  # 'var' type varName (',' varName)* ';'
  def compileVarDec(self):
    self.output_file.write('<varDec>\n')
    self.write_current_token()                # 'var'
    self.write_next_token()                   # type
    self.write_next_token()                   # varName
    self.compile_multiple(',', 'identifier')  # (',' varName)*
    self.write_current_token()                # ';'
    self.output_file.write('</varDec>\n')

  # statement*
  # letStatement | ifStatement | whileStatement | doStatement | returnStatement
  def compileStatements(self):
    self.output_file.write('<statements>\n')

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

      self.save_token()

    self.output_file.write('</statements>\n')

  # 'do' subroutineCall ';'
  # subroutineCall: subroutineName '(' expressionList ')' | ( className | varName) '.' subroutineName '(' expressionList ')'
  def compileDo(self):
    self.output_file.write('<doStatement>\n')
    self.write_current_token() # 'do'
    self.write_next_token() # (subroutineName | className | varName)

    self.save_token()

    if '.' in self.current_xml_token:
      self.write_current_token() # '.'
      self.write_next_token() # subroutineName

    self.write_next_token() # '('
    self.compileExpressionList() # expressionList
    self.write_next_token() # ')'
    self.write_next_token() # ';'
    self.output_file.write('</doStatement>\n')

  # 'let' varName ('[' expression ']')? '=' expression ';'
  def compileLet(self):
    self.output_file.write('<letStatement>\n')
    self.write_current_token()  # 'let'
    self.write_next_token()     # varName

    if self.is_expression():    # ('[' expression ']')?
      self.write_next_token()   # '['
      self.compileExpression()  # expression
      self.write_next_token()   # ']'

    self.write_next_token()     # '='
    self.compileExpression()    # expression
    self.write_next_token()     # ';'
    self.output_file.write('</letStatement>\n')

  # 'while' '(' expression ')' '{' statements '}'
  def compileWhile(self):
    self.output_file.write('<whileStatement>\n')
    self.output_file.write('</whileStatement>\n')

  # 'return' expression? ';'
  def compileReturn(self):
    self.output_file.write('<returnStatement>\n')
    self.write_current_token()  # 'return'

    if self.is_expression():    # expression?
      self.compileExpression()  # expression

    self.write_next_token()     # ';'
    self.output_file.write('</returnStatement>\n')

  # 'if' '(' expression ')' '{' statements '}' ( 'else' '{' statements '}' )?
  def compileIf(self):
    self.output_file.write('<ifStatement>\n')
    self.output_file.write('</ifStatement>\n')

  # term (op term)*
  def compileExpression(self):
    self.output_file.write('<expression>\n')
    self.compileTerm() # term
    self.output_file.write('</expression>\n')
    pass

  # integerConstant | stringConstant | keywordConstant | varName |
  # varName '[' expression ']' | subroutineCall | '(' expression ')' | unaryOp term
  def compileTerm(self):
    self.output_file.write('<term>\n')
    self.write_next_token() # term
    self.output_file.write('</term>\n')

  # (expression (',' expression)* )?
  def compileExpressionList(self):
    self.output_file.write('<expressionList>\n')
    self.output_file.write('</expressionList>\n')

  # 'int' | 'char' | 'boolean' | className

  # subroutineCall: subroutineName '(' expressionList ')' | ( className | varName) '.' subroutineName
  # '(' expressionList ')'

  # op: '+'|'-'|'*'|'/'|'&'|'|'|'<'|'>'|'='

  # unaryOp: '-' | '~'

  # KeywordConstant: 'true' | 'false' | 'null' | 'this'

  # private
  def is_class_var_dec(self):
    return 'static' in self.current_xml_token or 'field' in self.current_xml_token

  def is_subroutine_dec(self):
    return 'constructor' in self.current_xml_token or 'function' in self.current_xml_token or 'method' in self.current_xml_token

  def is_statement(self):
    return 'let' in self.current_xml_token or 'if' in self.current_xml_token or 'while' in self.current_xml_token or 'do' in self.current_xml_token or 'return' in self.current_xml_token

  # TODO: implement expressions
  def is_expression(self):
    return False

  def write_next_token(self):
    self.output_file.write(self.token_file.readline())

  def write_current_token(self):
    self.output_file.write(self.current_xml_token)

  def save_token(self):
    self.current_xml_token = self.token_file.readline()

  def compile_multiple(self, first_identifier, second_identifier):
    self.save_token()

    while first_identifier in self.current_xml_token or second_identifier in self.current_xml_token:
      self.write_current_token()
      self.save_token()

  def increase_indent(self):
    pass

  def decrease_indent(self):
    pass
