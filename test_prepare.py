import unittest
import prepare

class TestPrepare(unittest.TestCase):
    def test_splits_string_on_space(self):
        self.assertEqual(prepare.split_paragraph('Foo and bar. Baz.'), ['Foo and bar.', 'Baz.'])

if __name__ == '__main__':
    unittest.main()