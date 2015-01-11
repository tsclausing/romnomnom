"""
Translates a parsed Romnomnom AST into a Python executable code object.
"""
import ast
from functools import singledispatch

from romnomnom.parser import RomanNumeral
from romnomnom.parser import Add
from romnomnom.lexer import Num


def translate(tree):
    """
    >>> from romnomnom.lexer import lex
    >>> from romnomnom.parser import parse
    >>> eval(translate(parse(lex("XLII"))))
    42
    """
    return compile(
        source=ast.Expression(body=generate(tree)),
        filename="Romnomnom",
        mode="eval",
    )


@singledispatch
def generate(node):
    """
    Recursively transform a Romnomnom AST node into a Python AST node.
    """
    raise NotImplementedError('Python AST Generation Error: generate(%r)' % node)


@generate.register(RomanNumeral)
def _(node):
    return generate(node.expression)


@generate.register(Add)
def _(node):
    return ast.BinOp(
        lineno=1,
        col_offset=node.left.pos,
        left=generate(node.left),
        op=ast.Add(),
        right=generate(node.right),
    )


@generate.register(Num)
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
