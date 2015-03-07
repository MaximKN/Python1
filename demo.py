from fractions import Fraction

from openmath import *


print "Arithmetic operations:"

s = '<OMOBJ><OMA><OMS cd="arith1" name="plus"/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="minus"/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="times"/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="divide"/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

print "Rest of it"

s = '<OMOBJ> <OMI>42</OMI> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMF dec="0"/> <OMF dec="1."/> <OMF dec="0.5"/> <OMF dec="-1."/> <OMF dec="19487171."/> <OMF dec="5.1315811823070673e-08"/> <OMF dec="-19487171."/> <OMF dec="-5.1315811823070673e-08"/> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMS cd="logic1" name="false"/> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>1</OMI> <OMA> <OMS cd="nums1" name="rational"/> <OMI>1</OMI> <OMI>2</OMI> </OMA> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMSTR>This is a string</OMSTR> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="complex1" name="complex_cartesian"/><OMA><OMS cd="nums1" name="rational"/><OMI>2</OMI><OMI>3</OMI></OMA><OMA><OMS cd="nums1" name="rational"/><OMI>5</OMI><OMI>4</OMI></OMA></OMA></OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="interval1" name="integer_interval"/> <OMI>1</OMI> <OMI>10</OMI> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="linalg2" name="matrix"/> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>1</OMI> <OMI>2</OMI> <OMI>3</OMI> </OMA> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>42</OMI> <OMI>5</OMI> <OMI>6</OMI> </OMA> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>0</OMI> <OMI>-1</OMI> <OMI>-100</OMI> </OMA> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="integer1" name="factorial"/> <OMI>10</OMI> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

s = '<OMOBJ> <OMV name="x"/> </OMOBJ>'
print ">>", ParseOMstring(s)

ParseOMfile('tst/integer.xml')
ParseOMfile('tst/list.xml')
ParseOMfile('tst/listnested.xml')
ParseOMfile('tst/string.xml')
ParseOMfile('tst/float.xml')
ParseOMfile('tst/bool.xml')
ParseOMfile('tst/rational.xml')
ParseOMfile('tst/complex.xml')
ParseOMfile('tst/interval.xml')
ParseOMfile('tst/matrix.xml')
ParseOMfile('tst/factorial.xml')

OMstring(42)
OMprint(42)

OMstring([1, 2, 3])
OMprint([1, 2, 3])

OMstring([1, 2, [3, 4, 5]])
OMprint([1, 2, [3, 4, 5]])

OMstring("This is a string")
OMprint("This is a string")

OMstring([0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08])
OMprint([0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08])

OMstring(False)
OMprint(False)

OMstring([1, Fraction(1, 2)])
OMprint([1, Fraction(1, 2)])

OMstring(complex(2, 5))
OMprint(complex(2, 5))

################# ERROR CHECKING #####################

#s = '<OMOBJ> <OMA> <OMS cd="integer1" name="factorial"/> <OMV name="x"/></OMA> </OMOBJ>' 
#print "error-check >>>", ParseOMstring(s)

#s = '<OMOBJ> <OMA> <OMS cd="nums1" name="rational"/> <OMI>5</OMI> <OMI>4</OMI> </OMA> </OMOBJ>'
#print "error-check >>>", ParseOMstring(s)

#s = '<OMOBJ> <OMA> <OMS cd="nums1" name="rational"/> <OMV name="x"/> <OMV name="y"/> </OMA> </OMOBJ>'
#print "error-check >>>", ParseOMstring(s) 

######################################################

# tests
a = 42
b = ParseOMstring(OMstring(a))
print a, ":", b, " == ", a == b

a = [1, 2, 3]
b = ParseOMstring(OMstring(a))
print a, ":", b, " == ", a == b

a = [1, 2, [3, 4, 5]]
b = ParseOMstring(OMstring(a))
print a, ":", b, " == ", a == b

a = "This is a string"
b = ParseOMstring(OMstring(a))
print a, ":", b, " == ", a == b

a = [0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08]
b = ParseOMstring(OMstring(a))
print a, ":", b, " == ", a == b

a = False
b = ParseOMstring(OMstring(a))
print a, ":", b, " == ", a == b

a = [1, Fraction(1, 2)]
b = ParseOMstring(OMstring(a))
print a, ":", b, " == ", a == b

a = complex(Fraction(1, 2), 5)
b = ParseOMstring(OMstring(a))
print a, ":", b, " == ", a == b
