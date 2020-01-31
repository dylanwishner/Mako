from lexer.token import Token, TokenType as tok_type, reserved_keywords


class Lexer:
    """
    Lexer class for Mako. Reads the source code from the provided file
    and separates the source code into individual tokens.
    """
    source = ""
    tokens = []
    current = 0
    line = 1

    def __init__(self, source):
        self.source = source

    def scan_tokens(self) -> [Token]:
        """
        Return a list of all the token objects found in the file.
        """

        while not self._at_end_of_file():
            self._scan_next()

        self.tokens.append(Token(tok_type.EOF, self.line, 'eof'))
        return self.tokens

    def _scan_next(self):
        """
        Return the next character.
        """
        char = self.source[self.current]

        if char.isspace():
            self.current += 1
        elif char == '+':
            self.tokens.append(Token(tok_type.PLUS, self.line, char))
            self.current += 1
        elif char == '-':
            self.tokens.append(Token(tok_type.MINUS, self.line, char))
            self.current += 1
        elif char == '*':
            self.tokens.append(Token(tok_type.STAR, self.line, char))
            self.current += 1
        elif char == '/':
            self.tokens.append(Token(tok_type.SLASH, self.line, char))
            self.current += 1

        elif char == '(':
            self.tokens.append(Token(tok_type.LEFT_PAREN, self.line, char))
            self.current += 1
        elif char == ')':
            self.tokens.append(Token(tok_type.RIGHT_PAREN, self.line, char))
            self.current += 1
        elif char == '[':
            self.tokens.append(Token(tok_type.LEFT_BRACK, self.line, char))
            self.current += 1
        elif char == ']':
            self.tokens.append(Token(tok_type.RIGHT_BRACK, self.line, char))
            self.current += 1
        elif char == '{':
            self.tokens.append(Token(tok_type.LEFT_CURLY, self.line, char))
            self.current += 1
        elif char == '}':
            self.tokens.append(Token(tok_type.RIGHT_CURLY, self.line, char))
            self.current += 1
        elif char == ';':
            self.tokens.append(Token(tok_type.SEMICOLON, self.line, char))
            self.current += 1
        elif char == ':':
            self.tokens.append(Token(tok_type.COLON, self.line, char))
            self.current += 1
        elif char == '.':
            self.tokens.append(Token(tok_type.PERIOD, self.line, char))
            self.current += 1
        elif char == ',':
            self.tokens.append(Token(tok_type.COMMA, self.line, char))
            self.current += 1

        elif char == '=':
            if self._peek_next_char('='):
                self.tokens.append(Token(tok_type.IS_EQUAL, self.line, '=='))
                self.current += 1
            else:
                self.tokens.append(Token(tok_type.ASSIGN, self.line, char))
                self.current += 1
        elif char == '!':
            if self._peek_next_char('='):
                self.tokens.append(Token(tok_type.NOT_EQUAL, self.line, '!='))
                self.current += 1
            else:
                self.tokens.append(Token(tok_type.NOT, self.line, char))
                self.current += 1
        elif char == '>':
            if self._peek_next_char('='):
                self.tokens.append(Token(tok_type.GREATER_EQUAL, self.line, '>='))
                self.current += 1
            else:
                self.tokens.append(Token(tok_type.GREATER, self.line, char))
                self.current += 1
        elif char == '<':
            if self._peek_next_char('='):
                self.tokens.append(Token(tok_type.LESS_EQUAL, self.line, '<='))
                self.current += 1
            else:
                self.tokens.append(Token(tok_type.LESS, self.line, char))
                self.current += 1

        elif char.isalpha():
            self._add_alpha_token()

        elif char.isdigit():
            self._add_numeric_token()

    def _peek_next_char(self, expected) -> bool:
        """
        Peek the next character without consuming it.
        """
        return self.source[self.current + 1] == expected

    def _peek_at_substring(self, start, end, expected) -> bool:
        """
        Peek at a substring and compare it with the expected expression.
        """
        return self.source[start::end] == expected

    def _at_end_of_file(self) -> bool:
        """
        Ensure we haven't yet hit the end of file.
        """
        return self.current >= len(self.source)

    def _add_string(self):
        return NotImplementedError

    def _add_alpha_token(self):
        """
        Analyze alphabetic tokens.
        """
        keyword = ""

        while not self.source[self.current].isspace():
            keyword += self.source[self.current]
            self.current += 1

        if keyword in reserved_keywords:
            self.tokens.append(Token(tok_type.KEYWORD, self.line, keyword))
        else:
            self.tokens.append(Token(tok_type.IDENT, self.line, keyword))

    def _add_numeric_token(self):
        """
        Analyze a numeric token
        """
        number = ''

        while True:
            if self.source[self.current].isdigit():
                number += self.source[self.current]
                self.current += 1
            else:
                break

        self.tokens.append(Token(tok_type.INTEGER, self.line, int(number)))
