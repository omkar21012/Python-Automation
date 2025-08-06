from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from E2E.utils.browserutils import BrowserUtils


class LeftSidepanel(BrowserUtils):
    def __init__(self,driver):

        super().__init__(driver)
        self.driver= driver
        self.search_bar= (By.CSS_SELECTOR,"input[placeholder='Search']")
        #self.menu_list=(By.XPATH,"")

    def search_left_panel(self, value):
        search_input = self.driver.find_element(*self.search_bar)
        search_input.click()
        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(Keys.DELETE)
        search_input.send_keys(value)

    def list_results(self):
        return self.driver.find_elements(By.XPATH,f"//ul[@class='oxd-main-menu']//span[normalize-space(text())='']")

    def get_search_data(self):
        lst=self.list_results()
        return [el.text for el in lst]