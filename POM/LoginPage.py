import unittest
from Framework.Base import webPage
import xlrd
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory, webPage):
    userName = "userName"
    password = "password"
    loginButton = "login"

    def __init__(self, driver):
        self.driver = driver
        print("## driver initialized @LoginPage constructor ")
        print("\n")

    locators = {
        "userNameTextBox": ('NAME', 'userName'),
        "passwordTextBox": ('NAME', 'password'),
        "loginButtonPage": ('NAME', 'login')
    }

    def LoginToApp(self):
        self.sendkeys(self.userNameTextBox, "tutorials")
        self.sendkeys(self.passwordTextBox, "tutorials")
        self.click(self.loginButtonPage)

    def loginToAppDDT(self, dataFilePath):
        wb = xlrd.open_workbook(dataFilePath)
        sheet = wb.sheet_by_index(0)
        for i in range(sheet.nrows):
            self.sendkeys(self.userNameTextBox, sheet.cell_value(i, 1))
            self.sendkeys(self.passwordTextBox, sheet.cell_value(i, 2))
            self.click(self.loginButtonPage)
        wb.release_resources()
        del wb
