# Ignore this for now, this is how we import libraries
import unittest

def run(m):

    class TestProblemSolutions(unittest.TestCase):

        def test_is_name(self):
            self.assertTrue(m.is_name('Pili Quiroz'))
            self.assertTrue(m.is_name('David Janssen'))
            self.assertTrue(m.is_name('Cheesecake Factory'))
            self.assertFalse(m.is_name('Pili1 Quiroz'))
            self.assertFalse(m.is_name('Pili quiroz'))
            self.assertFalse(m.is_name('Piliquiroz'))
            self.assertFalse(m.is_name('Pili Andrea Quiroz'))

        def test_reverse_list(self):
            self.assertEqual(m.reverse_list([1, 2, 3]), [3, 2, 1])
            self.assertEqual(m.reverse_list('banana'), list('ananab'))

        def test_is_palindrome(self):
            self.assertTrue(m.is_palindrome('Bob'))
            self.assertFalse(m.is_palindrome('palindrome'))

        def test_count_palindromes(self):
            self.assertEqual(m.count_palindromes([]), 0)
            self.assertEqual(m.count_palindromes(['Abba', 'bob', 'tree']), 2)



    suite = unittest.TestLoader().loadTestsFromTestCase(TestProblemSolutions)
    unittest.TextTestRunner(verbosity=2).run(suite)
