import unittest

from compiler import lexer


class TestLexerLex(unittest.TestCase):
    """
    Test that lexer.lex(string) returns an iterable of Numeral tuples with the correct position and value.
    """

    def test_valid_tokens(self):
        for value in ("IV", "IX", "XL", "XC", "CD", "CM", "I", "V", "X", "L", "C", "D", "M"):
            self.assertEqual(
                list(lexer.lex(value)),
                [lexer.Numeral(0, value)]
            )

    def test_valid_string(self):
        self.assertEqual(
            list(lexer.lex("MDCLXVI")),
            [lexer.Numeral(0, "M"), lexer.Numeral(1, "D"), lexer.Numeral(2, "C"), lexer.Numeral(3, "L"), lexer.Numeral(4, "X"), lexer.Numeral(5, "V"), lexer.Numeral(6, "I")]
        )
        self.assertEqual(
            list(lexer.lex("IVIXXLXCCDCM")),
            [lexer.Numeral(0, "IV"), lexer.Numeral(2, "IX"), lexer.Numeral(4, "XL"), lexer.Numeral(6, "XC"), lexer.Numeral(8, "CD"), lexer.Numeral(10, "CM")]
        )

    def test_invalid_token(self):
        self.assertRaises(lexer.LexException, lambda: list(lexer.lex('!')))
