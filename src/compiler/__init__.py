"""
The compiler, which implements the "read" step of the REPL.

Import each of the compiler phases and compose them in a single function, read().
"""
from compiler.lexer import lex
from compiler.parser import parse
from compiler.translator import translate


def read(source: str):
    """
    >>> eval(read("XLII"))
    42
    """
    return translate(parse(lex(source)))
