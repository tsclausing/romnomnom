import ast
import types
import unittest

from romnomnom.parser import RomanNumeral
from romnomnom.parser import Add
from romnomnom.lexer import Num
from romnomnom import generator


class TestGeneratorGenerate(unittest.TestCase):

    def test_generate(self):
        expression = generator.generate(RomanNumeral(Num(0, "I")))
        self.assertIsInstance(expression, types.CodeType)

    def test_generate_eval(self):
        result = eval(generator.generate(RomanNumeral(Num(0, "I"))))
        self.assertEquals(1, result)


class TestGeneratorTranslate(unittest.TestCase):

    def test_translate_roman_numeral_num(self):
        node = generator.translate(RomanNumeral(Num(0, "I")))
        self.assertIsInstance(node, ast.Num)

    def test_translate_roman_numeral_add(self):
        node = generator.translate(RomanNumeral(Add(Num(0, "I"), Num(1, "I"))))
        self.assertIsInstance(node, ast.BinOp)

    def test_translate_num(self):
        node = generator.translate(Num(0, "I"))
        self.assertIsInstance(node, ast.Num)

    def test_translate_add(self):
        node = generator.translate(Add(Num(0, "I"), Num(1, "I")))
        self.assertIsInstance(node, ast.BinOp)
