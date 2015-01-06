"""
The lexer accepts a string of characters (source code) and returns a sequence of tokens, in this case only Numerals.
"""
from collections import namedtuple


class LexException(Exception):
    pass

Numeral = namedtuple('Numeral', 'pos value')


def lex(string) -> [Numeral]:
    """
    >>> list(lex("XLII"))
    [Numeral(pos=0, value='XL'), Numeral(pos=2, value='I'), Numeral(pos=3, value='I')]
    """
    pos = 0
    while string:
        token, string, pos = pop_token(string, pos)
        yield token


def pop_token(string, pos=0):
    """
    >>> pop_token("XLII", 0)
    (Numeral(pos=0, value='XL'), 'II', 2)
    """
    for pattern in ("IV", "IX", "XL", "XC", "CD", "CM", "I", "V", "X", "L", "C", "D", "M"):
        if string.startswith(pattern):
            return Numeral(pos, pattern), string[len(pattern):], pos+len(pattern)

    raise LexException("Invalid: '%s' at index %d" % (string[0], pos))
