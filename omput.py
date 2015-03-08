# Encoding Python parser for OpenMath (http://www.openmath.org/)
# See https://docs.python.org/2/library/xml.etree.elementtree.html#

import xml.etree.ElementTree as ET
from fractions import Fraction

Element = ET.Element
SubElement = ET.SubElement

################################################################
#
# OpenMath integer (OMI)
#
def OMInt(x):
    omelt = Element("OMI")
    omelt.text = str(x)
    return omelt

###############################################################
#
# OpenMath string (OMSTR)
#
def OMString(x):
    omelt = Element("OMSTR")
    omelt.text = x
    return omelt


################################################################
#
# OpenMath float (OMF)
#
def OMFloat(x):
    omelt = Element("OMF")
    omelt.attrib['dec'] = str(x)
    return omelt

#############################################################
#
# OpenMath boolean (OMS)
#
def OMBool(x):
    omelt = Element("OMS")
    omelt.attrib = {'cd': 'logic1', 'name': str(x).lower()}
    return omelt

################################################################
#
# List (list1.list)
#
def OMList(x):
    omelt = Element("OMA")
    oms   = Element("OMS")
    oms.attrib = {'cd': 'list1', 'name': 'list'}
    omelt.insert(1, oms)
    n = 1
    for t in x:
        n += 1
        omelt.insert(n, OMelement(t))
    return omelt

#############################################################
#
# Rational (nums1.rational)
#
def OMRational(x):
	omelt = Element("OMA")
	oms   = Element("OMS")
	oms.attrib = {'cd': 'nums1', 'name': 'rational'}
	omelt.insert(1, oms)
	omelt.insert(2, OMelement(x.numerator))
	omelt.insert(3, OMelement(x.denominator))
	return omelt

############################################################
#
# Cartesian (complex1.cartesian)
#
def OMComplex(x):
    omelt = Element("OMA")
    oms   = Element("OMS")
    oms.attrib = {'cd': 'complex1', 'name': 'complex_cartesian'}
    omelt.insert(1, oms)
    omelt.insert(2, OMelement(x.real))
    omelt.insert(3, OMelement(x.imag))
    return omelt

################################################################
#
# OMelement
#
# Dispatches OpenMath encoding method dependently on the type of x
#
def OMelement(x):
    t = type(x)
    if t == int:
        return OMInt(x)
    elif t == list:
        return OMList(x)
    elif t == str:
        return OMString(x)
    elif t == float:
        return OMFloat(x)
    elif t == bool:
        return OMBool(x)
    elif t == complex:
        return OMComplex(x)
    elif t == Fraction:
        return OMRational(x)

################################################################
#
# OMobject
#
# Wraps OpenMath encoding for x into OpenMath object
#
def OMobject(x):
    omobj = Element("OMOBJ")
    omobj.insert(1, OMelement(x))
    return omobj

################################################################
