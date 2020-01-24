"""
Lexer class for Mako. Reads the source code from the provided file
and separates the source code into individual tokens.
"""

from token import Token, TokenType as type


class Lexer:
    source = ""
    tokens = []
    start = 0
    current = 0
    line = 1

    def __init__(self, source):
        self.source = source

    """
    Return a list of all the token objects found in the file.
    """

    def scan_tokens(self) -> [Token]:
        while not self._at_end_of_file():
            self.start = self.current
            self._scan_next()

        self.tokens.append(Token(type.EOF, self.line))
        return self.tokens

    """
    Return the next character.
    """

    def _scan_next(self):
        char = self._consume_char()
        if char == '+':
            self.tokens.append(Token(type.PLUS, self.line))
        elif char == '-':
            self.tokens.append(Token(type.MINUS, self.line))
        elif char == '*':
            self.tokens.append(Token(type.STAR, self.line))
        elif char == '/':
            self.tokens.append(Token(type.SLASH, self.line))

        elif char == '(':
            self.tokens.append(Token(type.LEFT_PAREN, self.line))
        elif char == ')':
            self.tokens.append(Token(type.RIGHT_PAREN, self.line))
        elif char == '[':
            self.tokens.append(Token(type.LEFT_BRACK, self.line))
        elif char == ']':
            self.tokens.append(Token(type.RIGHT_BRACK, self.line))
        elif char == '{':
            self.tokens.append(Token(type.LEFT_CURLY, self.line))
        elif char == '}':
            self.tokens.append(Token(type.RIGHT_CURLY, self.line))
        elif char == ';':
            self.tokens.append(Token(type.SEMICOLON, self.line))
        elif char == ':':
            self.tokens.append(Token(type.COLON, self.line))
        elif char == '.':
            self.tokens.append(Token(type.PERIOD, self.line))
        elif char == ',':
            self.tokens.append(Token(type.COMMA, self.line))

        elif char == '=':
            if self._peek_next_char('='):
                self.tokens.append(Token(type.IS_EQUAL, self.line))
            else:
                self.tokens.append(Token(type.EQUALS, self.line))
        elif char == '!':
            if self._peek_next_char('='):
                self.tokens.append(Token(type.NOT_EQUAL, self.line))
            else:
                self.tokens.append(Token(type.NOT, self.line))
        elif char == '>':
            if self._peek_next_char('='):
                self.tokens.append(Token(type.GREATER_EQUAL, self.line))
            else:
                self.tokens.append(Token(type.GREATER, self.line))
        elif char == '<':
            if self._peek_next_char('='):
                self.tokens.append(Token(type.LESS_EQUAL, self.line))
            else:
                self.tokens.append(Token(type.LESS, self.line))

        elif char.isalpha():
            if char == 'e':
                if self._peek_at_substring(self.current, self.current + 4, 'else'):
                    if self._peek_at_substring(self.current, self.current + 7, 'else if'):
                        self.tokens.append(Token(type.ELSE_IF, self.line))
                    else:
                        self.tokens.append(Token(type.ELSE, self.line))
            if char == 'i':
                if self._peek_next_char('f'):
                    self.tokens.append(Token(type.IF, self.line))
            if char == 'w':
                if self._peek_at_substring(self.current, self.current + 5, 'while'):
                    self.tokens.append(Token(type.WHILE, self.line))

        elif char.isdigit():
            value = ""
            index = self.current

            while self.source[index].isdigit():
                value += self.source[index]
                index += 1

        elif char == '"':
            value = ""
            index = self.current

            while self.source[index] != '"':
                value += self.source[index]
                index += 1

    """
    Read, consume, and return the char at the current position.
    """

    def _consume_char(self) -> str:
        self.current += 1
        return self.source[self.current - 1]

    """
    Peek the next character without consuming it.
    """

    def _peek_next_char(self, expected) -> bool:
        return self.source[self.current + 1] == expected

    """
    Peek at a substring and compare it with the expected expression.
    """

    def _peek_at_substring(self, start, end, expected) -> bool:
        return self.source[start::end] == expected

    """
    Ensure we haven't yet hit the end of file
    """

    def _at_end_of_file(self) -> bool:
        return self.current >= len(self.source)
