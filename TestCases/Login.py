import unittest
import HtmlTestRunner
import sys
sys.path.append("D:\PyhtonProject\Demo")
from POM.LoginPage import LoginPage
from POM.FlightFinderPage import FlightFinderPage
from Framework.getDriverInstance import GetDriverInstance

class MyTestCase(unittest.TestCase):
    dataFilePath = "D://PyhtonProject/TestData_Login.xlsx"
    def test_launchChromeBrowser(self):
        global driver
        urlLink="http://www.newtours.demoaut.com/"
        FT=GetDriverInstance()
        driver=FT.LaunchDriver(urlLink)
        self.loginToNewTour(driver)

    def loginToNewTour(self,driver):
        MT=LoginPage(driver)
        #MT.LoginPOM()
        MT.loginToAppDDT(self.dataFilePath)
        FB = FlightFinderPage(driver)
        FB.flightBooking()
        print("Test case executed successfully")


    def tearDown(self):
        driver.close()
        print("Closed browser successfully")

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\Tosca\\Reports'))