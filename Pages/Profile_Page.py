from selenium.webdriver.common.by import By
from Pages.Base_Page import Base_Page
from Testscripts.test_Base import test_Base


class Profile_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)

    ter_test = (By.XPATH, "//*[text()='Test']")
    Profile = (By.XPATH, "//*[text()='My Profile']")
    MANAGE_ADDRESS = (By.XPATH, "//div[text()='Manage Addresses']")
    ADD_ADDRESS = (By.XPATH, "//button[text()='ADD ADDRESSES']")
    NAME = (By.XPATH, "//input[@name='name']")
    # MOBILE_NUMBER=(By.XPATH, "//input[@name='name']")
    PHONE = (By.XPATH, "//input[@name='phone']")
    PINCODE = (By.XPATH, "//input[@name='pincode']")
    LOCALITY = (By.XPATH, "//input[@name='addressLine2']")
    ADDRESS = (By.XPATH, "//textarea[@name='addressLine1']")
    CITY = (By.XPATH, "//input[@name='city']")
    STATE = (By.XPATH, "//select[@name='state']")
    HOME_CHECKBOX = (By.XPATH, "//span[text()='Home']/parent::div/parent::label")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Save']")
    ADDRESS_SAVED = (By.XPATH, "//span[text()='TAHA NAGAR TELIYA KOT RAEBARELI, msk, Rae Bareli, Uttar Pradesh']")
    Rand = (By.XPATH, "//*[@class='nt9Nxn row']")
    Filpkart_logo = (By.XPATH, "//img[@title='Flipkart']")
    Assertion_Element = (By.XPATH, "//*[@class='dpjmKp']")

    def navigate_to_address(self):
        log = test_Base.getLogger()
        log.info("Navigating to my profile section")
        self.Hover_operation(self.ter_test)
        self.click_operation(self.Profile)
        # self.click_operation(self.Rand)
        self.Hover_operation(self.Filpkart_logo)
        log.info("Into my profile section")
        self.click_operation(self.MANAGE_ADDRESS)
        log.info("Into my manage address section")
        # self.click_operation(self.Rand)
