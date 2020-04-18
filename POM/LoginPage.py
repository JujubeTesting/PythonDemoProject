import unittest
from Framework.Base import webPage

class LoginPage(webPage):
    userName="userName"
    password="password"
    loginButton="login"

    def __init__(self,driver):
        self.driver=driver
        print("## driver initialized @LoginPage constructor ")
        print("\n")

    def LoginPOM(self):
        global userNameTextBox,passwordTextBox,loginButtonPage
        userNameTextBox=self.driver.find_element_by_name(self.userName)
        passwordTextBox = self.driver.find_element_by_name(self.password)
        loginButtonPage = self.driver.find_element_by_name(self.loginButton)
        print("## webelement initialized successfully @ LoginPOM method ")
        print("\n")

    def LoginToApp(self):
        self.sendkeys(userNameTextBox,"tutorials")
        self.sendkeys(passwordTextBox, "tutorials")
        self.click(loginButtonPage)

    
