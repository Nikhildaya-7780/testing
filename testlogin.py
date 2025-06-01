import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import Config


@pytest.fixture(scope="function")
def setup():
    if Config.BROWSER == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif Config.BROWSER == "firefox":
        driver = webdriver.Firefox(executable_path="/path/to/geckodriver")
    else:
        raise Exception("Unsupported browser!")

    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_valid_user(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.enter_username("valid_username")
    login_page.enter_password("valid_password")
    login_page.click_login()

    dashboard_page = DashboardPage(driver)
    assert "Dashboard" in dashboard_page.get_dashboard_header_text()


def test_login_invalid_user(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.enter_username("invalid_username")
    login_page.enter_password("invalid_password")
    login_page.click_login()

    # Validate error message appears (assuming an error message is displayed for invalid login)
    assert login_page.is_element_present(By.ID, "error-message")


def test:
    Nikhil
