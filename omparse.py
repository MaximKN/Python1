################################################################
#
# Parsing OpenMath objects
#

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
           'interval1': {}, 'linalg2': {}, 'integer1': {}}

# list1    http://www.openmath.org/cd/list1.xhtml
# list1.list
def oms_list1_list(list):
    return list

omdicts['list1']['list'] = oms_list1_list


# logic1	http://www.openmath.org/cd/logic1.xhtml
# logic1.true
omdicts['logic1']['true'] = True

# logic1.false
omdicts['logic1']['false'] = False


# nums1     http://www.openmath.org/cd/nums1.xhtml
# nums1.rational
def oms_nums1_rational(obj):
    assert len(obj) == 2, "Rational requires exactly two elements."
    t = type(obj[0])
    assert t == type(obj[1]) and t is int, "Rational only accepts integer values."
    assert obj[1] != 0, "Denominator of rational needs to be non-integer"
    return obj

omdicts['nums1']['rational'] = oms_nums1_rational


# complex1  http://www.openmath.org/cd/complex1.xhtml
# complex1.complex_cartesian
def oms_complex1_cartesian(obj):
    return obj

omdicts['complex1']['complex_cartesian'] = oms_complex1_cartesian


# interval1 http://www.openmath.org/cd/interval1.xhtml
# interval1.integer_interval
def oms_interval1_interval(obj):
    return obj

omdicts['interval1']['integer_interval'] = oms_interval1_interval


# linalg2   http://www.openmath.org/cd/linalg2.xhtml
# linalg2.matrixrow
def oms_linalg2_matrixrow(obj):
    return obj

omdicts['linalg2']['matrixrow'] = oms_linalg2_matrixrow

# linalg2.matrix
def oms_linalg2_matrix(obj):
    # call matrixrow functon on obj
    return obj

omdicts['linalg2']['matrix'] = oms_linalg2_matrix


# integer1  http://www.openmath.org/cd/integer2.xhtml
# integer1.factorial
def oms_integer1_factorial(obj):
    assert len(obj) == 1, "Factorial only supports one element." 
    assert type(obj[0]) is int, "Can't compute factorial of a non-integer."
    assert obj[0] >= 0, "Can't compute factorial of negative integer."
    return obj

omdicts['integer1']['factorial'] = oms_integer1_factorial

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


ParseOMelementHandler = {'OMI': ParseOMI, 'OMSTR': ParseOMSTR, 'OMV': ParseOMV, 'OMF': ParseOMF, 'OMS': ParseOMS,
                         'OMA': ParseOMA}


def ParseOMelement(obj):
    return ParseOMelementHandler[obj.tag](obj)


def ParseOMroot(root):
    return ParseOMelement(root[0])


################################################################
