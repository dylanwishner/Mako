"""
Defines the structure of a token object.
"""

import enum


class Token:
    """
    type: token type
    line: the line the token appears on
    name (optional): a name value if the token is a variable, function, or class name
    literal (optional): the literal value of integer, string, or char tokens
    """

    def __init__(self, token_type, line, name=None, literal=None):
        self.token_type = token_type
        self.line = line
        self.name = name
        self.literal = literal


class TokenType(enum):
    # Mathematical tokens
    PLUS = '+'
    MINUS = '-'
    STAR = '*'
    SLASH = '/'

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
    EQUALS = '='
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
    ELSE_IF = 'else if'
    WHILE = 'while'
    EOF = 'eof'

    # Type tokens
    STRING = 'string'
    INT = 'int'
    CHAR = 'char'
