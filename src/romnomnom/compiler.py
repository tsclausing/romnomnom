"""
The compiler composes each phase in a single compile() function.
"""
from romnomnom.lexer import lex
from romnomnom.parser import parse
from romnomnom.translator import translate


def compile(source: str):
    """
    >>> eval(compile("XLII"))
    42
    """
    return translate(parse(lex(source)))
