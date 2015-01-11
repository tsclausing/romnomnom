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
            list(lexer.lex("IVIXXLXCCDCM")),
            [lexer.Num(0, "IV"), lexer.Num(2, "IX"), lexer.Num(4, "XL"), lexer.Num(6, "XC"), lexer.Num(8, "CD"), lexer.Num(10, "CM")]
        )

    def test_invalid_strings(self):
        for invalid in ("M.DCCC.XLIX", "HAI", "!"):
            self.assertRaises(lexer.LexException, lambda: list(lexer.lex(invalid)))
