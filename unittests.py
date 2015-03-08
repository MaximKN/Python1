import unittest

from openmath import *


class TestSequenceFunctions(unittest.TestCase):
    def test_int(self):
        a = 42
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_list(self):
        a = [1, 2, 3]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_list_of_list(self):
        a = [1, 2, [3, 4, 5]]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_string(self):
        a = "This is a string"
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_float(self):
        a = [0, 1., 0.5, -1.]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_bool(self):
        a = False
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_fraction(self):
        a = [1, Fraction(1, 2)]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_complex(self):
        a = complex(Fraction(1, 2), 5)
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_dict(self):
        a = {'a': 10, 2: 'blue', 'b': 20}
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)


if __name__ == '__main__':
    unittest.main()
