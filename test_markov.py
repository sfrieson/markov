import unittest
import index as markov

class TestMarkov(unittest.TestCase):

    def test_generate_returns_string(self):
        self.assertIsInstance(markov.generate({'_START_': ['hi'], 'hi': ['_END_']}), str)
        self.assertEqual(markov.generate({'_START_': ['hi'], 'hi': ['_END_']}), 'Hi')

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

    def test_join_chain_capitalizes_the_first_letter(self):
        self.assertEqual(
            markov.join_chain(['hi']),
            'Hi'
        )

    def test_join_chain_attaches_commas(self):
        self.assertEqual(
            markov.join_chain(['mine', ',', 'and']),
            'Mine, and'
        )

    def test_join_chain_attaches_quotes_directionally(self):
        # These cases will not be fixed until there is a better token system for contextual punctuation
        # self.assertEqual(
        #     markov.join_chain(['saying', '"', 'thanks', '"', 'is', 'in', 'order', '.']),
        #     'Saying "thanks" is in order.'
        # )
        # self.assertEqual(
        #     markov.join_chain(['"', 'please', 'and', 'thank', 'you', '"']),
        #     '"Please and thank you"'
        # )
        self.assertEqual(
            markov.join_chain(['mine', ',', 'and']),
            'Mine, and'
        )