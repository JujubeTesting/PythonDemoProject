import unittest
import HtmlTestRunner
import sys

sys.path.append("D:\PyhtonProject\Demo")
from POM.LoginPage import LoginPage
from Framework.getDriverInstance import GetDriverInstance

class MyTestCase(unittest.TestCase):

    def test_launchChromeBrowser(self):
        global driver
        urlLink="http://www.newtours.demoaut.com/"
        FT=GetDriverInstance()
        driver=FT.LaunchDriver(urlLink)
        self.loginToNewTour(driver)

    def loginToNewTour(self,driver):
        MT=LoginPage(driver)
        MT.LoginPOM()
        MT.LoginToApp()
        print("Test case executed successfully")


    def tearDown(self):
        driver.close()
        print("Closed browser successfully")

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\Tosca\\Reports'))