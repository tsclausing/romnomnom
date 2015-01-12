"""
The parser accepts a sequence of tokens (from lexer.lex) and returns a RomanNumeral abstract syntax tree.

Parsing: http://en.wikipedia.org/wiki/Parsing
"""
import sys
from collections import namedtuple

from romnomnom.exceptions import ParseException
from romnomnom.lexer import Num

RomanNumeral = namedtuple('RomanNumeral', 'expression')
Add = namedtuple('Add', 'left right')


def parse(tokens):
    """
    >>> from romnomnom.lexer import lex
    >>> parse(lex("XLII"))
    RomanNumeral(expression=Add(left=Num(pos=0, value='XL'), right=Add(left=Num(pos=2, value='I'), right=Num(pos=3, value='I'))))
    """
    tokens = enforce_descending_order(tokens)
    tokens = enforce_no_repeated_pairs(tokens)
    tokens = enforce_frequency(tokens)
    tree = ast(tokens)
    tree = enforce_denomination(tree)
    return RomanNumeral(tree)


def ast(tokens):
    token, *tokens = tokens
    return Add(token, ast(tokens)) if tokens else token


def enforce_descending_order(tokens):
    # Rule: Numerals must be arranged in descending order.
    descending_order = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    previous = 0  # ----^^^

    for token in tokens:
        index = descending_order.index(token.value)
        if index < previous:
            raise ParseException("Parse error: value %s not in descending order at index %d" % (token.value, token.pos))
        previous = index
        yield token


def enforce_no_repeated_pairs(tokens):
    # Rule: Subtractive pairs may not repeat.
    subtractive_pairs = ("IV", "IX", "XL", "XC", "CD", "CM")
    value = None

    for token in tokens:
        if token.value in subtractive_pairs:
            if token.value == value:
                raise ParseException("Parse error: repeated subtractive pair %s at index %d" % (token.value, token.pos))
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
                    raise ParseException("Parse error: frequency limit of %r exceeded at index %d" % (values, token.pos))
                countdown[values] -= 1
        yield token


def enforce_denomination(tree):
    # Rule: M, C, and X may not be equalled or exceeded by smaller denominations.
    values = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    denominations = [("X", 10), ("C", 100), ("M", 1000), ("_", sys.maxsize)]

    def num(node):
        return values[node.value] if isinstance(node, Num) else add(node)

    def add(node):
        left, right = num(node.left), num(node.right) if isinstance(node.right, Num) else add(node.right)
        total, denomination = left + right, denominations[0][1]
        if total >= denomination:
            if left >= denomination:
                while denominations and denominations[0][1] <= total:
                    del denominations[0]
            elif left < denomination:
                raise ParseException('Parse error: smaller denominations exceed %s at index %d' % (denominations[0][0], node.left.pos))
        return total

    num(tree)
    return tree
