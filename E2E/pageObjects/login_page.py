import json
from pathlib import Path

from selenium.webdriver.common.by import By

from E2E.utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@name='username']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.sign_btn = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_btn).click()

    def is_sign_present(self):
        return self.driver.find_element(*self.sign_btn).is_displayed()

    def credentials(self):
        path = Path(__file__).resolve().parent / "E2E" / "testdata" / "test_e2eTestFramework.json"
        print(f"Loading credentials from: {path}")

        if not path.exists():
            raise FileNotFoundError(f"test_e2eTestFramework.json not found at: {path}")

        with open(path) as f:
            return json.load(f)
    def invalid_login(self,credentials):
        user = credentials["data"][3]  # Extract first user's data

        self.driver.get(user["url"])
        login_page = LoginPage(self.driver)
        login_page.login(user["username_input"], user["password_input"])



