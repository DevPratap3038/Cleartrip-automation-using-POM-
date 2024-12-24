import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Locations

from base.base_driver import BaseDriver
from pages.search_page_result import SearchPage


class home_page(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locations
    Login_request = "//div[@class='pb-1 px-1 flex flex-middle nmx-1']"
    City_From_Location = "//input[@placeholder='Where from?']"
    City_From_List = "//div[contains(@class,'dropdown p-absolute t-13 ln-1 w-100p')]//li//p"
    City_To_Location = "//input[@placeholder='Where to?']"
    City_To_List = "//div[contains(@class,'dropdown p-absolute t-13 ln-1 w-100p')]//li//p"
    Go_Date_Location = "//div[@class='sc-aXZVg dSvAMK mr-2 mt-1']"
    Go_Date_List = "//div[@class='DayPicker-Months']//div[@aria-disabled!='true']//div[@style='height: 45px;']"
    Return_Date_Loction = "//span[@class=' c-neutral-400 flex flex-nowrap fs-16 fw-500']"
    Return_Date_List = "//div[@class='DayPicker-Months']//div[@aria-disabled!='true']//div[@style='height: 45px;']"
    Button_Location = "//button[@class='sc-dAlyuH cIApyz']"


    # getting elements functions
    def GetLogginRequest(self):
        return self.Wait_for_Element_finding(By.XPATH, self.Login_request)

    def GetCityFromLocation(self):
        return self.Wait_for_Element_finding(By.XPATH, self.City_From_Location)

    def GetCityFromList(self):
        return self.Wait_for_elements_finding(By.XPATH, self.City_From_List)

    def GetCityToLocation(self):
        return self.Wait_for_Element_finding(By.XPATH, self.City_To_Location)

    def GetCityToList(self):
        return self.Wait_for_elements_finding(By.XPATH, self.City_To_List)

    def GetGoDateLocation(self):
        return self.Wait_for_Element_finding(By.XPATH, self.Go_Date_Location)

    def GetGoDateList(self):
        return self.Wait_for_elements_finding(By.XPATH, self.Go_Date_List)

    def GetReturnDateLocation(self):
        return self.Wait_for_Element_finding(By.XPATH, self.Return_Date_Loction)

    def GetReturnDateList(self):
        return self.Wait_for_elements_finding(By.XPATH, self.Return_Date_List)

    def ClickSearchButton(self):
        return self.Wait_for_Element_finding(By.XPATH, self.Button_Location)




    # to cancel the login request
    def cencel_the_login(self):
        self.GetLogginRequest().click()

    #to select the city from where to take flight
    def selecting_from_city(self, city_from_name):
        self.GetCityFromLocation().click()
        self.GetCityFromLocation().send_keys(city_from_name)
        time.sleep(3)

        city_from = self.GetCityFromList()
        for city1 in city_from:
            if city_from_name in city1.text:
                city1.click()
                break

    # select where the flight goes
    def selecting_to_city(self, city_to_name):
        self.GetCityToLocation().click()
        self.GetCityToLocation().send_keys(city_to_name)

        time.sleep(3)
        city_to = self.GetCityToList()

        for city2 in city_to:
            if city_to_name in city2.text:
                city2.click()
                break


    # select the date of when to go
    def select_go_date(self, date_to):
        self.GetGoDateLocation().click()

        go_date = self.GetGoDateList()
        for date1 in go_date:
            if date_to in date1.text:
                date1.click()
                break


    #select the date when to return
    def select_return_date(self, date_return):
        self.GetReturnDateLocation().click()

        return_date = self.GetReturnDateList()
        for date2 in return_date:
            if date_return in date2.text:
                date2.click()
                break


    # clicking the search button
    def searching(self):
        print("code succesful till the search button")
        self.ClickSearchButton().click()

    def searchFlight(self, FromCity, ToCity, Go_Date,  ReturnDate):
        self.cencel_the_login()
        self.selecting_from_city(FromCity)
        self.selecting_to_city(ToCity)
        self.select_go_date(Go_Date)
        self.select_return_date(ReturnDate)
        self.searching()
        SearchResults = SearchPage(self.driver)
        return SearchResults





