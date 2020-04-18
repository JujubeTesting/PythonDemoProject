import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner

def setUpModule():
    print("Before all classes")

def tearDownModule():
    print("After all classes")

class Testcase2(unittest.TestCase):
    def test_m1(self):
        list1=[1,2,5,10,15]
        self.driver = webdriver.Chrome(executable_path="E:\Grid\chromedriver.exe")
        self.driver.get("https://paytm.com/")
        expectedTitle = self.driver.title
        print(expectedTitle)
        self.assertEqual(expectedTitle, "Paytm.com – Recharge & Utility Payments, Entertainment, Travel, DTH, Wallet & Payment")
        self.assertTrue(expectedTitle=="Paytm.com – Recharge & Utility Payments, Entertainment, Travel, DTH, Wallet & Payments","test case passed as assert equals")
        self.assertIn(5,list1)
        self.assertGreater(10,5,"value is not greater")


    def test_m2(self):
        self.driver = webdriver.Chrome(executable_path="E:\Grid\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        expectedTitle = self.driver.title
        print(expectedTitle)
        self.assertEqual(expectedTitle, "Google")

    def test_m3(self):
        print("Demo Test")

    @classmethod
    def setUp(self):
        print("Before Mevery Method")

    @classmethod
    def tearDown(self):
        print("After every method")

    @classmethod
    def setUpClass(cls):
        print("only once before all test of a class")

    @classmethod
    def tearDownClass(cls):
        print("only once after all test of a class")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Tosca\\Reports'))
