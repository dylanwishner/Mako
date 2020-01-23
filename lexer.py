"""
Lexer class for Mako. Reads the source code from the provided file path
and separates the file string into individual tokens.
"""

class Lexer:
    file_path = ""

    def __init__(self, file_path):
        self.file_path = file_path

    def is_valid_file_path(self) -> bool:
        try:
            open(self.file_path, "r")
        except IOError:


