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


def ParseOMV(node):
    return node.attrib['name']
################################################################
#
# OpenMath content dictionaries
#
omdicts = {'list1': {}}

# list1    http://www.openmath.org/cd/list1.xhtml


# list1.list
def oms_list1_list(list):
    return list

omdicts['list1']['list'] = oms_list1_list

# logic1	http://www.openmath.org/cd/logic1.xhtml
omdicts['logic1'] = {}

# logic1.true
omdicts['logic1']['true'] = True

# logic1.false
omdicts['logic1']['false'] = False

# nums1     http://www.openmath.org/cd/nums1.xhtml

def oms_nums1_rational(obj):
    pass
    # make sure it gets the actual children
    # check children if integer
    # make sure there are only two

omdicts['nums1'] = {}

# nums1.rational
omdicts['nums1']['rational'] = oms_nums1_rational

# complex1  https://www.openmath.org/cd/complex1.xhtml
omdicts['complex1'] = {}

# complex1.complex_cartesian
omdicts['complex1']['complex_cartesian'] = oms_list1_list

# interval1
omdicts['interval1'] = {}

# interval1
omdicts['interval1']['integer_interval'] = oms_list1_list

# linalg2
omdicts['linalg2'] = {}

# linalg2.matrixrow
omdicts['linalg2']['matrixrow'] = oms_list1_list

# linalg2.matrix
omdicts['linalg2']['matrix'] = oms_list1_list

# integer1
omdicts['integer1'] = {}

# linalg2.matrix
omdicts['integer1']['factorial'] = oms_list1_list

################################################################

def ParseOMS(node):
    # returns a function or an object
    return omdicts[node.get('cd')][node.get('name')]


def ParseOMA(node):
    elts = []
    for child in node.findall("*"):
        elts.append(ParseOMelement(child))
    # now the first element of 'elts' is a function to be applied to the rest of the list
    return elts[0](elts[1:len(elts)])


ParseOMelementHandler = {'OMI': ParseOMI, 'OMSTR': ParseOMSTR, 'OMV': ParseOMV, 'OMF': ParseOMF, 'OMS': ParseOMS,
                         'OMA': ParseOMA}


def ParseOMelement(obj):
    return ParseOMelementHandler[obj.tag](obj)


def ParseOMroot(root):
    return ParseOMelement(root[0])


################################################################
