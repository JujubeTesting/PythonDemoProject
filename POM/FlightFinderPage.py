from Framework.Base import webPage
from seleniumpagefactory.Pagefactory import PageFactory

class FlightFinderPage(PageFactory,webPage):

    def __init__(self, driver):
        self.driver = driver
        print("## driver initialized @LoginPage constructor ")
        print("\n")

    locators = {
        "Type_RadioButton": ('XPATH', "//input[@value='oneway']"),
        "PassengerCount_Dropdown": ('NAME', 'passCount'),
        "DepartureCity_Dropdown": ('NAME', 'fromPort'),
        "DepartureMonth_Dropdown": ('NAME', 'fromMonth'),
        "DepartureDay_Dropdown": ('NAME', 'fromDay'),
        "ArrivingCity_Dropdown": ('NAME', 'toPort'),
        "ReturnMonth_Dropdown": ('NAME', 'toMonth'),
        "ReturnDay_Dropdown": ('NAME', 'toDay'),
        "ServiceClass_RadioButton": ('XPATH', "//input[@value='Business']"),
        "Airline_Dropdown": ('NAME', 'airline'),
        "Continue_Button": ('NAME', 'findFlights'),
    }

    def flightBooking(self):
        self.click(self.Type_RadioButton)
        self.selectFromDropdown(self.PassengerCount_Dropdown,2)
        self.selectFromDropdown(self.DepartureCity_Dropdown, "Sydney")
        self.selectFromDropdown(self.DepartureMonth_Dropdown, "May")
        self.selectFromDropdown(self.DepartureDay_Dropdown, 22)
        self.selectFromDropdown(self.ArrivingCity_Dropdown, "Paris")
        self.selectFromDropdown(self.ReturnMonth_Dropdown, "June")
        self.selectFromDropdown(self.ReturnDay_Dropdown, 12)
        self.click(self.ServiceClass_RadioButton)
        self.selectFromDropdown(self.Airline_Dropdown, "Unified Airlines")
        self.click(self.Continue_Button)
