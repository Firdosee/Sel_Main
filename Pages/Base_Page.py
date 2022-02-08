from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page:

    def __init__(self, driver):
        self.driver = driver

    def enter_url_operation(self, url, locator):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
            print("Page is ready!")
        except TimeoutException as e:
            print("Loading took too much time!",e)

    def click_operation(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).click()

    def send_keys_operation(self, locator, keys):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).send_keys(keys)

    def get_text_from_locator(self, locator):
        text = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).text
        return text

    def get_attribute_value(self, locator, attribute):
        text = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute)
        return text
