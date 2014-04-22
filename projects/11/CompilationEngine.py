#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ ECS11
# FILENAME:....... CompilationEngine.py
# PYTHON VERSION:. 2.7.2
#============================================================

# TODO: implement vm code for different things by hand first
# TODO: peek method look further ahead
import re
from SymbolTable import SymbolTable

class CompilationEngine:
  CONVERT_KIND = {
    'ARG': 'ARG',
    'STATIC': 'STATIC',
    'VAR': 'LOCAL',
    'FIELD': 'THIS'
  }

  ARITHMETIC = {
    '+': 'ADD',
    '-': 'SUB',
    '=': 'EQ',
    '>': 'GT',
    '<': 'LT',
    '&': 'AND',
    '|': 'OR'
  }

  ARITHMETIC_UNARY = {
    '-': 'NEG',
    '~': 'NOT'
  }

  def __init__(self, vm_writer, tokenizer):
    self.vm_writer    = vm_writer
    self.tokenizer    = tokenizer
    self.symbol_table = SymbolTable()
    self.buffer       = []

  # 'class' className '{' classVarDec* subroutineDec* '}'
  def compileClass(self):
    self.get_token() # 'class'
    self.class_name = self.get_token() # className
    self.get_token() # '{'

    while self.is_class_var_dec():
      self.compileClassVarDec() # classVarDec*

    while self.is_subroutine_dec():
      self.compileSubroutine() # subroutineDec*

    self.vm_writer.close()

  # ('static' | 'field' ) type varName (',' varName)* ';'
  def compileClassVarDec(self):
    pass
    # self.write_open_tag('classVarDec')
    # self.write_next_token()                   # ('static' | 'field' )
    # self.write_next_token()                   # type
    # self.write_next_token()                   # varName
    # self.compile_multiple(',', 'identifier')  # (',' varName)*
    # self.write_next_token()                   # ';'
    # self.write_close_tag('classVarDec')

  # subroutineDec: ('constructor' | 'function' | 'method') ('void' | type) subroutineName '(' parameterList ')' subroutineBody
  # subroutineBody: '{' varDec* statements '}'
  def compileSubroutine(self):
    # for constructor call memory.alloc
    subroutine_kind = self.get_token() # ('constructor' | 'function' | 'method')
    self.get_token()                    # ('void' | type)
    subroutine_name = self.get_token()  # subroutineName
    self.symbol_table.startSubroutine()

    self.get_token() # '('
    self.compileParameterList()   # parameterList
    self.get_token() # ')'
    self.get_token() # '{'

    while 'var' == self.peek():
      self.compileVarDec() # varDec*

    function_name = '{}.{}'.format(self.class_name, subroutine_name)
    num_locals = self.symbol_table.varCount('VAR')
    self.vm_writer.writeFunction(function_name, num_locals)

    self.compileStatements() # statements
    self.get_token() # '}'

  # ( (type varName) (',' type varName)*)?
  def compileParameterList(self):
    if ')' != self.peek():
      type = self.get_token() # type
      name = self.get_token() # varName

      self.symbol_table.define(name, type, 'ARG')

    while ')' != self.peek():
      self.get_token() # ','

      type = self.get_token() # type
      name = self.get_token() # varName

      self.symbol_table.define(name, type, 'ARG')

    # self.write_open_tag('parameterList')

    # if ' ) ' not in self.current_token():
    #   self.write_next_token()  # type
    #   self.write_next_token()  # varName

    # while ' ) ' not in self.current_token():
    #   self.write_next_token()  # ','
    #   self.write_next_token()  # type
    #   self.write_next_token()  # varName

    # self.write_close_tag('parameterList')

  # 'var' type varName (',' varName)* ';'
  def compileVarDec(self):
    self.get_token() # 'var'
    type = self.get_token() # type
    name = self.get_token() # varName

    self.symbol_table.define(name, type, 'VAR')

    while self.peek() != ';': # (',' varName)*
      self.get_token() # ','
      name = self.get_token() # varName
      self.symbol_table.define(name, type, 'VAR')

    self.get_token() # ';'

  # statement*
  # letStatement | ifStatement | whileStatement | doStatement | returnStatement
  def compileStatements(self):
    while self.is_statement():
      token = self.get_token()

      if 'let' == token:
        self.compileLet()
      elif ' if ' == token:
        self.compileIf()
      elif 'while' == token:
        self.compileWhile()
      elif 'do' == token:
        self.compileDo()
      elif 'return' == token:
        self.compileReturn()

  # 'do' subroutineCall ';'
  # subroutineCall: subroutineName '(' expressionList ')' | ( className | varName) '.' subroutineName '(' expressionList ')'
  def compileDo(self):
    function_name = self.get_token() # (subroutineName | className | varName)

    token = self.get_token()

    if '.' == token:
      function_name += '.' + self.get_token() # '.' subroutineName

    self.get_token() # '('
    number_args = self.compileExpressionList()
    self.get_token() # ')'
    self.get_token() # ';'

    self.vm_writer.writeCall(function_name, number_args)
    self.vm_writer.writePop('TEMP', 0)

  # 'let' varName ('[' expression ']')? '=' expression ';'
  def compileLet(self):
    var_name = self.get_token() # varName
    var_kind  = self.CONVERT_KIND[self.symbol_table.kindOf(var_name)]
    var_index = self.symbol_table.indexOf(var_name)

    if '[' == self.peek(): # array assignment
      self.vm_writer.writePush(var_kind, var_index)

      self.get_token() # '['
      self.compileExpression() # expression
      self.get_token() # ']'

      self.vm_writer.writeArithmetic('ADD')
      self.vm_writer.writePop('TEMP', 0)

      self.get_token() # '='
      self.compileExpression()      # expression
      self.get_token() # ';'

      self.vm_writer.writePush('TEMP', 0)
      self.vm_writer.writePop('POINTER', 1)
      self.vm_writer.writePop('THAT', 0)
    else: # regular assignment
      self.get_token() # '='
      self.compileExpression()      # expression
      self.get_token() # ';'

      self.vm_writer.writePop(var_kind, var_index)

    # self.write_open_tag('letStatement')
    # self.write_next_token()       # 'let'
    # self.write_next_token()       # varName

    # if ' [ ' in self.current_token():      # ('[' expression ']')?
    #   self.write_next_token()     # '['
    #   self.compileExpression()    # expression
    #   self.write_next_token()     # ']'

    # self.write_next_token()       # '='
    # self.compileExpression()      # expression
    # self.write_next_token()       # ';'
    # self.write_close_tag('letStatement')

  # 'while' '(' expression ')' '{' statements '}'
  def compileWhile(self):
    pass
    # self.write_open_tag('whileStatement')
    # self.write_next_token()     # 'while'
    # self.write_next_token()     # '('
    # self.compileExpression()    # expression
    # self.write_next_token()     # ')'
    # self.write_next_token()     # '{'
    # self.compileStatements()    # statements
    # self.write_next_token()     # '}'
    # self.write_close_tag('whileStatement')

  # 'return' expression? ';'
  def compileReturn(self):
    # if expression:
    # self.compileExpression()
    # else:
    self.vm_writer.writePush('CONST', 0)

    self.vm_writer.writeReturn()

    self.get_token() # ';'

    # self.write_open_tag('returnStatement')
    # self.write_next_token()     # 'return'

    # if ' ; ' not in self.current_token():    # expression?
    #   self.compileExpression()  # expression

    # self.write_next_token()     # ';'
    # self.write_close_tag('returnStatement')

  # 'if' '(' expression ')' '{' statements '}' ( 'else' '{' statements '}' )?
  def compileIf(self):
    pass
    # self.write_open_tag('ifStatement')
    # self.write_next_token()     # if
    # self.write_next_token()     # '('
    # self.compileExpression()    # expression
    # self.write_next_token()     # ')'
    # self.write_next_token()     # '{'
    # self.compileStatements()    # statements
    # self.write_next_token()     # '}'

    # if 'else' in self.current_token(): # else?
    #   self.write_next_token()   # else
    #   self.write_next_token()   # '{'
    #   self.compileStatements()  # statements
    #   self.write_next_token()   # '}'

    # self.write_close_tag('ifStatement')

  # term (op term)*
  def compileExpression(self):
    self.compileTerm() # term

    while self.is_op(): # (op term)*
      op = self.get_token() # op
      self.compileTerm() # term

      if op in self.ARITHMETIC.keys():
        self.vm_writer.writeArithmetic(self.ARITHMETIC[op])
      elif op == '*':
        self.vm_writer.writeCall('Math.multiply', 2)
      elif op == '/':
        self.vm_writer.writeCall('Math.divide', 2)

  # integerConstant | stringConstant | keywordConstant | varName |
  # varName '[' expression ']' | subroutineCall | '(' expression ')' | unaryOp term
  def compileTerm(self):
    if self.is_unary_op_term():
      unary_op = self.get_token()          # unaryOp
      self.compileTerm()        # term
      self.vm_writer.writeArithmetic(self.ARITHMETIC_UNARY[unary_op])
    elif '(' == self.peek():
      self.get_token()          # '('
      self.compileExpression()  # expression
      self.get_token()          # ')'
    elif self.is_number():    # integerConstant
      self.vm_writer.writePush('CONST', self.get_token())
    elif self.is_string():    # stringConstant
      self.vm_writer.write('STRING CONST not implemented')
    elif self.is_keyword_constant():   # keywordConstant
      self.compile_keyword()
    else: # first is a var or subroutine
      identifier = self.get_token() # identifier

      if '[' == self.peek():
        self.get_token()          # '['
        self.compileExpression()  # expression
        self.get_token()          # ']'
      elif '.' == self.peek():
        self.get_token()              # '.'
        subroutine_name = self.get_token() # subroutineName
        self.get_token()              # '('
        number_args = self.compileExpressionList()  # expressionList
        self.get_token()              # ')'

        function_name = '{}.{}'.format(identifier, subroutine_name)
        self.vm_writer.writeCall(function_name, number_args)
      elif '(' == self.peek():
        self.get_token()              # '('
        self.compileExpressionList()  # expressionList
        self.get_token()              # ')'
      else:
        var_kind  = self.CONVERT_KIND[self.symbol_table.kindOf(identifier)]
        var_index = self.symbol_table.indexOf(identifier)
        self.vm_writer.writePush(var_kind, var_index)

  # (expression (',' expression)* )?
  def compileExpressionList(self):
    number_args = 0

    if ')' != self.peek():
      number_args += 1
      self.compileExpression()

    while ')' != self.peek():
      number_args += 1
      self.get_token() # ','
      self.compileExpression()

    return number_args

  # private
  def compile_keyword(self):
    self.vm_writer.writePush('CONST', 0)

    if self.peek() == 'true':
      self.vm_writer.writeArithmetic('NEG')

  def is_class_var_dec(self):
    return False
    # return 'static' in self.current_token() or 'field' in self.current_token()

  def is_subroutine_dec(self):
    return self.peek() in ['constructor', 'function', 'method']

  def is_statement(self):
    return self.peek() in ['let', 'if', 'while', 'do', 'return']

  # op: '+'|'-'|'*'|'/'|'&'|'|'|'<'|'>'|'='
  def is_op(self):
    return self.peek() in ['+', '-', '*', '/', '&', '|', '<', '>', '=']

  # unaryOp: '-' | '~'
  def is_unary_op_term(self):
    return self.peek() in ['~', '-']

  def is_number(self):
    return unicode(self.peek()).isnumeric()

  def is_string(self):
    return self.peek() == '"'

  def is_keyword_constant(self):
    return self.peek() in ['true', 'false', 'null']

  # TODO: peek method look further ahead
  def peek(self):
    token = self.get_token()
    self.unget_token(token)
    return token

  def get_token(self):
    if self.buffer:
      return self.buffer.pop(0)
    else:
      return self.get_next_token()

  def unget_token(self, token):
    self.buffer.append(token)

  def get_next_token(self):
    if self.tokenizer.hasMoreTokens():
      self.tokenizer.advance()

      if self.tokenizer.tokenType() is 'KEYWORD':
        return self.tokenizer.keyWord().lower()
      elif self.tokenizer.tokenType() is 'SYMBOL':
        return self.tokenizer.symbol()
      elif self.tokenizer.tokenType() is 'IDENTIFIER':
        return self.tokenizer.identifier()
      elif self.tokenizer.tokenType() is 'INT_CONST':
        return self.tokenizer.intVal()
      elif self.tokenizer.tokenType() is 'STRING_CONST':
        return self.tokenizer.stringVal()
