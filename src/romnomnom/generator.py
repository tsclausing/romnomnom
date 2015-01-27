"""
Translates a parsed Romnomnom AST into a Python executable code object.

Code Generation: http://en.wikipedia.org/wiki/Code_generation_(compiler)
"""
import ast
from functools import singledispatch

from romnomnom.parser import RomanNumeral
from romnomnom.parser import Add
from romnomnom.lexer import Num


def generate(tree):
    """
    >>> from romnomnom.lexer import lex
    >>> from romnomnom.parser import parse
    >>> eval(generate(parse(lex("XLII"))))
    42
    """
    return compile(
        source=ast.Expression(body=translate(tree)),
        filename="Romnomnom",
        mode="eval",
    )


@singledispatch
def translate(node):
    """
    Recursively transform a Romnomnom AST node into a Python AST node.
    """
    raise NotImplementedError('Python AST Generation Error: translate(%r)' % node)


@translate.register(RomanNumeral)
def _(node):
    return translate(node.expression)


@translate.register(Add)
def _(node):
    return ast.BinOp(
        lineno=1,
        col_offset=node.left.pos,
        left=translate(node.left),
        op=ast.Add(),
        right=translate(node.right),
    )


@translate.register(Num)
def _(node):
    values = {
        "M": 1000,
        "CM": 900,
        "D":  500,
        "CD": 400,
        "C":  100,
        "XC":  90,
        "L":   50,
        "XL":  40,
        "X":   10,
        "IX":   9,
        "V":    5,
        "IV":   4,
        "I":    1,
    }
    return ast.Num(
        lineno=1,
        col_offset=node.pos,
        n=values[node.value]
    )
