from openmath import *

tests = []

'''
Parse Arithmetic Operations OpenMath objects
'''
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="plus"/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="minus"/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="times"/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="divide"/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="pow"/><OMI>2</OMI> <OMI>3</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="sum"/><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="product"/><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="root"/><OMI>4</OMI><OMI>2</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="abs"/><OMI>-4</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="gcd"/><OMI>20</OMI><OMI>8</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="lcm"/><OMI>20</OMI><OMI>8</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="sum"/><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="product"/><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="root"/><OMI>4</OMI><OMI>2</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="abs"/><OMI>-4</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="gcd"/><OMI>20</OMI><OMI>8</OMI></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="lcm"/><OMI>20</OMI><OMI>8</OMI></OMA></OMOBJ>')
print "Basic arithmetic operations:"
tests.reverse()
while len(tests):
    print ">>", ParseOMstring(tests.pop())


'''
Parse Basic Requirement OpenMath objects
'''
tests.append('<OMOBJ> <OMI>42</OMI></OMOBJ>')
tests.append('<OMOBJ> <OMSTR>This is a string</OMSTR> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMF dec="0"/> <OMF dec="1."/> <OMF dec="0.5"/> <OMF dec="-1."/> <OMF dec="19487171."/> <OMF dec="5.1315811823070673e-08"/> <OMF dec="-19487171."/> <OMF dec="-5.1315811823070673e-08"/> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMS cd="logic1" name="false"/> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>1</OMI> <OMA> <OMS cd="nums1" name="rational"/> <OMI>1</OMI> <OMI>2</OMI> </OMA> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMA> </OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="complex1" name="complex_cartesian"/><OMA><OMS cd="nums1" name="rational"/><OMI>2</OMI><OMI>3</OMI></OMA><OMA><OMS cd="nums1" name="rational"/><OMI>5</OMI><OMI>4</OMI></OMA></OMA></OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="interval1" name="integer_interval"/> <OMI>1</OMI> <OMI>10</OMI> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="linalg2" name="matrix"/> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>1</OMI> <OMI>2</OMI> <OMI>3</OMI> </OMA> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>42</OMI> <OMI>5</OMI> <OMI>6</OMI> </OMA> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>0</OMI> <OMI>-1</OMI> <OMI>-100</OMI> </OMA> </OMA> </OMOBJ>')
print "\nBasic requirement:"
tests.reverse()
while len(tests):
    print ">>", ParseOMstring(tests.pop())



'''
Parse Additional Requirement XML files
'''
tests.append('<OMOBJ> <OMA> <OMS cd="integer1" name="factorial"/> <OMI>10</OMI> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="integer1" name="remainder"/> <OMI>5</OMI> <OMI>2</OMI> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="integer1" name="factorof"/> <OMI>25</OMI> <OMI>2</OMI> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="integer1" name="quotient"/> <OMI>5</OMI> <OMI>2</OMI> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMA> <OMS cd="integer1" name="quotient"/> <OMI>5</OMI> <OMI>2</OMI> </OMA> </OMOBJ>')
tests.append('<OMOBJ> <OMV name="x"/> </OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="dictionary" name="dict"/><OMA><OMS cd="dictionary" name="keyval"/><OMSTR>a</OMSTR><OMI>10</OMI></OMA><OMA><OMS cd="dictionary" name="keyval"/><OMSTR>b</OMSTR><OMI>20</OMI></OMA><OMA><OMS cd="dictionary" name="keyval"/><OMI>2</OMI><OMSTR>blue</OMSTR></OMA></OMA></OMOBJ>')
print "\nAdditional requirements:"
tests.reverse()
while len(tests):
    print ">>", ParseOMstring(tests.pop())

'''
Parse XML files
'''
print "\nParse XML files:"
print ">> ", ParseOMfile('../tst/integer.xml')
print ">> ", ParseOMfile('../tst/list.xml')
print ">> ", ParseOMfile('../tst/listnested.xml')
print ">> ", ParseOMfile('../tst/string.xml')
print ">> ", ParseOMfile('../tst/float.xml')
print ">> ", ParseOMfile('../tst/bool.xml')
print ">> ", ParseOMfile('../tst/rational.xml')
print ">> ", ParseOMfile('../tst/complex.xml')
print ">> ", ParseOMfile('../tst/interval.xml')
print ">> ", ParseOMfile('../tst/matrix.xml')
print ">> ", ParseOMfile('../tst/factorial.xml')
print ">> ", ParseOMfile('../tst/dict.xml')
print ">> ", ParseOMfile('../tst/factorof.xml')
print ">> ", ParseOMfile('../tst/remainder.xml')
print ">> ", ParseOMfile('../tst/quotient.xml')
print ">> ", ParseOMfile('../tst/omattr.xml')
print ">> ", ParseOMfile('../tst/arith-sum.xml')
print ">> ", ParseOMfile('../tst/range.xml')

'''
Compose XML files
'''
tests.append(42)
tests.append([1, 2, 3])
tests.append([1, 2, [3, 4, 5]])
tests.append("This is a string")
tests.append([0, 1., 0.5, -1., 19487171., 5.1315811823070673e-08, -19487171., -5.1315811823070673e-08])
tests.append(False)
tests.append([1, Fraction(1, 2)])
tests.append(complex(2, 5))
tests.append({'a': 10, 2: 'blue', 'b': 20})
print "\nOutput to OpenMath file:"
tests.reverse()
while len(tests):
    print "================================"
    OMprint(tests.pop())

