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

s = '<OMOBJ><OMA><OMS cd="arith1" name="pow"/><OMI>2</OMI> <OMI>3</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="sum"/><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="product"/><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="root"/><OMI>4</OMI><OMI>2</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="abs"/><OMI>-4</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="gcd"/><OMI>20</OMI><OMI>8</OMI><OMI>4</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="arith1" name="lcm"/><OMI>20</OMI><OMI>8</OMI></OMA></OMOBJ>'
print ">>>", ParseOMstring(s)

print "\nThe rest:"

# integer
s = '<OMOBJ> <OMI>42</OMI></OMOBJ>'
print ">>", ParseOMstring(s)

# list
s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

# nested lists
s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

# floats
s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMF dec="0"/> <OMF dec="1."/> <OMF dec="0.5"/> <OMF dec="-1."/> <OMF dec="19487171."/> <OMF dec="5.1315811823070673e-08"/> <OMF dec="-19487171."/> <OMF dec="-5.1315811823070673e-08"/> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

# boolean
s = '<OMOBJ> <OMS cd="logic1" name="false"/> </OMOBJ>'
print ">>", ParseOMstring(s)

# rational
s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>1</OMI> <OMA> <OMS cd="nums1" name="rational"/> <OMI>1</OMI> <OMI>2</OMI> </OMA> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

# string
s = '<OMOBJ> <OMSTR>This is a string</OMSTR> </OMOBJ>'
print ">>", ParseOMstring(s)

# complex cartesian
s = '<OMOBJ><OMA><OMS cd="complex1" name="complex_cartesian"/><OMA><OMS cd="nums1" name="rational"/><OMI>2</OMI><OMI>3</OMI></OMA><OMA><OMS cd="nums1" name="rational"/><OMI>5</OMI><OMI>4</OMI></OMA></OMA></OMOBJ>'
print ">>", ParseOMstring(s)

# interval
s = '<OMOBJ> <OMA> <OMS cd="interval1" name="integer_interval"/> <OMI>1</OMI> <OMI>10</OMI> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

# matrix
s = '<OMOBJ> <OMA> <OMS cd="linalg2" name="matrix"/> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>1</OMI> <OMI>2</OMI> <OMI>3</OMI> </OMA> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>42</OMI> <OMI>5</OMI> <OMI>6</OMI> </OMA> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>0</OMI> <OMI>-1</OMI> <OMI>-100</OMI> </OMA> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

# factorial
s = '<OMOBJ> <OMA> <OMS cd="integer1" name="factorial"/> <OMI>10</OMI> </OMA> </OMOBJ>'
print ">>", ParseOMstring(s)

# variable
s = '<OMOBJ> <OMV name="x"/> </OMOBJ>'
print ">>", ParseOMstring(s)

# dictionary
s = '<OMOBJ><OMA><OMS cd="dictionary" name="dict"/><OMA><OMS cd="dictionary" name="keyval"/><OMSTR>a</OMSTR><OMI>10</OMI></OMA><OMA><OMS cd="dictionary" name="keyval"/><OMSTR>b</OMSTR><OMI>20</OMI></OMA><OMA><OMS cd="dictionary" name="keyval"/><OMI>2</OMI><OMSTR>blue</OMSTR></OMA></OMA></OMOBJ>'
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
ParseOMfile('tst/dict.xml')

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

OMstring([['yellow', 2], ['blue', 3], [2, 'blue']])
OMprint([['yellow', 2], ['blue', 3], [2, 'blue']])

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

a = [['yellow', 2], ['blue', 3], [2, 'blue']]
b = ParseOMstring(OMstring(a))
print a, ":", b, "==", a == b
