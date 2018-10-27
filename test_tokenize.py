import unittest
import markov_tokenize as tokenize

class TestTokenize(unittest.TestCase):
    def test_splits_string_on_space(self):
        self.assertEqual(tokenize.split('foo bar'), ['foo', 'bar'])

    def test_makes_punctuation_its_own_token(self):
        self.assertEqual(tokenize.split('foo.'), ['foo', '.'])

if __name__ == '__main__':
    unittest.main()