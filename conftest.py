import json
import shutil
from pathlib import Path
import os
import pytest
import pytest_html
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service

from E2E.pageObjects.login_page import LoginPage
from E2E.pageObjects.logout_page import LogoutPage
from E2E.utils.browserutils import BrowserUtils


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Type browser name: chrome, firefox, or edge",
    )
@pytest.fixture(scope="session")
def credentials():
    path = Path(__file__).resolve().parent / "E2E" / "testdata" / "test_e2eTestFramework.json"
    print(f"Loading credentials from: {path}")

    if not path.exists():
        raise FileNotFoundError(f"test_e2eTestFramework.json not found at: {path}")

    with open(path) as f:
        return json.load(f)


@pytest.fixture(scope="session")
def browserInstance(request,credentials):
    name = request.config.getoption("browser_name")
    if name == "chrome":
        driver = webdriver.Chrome()

    elif name == "firefox":
        driver = webdriver.Firefox()

    elif name == "edge":
        root = Path(__file__).resolve().parent  # project root: Automation
        drv = root / "E2E" / "driver" / "msedgedriver.exe"
        print("Looking for EdgeDriver at:", drv)
        if not drv.is_file():
            raise FileNotFoundError(f"EdgeDriver not found at {drv}")
        service = Service(drv)
        driver = webdriver.Edge(service=service)

    driver.maximize_window()

    driver.implicitly_wait(30)

    user = credentials["data"][2]  # Extract first user's data

    driver.get(user["url"])
    login_page = LoginPage(driver)
    login_page.login(user["username_input"], user["password_input"])





    yield driver
    try:
        logout_page = LogoutPage(browserInstance)
        logout_page.logout()
        print("✅ Logout successful")
    except Exception as e:
        print(f"⚠️ Logout failed: {e}")

    try:
        browserInstance.quit()
        print(" Browser closed")
    except Exception as e:
        print(f"⚠️ Browser quit failed: {e}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browserInstance")
        if driver:
            screenshots_dir = Path(__file__).resolve().parent / "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Create screenshot filename
            fname = f"{item.name}_{datetime.now():%Y-%m-%d_%H-%M-%S}.png"
            full_path = screenshots_dir / fname
            driver.save_screenshot(str(full_path))

            # Embed screenshot
            plugin = item.config.pluginmanager.getplugin("html")
            if plugin:
                extra = getattr(rep, "extra", [])
                extra.append(plugin.extras.image(str(full_path)))
                rep.extra = extra

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    report_path = os.path.join(os.getcwd(), "reports", "report.html")
    if os.path.exists(report_path):
        os.remove(report_path)
        print(f"🧹 Cleared previous report: {report_path}")

def pytest_sessionstart(session):
    screenshots_dir = Path(__file__).resolve().parent / "screenshots"
    if screenshots_dir.exists() and screenshots_dir.is_dir():
        shutil.rmtree(screenshots_dir)
        print("🧹 Old screenshots deleted.")