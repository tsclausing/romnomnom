"""
The lexer accepts a string of characters (source code) and returns a sequence of tokens, in this case only Numerals.
"""
from collections import namedtuple

from romnomnom.exceptions import LexException

Num = namedtuple('Num', 'pos value')


def lex(source) -> [Num]:
    """
    >>> list(lex("XLII"))
    [Num(pos=0, value='XL'), Num(pos=2, value='I'), Num(pos=3, value='I')]
    """
    values = ("IV", "IX", "XL", "XC", "CD", "CM", "I", "V", "X", "L", "C", "D", "M")

    pos = 0
    while pos < len(source):
        value = next((value for value in values if source.startswith(value, pos)), None)
        if value:
            yield Num(pos, value)
            pos += len(value)
        else:
            raise LexException("Lex error: unknown character '%s' at index %d" % (source[pos], pos))
