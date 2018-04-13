
import unittest

def run(m):

    class TestProblemSolutions(unittest.TestCase):

        def test_capitalize(self):
            self.assertEqual(m.capitalize("david"), "DAVID")
            self.assertEqual(m.capitalize("PiLi"), "PILI")

        def test_is_odd(self):
            self.assertTrue(m.is_odd(3))
            self.assertFalse(m.is_odd(4))

        def test_filter_even(self):
            self.assertEqual(m.filter_even([1, 2, 3, 4, 5]), [2, 4])
            self.assertEqual(m.filter_even([0, 2, 4, 1, 3, 5]), [0, 2, 4])

        def test_my_all(self):
            self.assertTrue(m.my_all([True, True]))
            self.assertTrue(m.my_all([]))
            self.assertFalse(m.my_all([True, False]))

        def test_my_any(self):
            self.assertTrue(m.my_any([True, True]))
            self.assertFalse(m.my_any([]))
            self.assertFalse(m.my_any([False, False]))

        def test_my_capitalize(self):
            self.assertEqual(m.my_capitalize("david"), "DAVID")
            self.assertEqual(m.my_capitalize("PiLi"), "PILI")

        def test_make_dict(self):
            self.assertEqual(m.make_dict(1, 2, 3), {'name': 1, 'age': 2, 'hobby': 3})

        def test_filter_strings(self):
            self.assertEqual(m.filter_strings(["david", 3, True, "pili"]), ["david", "pili"])

        def test_describe_dog(self):
            self.assertEqual(m.describe_dog('beertje'), 'dead')
            self.assertEqual(m.describe_dog('BrunO'), 'brown')
            self.assertEqual(m.describe_dog('Pluto'), 'no such dog')

    suite = unittest.TestLoader().loadTestsFromTestCase(TestProblemSolutions)
    unittest.TextTestRunner(verbosity=2).run(suite)
