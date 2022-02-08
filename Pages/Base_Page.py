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
            print("Loading took too much time!", e)

    def click_operation(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).click()

    def send_keys_operation(self, locator, keys):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).send_keys(keys)

    def send_keys_js(self, locator, loc, keys):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        #self.driver.executeScript("document.getElementByClassName('" + loc + "').setAttribute('value', '" + keys + "')")
        javaScript = "document.getElementsByClassName('" + loc + "')[0].value = '" + keys + "' "
        self.driver.execute_script(javaScript)

    def get_text_from_locator(self, locator):
        text = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator)).text
        return text

    def get_attribute_value(self, locator, attribute):
        text = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute)
        return text

    def get_title(self):
        get_title = self.driver.title
        return get_title
