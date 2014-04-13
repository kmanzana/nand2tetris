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
  def __init__(self, input_filename, output_filename):
    pass

  # 'class' className '{' classVarDec* subroutineDec* '}'
  def compileClass(self):
    pass

  # ('static' | 'field' ) type varName (',' varName)* ';'
  def compileClassVarDec(self):
    pass

  # subroutineDec: ('static' | 'field' ) type varName (',' varName)* ';'
  # subroutineBody: '{' varDec* statements '}'
  def compileSubroutine(self):
    pass

  # ( (type varName) (',' type varName)*)?
  def compileParameterList(self):
    pass

  # 'var' type varName (',' varName)* ';'
  def compileVarDec(self):
    pass

  # use first token to determine statement type
  # statement*
  # letStatement | ifStatement | whileStatement | doStatement | returnStatement
  def compileStatements(self):
    pass

  # 'do' subroutineCall ';'
  def compileDo(self):
    pass

  # 'let' varName ('[' expression ']')? '=' expression ';'
  def compileLet(self):
    pass

  # 'while' '(' expression ')' '{' statements '}'
  def compileWhile(self):
    pass

  # 'return' expression? ';'
  def compileReturn(self):
    pass

  # 'if' '(' expression ')' '{' statements '}' ( 'else' '{' statements '}' )?
  def compileIf(self):
    pass

  # term (op term)*
  def compileExpression(self):
    pass

  # integerConstant | stringConstant | keywordConstant | varName |
  # varName '[' expression ']' | subroutineCall | '(' expression ')' | unaryOp term
  def compileTerm(self):
    pass

  # (expression (',' expression)* )?
  def compileExpressionList(self):
    pass

  # private
  # 'int' | 'char' | 'boolean' | className
  def compileType(self):
    pass

  # subroutineCall: subroutineName '(' expressionList ')' | ( className | varName) '.' subroutineName
  # '(' expressionList ')'

  # op: '+'|'-'|'*'|'/'|'&'|'|'|'<'|'>'|'='

  # unaryOp: '-' | '~'

  # KeywordConstant: 'true' | 'false' | 'null' | 'this'
