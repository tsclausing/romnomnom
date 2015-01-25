"""
The parser accepts a sequence of tokens (from lexer.lex) and returns a RomanNumeral abstract syntax tree.

Parsing: http://en.wikipedia.org/wiki/Parsing
"""
from collections import namedtuple

from romnomnom.exceptions import ParseException

RomanNumeral = namedtuple('RomanNumeral', 'expression')
Add = namedtuple('Add', 'left right')


def parse(tokens):
    """
    >>> from romnomnom.lexer import lex
    >>> parse(lex("XLII"))
    RomanNumeral(expression=Add(left=Num(pos=0, value='XL'), right=Add(left=Num(pos=2, value='I'), right=Num(pos=3, value='I'))))
    """
    tree = ast(tokens)
    tree = enforce_denomination(tree)
    return RomanNumeral(tree)


def ast(tokens):
    token, *tokens = tokens
    return Add(token, ast(tokens)) if tokens else token



def enforce_denomination(tree):
    # Rule: M, C, and X may not be equalled or exceeded by smaller denominations.
    values = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    levels = [10, 100, 1000]

    def flatten(node):
        nums = []
        while isinstance(node, Add):
            nums.append(node.left)
            node = node.right
        nums.append(node)
        return nums

    total = 0
    for num in reversed(flatten(tree)):
        value = values[num.value]
        while levels and value >= levels[0]:
            del levels[0]
        total += value
        if levels and total >= levels[0]:
            raise ParseException("Parse error: smaller denominations exceed %s at index %d" % (next(k for k in values if values[k] == levels[0]), num.pos))

    return tree
