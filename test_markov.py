import unittest
import index as markov

class TestMarkov(unittest.TestCase):

    def test_generate_returns_string(self):
        self.assertIsInstance(markov.generate({'_START_': ['hi'], 'hi': ['_END_']}), str)
        self.assertEqual(markov.generate({'_START_': ['hi'], 'hi': ['_END_']}), 'hi')

    def test_make_pairs(self):
        self.assertEqual(
            markov.make_pairs(['foo', 'bar', 'baz', '.'], {}),
            {
                '_START_': ['foo'],
                'foo': ['bar'],
                'bar': ['baz'],
                'baz': ['.'],
                '.': ['_END_']
            }
        )
    
    def test_select_element(self):
        choices = ['foo', 'bar', 'baz']
        self.assertIn(markov.select_element(choices), choices)