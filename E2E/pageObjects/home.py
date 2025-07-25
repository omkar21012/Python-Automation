from selenium.webdriver.common.by import By

from E2E.utils.browserutils import BrowserUtils


class HomePage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.homepage_locator = (By.XPATH, "//a[text()='ProtoCommerce Home']")  # Corrected locator

    def is_on_home_page(self):
        return self.driver.find_element(*self.homepage_locator).is_displayed()
