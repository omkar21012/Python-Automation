import time

import pytest

from E2E.pageObjects.home_page import HomePage
from E2E.pageObjects.login_page import LoginPage
from E2E.pageObjects.logout_page import LogoutPage


@pytest.mark.order(1)
def test_login_success(browserInstance):
    driver = browserInstance

    home = HomePage(driver)
    a= home.getTitle()
    print(a)

    isOnHomepage = home.is_on_home_page()
    assert isOnHomepage, "Page is not loaded"


    time.sleep(10)
    print("logout pass")


@pytest.mark.order(2)
def test_login_failed(browserInstance,):
    driver= browserInstance


    home = HomePage(driver)
    value= home.is_on_home_page()
    if value:
      logout=  LogoutPage(driver)
      logout.logout()
    else:
        print("already logged out")


    login_page = LoginPage(driver)
    til=login_page.getTitle()
    print(til)
    om=login_page.is_sign_present()
    assert om,"not on login page"

    login_page.login("abcd","rt6rhf")