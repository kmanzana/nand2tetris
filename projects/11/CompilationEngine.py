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

  if_index    = -1
  while_index = -1

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
    kind = self.get_token() # ('static' | 'field' )
    type = self.get_token() # type
    name = self.get_token() # varName

    self.symbol_table.define(name, type, kind.upper())

    while self.peek() != ';': # (',' varName)*
      self.get_token() # ','
      name = self.get_token() # varName
      self.symbol_table.define(name, type, kind.upper())

    self.get_token() # ';'

  # subroutineDec: ('constructor' | 'function' | 'method') ('void' | type) subroutineName '(' parameterList ')' subroutineBody
  # subroutineBody: '{' varDec* statements '}'
  def compileSubroutine(self):
    subroutine_kind = self.get_token() # ('constructor' | 'function' | 'method')
    self.get_token()                    # ('void' | type)
    subroutine_name = self.get_token()  # subroutineName
    self.symbol_table.startSubroutine()

    # if subroutine_kind == 'method':
    #   self.symbol_table.define('instance', self.class_name, 'ARG')

    self.get_token() # '('
    self.compileParameterList()   # parameterList
    self.get_token() # ')'
    self.get_token() # '{'

    while 'var' == self.peek():
      self.compileVarDec() # varDec*

    function_name = '{}.{}'.format(self.class_name, subroutine_name)
    num_locals = self.symbol_table.varCount('VAR')
    self.vm_writer.writeFunction(function_name, num_locals)

    if subroutine_kind == 'constructor':
      num_fields = self.symbol_table.varCount('FIELD')
      self.vm_writer.writePush('CONST', num_fields)
      self.vm_writer.writeCall('Memory.alloc', 1)
      self.vm_writer.writePop('POINTER', 0)
    elif subroutine_kind == 'method':
      self.vm_writer.writePush('ARG', 0)
      self.vm_writer.writePop('POINTER', 0)

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
      elif 'if' == token:
        self.compileIf()
      elif 'while' == token:
        self.compileWhile()
      elif 'do' == token:
        self.compileDo()
      elif 'return' == token:
        self.compileReturn()

  # 'do' subroutineCall ';'
  def compileDo(self):
    self.compile_subroutine_call()
    self.vm_writer.writePop('TEMP', 0)
    self.get_token() # ';'

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

  # 'while' '(' expression ')' '{' statements '}'
  def compileWhile(self):
    self.while_index += 1
    while_index = self.while_index

    self.vm_writer.writeLabel('WHILE{}\n'.format(while_index))

    self.get_token() # '('
    self.compileExpression() # expression
    self.vm_writer.writeArithmetic('NOT') # eval false condition first
    self.get_token() # ')'
    self.get_token() # '{'

    self.vm_writer.writeIf('WHILE_END{}\n'.format(while_index))
    self.compileStatements() # statements
    self.vm_writer.writeGoto('WHILE{}\n'.format(while_index))
    self.vm_writer.writeLabel('WHILE_END{}\n'.format(while_index))

    self.get_token() # '}'

  # 'return' expression? ';'
  def compileReturn(self):
    if self.peek() != ';':
      self.compileExpression()
    else:
      self.vm_writer.writePush('CONST', 0)

    self.vm_writer.writeReturn()
    self.get_token() # ';'

  # 'if' '(' expression ')' '{' statements '}' ( 'else' '{' statements '}' )?
  def compileIf(self):
    self.if_index += 1
    if_index = self.if_index

    self.get_token()     # '('
    self.compileExpression()    # expression
    self.get_token()     # ')'

    self.get_token() # '{'

    self.vm_writer.writeIf('IF_TRUE{}\n'.format(if_index))
    self.vm_writer.writeGoto('IF_FALSE{}\n'.format(if_index))
    self.vm_writer.writeLabel('IF_TRUE{}\n'.format(if_index))
    self.compileStatements() # statements
    self.vm_writer.writeGoto('IF_END{}\n'.format(if_index))

    self.get_token() # '}'

    self.vm_writer.writeLabel('IF_FALSE{}\n'.format(if_index))

    if self.peek() == 'else': # ( 'else' '{' statements '}' )?
      self.get_token() # 'else'
      self.get_token() # '{'
      self.compileStatements() # statements
      self.get_token() # '}'

    self.vm_writer.writeLabel('IF_END{}\n'.format(if_index))

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
    elif self.peek_type() == 'INT_CONST':    # integerConstant
      self.vm_writer.writePush('CONST', self.get_token())
    elif self.peek_type() == 'STRING_CONST':    # stringConstant
      self.vm_writer.write('STRING CONST not implemented')
    elif self.peek_type() == 'KEYWORD':   # keywordConstant
      self.compile_keyword()
    else: # first is a var or subroutine
      if self.is_array():
        self.get_token()          # '['
        self.compileExpression()  # expression
        self.get_token()          # ']'
      elif self.is_subroutine_call():
        self.compile_subroutine_call()
      else:
        var = self.get_token()
        var_kind  = self.CONVERT_KIND[self.symbol_table.kindOf(var)]
        var_index = self.symbol_table.indexOf(var)
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
    keyword = self.get_token() # keywordConstant

    if keyword == 'this':
      self.vm_writer.writePush('POINTER', 0)
    else:
      self.vm_writer.writePush('CONST', 0)

      if keyword == 'true':
        self.vm_writer.writeArithmetic('NOT')

  # subroutineCall: subroutineName '(' expressionList ')' | ( className | varName) '.' subroutineName '(' expressionList ')'
  def compile_subroutine_call(self):
    identifier = self.get_token() # (subroutineName | className | varName)
    function_name = identifier
    number_args = 0

    if '.' == self.peek():
      self.get_token()                    # '.'
      subroutine_name = self.get_token()  # subroutineName

      type = self.symbol_table.typeOf(identifier)

      if type != 'NONE': # it's an instance
        instance_kind = self.symbol_table.kindOf(identifier)
        instance_index = self.symbol_table.indexOf(identifier)

        self.vm_writer.writePush(self.CONVERT_KIND[instance_kind], instance_index)

        function_name = '{}.{}'.format(type, subroutine_name)
        number_args += 1
      else: # it's a class
        class_name = identifier
        function_name = '{}.{}'.format(class_name, subroutine_name)
    elif '(' == self.peek():
      subroutine_name = identifier
      function_name = '{}.{}'.format(self.class_name, subroutine_name)
      number_args += 1

      self.vm_writer.writePush('POINTER', 0)

    self.get_token()              # '('
    number_args += self.compileExpressionList()  # expressionList
    self.get_token()              # ')'

    self.vm_writer.writeCall(function_name, number_args)

  def is_subroutine_call(self):
    token = self.get_token()
    subroutine_call = self.peek() in ['.', '(']
    self.unget_token(token)
    self.peek() # reset buffer
    return subroutine_call

  def is_array(self):
    token = self.get_token()
    array = self.peek() == '['
    self.unget_token(token)
    self.peek() # reset buffer
    return array

  def is_class_var_dec(self):
    return self.peek() in ['static', 'field']

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

  # TODO: peek method look further ahead
  def peek(self):
    return self.peek_info()[0]

  def peek_type(self):
    return self.peek_info()[1]

  def peek_info(self):
    token_info = self.get_token_info()
    self.unget_token_info(token_info)
    return token_info

  def get_token(self):
    return self.get_token_info()[0]

  def get_token_info(self):
    if self.buffer:
      return self.buffer.pop(0)
    else:
      return self.get_next_token()

  def unget_token(self, token):
    self.unget_token_info((token, 'UNKNOWN'))

  def unget_token_info(self, token):
    self.buffer.append(token)

  def get_next_token(self):
    if self.tokenizer.hasMoreTokens():
      self.tokenizer.advance()

      if self.tokenizer.tokenType() is 'KEYWORD':
        return (self.tokenizer.keyWord().lower(), self.tokenizer.tokenType())
      elif self.tokenizer.tokenType() is 'SYMBOL':
        return (self.tokenizer.symbol(), self.tokenizer.tokenType())
      elif self.tokenizer.tokenType() is 'IDENTIFIER':
        return (self.tokenizer.identifier(), self.tokenizer.tokenType())
      elif self.tokenizer.tokenType() is 'INT_CONST':
        return (self.tokenizer.intVal(), self.tokenizer.tokenType())
      elif self.tokenizer.tokenType() is 'STRING_CONST':
        return (self.tokenizer.stringVal(), self.tokenizer.tokenType())
