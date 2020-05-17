import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class webPage:
    def sendkeys(self,element,inputText):
        try:
            element.clear()
            element.send_keys(inputText)
            print("## successfull entered value "+inputText+ " in field ")
            print("\r\n")
        except Exception as e:
            print(" ## failed to enter value in field ")

    def selectFromDropdown(self,sel,elementext):
        try:
            s= Select(sel)
            for opt in s.options:
                s.select_by_visible_text(elementext)
                print("## successfully selected an element ",elementext)

            print("\r\n")
        except  Exception as e:
            print(" ## failed to select value from field ")

    def click(self,element):
        try:
            element.click()
            print("## successfully clicked on element ")
            print("\r\n")
        except Exception as e:
            print("## Failed to click on element ")
            print("\r\n")

    def __init__(self, driver):
        self.driver = driver
        print("## driver initialised successfully @ base class ")
        print("\n")

    def explicitWait(self,By,Value):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By, Value)))
