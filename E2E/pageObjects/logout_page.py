from selenium.webdriver.common.by import By

from E2E.utils.browserutils import BrowserUtils


class LogoutPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.profileIcon=(By.CSS_SELECTOR, "i[class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
        self.logoutButton=(By.XPATH,"//a[text()='Logout']")




    def logout(self):
        self.driver.find_element(*self.profileIcon).click()
        self.driver.find_element(*self.logoutButton).click()