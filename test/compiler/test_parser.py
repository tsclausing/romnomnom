import unittest

from romnomnom import lexer
from romnomnom import parser
from romnomnom import exceptions


class TestParserParse(unittest.TestCase):
    """
    Test that parser.lex(tokens) returns an AST of tuples with the correct nodes.
    """

    def test_valid_individual_tokens(self):
        for value in ("IV", "IX", "XL", "XC", "CD", "CM", "I", "V", "X", "L", "C", "D", "M"):
            self.assertEqual(
                parser.parse(lexer.lex(value)),
                parser.RomanNumeral(lexer.Num(0, value))
            )

    def test_valid_tokens(self):
        self.assertEqual(
            parser.parse(lexer.lex("MDCLXVI")),  # 1666
            parser.RomanNumeral(parser.Add(lexer.Num(0, "M"), parser.Add(lexer.Num(1, "D"), parser.Add(lexer.Num(2, "C"), parser.Add(lexer.Num(3, "L"), parser.Add(lexer.Num(4, "X"), parser.Add(lexer.Num(5, "V"), lexer.Num(6, "I"))))))))
        )
        self.assertEqual(
            parser.parse(lexer.lex("CMXCIX")),  # 999
            parser.RomanNumeral(parser.Add(lexer.Num(0, "CM"), parser.Add(lexer.Num(2, "XC"), lexer.Num(4, "IX"))))
        )
        self.assertEqual(
            parser.parse(lexer.lex("CDXLIV")),  # 444
            parser.RomanNumeral(parser.Add(lexer.Num(0, "CD"), parser.Add(lexer.Num(2, "XL"), lexer.Num(4, "IV"))))
        )

    def test_invalid_tree__denomination(self):
        for invalid in ("IXI", "XCX", "CMC", "VIIIII", "IIIIIIIIII", "DCCCCC", "CCCCCCCCCC"):
            self.assertRaises(exceptions.SyntaxException, lambda: list(parser.enforce_denomination(parser.ast(lexer.lex(invalid)))))
