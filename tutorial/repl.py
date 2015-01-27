"""
Romnomnom Tutorial!

See the README.md file for instructions.
"""
from functools import singledispatch
from collections import namedtuple

import ast


#
# The Romnomnom REPL!
#

def repl():
    """
    Runs a Roman Numeral Read-Eval-Print-Loop.
    """
    while True:
        print(evaluate(input("Roman Numeral: ")))


def evaluate(source):
    """
    The "Eval" step in the REPL. Evaluation happens in two phases:

    * Compile: lex, parse, generate bytecode
    * Interpret: execute bytecode with Python's builtin `eval()`
    """
    return eval(generate(parse(lex(source))))


#
# The Romnomnom Compiler!
#

Numeral = namedtuple("Numeral", "value")
Add = namedtuple("Add", "left right")


def lex(string) -> "tokens":
    """
    Lex the string and output a generator of tokens for `parse()`.
    """
    values = ("I", ...)

    for value in string:
        if value in values:
            yield Numeral(value)


def parse(tokens) -> "tree":
    """
    Parse the tokens and output a tree which represents the meaning of the token stream for `generate()`.
    """
    token, *tokens = tokens
    return Add(token, parse(tokens)) if tokens else token


def generate(tree) -> "bytecode":
    """
    With the help of `translate()` below, generate Python bytecode for the Python's `eval()`.

    https://docs.python.org/3/library/functions.html#compile
    """
    return compile(
        source=ast.fix_missing_locations(ast.Expression(body=translate(tree))),
        filename="<input>",
        mode="eval"
    )


@singledispatch
def translate(node):
    """
    Recursively translate a Romnomnom Abstract Syntax Tree into a Python Abstract Syntax Tree for Python's `compile()`.
    """
    raise NotImplementedError('translate(%r)' % node)


@translate.register(Add)
def _(node):
    return ast.BinOp(
        left=translate(node.left),
        op=ast.Add(),
        right=translate(node.right)
    )


@translate.register(Numeral)
def _(node):
    values = {"I": 1, ...: ...}
    return ast.Num(
        n=values[node.value]
    )


#
# This module may be run as a Python 3 script.
#

if __name__ == "__main__":
    """
    Run this module with

    $ python3 repl.py
    """
    repl()
