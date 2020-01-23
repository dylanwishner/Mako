"""
Main class for the compiler. Gathers the input, validates arguments,
and does other checks before executing.
"""

from sys import argv, exit
from lexer import Lexer


class Mako:
    def __init__(self):
        if self._validate_args():
            self.report_error("Usage: mako <file>")
            exit(64)
        else:
            file_path = argv[1]
            if self._validate_file_path(file_path):
                file = open(file_path, "r")

    """
    Validate that the correct number of arguments were provided. (2): program + file_path
    """
    def _validate_args(self) -> bool:
        if len(argv) == 2:
            return True
        else:
            return False

    """
    Validate that the file exists at the file path provided
    """
    def _validate_file_path(self, file_path) -> bool:
        try:
            _file = open(file_path, "r")
            _file.close()
            return True
        except IOError:
            self.report_error("File not found at \'%s\'" % file_path)
            return False

    def _run_file(self, file_path):
        lexer = Lexer()

    """
    Report an error from anywhere in the compiling stage
    """
    @classmethod
    def report_error(cls, message, line):
        if line is not None:
            print("ERR << LINE %d << %s" % line, message)
        else:
            print("ERR << %s" % message)


if __name__ == "__main__":
    Mako()
