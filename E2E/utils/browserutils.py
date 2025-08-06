from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class BrowserUtils:


    def __init__(self, driver):
        self.driver= driver

    def getTitle(self):
        return self.driver.title

    def find_element(self, by, locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located((by, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element