"""
The REPL, or read eval print loop.
"""
from compiler import read

from compiler.lexer import LexException
from compiler.parser import ParseException


if __name__ == "__main__":
    while True:
        try:
            source = input('> ').strip()
            if source:
                # read, eval, print
                print(eval(read(source)))
                # loop ...
        except (LexException, ParseException) as e:
            print(e)
        except KeyboardInterrupt:
            exit(0)
