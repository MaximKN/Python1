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
omdicts['nums1'] = {}

#nums1.rational
omdicts['nums1']['rational'] = oms_list1_list

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


ParseOMelementHandler = {'OMI': ParseOMI, 'OMSTR': ParseOMSTR, 'OMF': ParseOMF, 'OMS': ParseOMS, 'OMA': ParseOMA}


def ParseOMelement(obj):
    return ParseOMelementHandler[obj.tag](obj)


def ParseOMroot(root):
    return ParseOMelement(root[0])


    ################################################################
