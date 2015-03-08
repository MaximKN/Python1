from fractions import *
from math import *

################################################################
#
# Basic OpenMath elements
#


# OpenMath integer
def ParseOMI(node):
    return int(node.text)


# OpenMath float
def ParseOMF(node):
    return float(node.attrib['dec'])


# OpenMath string
def ParseOMSTR(node):
    return node.text


# OpenMath variable
def ParseOMV(node):
    return node.attrib['name']


################################################################
#
# OpenMath content dictionaries
#
omdicts = {'list1': {}, 'nums1': {}, 'complex1': {}, 'logic1': {},
           'interval1': {}, 'linalg2': {}, 'integer1': {}, 'arith1': {}, 'dictionary': {}}


# list1    http://www.openmath.org/cd/list1.xhtml
# list1.list
def oms_list1_list(list):
    return list


omdicts['list1']['list'] = oms_list1_list


################################################################
#
# OpenMath all arithmetic operations
#

def oms_arith1_plus(obj):
    assert len(obj) == 2, "PLUS requires two elements"
    return obj[0] + obj[1]


def oms_arith1_minus(obj):
    assert len(obj) == 2, "MINUS requires two elements"
    return obj[0] - obj[1]


def oms_arith1_times(obj):
    assert len(obj) == 2, "TIMES requires two elements"
    return obj[0] * obj[1]


def oms_arith1_divide(obj):
    assert len(obj) == 2, "DIVIDE requires two elements"
    return obj[0] / obj[1]


def oms_arith1_pow(obj):
    assert len(obj) == 2, "POWER requires two elements"
    return obj[0] ** obj[1]


def oms_arith1_sum(obj):
    assert len(obj) >= 1, "SUM requires at least one element"
    return reduce(lambda x, y: x + y, obj[0])


def oms_arith1_product(obj):
    assert len(obj) >= 1, "PRODUCT requires at least one element"
    return reduce(lambda x, y: x * y, obj[0])


def oms_arith1_root(obj):
    assert len(obj) == 2, "ROOT requires two elements"
    return obj[0] ** 1 / obj[1]


def oms_arith1_abs(obj):
    assert len(obj) == 1, "ABS requires one element"
    return abs(obj[0])


def oms_arith1_gcd(obj):
    assert len(obj) == 2, "GCD requires two elements"
    return gcd(obj[0], obj[1])


def oms_arith1_lcm(obj):
    assert len(obj) == 2, "LCM requires at two elements"
    return (obj[0] * obj[1]) / gcd(obj[0], obj[1])


# arith1 http://www.openmath.org/cd/arith1.xhtml
# Basic arithmetic operations
omdicts['arith1']['plus'] = oms_arith1_plus
omdicts['arith1']['minus'] = oms_arith1_minus
omdicts['arith1']['times'] = oms_arith1_times
omdicts['arith1']['divide'] = oms_arith1_divide
omdicts['arith1']['pow'] = oms_arith1_pow

# Other non-trivial operations
omdicts['arith1']['sum'] = oms_arith1_sum
omdicts['arith1']['product'] = oms_arith1_product
omdicts['arith1']['root'] = oms_arith1_root
omdicts['arith1']['abs'] = oms_arith1_abs
omdicts['arith1']['gcd'] = oms_arith1_gcd
omdicts['arith1']['lcm'] = oms_arith1_lcm

# logic1	http://www.openmath.org/cd/logic1.xhtml
# logic1.true
omdicts['logic1']['true'] = True

# logic1.false
omdicts['logic1']['false'] = False


################################################################
#
# OpenMath all basic data types
#

# nums1     http://www.openmath.org/cd/nums1.xhtml
# nums1.rational
def oms_nums1_rational(obj):
    assert len(obj) == 2, "Rational requires exactly two elements."
    t = type(obj[0])
    assert t is int and t == type(obj[1]), "Rational only accepts integer values."
    assert obj[1] != 0, "Denominator of rational needs to be non-integer"
    return Fraction(obj[0], obj[1])


omdicts['nums1']['rational'] = oms_nums1_rational


# complex1  http://www.openmath.org/cd/complex1.xhtml
# complex1.complex_cartesian
def oms_complex1_cartesian(obj):
    assert len(obj) == 2, "Complex cartesian requires exactly two elements."
    t1 = type(obj[0])
    t2 = type(obj[1])
    assert t1 == int or t1 == float or t1 == Fraction
    assert t2 == int or t2 == float or t2 == Fraction
    return complex(obj[0], obj[1])


omdicts['complex1']['complex_cartesian'] = oms_complex1_cartesian


# interval1 http://www.openmath.org/cd/interval1.xhtml
# interval1.integer_interval
def oms_interval1_interval(obj):
    assert len(obj) == 2
    t = type(obj[0])
    assert t == type(obj[1]) and t == int
    return list(range(obj[0], obj[1] + 1))

omdicts['interval1']['integer_interval'] = oms_interval1_interval


# linalg2   http://www.openmath.org/cd/linalg2.xhtml
# linalg2.matrixrow
def oms_linalg2_matrixrow(obj):
    assert len(obj) > 0
    # check all cells have the same type
    t = type(obj[0])
    for i in obj:
        assert t == type(i)
    t = type(i)
    assert t == float or t == int
    return obj


omdicts['linalg2']['matrixrow'] = oms_linalg2_matrixrow

# linalg2.matrix
def oms_linalg2_matrix(obj):
    assert len(obj) > 0
    length = len(obj[0])
    for row in obj:
        assert len(row) == length, "Rows in matrix need to equal size"
    return obj

omdicts['linalg2']['matrix'] = oms_linalg2_matrix


# integer1  http://www.openmath.org/cd/integer2.xhtml
# integer1.factorial
def oms_integer1_factorial(obj):
    assert len(obj) == 1, "Factorial only supports one element."
    assert type(obj[0]) is int, "Can't compute factorial of a non-integer."
    assert obj[0] >= 0, "Can't compute factorial of negative integer."
    return factorial(obj[0])


omdicts['integer1']['factorial'] = oms_integer1_factorial


def oms_dictionary_keyval(obj):
    return obj

# dictionary.keyval
omdicts['dictionary']['keyval'] = oms_dictionary_keyval


def oms_dictionary_dict(obj):
    return obj

# dictionary.dict
omdicts['dictionary']['dict'] = oms_dictionary_dict

################################################################


def ParseOMS(node):
    # returns a function or an object
    return omdicts[node.get('cd')][node.get('name')]


def ParseOMA(node):
    elts = []
    for child in node.findall("*"):
        elts.append(ParseOMelement(child))
    # now the first element of 'elts' is a function to be applied to the rest of the list
    return elts[0](elts[1:])


def ParseOMATTR(node):
    pass


def ParseOMATP(node):
    pass


ParseOMelementHandler = {'OMI': ParseOMI, 'OMSTR': ParseOMSTR, 'OMV': ParseOMV, 'OMF': ParseOMF,
                         'OMS': ParseOMS, 'OMA': ParseOMA, 'OMATTR': ParseOMATTR, 'OMATP': ParseOMATP}


def ParseOMelement(obj):
    return ParseOMelementHandler[obj.tag](obj)


def ParseOMroot(root):
    return ParseOMelement(root[0])


################################################################
