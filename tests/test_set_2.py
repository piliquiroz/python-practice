
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

        # def test_id(self):
        #     self.assertEqual(m.id("hello"), "hello")
        #     self.assertEqual(m.id(3), 3)

        # def test_add1(self):
        #     self.assertEqual(m.add1(1), 2)
        #     self.assertEqual(m.add1(2), 3)

        # def test_add3(self):
        #     self.assertEqual(m.add3(0), 3)
        #     self.assertEqual(m.add3(1), 4)

        # def test_concat_strings(self):
        #     self.assertEqual(m.concat_strings("foo", "bar"), "foobar")

        # def test_is_negative(self):
        #     self.assertTrue(m.is_negative(-3))
        #     self.assertFalse(m.is_negative(3))

        # def test_count_positive(self):
        #     self.assertEqual(m.count_positive([1, -3, 3, 8, -7]), 3)

        # def test_reverse_tuple(self):
        #     self.assertEqual(m.reverse_tuple((1, 3)), (3, 1))
        #     self.assertEqual(m.reverse_tuple((2, 4)), (4, 2))

        # def test_is_between(self):
        #     self.assertTrue(m.is_between(3, 2, 4))
        #     self.assertFalse(m.is_between(3, 3, 4))
        #     self.assertFalse(m.is_between(3, 2, 3))
        #     self.assertFalse(m.is_between(3, 4, 2))

        # def test_is_ordered(self):
        #     self.assertTrue(m.is_ordered([1, 2, 3]))
        #     self.assertTrue(m.is_ordered([1, 10, 13]))
        #     self.assertFalse(m.is_ordered([2, 1, 3]))

    suite = unittest.TestLoader().loadTestsFromTestCase(TestProblemSolutions)
    unittest.TextTestRunner(verbosity=2).run(suite)
