
import unittest

def run(m):

    class TestProblemSolutions(unittest.TestCase):

        def test_write_number(self):
            ae = self.assertEqual
            ae(m.write_number(13132), "thirteen thousand one hundred thirty-two")
            ae(m.write_number(19), "nineteen")
            ae(m.write_number(21234567890987),
               "twenty-one trillion two hundred thirty-four billion five hundred " +
               "sixety-seven million eight hundred ninety thousand nine hundred eighty-seven ")
            ae(m.write_number(1000001), "one million one")

        def test_overlapping_keys(self):
            self.assertEqual(m.overlapping_keys({'a': 1, 'b': 2}, {'a': 4, 'c': 3}),  {'a'})
            self.assertEqual(m.overlapping_keys({'b': 2}, {'a': 'apples', 'c': True}), {})

        def test_raise_value_error(self):
            with self.assertRaises(ValueError):
                m.raise_value_error()

        def test_join_dicts(self):
            ae = self.assertEqual
            ae(m.join_dicts(), {})
            ae(m.join_dicts({'a': 1}), {'a': 1})
            ae(m.join_dicts({'a': 1, 'b': 2}, {'c': 3}), {'a': 1, 'b':2, 'c':3})
            ae(m.join_dicts({'a': 1}, {'b': 2}, {'c': 3}), {'a': 1, 'b':2, 'c':3})
            with self.assertRaises(ValueError):
               m.join_dicts({'a': 1}, {'a': 2})

        def test_unique_letters(self):
            self.assertEqual(m.unique_letters("abcdefg"), True)
            self.assertEqual(m.unique_letters("aa"), False)
            self.assertEqual(m.unique_letters("12345 !@#$%^"), True)
            self.assertEqual(m.unique_letters("this no wrk"), False)

        def test_import_dame_cinco(self):
            self.assertEqual(m.import_dame_cinco()(), 5)

        def test_read_foo(self):
            self.assertEqual(m.read_foo(), "This is the contents of foo.txt\n")




    suite = unittest.TestLoader().loadTestsFromTestCase(TestProblemSolutions)
    unittest.TextTestRunner(verbosity=2).run(suite)
