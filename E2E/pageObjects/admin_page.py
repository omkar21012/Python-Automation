from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Admin_Page:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//div[@class='oxd-form-row']//div//input[@class='oxd-input oxd-input--active']")
        self.emp_name = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
        self.user_role_dropdown = (By.XPATH, "//label[text()='User Role']/following::div[@class='oxd-select-text-input'][1]")
        self.status_dropdown = (By.XPATH, "//label[text()='Status']/following::div[@class='oxd-select-text-input'][1]")
        self.status_option = lambda status: (By.XPATH, f"//div[@role='listbox']//span[text()='{status}']")
        self.user_role_option = lambda role: (By.XPATH, f"//div[@role='listbox']//span[text()='{role}']")
        self.search_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.search_results=(By.CSS_SELECTOR,"div[class='oxd-table-card']")



        

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_emp_name(self, name):
        self.driver.find_element(*self.emp_name).send_keys(name)

    def select_user_role(self, role_name):
        self.driver.find_element(*self.user_role_dropdown).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.user_role_option(role_name))
        ).click()

    def select_status(self, status_value="Enabled"):
        self.driver.find_element(*self.status_dropdown).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.status_option(status_value))
        ).click()

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def get_Search_count(self):
       list= self.driver.find_elements(*self.search_results)
       return len(list)
