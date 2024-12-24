from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def Wait_for_Element_finding(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        single_element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return single_element

    def Wait_for_elements_finding(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        multi_element = wait.until(EC.presence_of_all_elements_located(
            (locator_type, locator)))

        return multi_element

