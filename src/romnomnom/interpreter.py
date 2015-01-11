"""
The interpreter returns the evaluated result of compiling source code.

Interpreter: http://en.wikipedia.org/wiki/Interpreter_(computing)
"""
from romnomnom.compiler import compile


def evaluate(source: str):
    """
    >>> evaluate("XLII")
    42
    """
    return eval(compile(source)) if source else None
