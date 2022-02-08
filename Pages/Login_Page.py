from selenium.webdriver.common.by import By

from Pages.Base_Page import Base_Page


class Login_Page(Base_Page):
    LOGIN_POPUP = (By.XPATH, "// a[ @ href = '/account/login?ret=/']")
    EMAIL_ADDRESS = (By.XPATH, "// input[ @ class ='_2IX_2- VJZDxU']")
    PASSWORD = (By.XPATH, "// input[@ class ='_2IX_2- _3mctLh VJZDxU']")
    LOGIN_BUTTON = (By.XPATH, "// button[@ class ='_2KpZ6l _2HKlqd _3AWRsL']")

    def __init__(self, driver):
        super().__init__(driver)

    def test_login_to_application(self):
        self.enter_url_operation("https://www.flipkart.com/", Login_Page.LOGIN_POPUP)
        self.send_keys_operation(Login_Page.EMAIL_ADDRESS, "alfotech512@gmail.com")
