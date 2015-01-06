"""
The parser accepts a sequence of tokens (from lexer.lex) and returns an abstract syntax tree.
"""
from collections import namedtuple

Add = namedtuple('Add', 'left right')


def parse(tokens):
    return valid(ast(tokens))


def ast(tokens):
    """
    >>> from compiler.lexer import lex
    >>> ast(lex("XLII"))
    Add(left=Numeral(pos=0, value='XL'), right=Add(left=Numeral(pos=2, value='I'), right=Numeral(pos=3, value='I')))
    """
    token, *tokens = tokens
    return Add(token, ast(tokens)) if tokens else token


def valid(tree):
    validate_order(tree)
    validate_denomination(tree)
    validate_frequency(tree)
    return tree


def validate_order(tree):
    # TODO: Numerals must be arranged in descending order of size.
    pass


def validate_denomination(tree):
    # TODO: M, C, and X man not be equalled or exceeded by smaller denominations.
    pass


def validate_frequency(tree):
    # TODO: D, L, and V may each only appear once.
    pass
