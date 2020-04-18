import unittest


class webPage:
    def sendkeys(self,element,inputText):
        try:
            element.send_keys(inputText)
            print("## successfull entered value "+inputText+ " in field ")
        except Exception as e:
            print(" ## failed to enter value in field ")

    def click(self,element):
        try:
            element.click()
            print("## successfully clicked on element ")
        except Exception as e:
            print("## Failed to click on element ")
            print("\n")

    def __init__(self, driver):
        self.driver = driver
        print("## driver initialised successfully @ base class ")
        print("\n")