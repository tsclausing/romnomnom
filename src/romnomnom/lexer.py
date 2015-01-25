"""
The lexer accepts a string of characters (source code) and returns a sequence of tokens, in this case only Numerals.

Lexical Analysis: http://en.wikipedia.org/wiki/Lexical_analysis
"""
from collections import namedtuple

from romnomnom.exceptions import SyntaxException

Num = namedtuple('Num', 'pos value')


def lex(source) -> [Num]:
    """
    >>> list(lex("XLII"))
    [Num(pos=0, value='XL'), Num(pos=2, value='I'), Num(pos=3, value='I')]
    """
    tokens = tokenize(source)
    tokens = enforce_descending_order(tokens)
    tokens = enforce_no_repeated_pairs(tokens)
    tokens = enforce_frequency(tokens)
    return tokens


def tokenize(source):
    values = ("IV", "IX", "XL", "XC", "CD", "CM", "I", "V", "X", "L", "C", "D", "M")

    pos = 0
    while pos < len(source):
        value = next((value for value in values if source.startswith(value, pos)), None)
        if value:
            yield Num(pos, value)
            pos += len(value)
        else:
            raise SyntaxException("Unknown character '%s' at index %d" % (source[pos], pos))


def enforce_descending_order(tokens):
    # Rule: Numerals must be arranged in descending order.
    descending_order = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    previous = 0  # ----^^^

    for token in tokens:
        index = descending_order.index(token.value)
        if index < previous:
            raise SyntaxException("Numeral %s not in descending order at index %d" % (token.value, token.pos))
        previous = index
        yield token


def enforce_no_repeated_pairs(tokens):
    # Rule: Subtractive pairs may not repeat.
    subtractive_pairs = ("IV", "IX", "XL", "XC", "CD", "CM")
    value = None

    for token in tokens:
        if token.value in subtractive_pairs:
            if token.value == value:
                raise SyntaxException("Repeated subtractive pair %s at index %d" % (token.value, token.pos))
            value = token.value
        yield token


def enforce_frequency(tokens):
    # Rule: D, L, and V may each only appear once.
    countdown = {
        ("D", "CD"): 1,
        ("L", "XL"): 1,
        ("V", "IV"): 1,
    }

    for token in tokens:
        for values in countdown:
            if token.value in values:
                if countdown[values] == 0:
                    raise SyntaxException("Frequency limit of %r exceeded at index %d" % (values, token.pos))
                countdown[values] -= 1
        yield token

