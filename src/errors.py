from openmath import *

tests = ["<OMOBJ><OMF hex='FFF8000000000001'/></OMOBJ>"]
tests.append("<OMOBJ><OMI></OMI></OMOBJ>")
tests.append("<OMOBJ><OMI>Hello</OMI></OMOBJ>")
tests.append("<OMOBJ><OMF dec='data'/></OMOBJ>")
tests.append("<OMOBJ><OMSTR></OMSTR></OMOBJ>")
tests.append("<OMOBJ><OMV name=''/></OMOBJ>")
tests.append("<OMOBJ><OMV /></OMOBJ>")
tests.append("<OMOBJ><OMA><OMS cd='arith1' name='plus'/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>")
tests.append("<OMOBJ><OMA><OMS cd='arith1' name='plus'/><OMSTR>Hi</OMSTR> <OMI>43</OMI></OMA></OMOBJ>")
tests.append("<OMOBJ><OMA><OMS cd='arith1' name='plus'/><OMI>0xf</OMI> <OMI>43</OMI></OMA></OMOBJ>")
tests.append("<OMOBJ><OMA><OMS cd='arith1' name='minus'/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>")
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="sum"/><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="sum"/> <OMA> <OMS cd="list1" name="list"/> <OMF dec="0"/> <OMF dec="1."/> <OMF dec="0.5"/> <OMF dec="-1."/> <OMF dec="19487171."/> <OMF dec="5.1315811823070673e-08"/> <OMF dec="-19487171."/> <OMF dec="-5.1315811823070673e-08"/> </OMA> </OMA></OMOBJ>')
tests.append('<OMOBJ><OMA><OMS cd="arith1" name="sum"/> <OMA> <OMS cd="list1" name="list"/> <OMF dec="0"/> <OMF dec="1."/> <OMSTR>test</OMSTR></OMA> </OMA></OMOBJ>')

tests.reverse()
while (len(tests)):
    print ">>", ParseOMstring(tests.pop())
