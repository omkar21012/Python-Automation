import pytest

from E2E.pageObjects.left_pannel_page import LeftSidepanel


@pytest.mark.order(1)
def test_search_left_admin(browserInstance):
    driver=browserInstance
    left_side=LeftSidepanel(driver)
    left_side.search_left_panel("Admin")
    results= left_side.get_search_data()
    assert results.__contains__("Admin"),"Admin option not found in results not found"

@pytest.mark.order(2)
def test_search_left_PIM(browserInstance):
    driver=browserInstance
    left_side=LeftSidepanel(driver)
    left_side.search_left_panel("PIM")
    results= left_side.get_search_data()
    assert results.__contains__("PIM"),"PIM option not found in results not found"

@pytest.mark.order(3)
def test_search_left_Time(browserInstance):
    driver=browserInstance
    left_side=LeftSidepanel(driver)
    left_side.search_left_panel("Time")
    results= left_side.get_search_data()
    assert results.__contains__("Time"),"Time option not found in results not found"

@pytest.mark.order(4)
def test_search_left_Dashboard(browserInstance):
    driver=browserInstance
    left_side=LeftSidepanel(driver)
    left_side.search_left_panel("Dashboard")
    results= left_side.get_search_data()
    assert results.__contains__("Dashboard"),"Dashboard option not found in results not found"

@pytest.mark.order(5)
def test_search_left_Performance(browserInstance):
        driver = browserInstance
        left_side = LeftSidepanel(driver)
        left_side.search_left_panel("Performance")
        results = left_side.get_search_data()
        assert results.__contains__("Performance"), "Time option not found in results not found"