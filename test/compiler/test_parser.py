import unittest

from romnomnom import lexer
from romnomnom import parser


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

    def test_invalid_tokens__descending_order(self):
        for invalid in ("IM", "IIV"):
            self.assertRaises(parser.ParseException, lambda: list(parser.enforce_descending_order(lexer.lex(invalid))))

    def test_invalid_tokens__no_repeated_pairs(self):
        for invalid in ("IVIV", "IXIX", "XLXL", "XCXC", "CDCD", "CMCM"):
            self.assertRaises(parser.ParseException, lambda: list(parser.enforce_no_repeated_pairs(lexer.lex(invalid))))

    def test_invalid_tokens__frequency(self):
        for invalid in ("DD", "DCD", "LL", "LXL", "VV", "VIV"):
            self.assertRaises(parser.ParseException, lambda: list(parser.enforce_frequency(lexer.lex(invalid))))

    def test_invalid_tree__denomination(self):
        for invalid in ("IXI", "XCX", "CMC", "VIIIII", "IIIIIIIIII", "DCCCCC", "CCCCCCCCCC"):
            self.assertRaises(parser.ParseException, lambda: list(parser.enforce_denomination(parser.ast(lexer.lex(invalid)))))
