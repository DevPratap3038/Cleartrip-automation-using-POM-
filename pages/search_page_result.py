import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SearchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def non_stop_filter(self):
        stops = self.Wait_for_elements_finding(By.XPATH, "//div[@class='nmx-1 ']//label[@class='checkbox w-100p checkbox flex-1 bs-border w-100p br-4 h-7 px-1 intl_checkbox py-1 hover:bg-neutral-0']//div[@class='flex flex-start p-relative flex-middle']//span[@class='checkbox__mark bs-border bc-neutral-500 bw-1 ba']")

        if stops[0].is_selected() == False:
            stops[0].click()

        if stops[1].is_selected() == True:
            stops[1].click()

    def one_stop_filter(self):
        stops = self.Wait_for_elements_finding(By.XPATH, "//div[@class='nmx-1 ']//label[@class='checkbox w-100p checkbox flex-1 bs-border w-100p br-4 h-7 px-1 intl_checkbox py-1 hover:bg-neutral-0']//div[@class='flex flex-start p-relative flex-middle']//span[@class='checkbox__mark bs-border bc-neutral-500 bw-1 ba']")
        stops[0].click()






