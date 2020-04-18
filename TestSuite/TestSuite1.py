import  unittest
from Demo1.Testcase1 import Testcase2
from Demo2.Testcase3 import MyTestCase

tc1=unittest.TestLoader().loadTestsFromTestCase(Testcase2)
tc2=unittest.TestLoader().loadTestsFromTestCase(MyTestCase)

sanityTestSuite=unittest.TestSuite(tc1)
functionalTestSuite=unittest.TestSuite(tc2)

unittest.TextTestRunner().run(sanityTestSuite)