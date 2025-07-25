import json
from pathlib import Path

import pytest

from E2E.pageObjects.home import HomePage
from E2E.pageObjects.login import LoginPage

test_data_path = Path(__file__).resolve().parent.parent / "data" / "test_e2eTestFramework.json"


with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = [test_data["data"][0]]


@pytest.mark.smoke
@pytest.mark.parametrize("credentials", test_list)
def test_e2eDesign(browserInstance, credentials):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()


    login_page = LoginPage(driver)
    print(login_page.getTitle())
    login_page.login(credentials["username_input"], credentials["password_input"])

    home = HomePage(driver)
    a= home.getTitle()
    print(a)

    isOpen = home.is_on_home_page()
    assert isOpen, "Page is not loaded"
