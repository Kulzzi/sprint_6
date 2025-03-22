from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from data import Url


class BasePageScooter:

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self):
        self.driver.get(Url.url_home_page)

    def driver_find_element(self, locator):
        return self.driver.find_element(*locator)

    def driver_find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def driver_wait_for_visibile_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def driver_wait_for_clickable_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def driver_click_element(self, element):
        element.click()

    def driver_send_keys_to_element(self, element, info):
        element.send_keys(info)

    def driver_scroll_to_element(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def driver_current_url(self):
        return self.driver.current_url

    def driver_switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])