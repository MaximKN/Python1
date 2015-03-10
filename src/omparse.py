################################################################
#
# Parsing OpenMath objects
#
from __future__ import division
from fractions  import Fraction, gcd
from math       import factorial
from operator   import add, mul, sub, truediv, pow

from numpy import matrix


################################################################
#
# Basic OpenMath elements
#

# OpenMath integer
def ParseOMI(node):
    try:
        return int(node.text)
    except TypeError:
        print "Couldn't find any integers in <OMI> tag."
    except ValueError:
        print "\"%s\" couldn't be converted into integer." % node.text
        
# OpenMath float
def ParseOMF(node):
    try:
        return float(node.attrib['dec'])
    except KeyError:
        print "Oops! Couldn't find float in decimal notation. "\
                        "Are you using hexadecimal?"
    except ValueError:
        print "Float's decimal notation is illegal. "\
                    "Do you have any characters in it?"
    
# OpenMath string
def ParseOMSTR(node):
    return node.text
    
# OpenMath variable
def ParseOMV(node):
    try:
        name = node.attrib['name']
        # make sure variable name contains at least one character
        if (len(name) == 0):
            print "Variable's name needs to have at least one character."
        else:
            return node.attrib['name']
    except KeyError:
        print "Variable's name could not be determined. "\
                        "Did you supply a name attribute?"

################################################################
#
# OpenMath content dictionaries
#
omdicts = {'list1': {}, 'nums1': {}, 'complex1': {}, 'logic1': {},
           'interval1': {}, 'linalg2': {}, 'integer1': {}, 'arith1': {},
           'dictionary': {}}


# list1    http://www.openmath.org/cd/list1.xhtml
# list1.list
def oms_list1_list(list):
    return list

omdicts['list1']['list'] = oms_list1_list

#####################################
# OpenMath arithmetic operations
#####################################

def oms_arith1_apply_op(obj, op):
    try:
        return op(obj[0], obj[1])
    except IndexError:
        print "Arithmetic calculation returns two operands"
    except TypeError:
        print "Invalid operand types"

'''
Basic arithmetic operations
'''      
def oms_arith1_plus(obj):   return oms_arith1_apply_op(obj, add)
def oms_arith1_minus(obj):  return oms_arith1_apply_op(obj, sub)
def oms_arith1_times(obj):  return oms_arith1_apply_op(obj, mul)
def oms_arith1_divide(obj): return oms_arith1_apply_op(obj, truediv)
def oms_arith1_pow(obj):    return oms_arith1_apply_op(obj, pow)
    
def oms_arith1_sum(obj):
    try:
        return sum(obj[0])
    except IndexError:
        print "SUM requires at least one element"
    except TypeError:
        print "Invalid operand types from SUM"

def oms_arith1_root(obj):
    try:
        return obj[0] ** (1 / obj[1])
    except IndexError:
        print "ROOT requires two elements"
    except TypeError:
        print "Invalid operand types from ROOT"
        
def oms_arith1_product(obj):
    try:
        return map(mul, obj[0])
    except IndexError:
        print "PRODUCT requires at least one element"
        
def oms_arith1_abs(obj):
    try:
        return abs(obj[0])
    except IndexError:
        print "ABS requires at least one element"
        
def oms_arith1_gcd(obj):
    try:
        return gcd(obj[0], obj[1])
    except IndexError:
        print "GCD requires two elements"
        
def oms_arith1_lcm(obj):
    try:
        return (obj[0] * obj[1]) / gcd(obj[0], obj[1])
    except IndexError:
        print "LCM requires two elements"
        
        
# arith1 http://www.openmath.org/cd/arith1.xhtml
# Basic arithmetic operations
omdicts['arith1']['plus']    = oms_arith1_plus
omdicts['arith1']['minus']   = oms_arith1_minus
omdicts['arith1']['times']   = oms_arith1_times
omdicts['arith1']['divide']  = oms_arith1_divide
omdicts['arith1']['pow']     = oms_arith1_pow
omdicts['arith1']['sum']     = oms_arith1_sum
omdicts['arith1']['product'] = oms_arith1_product
omdicts['arith1']['root']    = oms_arith1_root
omdicts['arith1']['abs']     = oms_arith1_abs
omdicts['arith1']['gcd']     = oms_arith1_gcd
omdicts['arith1']['lcm']     = oms_arith1_lcm

################################
# OpenMath all basic data types
################################

# logic1	http://www.openmath.org/cd/logic1.xhtml
omdicts['logic1']['true']  = True
omdicts['logic1']['false'] = False

# nums1     http://www.openmath.org/cd/nums1.xhtml
# nums1.rational
def oms_nums1_rational(obj):
    try:
        return Fraction(obj[0], obj[1])
    except IndexError:
        print "Rational requires at two elements"
    except TypeError:
        print "Invalid type for rational" 
    except ZeroDivisionError:
        print "Can't divide by zero"
       
omdicts['nums1']['rational'] = oms_nums1_rational


# complex1  http://www.openmath.org/cd/complex1.xhtml
# complex1.complex_cartesian
def oms_complex1_cartesian(obj):
    try:
        return complex(obj[0], obj[1])
    except IndexError:
        print "Complex cartesian requires two elements"
    except TypeError:
        print "Invalid type being used for complex number"
        
omdicts['complex1']['complex_cartesian'] = oms_complex1_cartesian


# interval1 http://www.openmath.org/cd/interval1.xhtml
# interval1.integer_interval
def oms_interval1_interval(obj):
    try:
        t = range(obj[0], obj[1] + 1)
        
        # support for python definition of range returning range type
        if type(t) == list: return t
        else: return list(t)
    except IndexError:
        print "Interval requires two elements for range"
    except TypeError:
        print "Invalid types used for interval"
        
omdicts['interval1']['integer_interval'] = oms_interval1_interval


# linalg2   http://www.openmath.org/cd/linalg2.xhtml
# linalg2.matrixrow
def oms_linalg2_matrixrow(obj):
    try:
        # check all cells have the same type
        t = type(obj[0])
        for i in obj:
            if t != type(i):
                print "Matrix row's cells must all contain the same type"
                exit()
        assert t == float or t == int, "Matrix can only contain ints or floats"
        return obj
    except IndexError:
        print "Need to have at least one element in matrix row"
        
omdicts['linalg2']['matrixrow'] = oms_linalg2_matrixrow

# linalg2.matrix
def oms_linalg2_matrix(obj):
    try:
        length = len(obj[0])
        for row in obj[1:]:
            if len(row) != length:
                print "Rows in matrix need to equal size"
                return
        return matrix(obj)
    except IndexError:
        print "Need to have at least one row in matrix"
        
def oms_linalg2_matrix_dict(obj):
    keys = obj[0]
    data = [dict(zip(keys, values)) for values in obj[1:]]
    return data

omdicts['linalg2']['matrix'] = oms_linalg2_matrix


# integer1  http://www.openmath.org/cd/integer2.xhtml
# integer1.factorial
def oms_integer1_factorial(obj):
    try:
        if len(obj) != 1:
            print "Factorial only supports one element."
            return
        if not type(obj[0]) is int:
            print"Can't compute factorial of a non-integer."
            return
        if obj[0] < 0:
            print "Can't compute factorial of negative integer."
            return
        return factorial(obj[0])
    except IndexError:
        print "Factorial must have only one element"
    except TypeError:
        print "Factorial must to be an integer"


omdicts['integer1']['factorial'] = oms_integer1_factorial


def oms_dictionary_keyval(obj):
    return obj

# dictionary.keyval
omdicts['dictionary']['keyval'] = oms_dictionary_keyval

def oms_dictionary_dict(obj):
    return dict((x[0], x[1]) for x in obj)

# dictionary.dict
omdicts['dictionary']['dict'] = oms_dictionary_dict


# error http://www.openmath.org/cd/error.xhtml
#omdicts['error']

################################################################

def ParseOMS(node):
    # returns a function or an object
    return omdicts[node.get('cd')][node.get('name')]


def ParseOMA(node):
    elts = []
    for child in node.findall("*"):
        elts.append(ParseOMelement(child))
    # first element of 'elts' is a function to be applied to the rest of list
    return elts[0](elts[1:])

def ParseOMATTR(node):
    return ParseOMelement(node[1])

def ParseOMATP(node):
    return node
    
def ParseOME(node):
    assert len(node) > 0
    return node[0].attrib['name']

ParseOMelementHandler = {'OMI': ParseOMI, 'OMSTR': ParseOMSTR, 'OMV': ParseOMV,
                         'OMF': ParseOMF, 'OMS': ParseOMS, 'OMA': ParseOMA,
                         'OMATTR': ParseOMATTR, 'OMATP': ParseOMATP,
                         'OME': ParseOME}

def ParseOMelement(obj):
    return ParseOMelementHandler[obj.tag](obj)
        
def ParseOMroot(root):
    return ParseOMelement(root[0])

