import unittest

from openmath import *

class TestIntegers(unittest.TestCase):
    def test_int(self):
        a = -50
        b = ParseOMstring(OMstring(a))
        self.assertEqual(a, b)

    def test_int_file(self):
        self.assertEquals(ParseOMfile('tst/integer.xml'), 42)

    def test_int_type(self):
        a = '<OMOBJ> <OMI>42</OMI></OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), int)

suite = unittest.TestLoader().loadTestsFromTestCase(TestIntegers)
unittest.TextTestRunner(verbosity=2).run(suite)

class TestStrings(unittest.TestCase):
    def test_string(self):
        a = "This is a string"
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_string_file(self):
        self.assertEquals(ParseOMfile('tst/string.xml'), 'This is a string')

    def test_string_type(self):
        a = '<OMOBJ> <OMSTR>This is a string</OMSTR> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), str)

suite1 = unittest.TestLoader().loadTestsFromTestCase(TestStrings)
unittest.TextTestRunner(verbosity=2).run(suite1)

class TestFloats(unittest.TestCase):
    def test_float(self):
        a = [0, 1., 0.5, -1.]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_float_file(self):
        self.assertEquals(ParseOMfile('tst/float.xml'), [0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08])

    def test_float_type(self):
        a = '<OMOBJ> <OMF dec="-5.1315811823070673e-08"/> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), float)

suite2 = unittest.TestLoader().loadTestsFromTestCase(TestFloats)
unittest.TextTestRunner(verbosity=2).run(suite2)

class TestBooleans(unittest.TestCase):
    def test_bool_False(self):
        a = False
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_bool_True(self):
        a = True
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_bool_File(self):
        self.assertEquals(ParseOMfile('tst/bool.xml'), False)

    def test_bool_type(self):
        a = '<OMOBJ> <OMS cd="logic1" name="false"/> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), bool)

suite3 = unittest.TestLoader().loadTestsFromTestCase(TestBooleans)
unittest.TextTestRunner(verbosity=2).run(suite3)

class TestLists(unittest.TestCase):
    def test_list(self):
        a = [1, 2, 3, 4, 5]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_listdifftypes(self):
        a = [True, 2, 'helloworld', -43.6]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_list_file(self):
        self.assertEquals(ParseOMfile('tst/list.xml'), [41, True, 43])

    def test_list_type(self):
        a = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), list)

    def test_list_of_list(self):
        a = [1, 2, [3, 4, 5]]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_list_of_list_difftypes(self):
        a = [False, 45, ['he', 'll', 'o'], [0.5, -1., 19487171., 5.131581182], 67, 'string']
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_listcomplex(self):
        a = [True, 2, 'helloworld', -43.6, [1, Fraction(1, 2)], complex(Fraction(1, 2), 5), [[2, 3], ['a', 'b'], [4.6, -0.5]]]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_lists_of_list_file(self):
        self.assertEquals(ParseOMfile('tst/listnested.xml'), [1, 2, [3, 4, 5]])


suite4 = unittest.TestLoader().loadTestsFromTestCase(TestLists)
unittest.TextTestRunner(verbosity=2).run(suite4)

class TestSequenceFunctions(unittest.TestCase):

    def test_fraction(self):
        a = [1, Fraction(1, 2)]
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_fraction_file(self):
        self.assertEquals(ParseOMfile('tst/rational.xml'), [1, Fraction(1, 2)])

    def test_fraction_type(self):
        a = '<OMOBJ><OMA><OMS cd="list1" name="list"/><OMI>1</OMI><OMA><OMS cd="nums1" name="rational"/><OMI>1</OMI><OMI>2</OMI></OMA></OMA></OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), list)

    def test_complex(self):
        a = complex(Fraction(1, 2), 5)
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_complex_file(self):
        self.assertEquals(ParseOMfile('tst/complex.xml'), (0.6666666666666666+1.25j))

    def test_complex_type(self):
        a = '<OMOBJ><OMA><OMS cd="complex1" name="complex_cartesian"/><OMA><OMS cd="nums1" name="rational"/><OMI>2</OMI><OMI>3</OMI></OMA><OMA><OMS cd="nums1" name="rational"/><OMI>5</OMI><OMI>4</OMI></OMA></OMA></OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), complex)


suite5 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite5)

class TestInteger1(unittest.TestCase):
    def test_interval_file(self):
        self.assertEquals(ParseOMfile('tst/interval.xml'), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_interval_type(self):
        a = '<OMOBJ> <OMA> <OMS cd="interval1" name="integer_interval"/> <OMI>1</OMI> <OMI>10</OMI> </OMA> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), list)

    def test_factorial_file(self):
        self.assertEquals(ParseOMfile('tst/factorial.xml'), 3628800)

    def test_factorial_type(self):
        a = '<OMOBJ> <OMA> <OMS cd="integer1" name="factorial"/> <OMI>10</OMI> </OMA> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), int)

    def test_remainder_file(self):
        self.assertEquals(ParseOMfile('tst/remainder.xml'), 1)

    def test_remainder_type(self):
        a = '<OMOBJ> <OMA> <OMS cd="integer1" name="remainder"/> <OMI>5</OMI> <OMI>2</OMI> </OMA> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), int)

    def test_factorof_file(self):
        self.assertEquals(ParseOMfile('tst/factorof.xml'), False)

    def test_factorof_type(self):
        a = '<OMOBJ> <OMA> <OMS cd="integer1" name="factorof"/> <OMI>25</OMI> <OMI>2</OMI> </OMA> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), bool)

    def test_quotient_file(self):
        self.assertEquals(ParseOMfile('tst/quotient.xml'), 2)

    def test_quotient_type(self):
        a = '<OMOBJ> <OMA> <OMS cd="integer1" name="quotient"/> <OMI>5</OMI> <OMI>2</OMI> </OMA> </OMOBJ>'
        self.assertEquals(type(ParseOMstring(a)), int)

suite6 = unittest.TestLoader().loadTestsFromTestCase(TestInteger1)
unittest.TextTestRunner(verbosity=2).run(suite6)


class TestDictionary(unittest.TestCase):
    def test_dict(self):
        a = {'a': 10, 2: 'blue', 'b': 20}
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_dict_with_bool(self):
        a = {'a': False, True: 'b', False: True}
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_dict_with_float(self):
        a = {'a': 0.5, -1.: 'b', 0.654: -23.5}
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_dict_with_list(self):
        a = {'a': [1, 2], 2: ['yellow', True, 'blue'], False: ['45', 3, 2]}
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_dict_with_listoflist(self):
        a = {'one': [[1, 2], [3, 4], [5, 6]], 'two': [[7, 8], [9, 10]]}
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_dict_with_fraction(self):
        a = {'one': [1, Fraction(1, 2)], 3: [Fraction(4, 5)]}
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_dict_with_complex(self):
        a = {'hello': complex(Fraction(1, 2), 5)}
        b = ParseOMstring(OMstring(a))
        self.assertEquals(a, b)

    def test_dict_file(self):
        self.assertEquals(ParseOMfile('tst/dict.xml'), {'a': 10, 2: 'blue', 'b': 20})

suite7 = unittest.TestLoader().loadTestsFromTestCase(TestDictionary)
unittest.TextTestRunner(verbosity=2).run(suite7)


class TestMatrix(unittest.TestCase):
    def test_matrix(self):
        self.assertEquals(ParseOMfile('tst/matrix.xml'), [[1, 2, 3], [42, 5, 6], [0, -1, -100]])


suite8 = unittest.TestLoader().loadTestsFromTestCase(TestMatrix)
unittest.TextTestRunner(verbosity=2).run(suite8)