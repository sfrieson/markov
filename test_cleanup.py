import unittest
import cleanup

class TestCleanUpStiring(unittest.TestCase):

    def test_remove_extra_spaces(self):
        self.assertEqual(cleanup.clean('This is foo.  This is bar.'), 'This is foo. This is bar.')
    
    def test_replace_ellipses(self):
        self.assertEqual(cleanup.clean('Where is baz...'), 'Where is baz…')

if __name__ == '__main__':
    unittest.main()