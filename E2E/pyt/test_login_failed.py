import json
from pathlib import Path

import pytest
from E2E.pageObjects.login import LoginPage


test_data_path = Path(__file__).resolve().parent.parent / "data" / "test_e2eTestFramework.json"
with open(test_data_path) as f:

    test_data = json.load(f)
    test_list = [test_data["data"][1]]


@pytest.mark.smoke
@pytest.mark.parametrize("credentials", test_list)
def test_negative_login(browserInstance,credentials):
    driver= browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()


    login_page = LoginPage(driver)
    login_page.login(credentials["username_input"], credentials["password_input"])
    til=login_page.getTitle()
    print(til)
    om=login_page.is_sign_present()
    assert om,"not on login page"
