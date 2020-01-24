from token import Token, TokenType as type


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

        self.tokens.append(Token(type.EOF, self.line))
        return self.tokens

    def _scan_next(self):
        """
        Return the next character.
        """
        char = self._consume_char()
        if char.isspace():
            self.current += 1
        elif char == '+':
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
            self._add_string()


    def _consume_char(self) -> str:
        """
        Read, consume, and return the char at the current position.
        """
        self.current += 1
        return self.source[self.current - 1]

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
        return self.current >= len(self.source) - 1

    def _add_string(self):
        print("adding")
        index = self.current
        var_name = ""
        literal = ""

        while not self.source[index].isspace():
            var_name += self.source[index]
            index += 1

        index += 1
        while self.source[index] != '"':
            index += 1

        index += 1
        while self.source[index] != '"':
            literal += self.source[index]
            index += 1

        self.tokens.append(Token(type.STRING, self.line, var_name, literal))
        self.current = index
