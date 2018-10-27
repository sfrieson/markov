import unittest
import index as markov

class TestMarkov(unittest.TestCase):

    def test_generate_returns_string(self):
        self.assertIsInstance(markov.generate(), str)