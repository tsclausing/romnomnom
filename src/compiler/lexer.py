"""
The lexer accepts a string of characters (source code) and returns a sequence of tokens, in this case only Numerals.
"""
from collections import namedtuple

from compiler.exceptions import LexException

Numeral = namedtuple('Numeral', 'pos value')


def lex(source) -> [Numeral]:
    """
    >>> list(lex("XLII"))
    [Numeral(pos=0, value='XL'), Numeral(pos=2, value='I'), Numeral(pos=3, value='I')]
    """
    values = ("IV", "IX", "XL", "XC", "CD", "CM", "I", "V", "X", "L", "C", "D", "M")

    pos = 0
    while pos < len(source):
        value = next((value for value in values if source.startswith(value, pos)), None)
        if value:
            yield Numeral(pos, value)
            pos += len(value)
        else:
            raise LexException("Lex error: unknown character '%s' at index %d" % (source[pos], pos))
