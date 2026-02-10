import unittest

# import everything from the wordle file
# if the file is named wordle.py:
from p2 import (
    score_guess,
    is_valid_guess,
    choose_secret,

    play_turn,
    WORDS
)


class TestScoreGuess(unittest.TestCase):

    def test_all_correct(self):
        self.assertEqual(score_guess("round", "round"), "YYYYY")
   


class TestIsValidGuess(unittest.TestCase):

    def test_valid_guess(self):
        self.assertTrue(is_valid_guess("grape"))


class TestChooseSecret(unittest.TestCase):

    def test_choose__word(self):
        words = ["trace", "slate", "blame"]
        self.assertIn(choose_secret(words), "trace")


class TestPlayTurn(unittest.TestCase):

    def test_invalid_guess(self):
        self.assertEqual(play_turn("flame", "bat"), "Invalid guess")

  

if __name__ == "__main__":
    unittest.main()


