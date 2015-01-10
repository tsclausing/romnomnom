"""
The parser accepts a sequence of tokens (from lexer.lex) and returns an abstract syntax tree.
"""
from collections import namedtuple

from compiler.exceptions import ParseException

Add = namedtuple('Add', 'left right')


def parse(tokens):
    tokens = enforce_descending_order(tokens)
    tokens = enforce_no_repeated_pairs(tokens)
    tokens = enforce_frequency(tokens)
    tree = ast(tokens)
    tree = enforce_denomination(tree)
    return tree


def ast(tokens):
    """
    >>> from compiler.lexer import lex
    >>> ast(lex("XLII"))
    Add(left=Numeral(pos=0, value='XL'), right=Add(left=Numeral(pos=2, value='I'), right=Numeral(pos=3, value='I')))
    """
    token, *tokens = tokens
    return Add(token, ast(tokens)) if tokens else token


def enforce_descending_order(tokens):
    # Numerals must be arranged in descending order.
    descending_order = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    previous = 0  # ----^^^

    for token in tokens:
        index = descending_order.index(token.value)
        if index < previous:
            raise ParseException("Parse error: value %s not in descending order at index %d" % (token.value, token.pos))
        previous = index
        yield token


def enforce_no_repeated_pairs(tokens):
    # Subtractive pairs may not repeat.
    subtractive_pairs = ("IV", "IX", "XL", "XC", "CD", "CM")
    value = None

    for token in tokens:
        if token.value in subtractive_pairs:
            if token.value == value:
                raise ParseException("Parse error: repeated subtractive pair %s at index %d" % (token.value, token.pos))
            value = token.value
        yield token


def enforce_frequency(tokens):
    # D, L, and V may each only appear once.
    countdown = {
        ("D", "CD"): 1,
        ("L", "XL"): 1,
        ("V", "IV"): 1,
    }

    for token in tokens:
        for values in countdown:
            if token.value in values:
                if countdown[values] == 0:
                    raise ParseException("Parse error: frequency limit of %r exceeded at index %d" % (values, token.pos))
                countdown[values] -= 1
        yield token


def enforce_denomination(tree):
    # TODO: M, C, and X man not be equalled or exceeded by smaller denominations.
    return tree
