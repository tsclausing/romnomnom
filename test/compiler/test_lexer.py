import unittest

from romnomnom import lexer


class TestLexerLex(unittest.TestCase):
    """
    Test that lexer.lex(string) returns an iterable of Num tuples with the correct position and value.
    """

    def test_valid_single_token_strings(self):
        for value in ("IV", "IX", "XL", "XC", "CD", "CM", "I", "V", "X", "L", "C", "D", "M"):
            self.assertEqual(
                list(lexer.lex(value)),
                [lexer.Num(0, value)]
            )

    def test_valid_multi_token_strings(self):
        self.assertEqual(
            list(lexer.lex("MDCLXVI")),
            [lexer.Num(0, "M"), lexer.Num(1, "D"), lexer.Num(2, "C"), lexer.Num(3, "L"), lexer.Num(4, "X"), lexer.Num(5, "V"), lexer.Num(6, "I")]
        )
        self.assertEqual(
            list(lexer.lex("CMCDXCXLIXIV")),
            [lexer.Num(0, "CM"), lexer.Num(2, "CD"), lexer.Num(4, "XC"), lexer.Num(6, "XL"), lexer.Num(8, "IX"), lexer.Num(10, "IV")]
        )

    def test_invalid_tokens__tokenize(self):
        for invalid in ("M.DCCC.XLIX", "HAI", "!"):
            self.assertRaises(lexer.SyntaxException, lambda: list(lexer.tokenize(invalid)))

    def test_invalid_tokens__descending_order(self):
        for invalid in ("IM", "IIV"):
            self.assertRaises(lexer.SyntaxException, lambda: list(lexer.enforce_descending_order(lexer.tokenize(invalid))))

    def test_invalid_tokens__no_repeated_pairs(self):
        for invalid in ("IVIV", "IXIX", "XLXL", "XCXC", "CDCD", "CMCM"):
            self.assertRaises(lexer.SyntaxException, lambda: list(lexer.enforce_no_repeated_pairs(lexer.tokenize(invalid))))

    def test_invalid_tokens__frequency(self):
        for invalid in ("DD", "DCD", "LL", "LXL", "VV", "VIV"):
            self.assertRaises(lexer.SyntaxException, lambda: list(lexer.enforce_frequency(lexer.tokenize(invalid))))
