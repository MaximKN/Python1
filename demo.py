import openmath
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

ParseOMfile('tst/integer.xml')
ParseOMfile('tst/list.xml')
ParseOMfile('tst/listnested.xml')
ParseOMfile('tst/float.xml')
ParseOMfile('tst/bool.xml')
ParseOMfile('tst/rational.xml')

OMstring(42)
OMprint(42)

OMstring([1, 2, 3])
OMprint([1, 2, 3])

OMstring([1, 2, [3, 4, 5]])
OMprint([1, 2, [3, 4, 5]])

OMstring([0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08])
OMprint([0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08])

OMstring(False)
OMprint(False)

OMstring([1, 1 / 2])
OMprint([1, 1 / 2])

# tests
a = 42
a == ParseOMstring(OMstring(a))

a = [1, 2, 3]
a == ParseOMstring(OMstring(a))

a = [1, 2, [3, 4, 5]]
a == ParseOMstring(OMstring(a))

a = [0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08]
a == ParseOMstring(OMstring(a))

a = False
a == ParseOMstring(OMstring(a))

a = [1, 1 / 2]
a == ParseOMstring(OMstring(a))

