from selenium.webdriver.common.by import By

from E2E.utils.browserutils import BrowserUtils


class HomePage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.homepage_locator = (By.CSS_SELECTOR, "div [class='oxd-layout orangehrm-upgrade-layout']")

    def is_on_home_page(self):
        return self.driver.find_element(*self.homepage_locator).is_displayed()

    def right_side_options(self, options):
        return (By.XPATH, f"//ul[contains(@class, 'oxd-main-menu')]//span[contains(normalize-space(.), '{options}')]")

    def select_menu_option(self, option):
        locator = self.right_side_options(option)
        self.driver.find_element(*locator).click()


