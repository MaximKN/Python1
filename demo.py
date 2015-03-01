from openmath import *

s = '<OMOBJ> <OMI>42</OMI> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMA> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMF dec="0"/> <OMF dec="1."/> <OMF dec="0.5"/> <OMF dec="-1."/> <OMF dec="19487171."/> <OMF dec="5.1315811823070673e-08"/> <OMF dec="-19487171."/> <OMF dec="-5.1315811823070673e-08"/> </OMA> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMS cd="logic1" name="false"/> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>1</OMI> <OMA> <OMS cd="nums1" name="rational"/> <OMI>1</OMI> <OMI>2</OMI> </OMA> </OMA> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMSTR>This is a string</OMSTR> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="complex1" name="complex_cartesian"/> <OMA> <OMS cd="nums1" name="rational"/> <OMI>2</OMI> <OMI>3</OMI> </OMA> <OMA> <OMS cd="nums1" name="rational"/> <OMI>5</OMI> <OMI>4</OMI> </OMA> </OMA> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ><OMA><OMS cd="linalg2" name="matrix"/><OMA><OMS cd="linalg2" name="matrixrow"/><OMI>1</OMI><OMI>2</OMI><OMI>3</OMI></OMA><OMA><OMS cd="linalg2" name="matrixrow"/><OMI>42</OMI><OMI>5</OMI><OMI>6</OMI></OMA><OMA><OMS cd="linalg2" name="matrixrow"/><OMI>0</OMI><OMI>-1</OMI><OMI>-100</OMI></OMA></OMA></OMOBJ>'
ParseOMstring(s)

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

OMstring([1, 1 / 2])
OMprint([1, 1 / 2])

OMstring(complex(2 / 3, 5 / 4))
OMprint(complex(2 / 3, 5 / 4))

# tests
a = 42
a == ParseOMstring(OMstring(a))

a = [1, 2, 3]
a == ParseOMstring(OMstring(a))

a = [1, 2, [3, 4, 5]]
a == ParseOMstring(OMstring(a))

a = "This is a string"
a == ParseOMstring(OMstring(a))

a = [0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08]
a == ParseOMstring(OMstring(a))

a = False
a == ParseOMstring(OMstring(a))

a = [1, 1 / 2]
a == ParseOMstring(OMstring(a))

a = complex(2 / 3, 5 / 4)
a == ParseOMstring(OMstring(a))
