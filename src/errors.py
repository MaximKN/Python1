from openmath import *

tests = ["<OMOBJ><OMF hex='FFF8000000000001'/></OMOBJ>", "<OMOBJ><OMI></OMI></OMOBJ>",
         "<OMOBJ><OMI>Hello</OMI></OMOBJ>", "<OMOBJ><OMF dec='data'/></OMOBJ>", "<OMOBJ><OMSTR></OMSTR></OMOBJ>",
         "<OMOBJ><OMV name=''/></OMOBJ>", "<OMOBJ><OMV /></OMOBJ>",
         "<OMOBJ><OMA><OMS cd='arith1' name='plus'/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>",
         "<OMOBJ><OMA><OMS cd='arith1' name='plus'/><OMSTR>Hi</OMSTR> <OMI>43</OMI></OMA></OMOBJ>",
         "<OMOBJ><OMA><OMS cd='arith1' name='plus'/><OMI>0xf</OMI> <OMI>43</OMI></OMA></OMOBJ>",
         "<OMOBJ><OMA><OMS cd='arith1' name='minus'/><OMI>42</OMI> <OMI>43</OMI></OMA></OMOBJ>",
         "<OMOBJ><OMA><OMS cd='arith1' name='minus'/><OMI>42</OMI></OMA></OMOBJ>",
         '<OMOBJ><OMA><OMS cd="arith1" name="sum"/><OMA><OMS cd="interval1" name="integer_interval"/><OMI>1</OMI><OMI>10</OMI></OMA></OMA></OMOBJ>',
         '<OMOBJ><OMA><OMS cd="arith1" name="sum"/> <OMA> <OMS cd="list1" name="list"/> <OMF dec="0"/> <OMF dec="1."/> <OMF dec="0.5"/> <OMF dec="-1."/> <OMF dec="19487171."/> <OMF dec="5.1315811823070673e-08"/> <OMF dec="-19487171."/> <OMF dec="-5.1315811823070673e-08"/> </OMA> </OMA></OMOBJ>',
         '<OMOBJ><OMA><OMS cd="arith1" name="sum"/> <OMA> <OMS cd="list1" name="list"/> <OMF dec="0"/> <OMF dec="1."/> <OMSTR>test</OMSTR></OMA> </OMA></OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="linalg2" name="matrix"/> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>1</OMI> <OMI>2</OMI> <OMI>3</OMI> </OMA> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>42</OMI> <OMI>5</OMI> </OMA> <OMA> <OMS cd="linalg2" name="matrixrow"/> <OMI>0</OMI>  </OMA> </OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="factorial"/></OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="factorial"/><OMSTR>4</OMSTR></OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="factorial"/><OMI>-6</OMI></OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="remainder"/> <OMI>5</OMI> <OMI>2.5</OMI> </OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="remainder"/> <OMI>5</OMI> </OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="factorof"/> <OMI>25.6</OMI> <OMI>2</OMI> </OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="factorof"/> <OMI>2</OMI> </OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="quotient"/> <OMI>5.5</OMI> <OMI>2</OMI> </OMA> </OMOBJ>',
         '<OMOBJ> <OMA> <OMS cd="integer1" name="quotient"/> <OMI>5</OMI> </OMA> </OMOBJ>']
tests.reverse()
while len(tests):
    print ">>", ParseOMstring(tests.pop())
