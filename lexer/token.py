from enum import Enum


class Token:
    """
    Defines the structure of a token object.

    type: token type
    line: the line the token appears on
    name (optional): a name value if the token is a variable, function, or class name
    literal (optional): the literal value of integer, string, or char tokens
    """

    def __init__(self, token_type, line, lexeme):
        self.token_type = token_type
        self.line = line
        self.lexeme = lexeme

    def __str__(self):
        return str(self.lexeme) + ' ' + str(self.token_type).replace('TokenType.', '') + ' ' + str(self.line)


class TokenType(Enum):
    # Mathematical tokens
    PLUS = '+',
    MINUS = '-',
    STAR = '*',
    SLASH = '/',

    # Single char tokens
    LEFT_PAREN = '('
    RIGHT_PAREN = ')'
    LEFT_BRACK = '['
    RIGHT_BRACK = ']'
    LEFT_CURLY = '{'
    RIGHT_CURLY = '}'
    SEMICOLON = ';'
    COLON = ':'
    PERIOD = '.'
    COMMA = ','

    # Comparison tokens
    ASSIGN = '='
    NOT = '!'
    IS_EQUAL = '=='
    NOT_EQUAL = '!='
    GREATER = '>'
    LESS = '<'
    GREATER_EQUAL = '>='
    LESS_EQUAL = '<='

    # Flow tokens
    IF = 'if'
    ELSE = 'else'
    ELSE_IF = 'elif'
    WHILE = 'while'
    EOF = 'eof'

    # Type tokens
    KEYWORD = 'keyword'
    IDENT = 'identifier'
    INTEGER = 'integer'
    STRING = 'string'


reserved_keywords = [
    'if', 'else', 'elif', 'while', 'int', 'string'
]