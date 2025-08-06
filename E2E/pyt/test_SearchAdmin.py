import time

import pytest

from E2E.pageObjects.admin_page import Admin_Page
from E2E.pageObjects.home_page import HomePage
from conftest import browserInstance

@pytest.mark.order(1)
def test_search_admin_user_details(browserInstance):
    driver= browserInstance
    home = HomePage(driver)
    home.select_menu_option("Admin")
    admin= Admin_Page(driver)
    admin.enter_username("Admin")
    #admin.enter_emp_name("manda user")

    admin.select_user_role("Admin")
    admin.select_status()

    admin.click_search()
    results= admin.get_Search_count()
    assert results!=0, "NO results found"
    time.sleep(10)



