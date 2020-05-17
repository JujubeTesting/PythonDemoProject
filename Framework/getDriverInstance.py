import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class GetDriverInstance:
    def LaunchDriver(self,urlLink):
        try:
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            self.driver.get(urlLink)
            self.driver.implicitly_wait(20)
            print("## successfully navigated to URL")
            print("\n")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            print("## Driver launched successfully")
            print("\n")
            return self.driver
        except Exception as e:
            print(e)
            print("## Unable to launch driver ")
            print("\n")
            return



