from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver
import os
from datetime import datetime


from selenium.webdriver.edge.service import Service


# Add browser selection from command line
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Type in browser name: chrome or edge"
    )


# WebDriver fixture
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    driver = None

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "edge":
        # Use pathlib for OS-safe path handling
        driver_path = Path("C:/Users/dell/PycharmProjects/Automation/drivers/msedgedriver.exe")

        print("Driver exists:", driver_path.exists())

        if not driver_path.is_file():
            raise FileNotFoundError(f"Edge driver not found at: {driver_path}")

        service = Service(driver_path)
        driver = webdriver.Edge(service=service)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()  # Ensures proper cleanup # safer than driver.close()

# Hook to capture test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browserInstance")
        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
            driver.save_screenshot(screenshot_path)
            if screenshot_path:
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(screenshot_path))
                rep.extra = extra