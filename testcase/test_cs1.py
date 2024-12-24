import time
import unittest
import pytest
from selenium.webdriver.common.by import By

from pages.home_page_CT import home_page
from utilites.util import Utils


@pytest.mark.usefixtures("setup")
class TestCleartripFile1():
    @pytest.fixture(autouse=True)
    def methods_setup(self):
        self.HP = home_page(self.driver)
        self.utils = Utils()

    def test_cleartrip_for_non_stop(self):

        SR = self.HP.searchFlight("Jaipur", "New Delhi", "25", "30")

        # search result page ------------------------------------------------------------------------
        # clicking on non-stop
        SR.Wait_for_Element_finding(By.XPATH, "//p[normalize-space()='Non-stop']").click()
        # // p[normalize - space() = 'Stops']s

        # SR.one_stop_filter()
        time.sleep(6)

        prizes = SR.Wait_for_elements_finding(By.XPATH, "//div[@class='rt-tuple-new-container__details__price ms-grid-column-3']//div[@class='flex flex-start flex-end ms-grid-row-1 ms-grid-column-2 mb-1']")

        # making a new object of utilities
        self.utils.print_list_elements(prizes)
        self.utils.Assertion_utils_for_assending(prizes)
