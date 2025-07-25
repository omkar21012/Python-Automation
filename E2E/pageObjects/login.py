from selenium.webdriver.common.by import By

from E2E.utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@id='username']")
        self.password_input = (By.XPATH, "//input[@id='password']")
        self.sign_btn = (By.XPATH, "//input[@id='signInBtn']")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_btn).click()


    def is_sign_present(self):
        return self.driver.find_element(*self.sign_btn).is_displayed()
